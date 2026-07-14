from fastapi import APIRouter
from database.sql import Database

router = APIRouter()


@router.get("/health")
def health():

    try:

        db = Database()

        db.execute("SELECT 1")

        return {
            "Application": "Running",
            "Database": "Connected"
        }

    except Exception as ex:

        return {
            "Application": "Running",
            "Database": "Disconnected",
            "Error": str(ex)
        }