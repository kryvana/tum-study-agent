import os
from google import genai
from google.genai import types
from google.adk.agents import Agent

def read_local_syllabus() -> str:
    """Reads the local student syllabus file securely from disk."""
    try:
        with open("syllabus.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "No syllabus file found locally."

study_agent = Agent(
    name="tum_study_planner",
    model="gemini-2.5-flash", 
    instruction=(
        "You are a concierge study assistant. "
        "Use the read_local_syllabus tool to find upcoming deadlines. "
        "Based on the deadlines found, generate a brief, structured bullet-point study schedule. "
        "Be concise to save tokens."
    ),
    tools=[read_local_syllabus]
)

if __name__ == "__main__":
    print("🤖 Simulating Agent run...\n")
    

    client = genai.Client()
    
    chat_session = client.chats.create(
        model=study_agent.model,
        config=types.GenerateContentConfig(
            system_instruction=study_agent.instruction,
            tools=study_agent.tools,
            temperature=0.2
        )
    )
    
    response = chat_session.send_message("Review my upcoming deadlines in the syllabus and make a quick study plan.")
    
    print(response.text)
    print("\n✅ Done! Ready for your video recording.")