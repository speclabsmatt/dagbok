from flask import Flask, render_template, redirect, url_for
from views.admin import admin
from models import Entry

app = Flask(__name__)
app.config.from_pyfile('dagbok.cfg')
app.register_blueprint(admin, url_prefix='/admin')
app.debug = True

@app.route("/")
def home():
    main_entry = Entry.query.order_by(Entry.pub_date.desc()).first()
    entries = Entry.query.order_by(Entry.pub_date.desc()).limit(4).offset(1)
    has_next = (Entry.query.count() > 5)
    next_page = 2
    return render_template('home.html', main_entry=main_entry, entries=entries,
                           has_next=has_next, next_page=next_page, title = "Home")

@app.route("/page/<int:page_num>")
def page(page_num):
    if (page_num == 1):
        return redirect(url_for('home'))
    offset = 5 + ((page_num - 2) * 5)
    entries = Entry.query.order_by(Entry.pub_date.desc()).limit(5).offset(offset)
    has_next = (Entry.query.count() > (offset + 5))
    next_page = page_num + 1
    prev_page = page_num - 1
    return render_template('blog_page.html', entries=entries, has_next=has_next,
                           next_page=next_page, prev_page=prev_page, title = "Blog")

