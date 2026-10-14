from dataclasses import dataclass, field
from enum import Enum


class AgentStatus(Enum):
    CREATED = "created"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class AgentState:
    task: str
    status: AgentStatus = AgentStatus.CREATED
    step: int = 0
    history: list[dict] = field(default_factory=list)
    tool_calls: list[dict] = field(default_factory=list)
    final_result: str | None = None
    error: str | None = None
