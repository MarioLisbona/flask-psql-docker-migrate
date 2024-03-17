from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, jsonify
from routes import init_routes
import os

# creates an application that is named after the name of the file
app = Flask(__name__)

app.config["SECRET_KEY"] = "some_dev_key"
print(os.environ.get('DATABASE_URL'))
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://mario:mypassword@pgsql:5432/todos"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')

# initializing routes
init_routes(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    def __repr__(self):
        return f"<Product {self.name}>"
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5007')