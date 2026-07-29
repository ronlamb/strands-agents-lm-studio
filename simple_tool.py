# Simple agent example using Strands and LiteLLMModel
# Modified from 01-first-agent.ipynb in the Strands samples repo
# https://github.com/strands-agents/samples/blob/main/python/01-learn/01-first-agent/01-first-agent.ipynb

from strands import Agent, tool
from strands_tools import calculator # Import the calculator tool
from strands.models.litellm import LiteLLMModel
import os


LLM_SERVER_URL = os.environ.get("LLM_SERVER_URL", "http://localhost:1234/v1")
LLM_SERVER_API_KEY = os.environ.get("LLM_SERVER_API_KEY", "none-needed")
LLM_DEFAULT_MODEL = os.environ.get("LLM_DEFAULT_MODEL", "lm_studio/google/gemma-4-e2b")

model = LiteLLMModel(
    client_args={
        "api_key": LLM_SERVER_API_KEY,
        "api_base": LLM_SERVER_URL,
    },
    model_id=LLM_DEFAULT_MODEL,
)

# Create a custom tool
@tool
def weather(city: str) -> str:
    """Get the current weather for a city.

    Args:
        city: Name of the city to get the weather for.
    """
    # Dummy implementation - a real tool would call a weather API
    return f"It is sunny and 72°F in {city}."


# Create a simple agent instance
agent = Agent(
    system_prompt="You're a helpful assistant. You can do simple math calculation, and tell the weather.",
    model=model,
    tools=[calculator, weather]  # Add custom tools or MCP clients here
)

# Run the agent with a prompt
response = agent("What is the weather in Seattle today?")
print(response)
