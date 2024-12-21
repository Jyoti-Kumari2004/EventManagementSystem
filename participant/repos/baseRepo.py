from sqlalchemy import create_engine 
import constants
class BaseRepo:
    engine:object 

    def __init__(self):
        self.engine = create_engine(constants.DATABASE_URL)
        