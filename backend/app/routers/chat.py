from fastapi import APIRouter
from pydantic import BaseModel
from langchain_core.messages import HumanMessage

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
        print("STEP 1")

        result = graph.invoke(
            {
                "messages": [
                    HumanMessage(content=request.message)
                ]
            }
        )

        print("STEP 2")
        print(result)

        return result

    except Exception as e:
     print(e)

    return {
        "status": "error",
        "message": str(e),
    }