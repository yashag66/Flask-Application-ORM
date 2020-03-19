from . import db, login

# for creating foreign key relationship between the tables
from sqlalchemy.orm import relationship

from flask_login import UserMixin


# we create the class User and extend it from the Base Class.
class User(UserMixin, db.Model):
    """User Model having required fields required in DB related to User"""

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Integer, nullable=False)
    email = db.Column(db.Integer, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    mobileNo = db.Column(db.Integer, nullable=False, unique=True)
    addressID = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    address = relationship("Address", uselist=False, back_populates="user")

    def get_name(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.name


# we create the class Address and extend it from the Base Class.
class Address(db.Model):
    """Address Model having required fields required in DB related to address of User"""

    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    houseNo = db.Column(db.String, nullable=False)
    addressLine1 = db.Column(db.String, nullable=False)
    addressLine2 = db.Column(db.String, nullable=True)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    pincode = db.Column(db.String, nullable=False)
    user = relationship("User", back_populates="address")


@login.user_loader
def load_user(id):
    """to load user id when used in different views/routes"""

    return User.query.get(int(id))