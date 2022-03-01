from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message
from sqlalchemy.orm import synonym

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/fitness_contact'
db = SQLAlchemy(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['mail_port'] = '465'
app.config['MAIL_USERNAME'] = "abhishekintheair001@gmail.com"
app.config['MAIL_PASSWORD'] = "bhaihain001"
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] =False


mail = Mail(app)

app.secret_key = 'super-secret-key'

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    phone_no = db.Column(db.String(12), nullable=True)
    msg = db.Column(db.String(120),nullable=True)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contact", methods =['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone_no = request.form.get('phone_no')
        msg = request.form.get('message')
        entry = Contacts(name = name, email=email,phone_no=phone_no,msg=msg)
        db.session.add(entry)
        db.session.commit() 
        message = Message("hello " + name, sender="abhsihekintheair001@gamil.com", recipients=[email])
        message.body = msg +"/n" + phone_no
        mail.send(message)
    return render_template("contact.html")

@app.route("/foods")
def foods():
    return render_template("foods.html")

@app.route("/blogs")
def blogs():
    return render_template("blogs.html")

@app.route("/training")
def training():
    return render_template("training.html")

app.run(debug=True)

