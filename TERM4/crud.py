import mysql.connector as sql

def create():
    try:
        cnx = sql.connect(user  = 'root'    ,     password =   'alyrzwm'  ,     host     =   '127.0.0.1'     ,   database =   'juniors')
        cursor = cnx.cursor()
        print('Successfully Connected!')



    except:
        print('Something is wrong with your connection')


    query ="""
    (first_name,last_name,birth_date,sex,email,phone,id_card,address)
    VALUES
    ('aly','reza','2000,01,01','m','l_awlirezz_l@outlook.com','09029741367','0250612626','Gilan');
    """    

    cursor.execute(query)
    cnx.commit()


    cursor.close()
    cnx.close()