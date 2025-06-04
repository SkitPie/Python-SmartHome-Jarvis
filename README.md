# Python SmartHome Jarvis

This project contains a simple ChatBot built with [CrewAI](https://github.com/Venture-Crew/crewai) that can query a simulated smart home. The bot uses Google Gemini as the LLM and supports tool calling to inspect the home state.

## Features

- **List rooms**: The bot can check which rooms exist in the home.
- **List room items**: For a given room, the bot can list all items and their current state.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set the Google API key in the environment:
   ```bash
   export GOOGLE_API_KEY=your-key-here
   ```

3. Run the chat bot:
   ```bash
   python main.py
   ```

Type `exit` to quit the chat.
