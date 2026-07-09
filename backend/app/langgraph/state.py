from typing import TypedDict, Optional, Dict, Any


class CRMState(TypedDict):
    user_message: str
    tool_name: Optional[str]
    tool_input: Dict[str, Any]
    tool_output: Dict[str, Any]