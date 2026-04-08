from fastapi import FastAPI, Query, HTTPException

app = FastAPI(title="PathGuard API")


@app.get("/users")
async def get_users(id: str = Query(..., description="User identifier")):
    """Return user information for the given id."""
    return {"id": id, "status": "active"}
