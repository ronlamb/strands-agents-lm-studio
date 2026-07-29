# Simple agent example using Strands and LiteLLMModel
# Modified from recipe_bot.py in the Strands samples repo
# https://github.com/strands-agents/samples/blob/main/python/01-learn/01-first-agent/recipe-bot-cli/recipe_bot.py

import logging
import os

from strands import Agent, tool
from simple_agent.tools.websearch_skill import websearch # Import the weather tool
from strands.models.litellm import LiteLLMModel

# Enables Strands logging
logging.getLogger("strands").setLevel(logging.INFO)

# Sets the logging format and streams logs to stderr
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)

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

# Create a recipe assistant agent
recipe_agent = Agent(
    model=model,
    system_prompt="""You are RecipeBot, a helpful cooking assistant.
    Help users find recipes based on ingredients and answer cooking questions.
    Use the websearch tool to find recipes when users mention ingredients or to
    look up cooking information.""",

    # Import the websearch tool we created above
    tools=[websearch],
)

if __name__ == "__main__":
    print("\nRecipeBot: Ask me about recipes or cooking! Type 'exit' to quit.\n")

    # Run the agent in a loop for interactive conversation
    while True:
        user_input = input("\nYou > ")
        if user_input.lower() == "exit":
            print("Happy cooking!")
            break
        response = recipe_agent(user_input)
        print(f"\nRecipeBot > {response}")
