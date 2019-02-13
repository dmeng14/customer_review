import json
from app import app
from api.db import DB
import pytest
from alchemy_mock.mocking import UnifiedAlchemyMagicMock


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = ""
    return app.test_client()


def test_most_reviewed_product(client):
    DB.session = UnifiedAlchemyMagicMock()
    rsp = client.get("/most_reviewed_product?count=3")
    assert rsp.status_code == 200


def test_customer_review(client):
    DB.session = UnifiedAlchemyMagicMock()
    rsp = client.get("/customer_review/ABC")
    assert rsp.status_code == 200


def test_product_review(client):
    DB.session = UnifiedAlchemyMagicMock()
    rsp = client.get("/product_review?product_id=ABC")
    assert rsp.status_code == 200


def test_insert_review(client):
    DB.session = UnifiedAlchemyMagicMock()

    # test case: payload failed REVIEW_SCHEMA validation
    payload = {
        "product_id": "B0042TNMMS"
    }
    rsp = client.post(
        "/insert_review",
        data=json.dumps(payload),
        content_type="application/json",
    )
    assert rsp.status_code == 400

    # test case: insert review
    payload = {
        "product_id": "B0042TNMMS",
        "star_rating": 5
    }
    rsp = client.post(
        "/insert_review",
        data=json.dumps(payload),
        content_type="application/json",
    )
    assert rsp.status_code == 200


def test_update_review(client):
    DB.session = UnifiedAlchemyMagicMock()

    # test case: payload failed UPDATE_REVIEW_SCHEMA validation
    payload = {
        "review_id": 100,
        "star_rating": 5
    }
    rsp = client.put(
        "/update_review",
        data=json.dumps(payload),
        content_type="application/json",
    )
    assert rsp.status_code == 400

    # test case: update review.
    payload = {
        "review_id": 'abc',
        "star_rating": 5
    }
    rsp = client.put(
        "/update_review",
        data=json.dumps(payload),
        content_type="application/json",
    )
    assert rsp.status_code == 200


def test_delete_review(client):
    DB.session = UnifiedAlchemyMagicMock()

    rsp = client.delete(
        "/delete_review/review_abc",
        content_type="application/json",
    )
    assert rsp.status_code == 200


def test_get_review(client):
    DB.session = UnifiedAlchemyMagicMock()

    rsp = client.get(
        "/get_review/review_abc",
        content_type="application/json",
    )
    assert rsp.status_code == 404
