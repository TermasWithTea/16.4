from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    username: str
    age: int
    id: int 

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
async def put_user(user_id: int, username: str, age: int) -> User:
    if user_id not in users:
        raise HTTPException(status_code=404, detail='User was not found')
    user = User(username=username, age=age, id=user_id)
    users[user_id] = user
    return user

@app.delete('/user/{user_id}')
async def del_del(user_id: int) -> User:
    if user_id not in users:
        raise HTTPException(status_code=404, detail='User was not found')
    
    del_del = users[user_id]
    del users[user_id]
    return del_del
