import json
from sqlalchemy import func, desc
from flask import request, make_response, jsonify
from api.db import DB, Reviews
from api import validate


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


def insert_review():
    payload = request.get_json() or {}
    is_valid, err = validate.validate_create_reivew(payload)
    if not is_valid:
        return make_response(
            json.dumps({"messages": err}), 400, {"Content-Type": "application/json"}
        )
    review = Reviews(
        marketplace=payload.get('marketplace'),
        customer_id=payload.get('customer_id'),
        review_id=payload.get('review_id'),
        product_id=payload.get('product_id'),
        product_parent=payload.get('product_parent'),
        product_title=payload.get('product_title'),
        product_category=payload.get('product_category'),
        star_rating=payload.get('star_rating'),
        helpful_votes=payload.get('helpful_votes'),
        total_votes=payload.get('total_votes'),
        vine=payload.get('vine'),
        verified_purchase=payload.get('verified_purchase'),
        review_headline=payload.get('review_headline'),
        review_body=payload.get('review_body'),
        review_date=payload.get('review_date'),
    )
    DB.session.add(review)
    DB.session.commit()
    return make_response(
        json.dumps({"id": review.id}),
        200,
        {"Content-Type": "application/json"},
    )


def update_review():
    payload = request.get_json() or {}
    is_valid, err = validate.validate_update_reivew(payload)
    if not is_valid:
        return make_response(
            json.dumps({"messages": err}), 400, {"Content-Type": "application/json"}
        )
    (
        DB.session.query(Reviews)
        .filter(Reviews.review_id == payload['review_id'])
        .first_or_404()
    )

    payload_list = dict(
        marketplace=payload.get('marketplace'),
        customer_id=payload.get('customer_id'),
        product_id=payload.get('product_id'),
        product_parent=payload.get('product_parent'),
        product_title=payload.get('product_title'),
        product_category=payload.get('product_category'),
        star_rating=payload.get('star_rating'),
        helpful_votes=payload.get('helpful_votes'),
        total_votes=payload.get('total_votes'),
        vine=payload.get('vine'),
        verified_purchase=payload.get('verified_purchase'),
        review_headline=payload.get('review_headline'),
        review_body=payload.get('review_body'),
        review_date=payload.get('review_date'),)

    res = {k: v for k, v in payload_list.items() if v is not None}

    DB.session.query(
        Reviews
    ).filter(
        Reviews.review_id == payload['review_id']
    ).update(res)

    DB.session.commit()
    return make_response(
        json.dumps({"review_id": payload['review_id']}),
        200,
        {"Content-Type": "application/json"},
    )


def delete_review(review_id):
    (
        DB.session.query(Reviews)
        .filter(Reviews.review_id == review_id)
        .first_or_404()
    )

    DB.session.query(Reviews).filter(Reviews.review_id == review_id).delete()
    return make_response(
        json.dumps({"review_id": review_id}),
        200,
        {"Content-Type": "application/json"},
    )


def get_review(review_id):
    data = DB.session.query(
        Reviews
    ).filter(
        Reviews.review_id == review_id
    ).first()
    if not data:
        return make_response(
            json.dumps({"messages": f'{review_id} not found'}), 404, {"Content-Type": "application/json"}
        )
    return data._asdict()
