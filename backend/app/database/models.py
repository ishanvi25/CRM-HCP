from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from .database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    hcp_name = Column(String)
    interaction_type = Column(String)

    date = Column(String)
    time = Column(String)

    attendees = Column(String)

    topics_discussed = Column(String)

    materials_shared = Column(String)

    samples_distributed = Column(String)

    sentiment = Column(String)

    outcomes = Column(String)

    follow_up_actions = Column(String)