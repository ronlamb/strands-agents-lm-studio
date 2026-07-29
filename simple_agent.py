from strands import Agent
import litellm
from strands.models.litellm import LiteLLMModel
import os

LLM_SERVER_IP = os.environ.get("LLM_SERVER_IP", "localhost")
LLM_SERVER_PORT = os.environ.get("LLM_SERVER_PORT", "1234")
LLM_SERVER_API_KEY = os.environ.get("LLM_SERVER_API_KEY", "none-needed")
LLM_DEFAULT_MODEL = os.environ.get("LLM_DEFAULT_MODEL", "lm_studio/google/gemma-4-e2b")

model = LiteLLMModel(
    client_args={
        "api_key": LLM_SERVER_API_KEY,
        "api_base": f"http://{LLM_SERVER_IP}:{LLM_SERVER_PORT}/v1",
    },
    model_id=LLM_DEFAULT_MODEL,
)
# Create a simple agent instance
agent = Agent(
    system_prompt="You are a helpful assistant.",
    model=model,
    tools=[]  # Add custom tools or MCP clients here
)

# Run the agent with a prompt
response = agent("What is the current time?")
print(response)
