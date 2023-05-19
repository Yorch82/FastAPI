from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(tags=["Users"],
                   responses={404: {"message": "No encontrado"}})

class User(BaseModel):
    id: int
    name: str
    surname: str 
    url: str
    age: int

users_list = [User(id=1, name="Jorge", surname="Campo", url="http://jorge.com", age=40),
            User(id=2,name="Kirk", surname="Hammett", url="http://kirk.com", age=60),
            User(id=3,name="James", surname="Hetfield", url="http://james.com", age=62)]  

@router.get("/users")
async def users():
    return users_list

# Path
@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# Query    
@router.get("/userquery/")
async def user(id: int):
    return search_user(id)
    
@router.post("/user/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
             
    users_list.append(user)
    return user

@router.put("/user/",response_model=User, status_code=200)
async def  user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        raise HTTPException(status_code=404, detail="No se ha actualizado el usuario")
    
    return user

@router.delete("/user/{id}",status_code=200)
async def  user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        raise HTTPException(status_code=404, detail="No se ha borrado el usuario")       

def search_user(id: int):
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        raise HTTPException(status_code=404, detail="No se ha encontrado el usuario")
