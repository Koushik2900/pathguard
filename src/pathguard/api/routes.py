from fastapi import APIRouter, HTTPException, Query

router = APIRouter()

# In-memory user store for demonstration
USERS = {
    "123": {"id": "123", "name": "Alice", "role": "admin"},
    "456": {"id": "456", "name": "Bob", "role": "viewer"},
    "789": {"id": "789", "name": "Charlie", "role": "analyst"},
}


@router.get("/users")
def get_user(user_id: str = Query(..., alias="id", description="The user ID to look up")):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id '{user_id}' not found")
    return user
