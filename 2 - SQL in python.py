from dbmodule import connect

# Create a connection object
connection = connect.('database', 'username', 'pswd')

# Create a cursor object
cursor = connection.cursor()

# Run queries
cursor.execute('select * from mytable')
results = cursor.fetchall()

# Free the resources and always make sure to close any connections
cursor.close()
connection.close()
