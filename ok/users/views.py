from ok import db
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from ok.views import login_required, flash_errors
from forms import RegisterForm, LoginForm
from ok.models import User
from sqlalchemy.exc import IntegrityError

#here is where I want to draw from one static folder rather than many
#changing the static_folder may be necessary here
mod = Blueprint('users', __name__, url_prefix='/users', template_folder='templates', static_folder='static')

@mod.route('/logout/')
def logout():
	session.pop('logged_in', None)
	session.pop('user_id', None)
	flash('You are logged out.')
	return redirect(url_for('.login'))

@mod.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		u = User.query.filter_by(name=request.form['name'],
			password=request.form['password']).first()   #still not sure what this .first method is
			if u is None:
				error = 'Invalid credentials'
			else:
				session['logged_in'] = True
				session['user_id'] = u.id
				flash('you are logged in')
				return redirect(url_for('shared_data.main')) #make sure to add your shared_data.main then
	return render_template("users/login.html", form = LoginForm(request.form), error=error)

@mod.route('/register/', methods=['GET','POST'])
def register():
	error = None
	form = RegisterForm(request.form, csrf_enabled=False)
	if form.validate_on_submit():
		new_user = User(form.name.data,
						form.email.data,
						form.password.data, # again, why is there an extra comma in here
						)	# this makes my python sense tingle