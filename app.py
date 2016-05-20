from flask import Flask
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'It just a secret key'
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class Results(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    address = db.Column(db.Text, unique=True)
    telephone = db.Column(db.Text)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/init')
def init_search():
    from find_it import Searcher
    searcher = Searcher('手机$数码$通信$通讯', 23.0525730000, 113.1989640000, 23.2904550000, 113.5010820000)
    searcher.get_all_data()

if __name__ == '__main__':
    app.run(debug=True)
