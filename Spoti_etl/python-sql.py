import pyodbc

server = 'Mi_DataBase.mssql.somee.com'
database = 'Mi_DataBase'
username = 'esteban_SQLLogin_1'
password = 'doyz7qycgl'

# Establishing a connection to the SQL Server
connection  = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                      SERVER='+server+';\
                      DATABASE='+database+';\
                      UID='+username+';\
                      PWD='+ password)
            
cursor = connection.cursor()

query = "select * from artist"
cursor.execute(query)


# Fetch one row at a time
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()

# Fetch all rows at once
rows = cursor.fetchall()
for row in rows:
    print(row)


cursor.close()