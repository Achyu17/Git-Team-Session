from fastapi import APIRouter

router = APIRouter()

@router.post("/api/mask")
def mask_password(payload: dict):
    password = payload.get("password", "")
    masked = "*" * len(password)
    return {
        "original": password,
        "masked": masked,
        "length": len(password)
    }
