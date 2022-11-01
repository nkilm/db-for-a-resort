import mysql.connector
from dotenv import load_dotenv
from os import environ

load_dotenv()

def connect():
    """ Establish connection to mysql database. Returns a cursor """
    db = mysql.connector.connect(
        host=environ.get("HOST"),
        user=environ.get("USER"),
    )

    if(db.is_connected()):
        print("DB Connected")
    else:
        print("DB Connection not successful")

    cursor = db.cursor()
    return cursor
