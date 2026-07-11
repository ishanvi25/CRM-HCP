from fastapi import APIRouter
from pydantic import BaseModel
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

import json

from app.langgraph.graph import graph

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


class ChatRequest(BaseModel):
    message: str


@router.post("/")
async def chat(request: ChatRequest):

    try:

        result = graph.invoke(
            {
                "messages": [
                    HumanMessage(content=request.message)
                ]
            }
        )

        messages = result["messages"]

        reply = ""
        interaction = None

        for message in messages:

            if isinstance(message, ToolMessage):

                data = json.loads(message.content)

                if "interaction" in data:
                    interaction = data["interaction"]

            elif isinstance(message, AIMessage):

                if message.content:
                    reply = message.content

        return {
            "reply": reply,
            "interaction": interaction,
        }

    except Exception as e:

        print(e)

        return {
            "status": "error",
            "message": str(e),
        }