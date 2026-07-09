from langchain_core.tools import tool

from app.database.database import SessionLocal
from app.database.crud import create_interaction


@tool
def log_interaction(
    hcp_name: str = "",
    interaction_type: str = "",
    date: str = "",
    time: str = "",
    attendees: str = "",
    topics_discussed: str = "",
    materials_shared: str = "",
    samples_distributed: str = "",
    sentiment: str = "",
    outcomes: str = "",
    follow_up_actions: str = "",
):
    """Log a new HCP interaction into the CRM."""

    db = SessionLocal()

    try:
        interaction = create_interaction(
            db,
            {
                "hcp_name": hcp_name,
                "interaction_type": interaction_type,
                "date": date,
                "time": time,
                "attendees": attendees,
                "topics_discussed": topics_discussed,
                "materials_shared": materials_shared,
                "samples_distributed": samples_distributed,
                "sentiment": sentiment,
                "outcomes": outcomes,
                "follow_up_actions": follow_up_actions,
            },
        )

        return {
            "status": "success",
            "action": "log_interaction",
            "id": interaction.id,
            "message": "Interaction saved successfully.",
        }

    finally:
        db.close()


@tool
def edit_interaction(field: str, value: str):
    """Edit one field of the current interaction."""

    return {
        "status": "success",
        "action": "edit_interaction",
        "field": field,
        "value": value,
    }


@tool
def summarize_interaction(text: str):
    """Summarize an HCP interaction."""

    return {
        "status": "success",
        "summary": text,
    }


@tool
def suggest_followup(topic: str):
    """Suggest follow-up actions after an HCP interaction."""

    return {
        "status": "success",
        "suggestion": f"Follow up regarding {topic}",
    }


@tool
def clear_interaction():
    """Clear the current interaction."""

    return {
        "status": "success",
        "action": "clear_interaction",
    }