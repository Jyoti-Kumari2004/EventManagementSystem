from models.event_participation import Event_Participation
from repos.event_participationRepo import Event_ParticipationRepo


class Event_Participation(Event_Participation):
    event_participationRepo: Event_ParticipationRepo

    def __init__(self, event_participation: Event_ParticipationRepo):
        self.event_participation = event_participation

    def getbyid(self, id) -> Event_Participation:
        return self.event_participation.getid(id)

    def create(self, Event_Participation):
        return self.event_participation.create(Event_Participation)
