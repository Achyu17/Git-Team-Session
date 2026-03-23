# 👁 Feature: Password Mask / Unmask Toggle
**Branch:** `feature/password-mask-toggle`

## What This Feature Does
Allows a user to type a password and toggle its visibility between
masked (●●●●●) and plain text. The backend returns the masked version
and character count. The frontend handles the show/hide toggle.

## API Endpoint
```
POST /api/mask
```
Request Body (JSON):
```json
{ "password": "MySecret123!" }
```

### Example Response
```json
{
  "original": "MySecret123!",
  "masked": "************",
  "length": 12
}
```

## How to Run
```bash
cd feature-password-mask-toggle
pip install -r requirements.txt
uvicorn main:app --reload --port 8002
# Visit http://localhost:8002
```

## Files
- `main.py` — FastAPI app entry point
- `routes/mask.py` — API route logic
- `templates/mask.html` — Frontend UI
