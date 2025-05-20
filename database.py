import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# ⏬ .env-Datei laden
load_dotenv()

# 🔐 Verbindung zur DB aus Umgebungsvariable lesen
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL wurde nicht gefunden! Bitte .env prüfen.")

#  Engine starten
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#  Basisklasse für Modelle
Base = declarative_base()
