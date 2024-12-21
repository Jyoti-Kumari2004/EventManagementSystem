from sqlalchemy import text
from .baseRepo import BaseRepo
from sqlalchemy import create_engine
from models.event import Event
from mysql.connector import Error


class EventRepo(BaseRepo):
    def __init__(self):
        super().__init__()

    def getid(self, id):
        with self.engine.connect() as conn:
            query = f"select id ,name,venue,startDate,endDate,description from event where id={id}"
            result = conn.execute(text(query))
            row = result.fetchone()
            return Event.model_construct(
                {"id", "name", "venue", "startDate", "endDate", "description"},
                **row._mapping,
            )

    def createEvent(self, event: Event):
        with self.engine.connect() as conn:
            query = f"insert into event (id,name,venue,startDate,endDate,description) values ({event.id},'{event.name}','{event.venue}','{event.startDate}','{event.endDate}','{event.description}')"
            conn.execute(text(query))
            conn.commit()

    def updateEvent(self, id, event: Event):
        try:
            with self.engine.connect() as conn:
                query = text(
                    f"Update event set name=:name,venue=:venue,startDate=:startDate,endDate=:endDate, description=:description where id={id} "
                )
                conn.execute(
                    query,
                    {
                        "name": event.name,
                        "venue": event.venue,
                        "startDate": event.startDate,
                        "endDate": event.endDate,
                        "description": event.description,
                    },
                )
                conn.commit()
                return {
                    "name": event.name,
                    "venue": event.venue,
                    "startDate": event.startDate,
                    "endDate": event.endDate,
                    "description": event.description,
                }
        except Error as err:
            print(f"Error:{err}")

    def deleteit(self, id):
        try:
            with self.engine.connect() as conn:
                query = f"DELETE FROM event WHERE id={id}"
                conn.execute(text(query))
                conn.commit()
        except Error as err:
            print(f"Error : {err}")
