# app/services.py

from typing import List, Optional
from models import NameResponse

# In-memory "database" of names
names_db = []
next_id = 1  # Auto-incrementing ID

def create_name(name: str) -> NameResponse:
    global next_id
    new_name = {"id": next_id, "name": name}
    names_db.append(new_name)
    next_id += 1
    return NameResponse(**new_name)

def get_all_names() -> List[NameResponse]:
    return [NameResponse(**n) for n in names_db]

def get_name_by_id(name_id: int) -> Optional[NameResponse]:
    for n in names_db:
        if n["id"] == name_id:
            return NameResponse(**n)
    return None

def update_name(name_id: int, new_name: str) -> Optional[NameResponse]:
    for n in names_db:
        if n["id"] == name_id:
            n["name"] = new_name
            return NameResponse(**n)
    return None

def delete_name(name_id: int) -> bool:
    global names_db
    for n in names_db:
        if n["id"] == name_id:
            names_db = [x for x in names_db if x["id"] != name_id]
            return True
    return False
