# starter code 
from dotenv import load_dotenv
from smolagents import CodeAgent, InferenceClientModel
from mcp.mcp_web_search import web_search # Updated import

load_dotenv()

def main():
    # Initialize the LLM model
    model = InferenceClientModel(model_id="Qwen/Qwen2.5-72B-Instruct")

    # Create agent
    agent = CodeAgent(
        tools=[web_search], # Updated to use web_search
        model=model,
        #add_base_tools=True,
        #additional_authorized_imports=["time", "pandas", "json"],
    )

    # Agent conversation
    while True:
        task = input("\nEnter task (or 'exit' to quit): ")
        if task.lower() in ['exit', 'quit']:
            break
        try:
            result = agent.run(task)
            print("\nAgent response:\n", result)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()

