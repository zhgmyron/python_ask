# -*- coding: UTF-8 -*-
from app import db
from hashlib import md5

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    nickname = db.Column(db.String(64),index= True,unique= True)
    email = db.Column(db.String(120),index= True,unique= True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    role_id= db.Column(db.Integer,db.ForeignKey('roles.id'))
    about_me= db.Column(db.String(140))
    last_seen = db.Column(db.DATETIME)

    @property
    def is_authenticated(self):
       return True
    @property
    def is_active(self):
        return True
    @property
    def is_anonymous(self):
        return False
    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)


    def __repr__(self):
        return '<User %r>' %(self.nickname)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)

    users = db.relationship('User',backref ='role')

    def __repr__(self):
        return '<Role %r' %self.name

class Post(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DATETIME)

    user_id= db.Column(db.Integer,db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
# class User(db.Model):
#     # ...
#     def avatar(self, size):
#         return 'http://www.gravatar.com/avatar/' + md5(self.email).hexdigest() + '?d=mm&s=' + str(size)
#