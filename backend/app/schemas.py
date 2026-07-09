from pydantic import BaseModel


class InteractionBase(BaseModel):

    hcp_name: str = ""

    interaction_type: str = ""

    date: str = ""

    time: str = ""

    attendees: str = ""

    topics_discussed: str = ""

    materials_shared: str = ""

    samples_distributed: str = ""

    sentiment: str = ""

    outcomes: str = ""

    follow_up_actions: str = ""


class InteractionCreate(InteractionBase):
    pass


class InteractionResponse(InteractionBase):

    id: int

    class Config:
        from_attributes = True