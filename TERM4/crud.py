import mysql.connector as sql


def create(name,last_name,b_date,sex,mail,phone,id_n,addr):
    try:
        cnx = sql.connect(user  = 'root'    ,     password =   'alyrzwm'  ,     host     =   '127.0.0.1'     ,   database =   'juniors')
        cursor = cnx.cursor()
        print('Successfully Connected!')



    except:
        print('Something is wrong with your connection')


    query =f"""
    (first_name,last_name,birth_date,sex,email,phone,id_card,address)
    VALUES
    ({name},{last_name},{b_date},{sex},{mail},{phone},{id_n},{addr});
    """    

    cursor.execute(query)
    cnx.commit()


    cursor.close()
    cnx.close()