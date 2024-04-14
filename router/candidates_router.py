from fastapi import APIRouter
from fastapi.responses import JSONResponse

from schemas.candidates_schema import NewCandidate, UpdateCandidate

from services.candidates_services import create_new_candidate, get_all_the_candidates, update_the_candidate, delete_a_candidate

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

@candidates_router.put('/candidates/update', tags=['candidates'])
def update_an_candidate(update_candidate: UpdateCandidate):
    uid = update_candidate.uid
    candidate = update_candidate.candidate
    brand = update_candidate.brand
    office = update_candidate.office
    response = update_the_candidate(uid=uid, candidate=candidate, brand=brand, office=office)
    return JSONResponse(status_code=200, content={'response' : response})

@candidates_router.delete('/candidates/delete/{candidate_id}', tags=['candidates'])
def delete_candidate(candidate_id:int):
    response = delete_a_candidate(candidate_id)
    return JSONResponse(status_code=200, content={'response' : response})
