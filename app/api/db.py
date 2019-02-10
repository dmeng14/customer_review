import datetime
from flask_sqlalchemy import SQLAlchemy


DB = db = SQLAlchemy()


class Reviews(db.Model):
    __tablename__ = "customer_review"

    id = db.Column(db.Integer, primary_key=True)
    marketplace = db.Column(db.String(2))
    customer_id = db.Column(db.String(256))
    review_id = db.Column(db.String(80))
    product_id = db.Column(db.String(80))
    product_parent = db.Column(db.String(80))
    product_title = db.Column(db.String(256))
    product_category = db.Column(db.String(80))
    star_rating = db.Column(db.Integer)
    helpful_votes = db.Column(db.Integer)
    total_votes = db.Column(db.Integer)
    vine = db.Column(db.Boolean, default=False)
    verified_purchase = db.Column(db.Boolean, default=False)
    review_headline = db.Column(db.Text)
    review_body = db.Column(db.Text)
    review_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
