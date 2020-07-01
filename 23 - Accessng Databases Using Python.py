from dbmodule import connect

# Create connection object
Connection = connect('databasename', 'username', 'pswd')

# Create a cursor object
Cursor = connection.cursor()

# Run queries
Cursor.excecute('select * from mytable')
Results = cursor.fetchall()

# Free resources
Cursor.close()
Connection.close()

# Identify database connection credentials
import imb_db

dsn_driver = 'IBM DB" ODBC DRIVER'
dsn_database = 'BLUDB'
dsn_hostname = 'dashdb-entry-yp-da110-01.services.dal.bluemix.net'
dsn_port = '50001'
dsn_protocol = 'TCPIP'
dsn_uid = 'dash***'
dsn_pwd = '****'

# Create a database connection
dsn = (
   'DRIVER = {{IBM DB" ODBC DRIVER}};'
   'DATABASE = {0};'
   'HOSTNAME = {1};'
   'PORT = {2};'
   'PROTOCOL = TCPIP;'
   'UID = {3};'
   'PWD = {4};').format(dsn_database, dsn_hostname, dsn_port, dsn_uid, dsn_pwd)

try:
   conn = ibm_db.connect(dsn, "", "")
   print('Connected!')

except:
   print('Unable to connect to database')

# Close the database connetion
ibmd_db.close(conn)
