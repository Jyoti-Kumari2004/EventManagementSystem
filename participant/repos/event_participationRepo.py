# from sqlalchemy import text
# from .baseRepo import BaseRepo
# from sqlalchemy import create_engine
# from models.event import Event
# from mysql.connector import Error


# class Event_ParticipationRepo(BaseRepo):
#     def __init__(self):
#         super().__init__()
#     def get(self,id):
#         with self.engine.connect() as conn:
#             query=f"select  from participant where id={id}"
#             result=conn.execute(text(query))
#             row=result.fetchone()
#             return User.model_construct({'id','name','contact','email'},**row._mapping)
#     def create(self,user:User):
#         with self.engine.connect() as conn:
#             query=f"insert into participant (id,name,contact,email) values ({user.id},'{user.name}','{user.contact}','{user.email}')"
#             conn.execute(text(query))
#             conn.commit()
