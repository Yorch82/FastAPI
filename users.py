from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str 
    url: str
    age: int

users_list = [User(id=1, name="Jorge", surname="Campo", url="http://jorge.com", age=40),
            User(id=2,name="Kirk", surname="Hammett", url="http://kirk.com", age=60),
            User(id=3,name="James", surname="Hetfield", url="http://james.com", age=62)]  

@app.get("/users")
async def users():
    return users_list

# Path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# Query    
@app.get("/userquery/")
async def user(id: int):
    return search_user(id)
    
@app.post("/user/")
async def user(user: User):
    if type(search_user(user.id)) == User:
         return {"error": "El usuario ya existe"}
    else:
        users_list.append(user)

    return user

@app.put("/user/")
async def  user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "No se ha actualizado el usuario"}
    
    return user

@app.delete("/user/{id}")
async def  user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha borrado el usuario"}        

def search_user(id: int):
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
