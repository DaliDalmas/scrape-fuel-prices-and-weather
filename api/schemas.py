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
    id: int
    country: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


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
    id: int
    country: str
    created_at: datetime
    updated_at: datetime
    class Config:
        orm_mode = True


class ExchangeRateBase(BaseModel):
    usd_rate: float
    euro_rate: float
class ExchangeRateCreate(ExchangeRateBase):
    country: str 
class ExchangeRate(ExchangeRateBase):
    id: int
    country: str
    created_at: datetime
    updated_at: datetime
    class Config:
        orm_mode = True
