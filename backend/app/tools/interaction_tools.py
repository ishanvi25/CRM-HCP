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
            "interaction": {
                "hcpName": hcp_name,
                "interactionType": interaction_type,
                "date": date,
                "time": time,
                "attendees": attendees,
                "topicsDiscussed": topics_discussed,
                "materialsShared": materials_shared,
                "samplesDistributed": samples_distributed,
                "sentiment": sentiment,
                "outcomes": outcomes,
                "followUpActions": follow_up_actions,
            },
        }

    finally:
        db.close()


@tool
def edit_interaction(field: str, value: str):
    """Edit one field of the current interaction."""

    field_map = {
        "hcp_name": "hcpName",
        "interaction_type": "interactionType",
        "date": "date",
        "time": "time",
        "attendees": "attendees",
        "topics_discussed": "topicsDiscussed",
        "materials_shared": "materialsShared",
        "samples_distributed": "samplesDistributed",
        "sentiment": "sentiment",
        "outcomes": "outcomes",
        "follow_up_actions": "followUpActions",
    }

    frontend_field = field_map.get(field)

    interaction = {}

    if frontend_field:
        interaction[frontend_field] = value

    return {
        "status": "success",
        "action": "edit_interaction",
        "interaction": interaction,
        "message": f"{field} updated successfully.",
    }


@tool
def summarize_interaction(text: str):
    """Summarize an HCP interaction."""

    return {
        "status": "success",
        "action": "summarize_interaction",
        "summary": text,
    }


@tool
def suggest_followup(topic: str):
    """Suggest follow-up actions after an HCP interaction."""

    return {
        "status": "success",
        "action": "suggest_followup",
        "suggestion": f"Follow up regarding {topic}",
    }


@tool
def clear_interaction():
    """Clear the current interaction."""

    return {
        "status": "success",
        "action": "clear_interaction",
        "clear": True,
    }