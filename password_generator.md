# 🔐 Feature: Password Generator
**Branch:** `feature/password-generator`

## What This Feature Does
Generates a random, secure password based on user-selected options:
- Password length (6–64 characters)
- Include Uppercase letters (A–Z)
- Include Lowercase letters (a–z)
- Include Digits (0–9)
- Include Symbols (!@#$%...)

## API Endpoint
```
GET /api/generate
```
Query Parameters:
| Param      | Type    | Default | Description                  |
|------------|---------|---------|------------------------------|
| length     | int     | 16      | Number of characters         |
| uppercase  | bool    | true    | Include uppercase letters    |
| lowercase  | bool    | true    | Include lowercase letters    |
| digits     | bool    | true    | Include digits               |
| symbols    | bool    | true    | Include special characters   |

### Example Request
```
GET /api/generate?length=20&uppercase=true&lowercase=true&digits=true&symbols=false
```

### Example Response
```json
{
  "password": "aB3kR9mNpQ2vLxTwYj7c",
  "length": 20
}
```

## How to Run
```bash
cd feature-password-generator
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
# Visit http://localhost:8000
```

## Files
- `main.py` — FastAPI app entry point
- `routes/generator.py` — API route logic
- `templates/generator.html` — Frontend UI
