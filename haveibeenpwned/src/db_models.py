from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Accounts(db.Model):
    account_id = db.Column(db.String, primary_key=True)
    breached = db.Column(db.Boolean)

class BreachedSites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.String)
    site = db.Column(db.String)