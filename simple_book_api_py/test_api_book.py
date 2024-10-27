import pytest
from helpers import (
    get_status,
    list_books,
    list_books_with_params,
    get_single_book,
    create_order,
    get_all_orders,
    get_single_order,
    update_order,
    delete_order,
    get_api_token
)

@pytest.fixture(scope="session")
def api_token():
    return get_api_token()

def test_status():
    response = get_status()
    assert response.status_code == 200
    assert response.json()["status"] == "OK"

def test_list_books():
    response = list_books()
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_list_books_with_query_params():
    response = list_books_with_params(type="fiction", limit=5)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) <= 5

def test_get_single_book():
    response = get_single_book(1)
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_create_order(api_token):
    response = create_order(api_token, book_id=1, customer_name="John")
    assert response.status_code == 201
    assert "orderId" in response.json()

def test_get_all_orders(api_token):
    response = get_all_orders(api_token)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_order(api_token):
    order_id = create_order(api_token, book_id=1, customer_name="John").json()["orderId"]
    response = get_single_order(api_token, order_id)
    assert response.status_code == 200
    assert response.json()["id"] == order_id

def test_update_order(api_token):
    order_id = create_order(api_token, book_id=1, customer_name="John").json()["orderId"]
    response = update_order(api_token, order_id, customer_name="Jane")
    assert response.status_code == 204

def test_delete_order(api_token):
    order_id = create_order(api_token, book_id=1, customer_name="John").json()["orderId"]
    response = delete_order(api_token, order_id)
    assert response.status_code == 204
