from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime,TIMESTAMP
from connection import Connection
from sqlalchemy.sql.function import func


Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    studentId  = Column(Integer(), primary_key=True, autoincrement=True)
    first_name = Column(String(225)) 
    last_name  = Column(String(225))
    birth_name = Column(Date)
    grade      = Column(Integer
    level      = Column(Integer)
    updated_at = Column(TIMESTAMP,server_default = func.now(),onedate = func.current_timestamp()) 


    def __init__(self, f_n, l_n,b_d , g , l):
        self.first_name = f_n
        self.last_name = l_n
        self.birth_date = b_d
        self.grade = g
        self.level = l

engine = Connection().get_connection()
if not engine.dialect.has_table(engine, 'student'):  # If table don't exist, Create. 
    Base.metadata.create_all(engine, checkfirst=True)
    print('Database Created')
else:
    print('Database {} exists!'.format('student'))