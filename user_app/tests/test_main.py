import random
import string
import unittest

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


def test_authenticate_user_success():
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


if __name__ == "__main__":
    import pytest
    raise SystemExit(pytest.main([__file__]))
