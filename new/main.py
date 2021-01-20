from connection import Connection
from sqlalchemy.sql.chema import MetaData
from sqlalchemy.sql import table,insert



engine = Connection.get_connection()
session = Connection.creat_session()



metadata = MetaData(bind=engine)
student = table('student',metadata,autoload=True)



i insert(student)
i = i.values({"name":"alireza","family":"tofighi","grade":99})
session.excute(i)