from dataclasses import dataclass, field
from enum import Enum


class AgentActionType(Enum):
    TOOL_CALL = "tool_call"
    FINAL = "final"


@dataclass
class AgentAction:
    action_type: AgentActionType
    tool_name: str | None = None
    arguments: dict = field(default_factory=dict)
    answer: str | None = None


tool_action = AgentAction(
    action_type=AgentActionType.TOOL_CALL,
    tool_name="read_file",
    arguments={"filename": "database.log"},
)

final_action = AgentAction(
    action_type=AgentActionType.FINAL,
    answer="The database service failed.",
)

print(tool_action)
print(final_action)
