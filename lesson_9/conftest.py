import pytest

from database import SessionLocal


@pytest.fixture
def session():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
