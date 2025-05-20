# models/energievertrag.py

from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class EnergieVertrag(Base):
    __tablename__ = "vertraege"

    id = Column(Integer, primary_key=True, index=True)
    vertragstyp = Column(String, index=True)  # z. B. Strom, Gas, Handy
    anbieter = Column(String, nullable=False)
    vertragsbeginn = Column(Date)
    vertragsende = Column(Date)
    grundpreis = Column(Float)  # monatlich
    arbeitspreis = Column(Float)  # z. B. €/kWh oder €/MB
    monatlicher_verbrauch = Column(Float)  # geschätzt z. B. kWh oder GB
