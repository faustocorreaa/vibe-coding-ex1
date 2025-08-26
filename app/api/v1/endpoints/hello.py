from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def hello_world():
    """Simple Hello World endpoint"""
    return {"message": "Hello World"}

@router.get("/name/{name}")
def hello_name(name: str):
    """Personalized hello endpoint"""
    return {"message": f"Hello {name}!"}
