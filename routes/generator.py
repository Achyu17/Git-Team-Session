from fastapi import APIRouter
import random
import string

router = APIRouter()

@router.get("/api/generate")
def generate_password(
    length: int = 16,
    uppercase: bool = True,
    lowercase: bool = True,
    digits: bool = True,
    symbols: bool = True
):
    charset = ""
    if uppercase:
        charset += string.ascii_uppercase
    if lowercase:
        charset += string.ascii_lowercase
    if digits:
        charset += string.digits
    if symbols:
        charset += string.punctuation

    if not charset:
        return {"error": "At least one character type must be selected."}

    password = ''.join(random.choices(charset, k=length))
    return {"password": password, "length": len(password)}
