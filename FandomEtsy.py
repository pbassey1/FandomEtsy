import mysql.connector

#Connecting to MySQL and Defining Cursor

db = mysql.connector.connect(user="root", host = "localhost", port="3306", passwd="admin", database = "testdatabase")
myC = db.cursor()

#Creating Tables

# myC.execute("CREATE TABLE client (client_id int AUTO_INCREMENT, name VARCHAR (100), PRIMARY KEY (client_id))")
# myC.execute("CREATE TABLE orders (order_number int, order_status VARCHAR (100), client_id int, plu int, FOREIGN KEY (client_id) references client(client_id))")
# myC.execute("CREATE TABLE products (item VARCHAR (100), plu int)")

#CRUD Operations
#Create
client_name = input("What column whould you like to add to? ")
name_of_client = input("What is the name of the client? ") 

myC.execute("INSERT INTO client (%s) VALUES ('%s')",(client_name, name_of_client))
db.commit()

#Read
query = input("What would you like to query for? ")
table_name = input("What table would you like to query in? ")

myC.execute("SELECT (%s) FROM (%s)", (query, table_name))

for x in myC:
    print(x)

#Update


#User Inputs

