## Building a simple agent harness

                 Agent Harness
                      │
              reads / writes
                      │
                      ▼
               ┌─────────────┐
               │ AgentState  │
               ├─────────────┤
               │ task        │
               │ status      │
               │ step        │
               │ history     │
               │ tool_calls  │
               │ result      │
               │ error       │
               └─────────────┘
