from fastapi import APIRouter, HTTPException

from app.database.database import SessionLocal
from app.database.crud import (
    create_interaction,
    get_interactions,
    get_interaction,
    update_interaction,
    delete_interaction,
)

from app.schemas import (
    InteractionCreate,
    InteractionResponse,
)

router = APIRouter(
    prefix="/interactions",
    tags=["Interactions"],
)


@router.post("/", response_model=InteractionResponse)
def create(data: InteractionCreate):

    db = SessionLocal()

    try:
        return create_interaction(db, data.model_dump())

    finally:
        db.close()


@router.get("/", response_model=list[InteractionResponse])
def list_interactions():

    db = SessionLocal()

    try:
        return get_interactions(db)

    finally:
        db.close()


@router.get("/{interaction_id}", response_model=InteractionResponse)
def get(interaction_id: int):

    db = SessionLocal()

    try:

        interaction = get_interaction(db, interaction_id)

        if interaction is None:
            raise HTTPException(
                status_code=404,
                detail="Interaction not found",
            )

        return interaction

    finally:
        db.close()


@router.put("/{interaction_id}", response_model=InteractionResponse)
def update(
    interaction_id: int,
    data: InteractionCreate,
):

    db = SessionLocal()

    try:

        interaction = update_interaction(
            db,
            interaction_id,
            data.model_dump(),
        )

        if interaction is None:
            raise HTTPException(
                status_code=404,
                detail="Interaction not found",
            )

        return interaction

    finally:
        db.close()


@router.delete("/{interaction_id}")
def delete(interaction_id: int):

    db = SessionLocal()

    try:

        interaction = delete_interaction(
            db,
            interaction_id,
        )

        if interaction is None:
            raise HTTPException(
                status_code=404,
                detail="Interaction not found",
            )

        return {
            "message": "Interaction deleted successfully"
        }

    finally:
        db.close()