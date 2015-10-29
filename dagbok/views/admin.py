from flask import Blueprint, render_template
from dagbok.database import db_session
from dagbok.models import User, Entry

admin = Blueprint('admin', __name__)

@admin.route('/')
def login():
    #TODO: implement login
    render_template("layout.html")

