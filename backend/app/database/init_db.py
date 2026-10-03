from backend.app.database.base import Base
from backend.app.database.connection import engine
from backend.app.models.user import User


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Database tables created successfully.")