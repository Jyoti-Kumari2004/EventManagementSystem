from fastapi import FastAPI
import uvicorn
from models.user import User
from models.event import Event
from services.userService import UserService
from services.eventService import EventService

from fastapi.encoders import jsonable_encoder
from mysql.connector import Error

from repos.userRepo import UserRepo
from repos.eventRepo import EventRepo


app = FastAPI()
userRepo = UserRepo()
userService = UserService(userRepo)


@app.get("/{id}")
def getHome(id: int):
    return {"message": "welcome to fastapi {id}"}


@app.get("/participant/{id}")
def getUser(id: int):
    resultUser = userService.getbyid(id)
    return jsonable_encoder(resultUser)


@app.post("/participant")
def createUser(user: User):
    userService.createUser(user)
    return {"message": "created!"}


@app.put("/participant/{id}")
def updateUser(id: int, user: User):
    result = userService.updateUser(id, user)
    return jsonable_encoder(result)


@app.delete("/participant/delete/{id}")
def deleteUser(id: int):
    try:
        userService.deleteUser(id)
        return {"message": "user deleted!"}
    except Error as err:
        print(f"Error :{err}")


eventRepo = EventRepo()
eventService = EventService(eventRepo)


@app.get("/event/{id}")
def getEvent(id: int):
    result = eventService.getbyid(id)
    return jsonable_encoder(result)


@app.post("/event")
def createEvent(event: Event):
    eventService.createEvent(event)
    return {"message": "created!"}


@app.put("/event/{id}")
def updateEvent(id: int, event: Event):
    result = eventService.updateEvent(id, event)
    return jsonable_encoder(result)


@app.delete("/event/delete/{id}")
def deleteEvent(id: int):
    try:
        eventService.deleteEvent(id)
        return {"message": "event deleted!"}
    except Error as err:
        print(f"Error :{err}")


@app.post("/event/{eventid}/participant/{participantid}")
def createEvent_Participation(eventid: int, participationid: int):
    Event_ParticipationService.createEvent_Participation(eventid, participationid)
    return {"message": "created!!"}
