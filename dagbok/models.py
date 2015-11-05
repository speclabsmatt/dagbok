from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime
import re

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

