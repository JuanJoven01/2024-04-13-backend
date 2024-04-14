from fastapi.responses import JSONResponse
from sqlalchemy import select
from db.models import Candidates, Brands, Offices
from db.config import Session

def create_new_candidate(brand: str, office:str, candidate: str):
    '''
    This function receives a necessary data to create a new candidate, but fst, verify if brand or office exist to
    avoid duplicated registers on the db, created the user and
    return the user data
    
    '''

    db_brand = __verify_if_brand_exist(brand_name= brand)
    if not db_brand:
        db_brand = __create_a_new_brand(brand_name=brand)

    db_office = __verify_if_office_exist(office_name=office)
    if not db_office:
        db_office = __create_a_new_office(office_name=office)

    with Session() as session:
        new_candidate = Candidates(name=candidate.strip(),
                                   brand_id= db_brand.id,
                                    office_id= db_office.id
                                   )
        session.add(new_candidate)
        session.commit()
    return __find_candidate_per_name(candidate_name=candidate.strip())

def update_the_candidate(uid: int,brand: str, office:str, candidate: str):
    '''
    This function receives a necessary data to update a candidate, but fst, verify if brand or office exist to
    avoid duplicated registers on the db, update the user and
    return the user data
    '''

    db_brand = __verify_if_brand_exist(brand_name= brand)
    if not db_brand:
        db_brand = __create_a_new_brand(brand_name=brand)

    db_office = __verify_if_office_exist(office_name=office)
    if not db_office:
        db_office = __create_a_new_office(office_name=office)

    with Session() as session:
        smtp = select(Candidates).where(Candidates.id == uid)
        db_candidate = session.execute(smtp).scalar()
        db_candidate.name = candidate
        db_candidate.brand_id = db_brand.id
        db_candidate.office_id = db_office.id
        session.commit()
        smtp = select(Candidates).where(Candidates.id == uid)
        db_candidate = session.execute(smtp).scalar()
        return db_candidate


def delete_a_candidate(uid:int):
    '''
    find a candidate on the db and remove that
    return a string if deleted successful
    '''
    with Session() as session:
        smtp = select(Candidates).where(Candidates.id == uid)
        to_delete = session.execute(smtp).scalar()
        session.delete(to_delete)
        session.commit()
    return 'User deleted'


def get_all_the_candidates():
    '''
    Get all the candidates joined with offices and brands,
    return a list with a dictionary for any candidate registered
    '''
    with Session() as session:
        smtp = select(Candidates).join(Brands).join(Offices)
        all_candidates = session.execute(smtp).scalars().all()
        candidates_as_dict = []
        for candidate in all_candidates:
            candidates_as_dict.append(
                {
                    'id': candidate.id,
                    'name': candidate.name,
                    'brand': candidate.brand.name,
                    'office': candidate.office.name
                }
            )
        return candidates_as_dict


def __find_candidate_per_name(candidate_name: str):
    '''
    receives an candidate name and find the exact coincidences on the db,
    return the last coincidence
    '''
    with Session() as session:
        smtp = select(Candidates).where(Candidates.name == candidate_name)
        query_candidate = session.execute(smtp).scalars().all()
        query_candidate = query_candidate[-1]
        return {
        'id': query_candidate.id,
        'name': query_candidate.name,
        'brand_id': query_candidate.brand_id,
        'office_id': query_candidate.office_id
    }

def __create_a_new_brand(brand_name:str):
    with Session() as session:
        new_brand = Brands(name = brand_name.strip())
        session.add(new_brand)
        session.commit()
    return __verify_if_brand_exist(brand_name=brand_name)


def __create_a_new_office(office_name:str):
    with Session() as session:
        new_office = Offices(name = office_name.strip())
        session.add(new_office)
        session.commit()
    return __verify_if_brand_exist(brand_name=office_name)
        

def __verify_if_brand_exist(brand_name:str):
    '''
    Search in the db if the brand already exist, if exist return that
    '''
    with Session() as session:
        smtp = select(Brands).where(Brands.name.ilike('%'+brand_name.strip()+'%'))
        query_brand = session.execute(smtp).scalar()
        return query_brand
        

def __verify_if_office_exist(office_name:str):
    '''
    Search in the db if the office already exist, if exist return that
    '''
    with Session() as session:
        smtp = select(Offices).where(Offices.name.ilike('%'+office_name.strip()+'%'))
        query_office = session.execute(smtp).scalar()
        return query_office

