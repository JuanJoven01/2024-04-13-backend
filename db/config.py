import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


load_dotenv()

db_host=os.getenv('POSTGRES_HOST')
db_user=os.getenv('POSTGRES_USER')
db_password=os.getenv('POSTGRES_PASSWORD')
db_name=os.getenv('DB_NAME')

engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()