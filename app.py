from flask import Flask, render_template
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity

from resources.user import UserRegister
from resources.coin import Coin, CoinList
from resources.historical import Historical, HistoricalList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'bmzi'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) # /auth

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


api.add_resource(CoinList, '/coins')
api.add_resource(HistoricalList, '/historicals')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)