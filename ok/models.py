from ok import db

class FPosts(db.Model):
	__tablename__ = "fposts"

	post_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, nullable=False)
	posted_date = db.Column(db.Date, nullable=False)
	content = db.Column(db.String, nullable=False)

	def __init__(self, title, posted_date, content):
		self.post_id = post_id
		self.title = title
		self.posted_date = posted_date
		self.content = content

	def __repr__(self):
		return '<post_id %r>' % (self.body)

