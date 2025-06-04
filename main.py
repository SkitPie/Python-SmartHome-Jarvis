import os
from typing import Dict, List

from crewai import Agent, Crew, Process, Task, LLM
from crewai.tools import tool

# Example smart home data
HOME_STATE: Dict[str, Dict[str, str]] = {
    "living room": {
        "light": "off",
        "fan": "on",
    },
    "kitchen": {
        "light": "on",
        "fridge": "closed",
    },
    "bedroom": {
        "light": "off",
        "window": "open",
    },
}


@tool
def get_rooms() -> List[str]:
    """Return the list of rooms available in the smart home."""
    return list(HOME_STATE.keys())


@tool
def list_room_items(room: str) -> Dict[str, str]:
    """List all the items in the given room with their current state."""
    return HOME_STATE.get(room.lower(), {})


def main() -> None:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY environment variable not set")

    llm = LLM(model="gemini-pro", api_key=api_key)

    assistant = Agent(
        role="SmartHome Assistant",
        goal="Answer questions about the home by using tools when needed.",
        backstory="You are an AI assistant that helps manage a smart home.",
        llm=llm,
        tools=[get_rooms, list_room_items],
    )

    print("SmartHome ChatBot. Type 'exit' to quit.")
    while True:
        try:
            query = input("User: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not query or query.lower() == "exit":
            break

        task = Task(
            description=query,
            expected_output="Answer to the user's question",
            agent=assistant,
        )
        crew = Crew(
            agents=[assistant],
            tasks=[task],
            process=Process.sequential,
        )
        result = crew.kickoff()
        print("Assistant:", result.raw)


if __name__ == "__main__":
    main()
