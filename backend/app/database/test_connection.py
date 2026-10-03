from backend.app.database.dependencies import get_db


db_generator = get_db()
db = next(db_generator)

try:
    print("Database session created successfully.")
finally:
    db_generator.close()