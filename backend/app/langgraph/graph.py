from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition

from langchain_core.messages import SystemMessage

from app.prompts import SYSTEM_PROMPT
from app.services.ai_service import llm

from app.tools.interaction_tools import (
    log_interaction,
    edit_interaction,
    summarize_interaction,
    suggest_followup,
    clear_interaction,
)

tools = [
    log_interaction,
    edit_interaction,
    summarize_interaction,
    suggest_followup,
    clear_interaction,
]

llm_with_tools = llm.bind_tools(tools)


def assistant(state: MessagesState):

    messages = state["messages"]

    if not messages or not isinstance(messages[0], SystemMessage):
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            *messages,
        ]

    response = llm_with_tools.invoke(messages)

    return {
        "messages": [response]
    }


builder = StateGraph(MessagesState)

builder.add_node("assistant", assistant)

builder.add_node(
    "tools",
    ToolNode(tools)
)

builder.add_edge(
    START,
    "assistant",
)

builder.add_conditional_edges(
    "assistant",
    tools_condition,
)

builder.add_edge(
    "tools",
    "assistant",
)

graph = builder.compile()