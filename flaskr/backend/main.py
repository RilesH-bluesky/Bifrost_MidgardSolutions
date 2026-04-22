from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session

from db_model import Base, Drink, Ingredient
from api_model import IngredientModel, DrinkModel, BaseModel

import random

app = FastAPI()

engine = create_engine("sqlite:///./drinks.db")
Base.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()