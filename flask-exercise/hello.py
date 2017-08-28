from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask import request,make_response,abort
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask_moment import Moment
from flask import session,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message
import  datetime
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sq;ite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']= True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('zhgmyron@gmail.com')
app.config['MAIL_PASSWORD'] = os.environ.get('Asdfg1234567')
mail= Mail(app)
db = SQLAlchemy(app)
class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    users = db.relationship('User',backref='role',lazy='dynamic')

    def __repr__(self):
        return '<Role %r>'% self.name
class User(db.Model):
    __tablename__= 'users'
    id= db.Column(db.Integer,primary_key=True)
    username= db.Column(db.String(64),unique=True,index=True)
    role_id= db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>'%self.username

class NameForm(FlaskForm):
    name = StringField('what is your name?',validators=[Required()])
    submit =SubmitField('Submit')
manger= Manager(app)

def send_email(to,subject,template,**kwargs)
@app.route('/index')
def hello_world():

    return render_template('index.html',current_time= datetime.datetime.utcnow())
@app.route('/user/<name>')
def user(name):
    return  render_template('user.html',name=name)

@app.route('/',methods=['GET','POST'])
def index():

    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is not None:
            user=User(username =form.name.data)
            db.session.add(user)
            session['known']= False
        else:
            session['known']=True
        session['name']=form.name.data
        form.name.data=''
        return redirect(url_for('index'))
    return  render_template('index.html',form=form,name=session.get('name'),
                            known= session.get('known',False))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
if __name__ == '__main__':
    manger.run()
