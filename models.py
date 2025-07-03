# app/models.py

from pydantic import BaseModel
from typing import List

# -----------------------
# Request Models
# -----------------------

class NameCreateRequest(BaseModel):
    name: str

class NameUpdateRequest(BaseModel):
    name: str

# -----------------------
# Response Models
# -----------------------

class NameResponse(BaseModel):
    id: int
    name: str

class NamesListResponse(BaseModel):
    names: List[NameResponse]
