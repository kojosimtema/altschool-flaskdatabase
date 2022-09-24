
import imp
from multiprocessing import context
from sqlite3 import dbapi2
import this
from wsgiref.util import request_uri
from xml.dom.minidom import Document, Element
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
import os

base_dir = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///' + os.path.join(base_dir,'users.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    # registerd_on = db.Column(db.DateTime, default=func.now())
    # updated_on = db.Column(db.DateTime, default=func.now(), onupdate=func.now())
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    # password_hash = db.Column(db.String(100))
    # role = db.relationship('Role', secondary='user_role', backref=db.backref('users', lazy='joined'), uselist=False)

    def __repr__(self):
        return '<user %r>' % self.username

    # def as_dict(self):
    #     return {c.name: getattr(self, c.name) for c in self.__tablename__.columns}

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    
    users = User.query.all()
   
    context = {
        'users':users
    }

    return render_template('index.html', **context)

# @app.route('/users/<name>')
# def success(name):
    
#     return f'welcome {name}'

@app.route('/users', methods=['POST'])
def create_user():
    username = request.form.get('username')
    email = request.form.get('email')
    firstname = request.form.get('fname')
    lastname = request.form.get('lname')
    
    new_user = User(username=username, email=email, firstname=firstname, lastname=lastname)

    
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('home'))


@app.route('/user/<id>')
def get_user(id):
         
    user = User.query.filter_by(id=id)

    return render_template('update.html', users=user)
 

@app.route('/update/<id>', methods=['POST'])
def update_user(id):
    # userid = request.form.get('username')
    user = User.query.filter_by(id=id).first()
    user.username = request.form.get('username')
    # user.username = new_username
    user.email = request.form.get('email')
    user.firstname = request.form.get('fname')
    user.lastname = request.form.get('lname')
    
   
    db.session.add(user)
    db.session.commit()
    
    return redirect(url_for('home'))

@app.route('/delete/<id>', methods=['GET'])
def delete_user(id):
         
    user = User.query.filter_by(id=id).first()

    db.session.delete(user)
    db.session.commit()

    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)