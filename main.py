from http.client import HTTPException
from typing import List
from models import User,Gender,Role  # type: ignore
from uuid import UUID,uuid4
from fastapi import FastAPI

app = FastAPI() #application app as object/instance

db:List[User] =[
    User(
         id=UUID("50ecc8e8-64c2-40e5-95ab-ab4ee5740e49"),
         first_name="Tulip",
         last_name = "A",
         gender = Gender.female,
         roles = [Role.student]

         
         ),
     User(
         id=UUID("7b13a673-361a-4aca-ab44-a94fb8d8e73e"), 
         first_name="Jasmine",
         last_name = "S",
         gender = Gender.male,
         roles = [Role.student]

         
         ),

    User(
         id=UUID("5bfb7117-1ac9-4911-b9ed-ce537745d596"),
         first_name="Rose",
         last_name = "V",
         gender = Gender.female,
         roles = [Role.user]

         
         )

]

@app.get("/")
def root():
    return{"Hey" : "Sakthi"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user:User):
    db.append(user)
    return{"id": user.id}

async def delete_user(first_name: str):
    for user in db:
        if user.first_name == first_name:
            db.remove(user)
            return {"detail": "User deleted successfully"}
