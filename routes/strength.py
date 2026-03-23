from fastapi import APIRouter
import re

router = APIRouter()

@router.post("/api/strength")
def check_strength(payload: dict):
    password = payload.get("password", "")
    score = 0
    feedback = []

    checks = {
        "length_8":   (len(password) >= 8,  "At least 8 characters"),
        "length_12":  (len(password) >= 12, "At least 12 characters"),
        "uppercase":  (bool(re.search(r'[A-Z]', password)), "Contains uppercase letters"),
        "lowercase":  (bool(re.search(r'[a-z]', password)), "Contains lowercase letters"),
        "digits":     (bool(re.search(r'\d', password)),    "Contains numbers"),
        "symbols":    (bool(re.search(r'[^A-Za-z0-9]', password)), "Contains special characters"),
        "no_spaces":  (' ' not in password, "No spaces"),
        "long":       (len(password) >= 16, "16+ characters (excellent length)"),
    }

    weights = {"length_8": 1, "length_12": 1, "uppercase": 1,
               "lowercase": 1, "digits": 1, "symbols": 2, "no_spaces": 1, "long": 2}

    passed = []
    failed = []
    for key, (passed_check, msg) in checks.items():
        if passed_check:
            score += weights[key]
            passed.append(msg)
        else:
            failed.append(msg)

    max_score = sum(weights.values())
    percent = round((score / max_score) * 100)

    if percent < 30:
        label = "Very Weak"
        color = "#ef4444"
    elif percent < 50:
        label = "Weak"
        color = "#f97316"
    elif percent < 70:
        label = "Fair"
        color = "#eab308"
    elif percent < 85:
        label = "Strong"
        color = "#22c55e"
    else:
        label = "Very Strong"
        color = "#10b981"

    return {
        "score": percent,
        "label": label,
        "color": color,
        "passed": passed,
        "suggestions": failed
    }
