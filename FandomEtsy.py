import mysql.connector
import re

#Connecting to MySQL and Defining Cursor

db = mysql.connector.connect(user="root", host = "localhost", port="3306", passwd="admin", database = "testdatabase")
myC = db.cursor()

#Creating Tables

# myC.execute("CREATE TABLE client (client_id int AUTO_INCREMENT, name VARCHAR (100), PRIMARY KEY (client_id))")
# myC.execute("CREATE TABLE orders (order_number int, order_status VARCHAR (100), client_id int, plu int, FOREIGN KEY (client_id) references client(client_id))")
# myC.execute("CREATE TABLE products (item VARCHAR (100), plu int)")

#CRUD Operations
#Create

def createClient():
    name_of_client = input("What is the name of the client? ") 
    for i in name_of_client:
        if not (i.isalpha() or i in ("'","-",".")):
            raise Exception("Name contained an invalid character.")

    myC.execute(f"INSERT INTO client (name) VALUES ({name_of_client})")
    db.commit()

#Read

def readTable():
    query = input("What would you like to query for? ")
    table_name = input("What table would you like to use? ")

    myC.execute(f"SELECT {query} FROM {table_name}")

    for x in myC:
        print(x)

#Update

def updateTable():
    table_name = input("What table would you like to use? ")
    col1 = input("What column would you like to change? " )
    val1 = input("What would you like to set the new value to? ")
    col2 = input("What is the key column? ")
    val2 = input("What is the key? ")

    myC.execute(f"UPDATE {table_name} SET {col1} = '{val1}' WHERE {col2} = {val2}")
    db.commit()

#Delete

def deleteRecord():
    table_name = input("What table would you like to use? ")
    col2 = input("What is the key column? ")
    val2 = input("What is the key? ")
    myC.execute(f"DELETE FROM {table_name} WHERE {col2} = {val2}")
    db.commit()

#Menu

menu_options = {
    1: 'Create a New Client',
    2: 'Read a Table',
    3: 'Update a Table',
    4: 'Delete a Record',
    5: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def startup():
    while (True):
        print_menu()
        option = ''
        try:
            option = int(input("Choose an option: "))
        except:
            print("Invalid input. Please enter a number")
        if option == 1:
            createClient()
        elif option == 2:
            readTable()
        elif option == 3:
            updateTable()
        elif option == 4:
            deleteRecord()
        elif option == 5:
            print("Thank you for visiting! ")
            exit()
        else:
            print("Invalid option. Please input a number between 1 and 5.")
startup()