from crud import connect,create

cnx,cursor= connect()
create(cnx,cursor,'Antonio','jamali','2001-01-001','m','a@a.com','09123145687','2345697896','asd')