from fastapi import APIRouter
from fastapi.responses import JSONResponse

from schemas.candidates_schema import NewCandidate

from services.candidates_services import cretate_new_candidate

candidates_router = APIRouter()

@candidates_router.post('/candidates/new', tags=['candidates'])
def get_candidates_try(new_candidate: NewCandidate):
    candidate = new_candidate['candidate']
    brand = new_candidate['brand']
    office = new_candidate['office']
    response = cretate_new_candidate(brand=brand, office=office, candidate=candidate)
    return JSONResponse(status_code=200, content={'message': 'done'})