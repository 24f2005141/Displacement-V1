from flask import Flask,render_template,request,url_for,redirect,flash,session,jsonify
from models import *
from werkzeug.security import generate_password_hash, check_password_hash  
import os
from werkzeug.utils import secure_filename


app=Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///displacement.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
def initialize_admin():
    with app.app_context():
        if not users.query.filter_by(username='admin').first():
            admin = users(username='admin', email='admin@displacement', password_hash=generate_password_hash('admin123'), role='admin')
            db.session.add(admin)
            db.session.commit()
with app.app_context():
    db.create_all()

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        form_id = request.form.get('form_id')
        if form_id=='signUpForm':
            name=request.form['signUpName']
            email=request.form['signUpEmail']
            phone=request.form['signUpPhone']
            password=request.form['signUpPassword']
            user=users(username=name,email=email,phone_no=phone,password_hash=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            flash("Account created successfully!","success")
            return redirect(url_for('index'))
        if form_id=='signInForm':
            email=request.form['signInEmail']
            password=request.form['signInPassword']
            user=users.query.filter_by(email=email).first()
            if user and check_password_hash(user.password_hash,password):
                session['user_id'] = user.id
                return redirect(url_for('dashboard',username=user.username))
            else:
                flash("Invalid email or password","danger")
                return redirect(url_for('index'))

    return render_template('index.html')
@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        name=request.form['fullName']
        email=request.form['email']
        phone=request.form['phone']
        password=request.form['password']
        user=users(username=name,email=email,phone_no=phone,password_hash=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        flash("Account created successfully!","success")
        return redirect(url_for('signin'))
    return render_template('signup.html')
@app.route('/signin',methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        email = request.form.get('email')  # ✅ use parentheses
        password=request.form.get('password')
        user=users.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash,password):
            session['user_id'] = user.id
            print("ok")
            return redirect(url_for('user_dashboard',username=user.username))
        else:
            print("not ok")
            flash("Invalid email or password","danger")
            return redirect(url_for('index'))
    return render_template('signin.html')  
@app.route('/user/<username>',methods=['GET'])
def user_dashboard(username):
    return render_template('user/dashboard.html',user=users.query.filter_by(username=username).first())

def to_bool(value):
    return value == 'on'
@app.route('/user/rental', methods=['GET','POST'])
def rental():
    if request.method == 'POST':
        pincode=request.form.get('pin_code')
        address=request.form.get('address')
        gmap_link=request.form.get('gmap_link')
        security=to_bool(request.form.get('security'))
        cctv=to_bool(request.form.get('cctv'))
        covered=to_bool(request.form.get('covered'))
        length=float(request.form.get('length', 0))
        width=float(request.form.get('width', 0))
        price=float(request.form.get('price', 0))
        space=ParkingSpace(owner_id=session['user_id'],pin_code=pincode,address=address,gmap_link=gmap_link,security=security,cctv=cctv,covered=covered,length=length,width=width,price=price)
        db.session.add(space)
        db.session.commit()
        return render_template('user/dashboard.html',user=users.query.filter_by(id=session['user_id']).first())
    return render_template('user/rental.html')
@app.route('/user/my_reservations')
def my_reservations():
    user_id = session['user_id']
    spaces = ParkingSpace.query.filter_by(owner_id=user_id).all()
    return render_template('user/spaces.html', spaces=spaces)
@app.route('/user/service')
def service():
    return render_template('user/parking_services_page.html')
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))
with app.app_context():
    db.create_all()
    initialize_admin()
    print("Database created")

if __name__ == "__main__":
    app.run(debug=True)

