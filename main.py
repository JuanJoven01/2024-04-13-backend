from fastapi import FastAPI

from db.config import engine, Base
from db.models import Candidates, Brands, Offices

from router.candidates_router import candidates_router

app = FastAPI()

app.include_router(candidates_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}