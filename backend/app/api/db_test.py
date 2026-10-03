from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from backend.app.database.dependencies import get_db

router = APIRouter()


@router.get("/db-test")
def database_test(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1"))
    
    return {
        "status": "connected",
        "database_response": result.scalar(),
    }