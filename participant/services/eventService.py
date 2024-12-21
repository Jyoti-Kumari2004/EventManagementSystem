from models.event import Event
from repos.eventRepo import EventRepo


class EventService:
    eventRepo:EventRepo
    def __init__(self, eventRepo: EventRepo):
        self.eventRepo = eventRepo

    def getbyid(self, id) -> Event:
        return self.eventRepo.getid(id)

    def createEvent(self, Event):
        return self.eventRepo.createEvent(Event)

    def updateEvent(self, Event, id):
        return self.eventRepo.updateEvent(Event, id)

    def deleteEvent(self, id):
        return self.eventRepo.deleteit(id)
