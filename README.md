# ✅ Feature: Password Validator
**Branch:** `feature/password-validator`

## What This Feature Does
Validates a password against a configurable set of rules chosen by the user.
Returns whether the password is valid overall and which specific rules passed or failed.

## API Endpoint
```
POST /api/validate
```
Request Body (JSON):
```json
{
  "password": "MyPass@123",
  "rules": {
    "min_length": 8,
    "require_uppercase": true,
    "require_lowercase": true,
    "require_digit": true,
    "require_special": true,
    "no_spaces": true,
    "no_repeats": false
  }
}
```

### Example Response
```json
{
  "valid": true,
  "password_length": 10,
  "results": [
    { "rule": "Minimum 8 characters",       "passed": true  },
    { "rule": "At least one uppercase letter","passed": true  },
    { "rule": "At least one lowercase letter","passed": true  },
    { "rule": "At least one digit",           "passed": true  },
    { "rule": "At least one special character","passed": true  },
    { "rule": "No spaces allowed",            "passed": true  }
  ]
}
```

## Configurable Rules
| Rule Key           | Type | Default | Description                          |
|--------------------|------|---------|--------------------------------------|
| min_length         | int  | 8       | Minimum number of characters         |
| require_uppercase  | bool | true    | Must have at least one A–Z           |
| require_lowercase  | bool | true    | Must have at least one a–z           |
| require_digit      | bool | true    | Must have at least one 0–9           |
| require_special    | bool | true    | Must have at least one special char  |
| no_spaces          | bool | true    | Password must not contain spaces     |
| no_repeats         | bool | false   | No 3+ consecutive repeated characters|

## How to Run
```bash
cd feature-password-validator
pip install -r requirements.txt
uvicorn main:app --reload --port 8003
# Visit http://localhost:8003
```

## Files
- `main.py` — FastAPI app entry point
- `routes/validator.py` — API route logic
- `templates/validator.html` — Frontend UI
