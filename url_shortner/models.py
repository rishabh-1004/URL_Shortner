import string
from datetime import datetime
from .extensions import db
from random import choices

class Link(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(5),unique=True)
    visits=db.Column(db.Integer,default=0)
    date_created= db.Column(db.DateTime,default=datetime.now)

    # Automatically start creation of short url when a new Link is added
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url=self.generate_short_link()

    # Generate short Link with random charecters and numbers
    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        short_url= ''.join(choices(characters,k=5))

        link=self.query.filter_by(short_url=short_url).first()

        if link:
            return self.generate_short_link()
        
        return short_url