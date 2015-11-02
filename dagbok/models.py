from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime
import re

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    slug = Column(String(100))
    summary = Column(String(250))
    body = Column(Text)
    pub_date = Column(DateTime)
    tags = Column(String(100))

    def __init__(self, title, summary, body, tags, pub_date=None):
        self.title = title
        self.summary = summary
        self.slug = re.sub('[^\w]+', '_', self.title.lower())
        self.body = body
        if pub_date is None:
            pub_date = datetime.now()
        self.pub_date = pub_date
        self.tags = tags

    def __repr__(self):
        return '<Post %r>' % self.title

