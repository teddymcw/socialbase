from ok import db
from ok.models import FPosts
from datetime import date 

db.create_all()

#insert mock data
db.session.add(FPosts("Fake Title", date(2014, 1, 4), "This is a fake and really, really short post", 1)

db.session.commit()
