import random
import string

from fastapi.testclient import TestClient

from user_app.main import app

client = TestClient(app)


def test_create_user():
    username = ''.join(random.choice(string.ascii_letters) for i in range(10))
    response = client.post("/user", json={
        "username": username,
        "password": "12345",
        "fullname": "Medium aloha"
    })
    assert response.status_code == 200
    assert response.json()["username"] == username


def test_authen_user_success():
    response = client.post("/authenticate", json={
        "username": "medium",
        "password": "12345",
    })
    assert response.status_code == 200


def test_authenticate_user_wrong_password():
    response = client.post("/authenticate", json={
        "username": "medium",
        "password": "123456",
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Password is not correct"


def test_authenticate_user_wrong_username():
    response = client.post("/authenticate", json={
        "username": "medium55",
        "password": "123456",
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Username not existed"
# def test_read_item_bad_token():
#     response = client.get("/items/foo", headers={"X-Token": "hailhydra"})
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Invalid X-Token header"}
#
#
# def test_read_inexistent_item():
#     response = client.get("/items/baz", headers={"X-Token": "coneofsilence"})
#     assert response.status_code == 404
#     assert response.json() == {"detail": "Item not found"}
#
#
# def test_create_item():
#     response = client.post(
#         "/items/",
#         headers={"X-Token": "coneofsilence"},
#         json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
#     )
#     assert response.status_code == 200
#     assert response.json() == {
#         "id": "foobar",
#         "title": "Foo Bar",
#         "description": "The Foo Barters",
#     }
#
#
# def test_create_item_bad_token():
#     response = client.post(
#         "/items/",
#         headers={"X-Token": "hailhydra"},
#         json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},
#     )
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Invalid X-Token header"}
#
#
# def test_create_existing_item():
#     response = client.post(
#         "/items/",
#         headers={"X-Token": "coneofsilence"},
#         json={
#             "id": "foo",
#             "title": "The Foo ID Stealers",
#             "description": "There goes my stealer",
#         },
#     )
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Item already exists"}
