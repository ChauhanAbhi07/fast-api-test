# app/handlers.py

from fastapi import APIRouter, HTTPException
from models import (
    NameCreateRequest,
    NameUpdateRequest,
    NameResponse,
    NamesListResponse,
)
import services as services

router = APIRouter()

@router.post("/names/", response_model=NameResponse)
def create_name(request: NameCreateRequest):
    return services.create_name(request.name)

@router.get("/names/", response_model=NamesListResponse)
def get_names():
    names = services.get_all_names()
    return NamesListResponse(names=names)

@router.get("/names/{name_id}", response_model=NameResponse)
def get_name(name_id: int):
    name = services.get_name_by_id(name_id)
    if not name:
        raise HTTPException(status_code=404, detail="Name not found")
    return name

@router.put("/names/{name_id}", response_model=NameResponse)
def update_name(name_id: int, request: NameUpdateRequest):
    updated = services.update_name(name_id, request.name)
    if not updated:
        raise HTTPException(status_code=404, detail="Name not found")
    return updated

@router.delete("/names/{name_id}")
def delete_name(name_id: int):
    deleted = services.delete_name(name_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Name not found")
    return {"message": "Name deleted successfully"}
