from flask_wtf import Form
from wtforms import TextField, DateField, IntegerField, SelectField, PasswordField, DateField
from wtforms.validators import DataRequired

class AddPost(Form):
	post_id = IntegerField('id')
	title = TextField('Title', validators=[DataRequired()])
	posted_date = DateField('Posted')
	content = TextField('Post')
	status = IntegerField('Status')

