from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal

app = FastAPI()

# Funktion zur Übergabe einer DB-Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root-Endpunkt zum Testen der DB-Verbindung
@app.get("/")
def test_connection(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))  # Einfache Test-Query
        return {"message": "✅ Datenbankverbindung erfolgreich!"}
    except Exception as e:
        return {"error": str(e)}
