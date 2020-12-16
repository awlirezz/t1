
import mysql.connector as sql

def connect():
    try:
        cnx = sql.connect(user='root', password='alyrzwm',
        host='127.0.0.1', database='gym')
        cursor = cnx.cursor()
        print("Successfully Connected!")
        return cnx, cursor
    except :
        print("Something is wrong with your connection")
        return None, None

def create(cnx, cursor, first_name, last_name, phone, sex):
    data = (first_name, last_name, phone, sex)
    query = """
    INSERT INTO athles
    (first_name, last_name, phone, sex)
    VALUES
    (%s, %s, %s, %s);
    """
    cursor.execute(query, data)
    cnx.commit()
    cursor.close()
    cnx.close()

