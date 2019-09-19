from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_suer, logout_user, login_required
from malarianet import db
from malarianet.users import User
from malarianet.users.forms import LoginForm, RegistrationForm


users = Blueprint('users',__name__)

@users.route('/register',methods=['GET','POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.username.password)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('register.html',form=form)


@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.index'))

@users.route('/login',methods=['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('You have been logged in!')

            next = request.args.get('next')
            if next==None or next[0]!='/':
                next = 'core.index'

            return redirect(url_for(next))
    return render_template('login.html',form=form)
