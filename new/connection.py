from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
class Connection:
    def __init__(self):
        self.engine = create_engine('mysql://root:alyrzwm@localhost/a')




    def get_conncetion(self):
        return self.engine



    def create_session(self):
        Session=sessionmaker(bind=self.get_connection())
        return Session    










