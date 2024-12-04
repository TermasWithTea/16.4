from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    username: str
    age: int

@app.get('/users')
async def get_reurn() -> list:
    return users

@app.post('user/{username}/{age}')
async def post_ret(username: str, age: int) -> User:
    user_id = max(list(users.keys()), default= 0) +1
    user = User(username = username,age = age)
    users[user_id] = user
    return user

@app.put('/user/{user_id}/{username}/{age}')
async def put_ret(user_id: int, username: str, age: str) -> str:
    if user_id not in users:
        raise HTTPException(status_code = 404, detail = 'User not found')
    users[user_id] = User(username = username, age = age)
    return f'The user {user_id} is update!'

@app.delete('/user/{user_id}')
async def del_del(user_id: int) -> dict:
    if user_id not in users:
        raise HTTPException(status_code= 404, detail= 'User not found')
    del users[user_id]
    return {'message':f'User {user_id} has been deleted'}

