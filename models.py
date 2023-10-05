from flask_sqlalchemy import SQLAlchemy, inspect
from faker import Faker
import random

db = SQLAlchemy()

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


class PersonalData(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    dateOfBirth = db.Column(db.String(100))
    pesel = db.Column(db.String(100))
    sex = db.Column(db.String(100))
    city = db.Column(db.String(100))
    street = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    idCard = db.Column(db.String(100))
    passport = db.Column(db.String(100))

    def __init__(self, language):
        faker = Faker(language)
        self.firstName = faker.first_name()
        self.lastName = faker.last_name()
        self.dateOfBirth = faker.date_of_birth().strftime("%Y/%m/%d")
        self.sex = random.choice(['Male', 'Female'])
        self.city = faker.city()
        self.street = faker.street_name()
        self.phone = faker.phone_number()
        self.idCard = faker.license_plate()
        self.passport = faker.license_plate()
        if language == 'pl':
            self.pesel = faker.pesel()


class CompanyData(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    companyName = db.Column(db.String(100))
    regon = db.Column(db.String(100))
    nip = db.Column(db.String(100))

    def __init__(self, language):
        faker = Faker(language)
        self.companyName = faker.company()
        self.nip = faker.nip()
        self.regon = faker.regon()


class CreditData(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    bankAccount = db.Column(db.String(100))
    ibanAccount = db.Column(db.String(100))
    cardVendor = db.Column(db.String(100))
    cvv = db.Column(db.String(100))
    expirationDate = db.Column(db.String(100))

    def __init__(self, language):
        faker = Faker(language)
        self.bankAccount = faker.bban()
        self.ibanAccount = faker.iban()
        self.cardVendor = faker.credit_card_provider()
        self.cvv = faker.credit_card_security_code()
        self.expirationDate = faker.credit_card_expire()