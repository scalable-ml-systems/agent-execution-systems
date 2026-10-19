from state import AgentState
from tools import TOOLS
from actions import AgentAction, AgentActionType


def build_context(state: AgentState) -> str:
    tool_names = list(TOOLS.keys())

    history_lines = []

    for event in state.history:
        history_lines.append(str(event))

    tool_call_lines = []

    for tool_call in state.tool_calls:
        tool_call_lines.append(str(tool_call))

    context = f"""
TASK:
{state.task}

STATUS:
{state.status.value}

STEP:
{state.step}

AVAILABLE TOOLS:
{tool_names}

TOOL CALLS SO FAR:
{tool_call_lines}

EXECUTION HISTORY:
{history_lines}

Choose the next action.
"""

    return context

def call_model(context: str, step: int) -> AgentAction:
    if step == 0:
        return AgentAction(
            action_type=AgentActionType.TOOL_CALL,
            tool_name="list_files",
            arguments={},
        )

    if step == 1:
        return AgentAction(
            action_type=AgentActionType.TOOL_CALL,
            tool_name="read_file",
            arguments={
                "filename": "database.log"
            },
        )

    return AgentAction(
        action_type=AgentActionType.FINAL,
        answer="The database service failed.",
    )


if __name__ == "__main__":
    state = AgentState(
        task="Find which service failed."
    )

    context = build_context(state)

    action = call_model(
        context,
        state.step,
    )

    print(action)
