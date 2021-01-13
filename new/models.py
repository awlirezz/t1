from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()




class Student(Base):
    __tablename__ = 'Student'


    studentId = Column()
    name = 
    family = 
    grade = 
    created_at = 