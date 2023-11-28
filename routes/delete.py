from flask import Flask, redirect

from db import Database

user = Database()

app =  Flask(__name__, template_folder="public")

def delete(id):
    conn = user.connectDB()
    try:
        if conn.is_connected():

            cursor = conn.cursor()

            cursor.execute('delete from user where id = {}'.format(id))

            conn.commit()

            return redirect('/')

    except Exception as e:
       print(e)
       return redirect('/')