# TUM Concierge Study Planner Agent

An AI Agent built for Kaggle's 5-Day Vibe Coding Course utilizing the Google Agent Development Kit (ADK) and Model Context Protocol (MCP).

## Problem & Solution
University students manage complex, overlapping deadlines. This Concierge Agent securely reads local course syllabus files and automatically synthesizes a chronological study schedule without exposing private university data to external databases.

## Architecture
- **Framework**: `google-adk` and `google-genai` client.
- **Model**: `gemini-2.5-flash` for high speed and token efficiency.
- **MCP Tooling**: Utilizes the `@modelcontextprotocol/server-filesystem` to grant the agent secure read-only access to local `.txt` schedules.

## Setup Instructions
1. Clone this repository to your local machine.
2. Ensure you have Python and the `uv` package manager installed.
3. Install dependencies by running: `uv add google-genai google-adk`
4. Export your Gemini API key in your terminal: `export GEMINI_API_KEY="your_api_key"`
5. Run the agent: `uv run agent.py`
