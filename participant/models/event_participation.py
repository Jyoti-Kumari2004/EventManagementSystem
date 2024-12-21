from pydantic import BaseModel


class Event_Participation(BaseModel):
    id: int
    eventid: int
    participationid: int
