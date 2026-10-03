from pydantic import BaseModel,conint,constr
from typing import Optional
from fastapi import FastAPI

app=FastAPI()

class User(BaseModel):
    id: int
    name:str
    age:conint(gt=0)
    email:constr(min_length=5)
    gender:Optional[str]=None

# api=ure nderlidhese mes dy kompotentave

@app.post("/user")
async def create_user(user:User):
    return user


def main():
    user1:User=User(id=1,name="John",age=21,email="xyz@gmail.com",gender="Male")

    print(user1.name)

if __name__=="__main__":
    main()