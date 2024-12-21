from pydantic import BaseModel
class User(BaseModel):
    id:int
    name:str
    contact:str
    email:str
