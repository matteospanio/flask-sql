from sqlalchemy.orm import relationship
from sqlalchemy import *
from . import db


class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')


    def __repr__(self):
        return f'<Role: {self.name}>'


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, nullable=False)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


    def __init__(self, username, email, password):
        self.username = username
        self.password = password
        self.email = email


    def __repr__(self):
        return f'<User: {self.username}>'
