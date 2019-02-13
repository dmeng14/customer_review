import json
import pytest
from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_most_reviewed_product(client):
    rsp = client.get("/most_reviewed_product?count=3")
    product_id = 'B006MIUM20'
    assert rsp.status_code == 200
    assert product_id in rsp.get_data(as_text=True)


def test_customer_review(client):
    rsp = client.get("/customer_review/14522766")
    product_id = 'B001T4XU1C'
    assert rsp.status_code == 200
    assert product_id in rsp.get_data(as_text=True)


def test_product_review(client):
    rsp = client.get("/product_review?product_id=B0042TNMMS")
    customer_id = '34731776'
    assert rsp.status_code == 200
    assert customer_id in rsp.get_data(as_text=True)


def test_get_review(client):
    rsp = client.get(
        "/get_review/RD46RNVOHNZSC",
        content_type="application/json",
    )
    product_id = 'B001T4XU1C'
    assert rsp.status_code == 200
    assert product_id in rsp.get_data(as_text=True)


def test_insert_review(client):
    payload = {
        "review_id": "test_review",
        "product_id": "B0042TNMMS",
        "star_rating": 5
    }
    rsp = client.post(
        "/insert_review",
        data=json.dumps(payload),
        content_type="application/json",
    )
    assert rsp.status_code == 200
    rsp = client.get(
        "/get_review/test_review",
        content_type="application/json",
    )
    product_id = 'B0042TNMMS'
    assert product_id in rsp.get_data(as_text=True)


def test_update_review(client):
    review_body = "good product"
    payload = {
        "review_id": "test_review",
        "review_body": review_body
    }
    rsp = client.put(
        "/update_review",
        data=json.dumps(payload),
        content_type="application/json",
    )
    assert rsp.status_code == 200
    rsp = client.get(
        "/get_review/test_review",
        content_type="application/json",
    )
    assert review_body in rsp.get_data(as_text=True)


def test_delete_review(client):
    rsp = client.delete(
        "/delete_review/test_review",
        content_type="application/json",
    )
    assert rsp.status_code == 200
    rsp = client.get(
        "/get_review/test_review",
        content_type="application/json",
    )
    assert rsp.status_code == 404
