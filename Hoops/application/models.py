from application import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    comments = db.relationship('Comments', backref='author', lazy=True)

    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n', 'Email: ', self.email, '\r\n', 'Name: ', self.first_name, ' ', self.last_name])


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    player_name = db.relationship('Players')
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return ''.join([
            'User ID: ', self.user_id, '\r\n',
            'Player ID; ', self.player_id, '\r\n',
            'Title: ', self.title, '\r\n', self.content
            ])


class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    comments = db.relationship('Comments', backref='player', lazy=True)

    def __repr__(self):
        return ''.join([
            'PlayerID: ', str(self.id), '\r\n',
            'Name: ' , self.name, 
            ])

