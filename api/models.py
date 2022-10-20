from enum import auto
from sqlalchemy import INTEGER, Column, String, Float, DateTime
import datetime

from .database import Base

class Fuel(Base):
    __tablename__ = "fuel"

    id = Column(INTEGER, primary_key=True)
    usd_price_per_litre = Column(Float)
    usd_price_per_gallon = Column(Float)
    eur_price_per_litre = Column(Float)
    eur_price_per_gallon = Column(Float)
    country = Column(String(2))
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    __table_args__ = {'schema': 'data'}

class Weather(Base):
    __tablename__ = "weather"

    id = Column(INTEGER, primary_key=True)
    temperature = Column(Float)
    temperature_unit = Column(String)
    wind = Column(Float)
    wind_unit = Column(String)
    visibility = Column(Float, nullable=True)
    visibility_unit = Column(String, nullable=True)
    humidity = Column(Float, nullable=True)
    humidity_unit = Column(String, nullable=True)
    clouds = Column(Float)
    clouds_unit = Column(String)
    cloud_base = Column(Float)
    cloud_base_unit = Column(String)
    country = Column(String(2))
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    __table_args__ = {'schema': 'data'}

class ExchangeRate(Base):
    __tablename__ = "exchange_rate"

    id = Column(INTEGER, primary_key=True)
    country = Column(String(2))
    usd_rate = Column(Float)
    euro_rate = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    __table_args__ = {'schema': 'data'}