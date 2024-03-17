from init import create_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = create_app()
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