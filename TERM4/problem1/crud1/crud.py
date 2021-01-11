import mysql.connector as sql

class Database:


    def __init__(self):
        try:
            self.cnx = sql.connect(user='root', password='alyrzwm',
                host='127.0.0.1', database='juniors')
            self.cursor = self.cnx.cursor()
            print("Successfully Connected!")
            
        except :
            print("Something is wrong with your connection")
            

    def close(self):
        self.cnx.commit()
        self.cnx.close()


    def create(self, name, last_name, b_date, sex, mail, phone, id_n, addr):
        data = (name, last_name, b_date, sex, mail, phone, id_n, addr)
        query = """
        INSERT INTO student
        (first_name, last_name, birth_date, sex, email, phone, id_card, address)
        VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        self.cursor.execute(query, data)
        self.close()

    def read(self):
        query = """
        SELECT * FROM athles;
        """
        self.cursor.execute(query)
        data = cursor.fetchall()
        self.close()
        print("READ SUCCESSFULLY DONE!")
        return data


    def update(self,f,l,p,s,id_):
        data = (val,id_)
        query = "UPDATE student SET "+ col +"=%s WHERE student_id=%s;"
        self.cursor.execute(query, data)
        self.close()



    def delete(self, id_):
        data = (id_, )
        query = """
        DELETE FROM student WHERE student_id=%s;
        """
        self.cursor.execute(query, data)
        self.close()
    
        













