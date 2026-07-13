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
        summary = None
        suggestion = None
        clear = False

        for message in messages:

            if isinstance(message, ToolMessage):

                data = json.loads(message.content)
                print("TOOL DATA:", data)

                if "interaction" in data:

                    if interaction is None:
                        interaction = {}

                    interaction.update(data["interaction"])

                if "summary" in data:
                    summary = data["summary"]

                if "suggestion" in data:
                    suggestion = data["suggestion"]

                if data.get("clear"):
                    clear = True

            elif isinstance(message, AIMessage):

                if message.content:
                    reply = message.content

        return {
            "reply": reply,
            "interaction": interaction,
            "summary": summary,
            "suggestion": suggestion,
            "clear": clear,
        }

    except Exception as e:

        print(e)

        return {
            "status": "error",
            "message": str(e),
        }