from flask import Flask, render_template
from views.admin import admin
from models import Entry

dagbok = Flask(__name__)
dagbok.register_blueprint(admin, url_prefix='/admin')

@dagbok.route("/")
def home():
    main_entry = Entry.query.order_by(Entry.pub_date.desc()).first()
    return render_template('home.html', main_entry=main_entry, title = "Home")

