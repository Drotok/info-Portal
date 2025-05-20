# Energie- & Vertrags-Info-Portal (Backend mit FastAPI + PostgreSQL)

Ein privates Backend-System zur Verwaltung von Strom-, Gas- und Handyverträgen.  
Ziel ist die Speicherung, Analyse und Prognose von Verbrauchsdaten.

---

## Aktueller Projektstatus

- [x] FastAPI erfolgreich eingerichtet
- [x] PostgreSQL-Datenbank angebunden (via SQLAlchemy)
- [x] Umgebungsvariablen über `.env` integriert
- [x] Test-Endpunkt zur DB-Verbindung ist aktiv

---

Projekt starten

Im Terminal ausführen:

uvicorn main:app --reload

Dann im Browser öffnen:

    API root (Test): http://127.0.0.1:8000

    Swagger-Doku: http://127.0.0.1:8000/docs

Wenn die Datenbank korrekt angebunden ist, bekommst du:

{ "message": " Datenbankverbindung erfolgreich!" }

⏭ Nächste Schritte

Modell energievertrag.py erstellen

Endpunkte für POST / GET aufbauen

Verbrauchsdaten modellieren

Diagramme und Prognose vorbereiten

----------- Abhängigkeiten ------------
pip install fastapi uvicorn sqlalchemy python-dotenv psycopg2-binary

## Projektstruktur

    energy-portal/
    ├── .env                # enthält DATABASE_URL (nicht in Git hochladen!)
    ├── main.py             # Einstiegspunkt – FastAPI + Test-Endpunkt
    ├── database.py         # DB-Session & Verbindung
    ├── requirements.txt    # alle nötigen Python-Abhängigkeiten
    ├── models/
    │   └── energievertrag.py  # (in Vorbereitung) Vertragsmodell
