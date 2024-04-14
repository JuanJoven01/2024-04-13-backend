from fastapi import APIRouter
from fastapi.responses import JSONResponse

from schemas.candidates_schema import NewCandidate

from services.candidates_services import create_new_candidate, get_all_the_candidates

candidates_router = APIRouter()

@candidates_router.post('/candidates/new', tags=['candidates'])
def create_candidate(new_candidate: NewCandidate):
    candidate = new_candidate.candidate
    brand = new_candidate.brand
    office = new_candidate.office
    response = create_new_candidate(brand=brand, office=office, candidate=candidate)
    return JSONResponse(status_code=201, content={'response' : response})

@candidates_router.get('/candidates/get', tags=['candidates'])
def get_all_candidates():
    response = get_all_the_candidates()
    return JSONResponse(status_code=200, content={'response' : response})
