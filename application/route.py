from application import app
from flask import Flask, render_template, request, flash, redirect, url_for
from .form import TodoForm
from datetime import datetime
from application import db
from bson import ObjectId, objectid

@app.route('/')
def index():
    todos = []
    for todo in db.userData.find().sort('competed_date', -1):
        todo['_id'] = str(todo['_id'])
        todo['completed_date'] = todo['completed_date'].strftime('%b %d %Y %H:%M%S')
        todos.append(todo)
    return render_template('view_todo.html', title = 'Page', todos = todos)

@app.route('/add_todo', methods = ['POST', 'GET'])
def add_todo():
    if request.method == 'POST':
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        todo_completed = form.completed.data
        doc = {
            'name': todo_name,
            'description': todo_description,
            'completed': todo_completed,
            'completed_date': datetime.now(),
        }
        db.userData.insert_one(doc)
        flash('Data Inseted Successfully', 'success')
        return redirect('/')
    else:
        form = TodoForm()
    return render_template('add_todo.html', form = form)

@app.route('/update/<id>', methods=['POST', 'GET'])
def update_todo(id):
    # print('name')
    # print(request.method)

    if request.method == 'POST':
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        todo_completed = form.completed.data

        db.userData.find_one_and_update({'_id': ObjectId(id)}, {'$set': {
           'name': todo_name,
            'description': todo_description,
            'completed': todo_completed,
            'completed_date': datetime.now(), 
        }})
        flash('Successfully Updated..', "success")
        return redirect('/')
    else:
        # print('done')
        form = TodoForm()
        todo = db.userData.find_one({'_id': ObjectId(id)})
        form.name.data = todo.get('name', None)
        form.description.data = todo.get('description', None)
        form.completed.data = todo.get('completed', None)

    return render_template('add_todo.html', form = form)

@app.route('/delete_todo/<id>')
def delete_todo(id):
    db.userData.find_one_and_delete({'_id': ObjectId(id)})
    flash('Deleted Successfully', "success")
    return redirect('/')
