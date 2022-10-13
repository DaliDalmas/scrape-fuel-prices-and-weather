from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas
import datetime


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

def delete_fuel(fuel_id: str, db: Session):
    fuel_item = db.query(models.Fuel).filter(models.Fuel.id == fuel_id).first()
    if fuel_item is None:
        raise HTTPException(status_code=404, detail="Fuel value not found")
    db.delete(fuel_item)
    db.commit()
    return {"delete": True, "Item": fuel_item}

def update_fuel(fuel_id: str, db: Session, updated_fuel: schemas.FuelCreate):
    fuel_to_update = db.query(models.Fuel).filter(models.Fuel.id == fuel_id).first()
    fuel_to_update.usd_price_per_litre = updated_fuel.usd_price_per_litre
    fuel_to_update.usd_price_per_gallon = updated_fuel.usd_price_per_gallon
    fuel_to_update.eur_price_per_litre = updated_fuel.eur_price_per_litre
    fuel_to_update.eur_price_per_gallon = updated_fuel.eur_price_per_gallon
    fuel_to_update.country = updated_fuel.country
    fuel_to_update.updated_at = datetime.datetime.utcnow()
    db.commit()

    return fuel_to_update



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

def delete_weather(weather_id: str, db: Session):
    weather_item = db.query(models.Weather).filter(models.Weather.id == weather_id).first()
    if weather_item is None:
        raise HTTPException(status_code=404, detail="Weather value not found")
    db.delete(weather_item)
    db.commit()
    return {"delete": True, "Item": weather_item}

def update_weather(weather_id: str, db: Session, updated_weather: schemas.WeatherCreate):
    weather_to_update = db.query(models.Weather).filter(models.Weather.id == weather_id).first()
    weather_to_update.temperature = updated_weather.temperature
    weather_to_update.temperature_unit = updated_weather.temperature_unit
    weather_to_update.wind = updated_weather.wind
    weather_to_update.wind_unit = updated_weather.wind_unit
    weather_to_update.visibility = updated_weather.visibility
    weather_to_update.visibility_unit = updated_weather.visibility_unit
    weather_to_update.humidity = updated_weather.humidity
    weather_to_update.humidity_unit = updated_weather.humidity_unit
    weather_to_update.clouds = updated_weather.clouds
    weather_to_update.clouds_unit = updated_weather.clouds_unit
    weather_to_update.cloud_base = updated_weather.cloud_base
    weather_to_update.cloud_base_unit = updated_weather.cloud_base_unit
    weather_to_update.country = updated_weather.country
    weather_to_update.updated_at = datetime.datetime.utcnow()
    db.commit()

    return weather_to_update




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

def delete_exchange_rate(exchange_rate_id: str, db: Session):
    exchange_rate_item = db.query(models.ExchangeRate).filter(models.ExchangeRate.id == exchange_rate_id).first()
    if exchange_rate_item is None:
        raise HTTPException(status_code=404, detail="ExchangeRate value not found")
    db.delete(exchange_rate_item)
    db.commit()
    return {"delete": True, "Item": exchange_rate_item}

def update_exchange_rate(exchange_rate_id: str, db: Session, updated_exchange_rate: schemas.ExchangeRateCreate):
    exchange_rate_to_update = db.query(models.ExchangeRate).filter(models.ExchangeRate.id == exchange_rate_id).first()
    exchange_rate_to_update.usd_rate = updated_exchange_rate.usd_rate
    exchange_rate_to_update.euro_rate = updated_exchange_rate.euro_rate
    exchange_rate_to_update.country = updated_exchange_rate.country
    exchange_rate_to_update.updated_at = datetime.datetime.utcnow()
    db.commit()

    return exchange_rate_to_update