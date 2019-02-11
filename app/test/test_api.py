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
    rsp = client.get("/customer_review?customer_id=ABC")
    assert rsp.status_code == 200


def test_product_review(client):
    DB.session = UnifiedAlchemyMagicMock()
    rsp = client.get("/product_review?product_id=ABC")
    assert rsp.status_code == 200
