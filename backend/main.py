from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    email: str
    role: Optional[str] = None


users_db: dict[int, User] = {
    1: User(id=1, name="Alice", email="alice@example.com", role="admin"),
    2: User(id=2, name="Bob", email="bob@example.com"),
}


@app.get("/users/{user_id}")
def get_user(user_id: int) -> User:
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]


@app.post("/users")
def create_user(user: User) -> User:
    if user.id in users_db:
        raise HTTPException(status_code=409, detail="User already exists")
    users_db[user.id] = user
    return user
