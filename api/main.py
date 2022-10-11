from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import sessionLocal1, engine

app = FastAPI()
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

@app.get("/fuels/", response_model=list[schemas.Fuel])
def read_fuels(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    fuels = crud.get_fuels(db, skip=skip, limit=limit)
    return fuels

@app.post("/add_fuel/", response_model=schemas.Fuel)
def add_fuel(fuel: schemas.FuelCreate, db: Session = Depends(get_db)):
    return crud.create_fuel(db=db, fuel=fuel)


@app.get("/weathers/", response_model=list[schemas.Weather])
def read_weathers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    weathers = crud.get_weathers(db, skip=skip, limit=limit)
    return weathers

@app.get("/exchange_rates/", response_model=list[schemas.ExchangeRate])
def read_exchange_rates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    exchanges = crud.get_exchange_rates(db, skip=skip, limit=limit)
    return exchanges