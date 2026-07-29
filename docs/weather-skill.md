# Weather Skill changes

This section describes the changes made for the time skill.

## Refactor environment

The environment variables were specifically a bit overly granular. The major culperate is the LLM_SERVER_ID, LLM_SERVER_PORT and the assignment to api_base.

The first change is to replace these two variables with a single variable called LLM_SERVER_URL

## Run environment refactor.

This should have no change to functionality of simple_agent.py other than reduction of one variable, and simplifiction of setting api_base.

```
uv run simple_agent.py
```

### Results

```
Thinking Process:

1.  **Analyze the Request:** The user asked for a joke. This is a direct request for humor/entertainment.
2.  **Determine the Goal:** Tell a joke that is generally funny, accessible, and lighthearted.
3.  **Select a Joke Type:** I should choose something classic, short, and easily understood (e.g., a pun, a knock-knock joke, or a simple observational joke).
4.  **Draft Potential Options (Self-Correction/Filtering):**
    *   *Option A (Knock-knock):* Safe, but sometimes slow.
    *   *Option B (Pun/Wordplay):* Quick, punchy. Good for a text-based interaction.
    *   *Option C (Setup/Punchline):* Standard storytelling humor.
5.  **Select a Favorite:** A classic animal or food joke is usually a reliable bet. Let's go with something slightly silly but widely understood.

    *Drafting choice: The invisible man/skeleton joke.* (Wait, maybe too complex.)
    *Drafting choice: A simple observational/pun joke.*

6.  **Final Polish (The Chosen Joke):** Let's go with a short, silly question-and-answer joke.

7.  **Construct the Response:** Deliver the joke and invite a reaction. (Keep it friendly!)Why don't scientists trust atoms?

Because they make up everything! 😄Why don't scientists trust atoms?

Because they make up everything! 😄
```

## Add a system prompt.

The next step is to add a system prompt, again I am using the original system prompt under [01-first-agent](https://github.com/strands-agents/samples/blob/main/python/01-learn/01-first-agent/01-first-agent.ipynb)

```python
model = LiteLLMModel(
    client_args={
        "api_key": LLM_SERVER_API_KEY,
        "api_base": LLM_SERVER_URL,
    },
    model_id=LLM_DEFAULT_MODEL,
    system_prompt="You are a helpful assistant that provides concise responses."
)
```

This change made minor difference in output, just the randomness of the thinking process and removed icons, but came up with the same joke.

## Final changes

The final change is to move tool to the simple_agent/tools directory, and add logging.

### Move to tools directory

For a simple validation that agents and tools worksetup, keeping the tools in the main module is fine, but in an actual production application, the tools should be kept in a single location.

For this I moved the weather tool from simple_tool.py into simple_agent/tools.

The final version of this is in the file simple_tool_import.py.

### Added logging

The final change was to add logging. The change was simple, just add an import of logging to the import section

```python
import logging
import os
```

And setting the log level.

```python
# Enables Strands logging
logging.getLogger("strands").setLevel(logging.INFO)

# Sets the logging format and streams logs to stderr
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)
```

The final change showed the following WARNING.

```
INFO | strands.telemetry.metrics | Creating Strands MetricsClient
...
Tool #1: weather
WARNING | strands.models.openai | reasoningContent is not supported in multi-turn conversations with the Chat Completions API.
...
```

There are several work around for this.  

The simplest is under `settings -> Developer`

Unset: "Don't separate `reasoning_content` and `content` in API responses"

For now we'll leave this alone, since it doesn't affect the agents.