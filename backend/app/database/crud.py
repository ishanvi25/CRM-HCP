from sqlalchemy.orm import Session

from .models import Interaction


def create_interaction(db: Session, data: dict):
    interaction = Interaction(**data)

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return interaction


def get_interactions(db: Session):
    return (
        db.query(Interaction)
        .order_by(Interaction.id.desc())
        .all()
    )


def get_interaction(db: Session, interaction_id: int):
    return (
        db.query(Interaction)
        .filter(Interaction.id == interaction_id)
        .first()
    )


def update_interaction(db: Session, interaction_id: int, data: dict):

    interaction = get_interaction(db, interaction_id)

    if not interaction:
        return None

    for key, value in data.items():
        setattr(interaction, key, value)

    db.commit()
    db.refresh(interaction)

    return interaction


def delete_interaction(db: Session, interaction_id: int):

    interaction = get_interaction(db, interaction_id)

    if not interaction:
        return None

    db.delete(interaction)
    db.commit()

    return interaction