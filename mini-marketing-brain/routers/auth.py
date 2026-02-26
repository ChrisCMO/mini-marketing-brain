from fastapi import APIRouter

router = APIRouter()

@router.post("/dev-login")
def dev_login():
    return {
        "access_token": "mini-brain-dev-token",
        "token_type": "bearer",
        "user": {"id": "dev-user-1", "email": "dev@yorcmo.com", "name": "Dev User"}
    }

@router.get("/me")
def get_me():
    return {"id": "dev-user-1", "email": "dev@yorcmo.com", "name": "Dev User"}
