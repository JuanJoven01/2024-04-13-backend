from fastapi import FastAPI

from db.config import engine, Base
from db.models import Candidates, Brands, Offices

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}