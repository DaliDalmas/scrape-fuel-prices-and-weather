from pydantic import BaseModel
from datetime import datetime


class FuelBase(BaseModel):
    usd_price_per_litre: float
    usd_price_per_gallon: float
    eur_price_per_litre: float
    eur_price_per_gallon: float
class FuelCreate(FuelBase):
    country: str 
class Fuel(FuelBase):
    id: str
    country: str
    datetime: datetime


class WeatherBase(BaseModel):
    temperature: float
    temperature_unit: str
    wind: float
    wind_unit: str
    visibility: float
    visibility_unit: str
    humidity: float
    humidity_unit: str
    clouds: float
    clouds_unit: str
    cloud_base: float
    cloud_base_unit: str
class WeatherCreate(WeatherBase):
    country: str 
class Weather(WeatherBase):
    id: str
    country: str
    datetime: datetime


class ExchangeRateBase(BaseModel):
    usd_rate: float
    euro_rate: float
class ExchangeRateCreate(ExchangeRateBase):
    country: str 
class ExchangeRate(ExchangeRateBase):
    id: str
    country: str
    datetime: datetime
