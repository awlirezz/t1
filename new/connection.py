from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Connection:
    def __init__(self):            #engine://username:password@localhost/database
        self.engine = create_engine('mysql+pymysql://root:alyrzwm@localhost/a')

    def get_connection(self):
        return self.engine

    def create_session(self):
        Session = sessionmaker(bind=self.get_connection())
        return Session




        










