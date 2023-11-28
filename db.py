import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

class Database:

    def __init__(self):
        self.host = os.getenv('host')
        self.user =  os.getenv('user')
        self.password =  os.getenv('password')
        self.database = os.getenv('database')

    def connectDB(self):
        conn =  mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

        return conn