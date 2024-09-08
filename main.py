from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

# ユーザー情報を保存するための辞書
users: Dict[int, User] = {}

@app.post("/users/", response_model=User)
async def create_user(user: User):
    """ 新しいユーザーを作成します。
    すでに同じIDのユーザーが存在する場合はエラーを返します。 """
    if user.id in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user.id] = user
    return user

@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    """ 特定のIDを持つユーザーを取得します。
    存在しないユーザーIDの場合は404エラーを返します。 """
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    """ ユーザー情報を更新します。
    存在しないユーザーIDの場合は404エラーを返します。 """
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = user
    return user

@app.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: int):
    """ ユーザーを削除します。
    存在しないユーザーIDの場合は404エラーを返します。
    削除されたユーザーの情報を返します。 """
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    deleted_user = users.pop(user_id)
    return deleted_user
