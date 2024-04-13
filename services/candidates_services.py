from sqlalchemy import select
from db.models import Candidates, Brands, Offices
from db.config import Session

def cretate_new_candidate(brand: str, office:str, candidate: str):
    '''
    This function receives a necessary data to create a new candidate, but fst, verify if brand or office exist to
    avoid duplicated registers on the db
    '''
    if not __verify_if_brand_exist(brand=brand):
        return 'its null'
    pass

def __verify_if_brand_exist(brand:str):
    with Session() as session:
        smtp = select(Brands).where(Brands.name.ilike('%'+brand.strip()+'%'))
        query_brand = session.execute(smtp).scalar()
        return query_brand
        

def __verify_if_office_exist(office:str):
    pass

