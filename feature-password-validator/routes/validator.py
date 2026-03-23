from fastapi import APIRouter
import re

router = APIRouter()

@router.post("/api/validate")
def validate_password(payload: dict):
    password = payload.get("password", "")
    rules = payload.get("rules", {})

    results = []
    all_pass = True

    # Rule: minimum length
    min_len = rules.get("min_length", 8)
    passed = len(password) >= min_len
    results.append({"rule": f"Minimum {min_len} characters", "passed": passed})
    if not passed: all_pass = False

    # Rule: uppercase required
    if rules.get("require_uppercase", True):
        passed = bool(re.search(r'[A-Z]', password))
        results.append({"rule": "At least one uppercase letter", "passed": passed})
        if not passed: all_pass = False

    # Rule: lowercase required
    if rules.get("require_lowercase", True):
        passed = bool(re.search(r'[a-z]', password))
        results.append({"rule": "At least one lowercase letter", "passed": passed})
        if not passed: all_pass = False

    # Rule: digit required
    if rules.get("require_digit", True):
        passed = bool(re.search(r'\d', password))
        results.append({"rule": "At least one digit", "passed": passed})
        if not passed: all_pass = False

    # Rule: special character required
    if rules.get("require_special", True):
        passed = bool(re.search(r'[^A-Za-z0-9]', password))
        results.append({"rule": "At least one special character", "passed": passed})
        if not passed: all_pass = False

    # Rule: no spaces
    if rules.get("no_spaces", True):
        passed = ' ' not in password
        results.append({"rule": "No spaces allowed", "passed": passed})
        if not passed: all_pass = False

    # Rule: no repeating characters (3+)
    if rules.get("no_repeats", False):
        passed = not bool(re.search(r'(.)\1{2,}', password))
        results.append({"rule": "No 3+ repeating characters", "passed": passed})
        if not passed: all_pass = False

    return {
        "valid": all_pass,
        "results": results,
        "password_length": len(password)
    }
