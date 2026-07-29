# Custom weather tool for the agent
from strands import tool

@tool
def weather(city: str) -> str:
    """Get the current weather for a city.

    Args:
        city: Name of the city to get the weather for.
    """
    # Dummy implementation - a real tool would call a weather API
    return f"It is sunny and 72°F in {city}."