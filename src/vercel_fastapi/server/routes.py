from typing import Any

from fastapi import APIRouter
from fastapi import Body
from fastapi.encoders import jsonable_encoder

from vercel_fastapi.server.model import NoteSchema


router = APIRouter()


notes = {
    0: {
        "title": "My first note",
        "content": "This is the first note in my notes application",
    },
    1: {
        "title": "Uniform circular motion.",
        "content": "Consider a body moving round a circle of radius r, with "
        + "uniform speed v as shown below. The speed everywhere is the same "
        + "as v but direction changes as it moves round the circle.",
    },
}


@router.get("/")
async def get_notes() -> dict[str, Any]:
    return {"data": notes}


@router.get("/{id}")
async def get_note(id: int) -> dict[str, Any]:
    try:
        return {"data": notes[id]}
    except KeyError:
        return {"error": "Invalid note ID"}


@router.post("/note")
async def add_note(note: NoteSchema = Body(...)) -> dict[str, Any]:
    id = len(notes)
    notes[id] = note.dict()
    return {"message": "Note added successfully"}


@router.put("/{id}")
def update_note(id: int, note: NoteSchema) -> dict[str, Any]:
    try:
        curr = notes[id]
    except KeyError:
        return {"error": "No such with ID passed exists."}
    else:
        update = note.dict(exclude_unset=True)
        updated_note = NoteSchema(**curr).copy(update=update)
        notes[id] = jsonable_encoder(updated_note)
        return {"message": "Note updated successfully"}


@router.delete("/{id}")
def delete_note(id: int) -> dict[str, Any]:
    try:
        del notes[id]
    except KeyError:
        return {"error": f"Note with {id=} doesn't exist"}
    else:
        return {"message": "Note deleted"}
