from ok import db
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from ok.views import login_required, flash_errors
from forms import AddPost
from ok.models import FPosts

mod = Blueprint('shared_data', __name__, url_prefix='/shared_data', template_folder='templates', static_folder='static')

@mod.route('/grid')
@login_required
def posts_grid():
	open_posts = db.session.query(FPosts).filter_by(status='1').order_by(FPosts.posted_date.asc())
	old_posts = db.session.query(FPosts).filter_by(status='0').order_by(FPosts.posted_date.acs())
	return render_template('shared_data/grid.html', form=AddPost(request.form), open_posts=open_posts, old_posts=old_posts)


@mod.route('/add/', methods=['GET', 'POST'])
@login_required
def new_post():
	#make sure you know what this request method is and does
	form = AddPost(request.form, csrf_enabled=False)
	if form.validate_on_submit():
		new_post = FPosts(form.title.data,
						  form.posted_date.data,
						  form.content.data,
						  '1',
						  session['user_id']
						  )
		db.session.add(new_post)
		db.session.commit()
		flash('New entry was successfully posted')
	else:
		flash_errors(form)
	return redirect(url_for('.grid'))

@mod.route('/mark_old/<int:post_id>/',)
@login_required
def old(post_id):
	new_id = post_id
	#I'm not really understand this new_id convention
	db.session.query(FPosts).filter_by(post_id=new_id).update({'status':'0'})
	db.session.commit()
	flash('This post was marked old')
	return redirect(url_for('.grid'))

@mod.route('/delete/<int:post_id>/',)
@login_required
def delete(post_id):
	new_id = post_id
	#I'm not really understand this new_id=post_id and vice versa convention
	db.session.query(FPosts).filter_by(post_id=new_id).delete()
	db.session.commit()
	flash('This post was deleted')
	return redirect(url_for('.grid'))



