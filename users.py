from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    surname: str | None = None
    url: str    

app = FastAPI()

@app.get("/users")
async def users():
    return {"name":"Yorch", "surname": "Campo", "url": "http://yorch82.com"}

