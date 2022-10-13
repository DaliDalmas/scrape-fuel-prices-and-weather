from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import sessionLocal1, engine

description = """
Fuel Weather api helps you to collect and share data
about weather and fuel prices of a country
"""

app = FastAPI(
    title="Fuel Weather API",
    description=description,
    version="0.0.1",
    contact={
        "name": "Dalmas Otieno",
        "url": "https://github.com/DaliDalmas"
    },
    license_info={
        "name": "MIT License",
        "url": "https://github.com/DaliDalmas/scrape-fuel-prices-and-weather/blob/main/LICENSE",
    },
)

models.Base.metadata.create_all(bind=engine)


# Dependency
async def get_db():
    db = sessionLocal1()
    try:
        yield db
    except Exception as e:
        print(e)
    finally:
        db.close()

@app.get("/fuels/", response_model=list[schemas.Fuel], tags=["fuel"])
def read_fuels(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    fuels = crud.get_fuels(db, skip=skip, limit=limit)
    return fuels

@app.get("/fuel/{fuel_id}", response_model=schemas.Fuel, tags=["fuel"])
def read_fuel(fuel_id: int, db: Session = Depends(get_db)):
    db_fuel = crud.get_fuel(db=db, fuel_id=fuel_id)
    if db_fuel is None:
        raise HTTPException(status_code=404, detail="Fuel values not found")
    return db_fuel

@app.post("/add_fuel/", response_model=schemas.Fuel, tags=["fuel"])
def add_fuel(fuel: schemas.FuelCreate, db: Session = Depends(get_db)):
    return crud.create_fuel(db=db, fuel=fuel)

@app.delete("/delete_fuel/{fuel_id}", tags=["fuel"])
def delete_fuel(fuel_id: int, db: Session = Depends(get_db)):
    return crud.delete_fuel(fuel_id=fuel_id, db=db)

@app.put("/update_fuel/{fuel_id}",response_model=schemas.Fuel, tags=["fuel"])
def put_fuel(fuel_id: int, updated_fuel: schemas.FuelCreate, db: Session = Depends(get_db)):
    return crud.update_fuel(fuel_id=fuel_id, db=db, updated_fuel=updated_fuel)




@app.get("/weathers/", response_model=list[schemas.Weather], tags=["weather"])
def read_weathers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    weathers = crud.get_weathers(db, skip=skip, limit=limit)
    return weathers

@app.get("/weather/{weather_id}", response_model=schemas.Weather, tags=["weather"])
def read_weather(weather_id: str, db: Session = Depends(get_db)):
    db_weather = crud.get_weather(db=db, weather_id=weather_id)
    if db_weather is None:
        raise HTTPException(status_code=404, detail="Weather values not found")
    return db_weather

@app.post("/add_weather/", response_model=schemas.Weather, tags=["weather"])
def add_weather(weather: schemas.WeatherCreate, db: Session = Depends(get_db)):
    return crud.create_weather(db=db, weather=weather)

@app.delete("/delete_weather/{weather_id}", tags=["weather"])
def delete_weather(weather_id: str, db: Session = Depends(get_db)):
    return crud.delete_weather(weather_id=weather_id, db=db)

@app.put("/update_weather/{weather_id}",response_model=schemas.Fuel, tags=["weather"])
def put_weather(weather_id: int, updated_weather: schemas.WeatherCreate, db: Session = Depends(get_db)):
    return crud.update_weather(weather_id=weather_id, db=db, updated_weather=updated_weather)



@app.get("/exchange_rates/", response_model=list[schemas.ExchangeRate], tags=["exchange rate"])
def read_exchange_rates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    exchanges = crud.get_exchange_rates(db, skip=skip, limit=limit)
    return exchanges

@app.get("/exchange_rate/{exchange_rate_id}", response_model=schemas.ExchangeRate, tags=["exchange rate"])
def read_exchange_rate(exchange_rate_id: str, db: Session = Depends(get_db)):
    db_exchange_rate = crud.get_exchange_rate(db=db, exchange_rate_id=exchange_rate_id)
    if db_exchange_rate is None:
        raise HTTPException(status_code=404, detail="Exchange rate values not found")
    return db_exchange_rate

@app.post("/add_exchange_rates/", response_model=schemas.ExchangeRate, tags=["exchange rate"])
def add_exchange_rates(exchanges: schemas.ExchangeRateCreate, db: Session = Depends(get_db)):
    return crud.create_weather(db=db, exchange=exchanges)

@app.delete("/delete_exchange_rate/{exchange_rate_id}", tags=["exchange rate"])
def delete_exchange_rate(exchange_rate_id: str, db: Session = Depends(get_db)):
    return crud.delete_exchange_rate(exchange_rate_id=exchange_rate_id, db=db)

@app.put("/update_exchange_rate/{exchange_rate_id}",response_model=schemas.ExchangeRate, tags=["exchange rate"])
def put_exchange_rate(exchange_rate_id: int, updated_exchange_rate: schemas.ExchangeRateCreate, db: Session = Depends(get_db)):
    return crud.update_exchange_rate(exchange_rate_id=exchange_rate_id, db=db, updated_exchange_rate=updated_exchange_rate)