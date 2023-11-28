from flask import Flask, render_template, request, redirect

from routes.index import index

from routes.create import create

from routes.delete import delete

from routes.update import update


app =  Flask(__name__, template_folder="public")


@app.route('/')
def route_main():
    return index()

@app.route('/create')
def route_create():
    return render_template('crear.html')

@app.post('/create')
def insert_user():
    data = request.form

    name =  data['Nombre']
    foto = data['Foto']
    create(name,foto)

    return redirect('/')

@app.route('/delete')
def route_delete():
    return render_template('borrar.html')

@app.post('/delete')
def delete_user():
    data = request.form
    id =  data['id']

    try:
        int(id)

        if id.isdigit():
            return delete(id)
        else:
            return redirect('/')
    
    except Exception as e:
            return redirect('/')
    

    
@app.route('/update')
def route_update():
    return render_template('update.html')

@app.post('/update')
def update_user():
    data = request.form

    nombre = data['Nombre']
    foto = data['Foto']
    id = data['id']

    try:
        int(id)

        if id.isdigit():
            return update(nombre,foto,id)
        else:
            return redirect('/')
    
    except Exception as e:
            return redirect('/')

if __name__ ==  '__main__':
    app.run(port=3000, debug=True)