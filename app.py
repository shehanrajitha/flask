from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from secuirity import authenticate,identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
import os
import re

uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(uri,'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
app.secret_key='shehan'
jwt = JWT(app,authenticate,identity)








api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList,'/stores')


if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
