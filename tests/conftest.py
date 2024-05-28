import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings
from app.database import Base, get_db
from app.main import app

# postgresql://<username>:<password>@<host>[:<port>]/<database>
SQLALCHEMY_DB_URL = (
    "postgresql://{db_uname}:{db_pwd}@{db_host}:{db_port}/{db_name}_test".format(
        db_uname=settings.database_username,
        db_pwd=settings.database_password,
        db_host=settings.database_hostname,
        db_port=settings.database_port,
        db_name=settings.database_name,
    )
)

engine = create_engine(SQLALCHEMY_DB_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def test_user(client):
    # first create a user
    user_data = {"email": "daya@cid.com", "password": "daya123"}
    res = client.post("/users/", json=user_data)

    assert res.status_code == 201

    # append the password to the response
    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user
