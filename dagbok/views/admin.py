from flask import Blueprint, render_template, request, current_app, session, \
     redirect, url_for
from dagbok.database import db_session
from dagbok.models import User, Entry

admin = Blueprint('admin', __name__)

@admin.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('admin.login'))
    return render_template('admin.html')

@admin.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != current_app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != current_app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['username'] = request.form['username']
            session['logged_in'] = True
            return redirect(url_for('admin.index'))
    return render_template('login.html', error=error)

@admin.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('show_entries'))

@admin.route('/post', methods=['GET', 'POST'])
def post_entry():
    if request.method == 'GET':
        return render_template('post_entry.html')
    if not session.get('logged_in'):
        abort(401)
    entry = Entry(request.form['title'], request.form['body'],
                  request.form['tags'])
    db_session.add(entry)
    db_session.commit()
    return redirect(url_for('home'))
