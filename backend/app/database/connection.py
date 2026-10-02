import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

load_dotenv()

database_url = URL.create(
    drivername="postgresql+psycopg",
    username="postgres",
    password=os.getenv("POSTGRES_PASSWORD"),
    host="localhost",
    port=5432,
    database="solace_ai",
)

engine = create_engine(database_url)