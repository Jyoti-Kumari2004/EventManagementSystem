from pydantic import BaseModel
from datetime import date
class Event(BaseModel):
    id:int
    name:str
    venue:str
    startDate:date
    endDate:date
    description:str