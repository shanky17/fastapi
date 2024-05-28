import pytest
from jose import jwt

from app import schemas
from app.config import settings

# def test_root(client):
#     resp = client.get("/")
#     assert resp.status_code == 200
#     assert resp.json() == {"message": "Hello World"}


def test_create_user(client):
    resp = client.post("/users/", json={"email": "daya@cid.com", "password": "daya123"})
    new_user = schemas.UserOut(**resp.json())

    assert resp.status_code == 201


def test_get_user(client, test_user):
    resp = client.get(f"/users/{test_user['id']}")
    user = schemas.UserOut(**resp.json())

    assert resp.status_code == 200


def test_login_user(client, test_user):
    resp = client.post(
        "/login",
        data={"username": test_user["email"], "password": test_user["password"]},
    )
    # validate the response using pydantic model
    login_resp = schemas.Token(**resp.json())

    # decode the JWT and validate it to make
    # sure we have a user_id in the token
    payload = jwt.decode(
        login_resp.access_token, settings.secret_key, algorithms=[settings.algorithm]
    )
    id = payload.get("user_id")

    assert id == test_user["id"]
    assert login_resp.token_type == "bearer"
    assert resp.status_code == 200


@pytest.mark.parametrize(
    "email, password, status_code",
    [
        ("wrong@gmail.com", "daya123", 403),
        ("daya@cid.com", "rickROll", 403),
        ("wrong@gmail.com", "rickROll", 403),
        (None, "daya123", 422),
        ("daya@cid.com", None, 422),
    ],
)
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})

    assert res.status_code == status_code
