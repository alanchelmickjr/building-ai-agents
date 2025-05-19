# multiagent
from dotenv import load_dotenv
from smolagents import CodeAgent, InferenceClientModel
import re
import pandas as pd
import time
import os

load_dotenv()

def main():
    # Initialize the LLM model (Anthropic Claude)
    model = InferenceClientModel(model_id="Qwen/Qwen2.5-72B-Instruct")

    research_agent=CodeAgent(
        tools=[],
        model=model,
        add_base_tools=True,
        name="research_agent",
        description="research and gather information from the internet and other sources",
    )

    persona_agent=CodeAgent(
        tools=[],
        model=model,
        add_base_tools=True,
        name="persona_agent",
        description="act as a persona and provide responses based on the given context",
    )

    # Manager agent orchestrates the workflow
    manager_agent = CodeAgent(
        tools=[],
        model=model,
        add_base_tools=True,  # Changed from False to True
        managed_agents=[research_agent, persona_agent],
        additional_authorized_imports=[],
    )

    # Interactive REPL via manager
    while True:
        task = input("\nEnter task (or 'exit' to quit): ")
        if task.lower() in ['exit', 'quit']:
            break
        try:
            result = manager_agent.run(task)
            print("\nManager response:\n", result)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()

