from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(pwd: str) -> str:
    return pwd_context.hash(pwd)


def verify(input_pwd: str, hashed_pwd: str) -> bool:
    return pwd_context.verify(input_pwd, hashed_pwd)
