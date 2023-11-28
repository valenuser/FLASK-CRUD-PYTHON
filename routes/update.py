from flask import Flask, redirect

from db import Database

user = Database()

app =  Flask(__name__, template_folder="public")

def update(nombre,foto,id):
    conn = user.connectDB()
    try:
        if conn.is_connected():

            cursor = conn.cursor()

            cursor.execute("update user set nombre = '{}', user_foto = '{}' where id = '{}' ".format(nombre,foto,id))

            conn.commit()

            return redirect('/')

    except Exception as e:
       print(e)
       return redirect('/')