from api.db import DB, Reviews
from sqlalchemy import func, desc


def healthcheck():
    return {"msg": "ok"}


def most_reviewed_product(count):
    query = DB.session.query(
        Reviews.product_title,
        Reviews.product_id,
        func.count(Reviews.review_id).label("review_count"),
    )
    query = query.group_by(Reviews.product_id).order_by(desc("review_count")).limit(count)
    data_set = query.all()
    data = [item._asdict() for item in data_set]
    return data


def product_review(product_id):
    review_q = DB.session.query(
        Reviews.review_headline,
        Reviews.review_body,
        Reviews.star_rating,
        Reviews.review_date,
        Reviews.customer_id,
    ).filter(Reviews.product_id == product_id).order_by(desc(Reviews.star_rating))
    data_set = review_q.all()
    reviews = [item._asdict() for item in data_set]
    ratings = [review.get('star_rating') for review in reviews if review.get('star_rating')]
    average_rating = sum(ratings) / len(ratings) if ratings else None
    product_q = DB.session.query(
        Reviews.product_title).filter(Reviews.product_id == product_id)
    product = product_q.first()
    product_title = product[0] if product else ''
    return {"product_title": product_title,
            "average_rating": average_rating,
            "reviews": reviews}


def customer_review(customer_id):
    query = DB.session.query(
        Reviews.product_title,
        Reviews.review_headline,
        Reviews.review_body,
        Reviews.star_rating,
        Reviews.review_date,
        Reviews.product_id,
    ).filter(Reviews.customer_id == customer_id).order_by(desc(Reviews.star_rating))
    data_set = query.all()
    data = [item._asdict() for item in data_set]
    return data
