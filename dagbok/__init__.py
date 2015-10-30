from flask import Flask, render_template
from views.admin import admin
from models import Entry

app = Flask(__name__)
app.config.from_pyfile('dagbok.cfg')
app.register_blueprint(admin, url_prefix='/admin')
app.debug = True

@app.route("/")
def home():
    main_entry = Entry.query.order_by(Entry.pub_date.desc()).first()
    return render_template('home.html', main_entry=main_entry, title = "Home")

