from fastapi import APIRouter
import random, string, re

router = APIRouter()

# ── Feature 1: Generator ────────────────────────────────────────────
@router.get("/api/generate")
def generate_password(length: int = 16, uppercase: bool = True,
                      lowercase: bool = True, digits: bool = True, symbols: bool = True):
    charset = ""
    if uppercase: charset += string.ascii_uppercase
    if lowercase: charset += string.ascii_lowercase
    if digits:    charset += string.digits
    if symbols:   charset += string.punctuation
    if not charset:
        return {"error": "Select at least one character type."}
    return {"password": ''.join(random.choices(charset, k=length)), "length": length}


# ── Feature 2: Strength Checker ─────────────────────────────────────
@router.post("/api/strength")
def check_strength(payload: dict):
    password = payload.get("password", "")
    checks = {
        "length_8":  (len(password) >= 8,  "At least 8 characters",     1),
        "length_12": (len(password) >= 12, "At least 12 characters",     1),
        "uppercase": (bool(re.search(r'[A-Z]', password)), "Uppercase letters", 1),
        "lowercase": (bool(re.search(r'[a-z]', password)), "Lowercase letters", 1),
        "digits":    (bool(re.search(r'\d', password)),    "Contains numbers",  1),
        "symbols":   (bool(re.search(r'[^A-Za-z0-9]', password)), "Special characters", 2),
        "no_spaces": (' ' not in password, "No spaces",                   1),
        "long":      (len(password) >= 16, "16+ characters (excellent)", 2),
    }
    score = sum(w for (ok, _, w) in checks.values() if ok)
    max_score = sum(w for (_, _, w) in checks.values())
    percent = round((score / max_score) * 100) if max_score else 0
    passed = [m for (ok, m, _) in checks.values() if ok]
    suggestions = [m for (ok, m, _) in checks.values() if not ok]
    label, color = (
        ("Very Weak", "#ef4444") if percent < 30 else
        ("Weak",      "#f97316") if percent < 50 else
        ("Fair",      "#eab308") if percent < 70 else
        ("Strong",    "#22c55e") if percent < 85 else
        ("Very Strong","#10b981")
    )
    return {"score": percent, "label": label, "color": color,
            "passed": passed, "suggestions": suggestions}


# ── Feature 3: Mask Toggle ───────────────────────────────────────────
@router.post("/api/mask")
def mask_password(payload: dict):
    password = payload.get("password", "")
    return {"original": password, "masked": "*" * len(password), "length": len(password)}


# ── Feature 4: Validator ─────────────────────────────────────────────
@router.post("/api/validate")
def validate_password(payload: dict):
    password = payload.get("password", "")
    rules = payload.get("rules", {})
    results, all_pass = [], True

    def check(label, passed):
        nonlocal all_pass
        results.append({"rule": label, "passed": passed})
        if not passed: all_pass = False

    min_len = rules.get("min_length", 8)
    check(f"Minimum {min_len} characters", len(password) >= min_len)
    if rules.get("require_uppercase", True):  check("At least one uppercase letter", bool(re.search(r'[A-Z]', password)))
    if rules.get("require_lowercase", True):  check("At least one lowercase letter", bool(re.search(r'[a-z]', password)))
    if rules.get("require_digit", True):      check("At least one digit",             bool(re.search(r'\d', password)))
    if rules.get("require_special", True):    check("At least one special character", bool(re.search(r'[^A-Za-z0-9]', password)))
    if rules.get("no_spaces", True):          check("No spaces allowed",              ' ' not in password)
    if rules.get("no_repeats", False):        check("No 3+ repeating characters",     not bool(re.search(r'(.)\1{2,}', password)))

    return {"valid": all_pass, "results": results, "password_length": len(password)}
