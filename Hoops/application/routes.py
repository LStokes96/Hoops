from flask import render_template, url_for, redirect, request
from application import app, db, bcrypt 
from application.models import Comments, Users, Players
from application.forms import CommentForm, RegistrationForm, LoginForm, UpdateCommentForm, DeleteCommentForm
from flask_login import login_required, login_user, current_user, logout_user 


@app.route('/')
@app.route('/home')
def home():
    postData = Comments.query.all()
    return render_template('home.html', title='Home', comments=postData)

@app.route('/players')
def players():
    playerData = Players.query.all()
    return render_template('players.html', title='Players', players=playerData )

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                password=hash_pw)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('comment'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route('/comment', methods=['GET', 'POST'])
@login_required
def comment():
    form = CommentForm()
    if form.validate_on_submit():
        if Players.query.filter_by(name=form.player.data).first():
            postData = Comments(
                    title = form.title.data,
                    content = form.content.data,
                    author = current_user,
                    player =  Players.query.filter_by(name=form.player.data).first()

                )   
            db.session.add(postData)
            db.session.commit()

            return redirect(url_for('home'))
        else:
            postData = Comments(
                    title = form.title.data,
                    content = form.content.data,
                    author = current_user,
                    player = Players(name=(form.player.data))

                )
            db.session.add(postData)
            db.session.commit()

            return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('comment.html', title='Comment', form=form)


@app.route('/update', methods=['GET','POST'])
@login_required
def update():
    form = UpdateCommentForm()
    if form.validate_on_submit():
        user = current_user.id
        if Comments.query.filter_by(user_id=user).first():
            old = Comments.query.filter_by(id=form.comment_id.data).first()
            old.title = form.title.data
            old.content = form.content.data
            old.player = Players.query.filter_by(name=form.player.data).first()
            db.session.commit()
            return redirect(url_for('home'))
        else:
            return redirect(url_for('home'))
    return render_template('update.html', title='Update', form=form)


@app.route('/delete', methods=['GET', 'POST'])
@login_required
def delete():
    form = DeleteCommentForm()
    if form.validate_on_submit():
        user = current_user.id
        if Comments.query.filter_by(user_id=user).first():
            comment_d = Comments.query.filter_by(id=form.comment_id.data).first()
            db.session.delete(comment_d)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            return redirect(url_for('home'))
    return render_template('delete.html', title='Delete', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
