from flask import Flask, render_template, redirect, url_for

from db import Database

user = Database()

app =  Flask(__name__, template_folder="public")

def create(nombre,foto):
    conn = user.connectDB()
    try:
        if conn.is_connected():

            cursor = conn.cursor()

            cursor.execute("insert into user(nombre,user_foto) values ('{}','{}')".format(nombre,foto))

            conn.commit()


    except Exception as e:
        print(e)


