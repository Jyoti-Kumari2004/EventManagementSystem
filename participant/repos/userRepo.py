
from sqlalchemy import text
from .baseRepo import BaseRepo
from sqlalchemy import create_engine
from models.user import User
from mysql.connector import Error
class UserRepo(BaseRepo):
    def __init__(self):
        super().__init__()
    def get(self,id):
        with self.engine.connect() as conn:
            query=f"select id ,name,contact,email from participant where id={id}"
            result=conn.execute(text(query))
            row=result.fetchone()
            return User.model_construct({'id','name','contact','email'},**row._mapping)
    def createUser(self,user:User):
        with self.engine.connect() as conn:
            query=f"insert into participant (id,name,contact,email) values ({user.id},'{user.name}','{user.contact}','{user.email}')"
            conn.execute(text(query))
            conn.commit()
            
    def updateUser(self,id,user):
        try:
            with self.engine.connect() as conn:
                query=text(f"Update participant set name=:name,contact=:contact,email=:email where id={id}")
                result=conn.execute(query, { "name": user.name, "contact":user.contact,"email":user.email})
                conn.commit()
              
                return {"name":user.name,"contact":user.contact,"email":user.email}
        except Error as err:
            print(f"Error:{err}")
    def deleteit(self,id):
        try:
            with self.engine.connect() as conn:
                query=f"DELETE FROM participant WHERE id={id}"
                conn.execute(text(query))
                conn.commit()
        except Error as err:
            print(f"Error : {err}")
        
