from flask import request, render_template, redirect, url_for
from flask import current_app as app
from .models import db, User, Address
from flask_login import current_user, login_required, login_user


# def validate_mobileNo(mobileNo):
#     user = User.query.filter_by(mobileNo).first()
#     if user is not None:
#         raise Exception('Please use a different username.')
#
#
# def validate_email(self, email):
#     user = User.query.filter_by(email=email).first()
#     if user is not None:
#         raise Exception('Please use a different email address.')


# Register User(Default Field)
@app.route('/', methods=['POST', 'GET'])
@app.route('/register', methods=['POST', 'GET'])
def register():
    """Register new user"""

    if request.method == "POST":
        # Fetching all values from form for user registration
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        print(password)
        mobileNo = request.form['mobileNo']
        houseNo = request.form['houseNo']
        addressLine1 = request.form['addressLine1']
        addressLine2 = request.form['addressLine2']
        city = request.form['city']
        state = request.form['state']
        pincode = request.form['pincode']

        try:
            # Adding address for new user
            newAddress = Address(houseNo=houseNo, addressLine1=addressLine1, addressLine2=addressLine2, city=city,
                                 state=state, pincode=pincode)
            db.session.add(newAddress)
            db.session.commit()

            # Adding remaining user details for new user
            newUser = User(name=name, email=email, password=password, mobileNo=mobileNo, addressID=newAddress.id)
            db.session.add(newUser)
            db.session.commit()
        except:
            return "User with the same details exists. Please Login"

        return redirect(url_for("login"))
    else:
        return render_template('register.html')



@app.route('/login', methods=['POST', 'GET'])
def login():
    """Login User"""

    # If a logged in user tries to open the login page, then it should automatically get redirected to welcome page
    if current_user.is_authenticated:
        return redirect(url_for('welcome'))
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        login = User.query.filter_by(email=email, password=password).first()
        # Checking if a user exists, if yes then allow it to move to a different page
        if login is not None:
            login_user(login)
            return redirect(url_for("welcome"))
        return render_template("login.html")
    else:
        return render_template('login.html')


# Currently updating name to new one
@app.route("/update", methods=["GET", "POST"])
@login_required
def update():
    """Update User Details"""

    # Checking if a user is authenticated
    if current_user.is_authenticated:
        id = current_user.get_id()
        # name = request.form["name"]
        user = User.query.filter_by(id=id).first()
        user.name = "Harry"
        db.session.commit()
        return redirect("/welcome")
    else:
        return redirect("/login")


# Login Required to visit this page
@app.route('/welcome', methods=['GET'])
@login_required
def welcome():
    """Welcoming User/Home Page"""

    return "Welcome User: " + current_user.get_name()

