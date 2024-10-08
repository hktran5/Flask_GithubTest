#from flask import Flask
#app = Flask(__name__)

#@app.route("/") 
#def hello_world(): 
#    return "Hello, World!"
#if __name__ == "__main__": app.run(debug=True)

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/genericdatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Route 1 (page 1) #landing page
@app.route('/')
def home():
    user = User.query.filter_by(email='john@example.com)').first()
    user.name = 'Johnny Doe'
    db.session.commit() #Delete the record
    return render_template('index.html')

#class model
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Route 2 (page 2) #user
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', username=name)

# Route 3 (page 3) #stocks
@app.route("/stocks")
def stocks():
    stocks = ['Apple', 'Microsoft']
    return render_template('stocks.html', stocks=stocks)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/add-product/<product_name>/<price>')
def add_product(product_name, price):
    new_product = Product(product_name=product_name, price=float(price))
    db.session.add(new_product)
    db.session.commit()
    return f"Product {product_name} added with price {price}"

@app.route('/products')
def list_products():
    products = Product.query.all()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)