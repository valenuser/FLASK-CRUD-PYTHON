from flask import Flask, render_template

from db import Database

user = Database()

app =  Flask(__name__, template_folder="public")

def index():
    conn = user.connectDB()

    if conn.is_connected():

        cursor = conn.cursor()

        cursor.execute('select * from user')

        datos = cursor.fetchall()


        if len(datos) == 0:
            return render_template("index.html")
        else:
            return render_template("index.html",datos=datos)




