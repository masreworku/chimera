# Project Chimera: Tooling Strategy

## 1. Developer MCP Servers (Build-Time)
To enable Spec-Driven Development, the following MCP servers are integrated into the IDE context:

* **File-System MCP:** Allows the agent to read/write specs and code with high precision.
* **Git MCP:** Enables the agent to manage version control, create branches for features, and document changes autonomously.
* **Memory MCP:** Used to maintain a 'Context Graph' of architectural decisions across long chat sessions.

## 2. Rationale
By using MCP for development, we ensure that the AI Agent is not just a 'chatbot' but a 'co-engineer' with direct, governed access to the project repository.