from fastapi import FastAPI

import os
from dotenv import load_dotenv

from fastapi.middleware.cors import CORSMiddleware

from middlewares.error_handler import ErrorHandler

from db.config import engine, Base
from db.models import Candidates, Brands, Offices

from router.candidates_router import candidates_router

load_dotenv()

app = FastAPI()

app.add_middleware(ErrorHandler)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv('CORS_HOST')],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(candidates_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}