from sqlalchemy.orm import Session
from . import models, schemas


def get_fuel(db: Session, fuel_id: str):
    return db.query(models.Fuel).filter(models.Fuel.id == fuel_id).first()

def get_fuels(db: Session, skip: int = 0, limit = 100):
    return db.query(models.Fuel).offset(skip).limit(limit).all()

def create_fuel(db: Session, fuel: schemas.FuelCreate):
    db_item = models.Fuel(**fuel.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_weather(db: Session, weather_id: str):
    return db.query(models.Weather).filter(models.Weather.id == weather_id).first()

def get_weathers(db: Session, skip: int = 0, limit = 100):
    return db.query(models.Weather).offset(skip).limit(limit).all()

def create_weather(db: Session, weather: schemas.WeatherCreate):
    db_item = models.Weather(**weather.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item



def get_exchange_rate(db: Session, exchange_rate_id: str):
    return db.query(models.ExchangeRate).filter(models.ExchangeRate.id == exchange_rate_id).first()

def get_exchange_rates(db: Session, skip: int = 0, limit = 100):
    return db.query(models.ExchangeRate).offset(skip).limit(limit).all()

def create_exchange_rate(db: Session, exchange: schemas.ExchangeRateCreate):
    db_item = models.Weather(**exchange.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
