# Simple agent example using Strands and LiteLLMModel
# Modified from the readme: https://github.com/strands-agents/samples

from strands import Agent
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

# Create a simple agent instance
agent = Agent(
    system_prompt="You are a helpful assistant that provides concise responses.",
    model=model,
    tools=[]  # Add custom tools or MCP clients here
)

# Run the agent with a prompt
response = agent("Hello! Tell me a joke.")
print(response)
