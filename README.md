# strands-agents-lm-studio
A step by step creation of a simple Strands agent locally using LM Studio and LiteLLM instead of AWS. 

## Purpose

This repo was created to capture how I created a simple Strands agent, and is intended to be used by other people as a tutorial for creating a Strands agent without having to use AWS Bedrock.

## Branch Structure

Each step of the project will be created in a branch using the following naming convention:

`'step number'`_`'short description'`

Where:
- **step number** - Us the steps in order to follow along.
- **short_description** - is a short description of the change

## Current branches

| Branch Name | Description |
| ----------- | ----------- |
| main | The base branch.  Contains instruction on how to run and setup a bare bones agent |
| [01_time_skill](docs/time-skill) | Refactor environment and add the time skill |

## Directory Layout

```
├── docs/
├── tests/
└── strands_agent/
```

## Setting up python and uv

For this project uv is used to build the application.  For directions on installing uv see the [uv](https://github.com/astral-sh/uv) github repo.

The following steps were run to create the initial pyproject.toml file

```
uv init --python 3.13
uv add strands-agents[litellm]
uv add strands-agents-tools
```

The dependency strands-agents[litellm], also installs strands agents.

## Run the agent

To run the agent you either activate and run the script.

```
. .venv/Scripts/activate
python -m simple_agent
```

or through uv

```
uv run simple_agent.py
```

### Results

```
Thinking Process:

1.  **Analyze the Request:** The user asked for a joke.
2.  **Determine the Goal:** Tell a joke that is generally funny and appropriate.
3.  **Select a Joke Category/Type:** Since I don't know the user's preference, a classic, clean, widely accessible joke (like a knock-knock joke or a simple riddle/setup) works well.
4.  **Draft Joke Options (Internal Selection):**
    *   Option A: Knock-knock. (Safe, but sometimes cliché.)
    *   Option B: Pun/Wordplay. (Good for quick delivery.)
    *   Option C: Story setup. (More elaborate.)
5.  **Select a Specific Joke:** I'll go with a slightly silly, observational joke that is quick to deliver. (The invisible man or something similar often works.)

6.  **Refine and Deliver:** (Self-Correction: Let's go with a classic animal joke—they are usually reliable.)

    *   *Idea:* Why don't scientists trust atoms? Because they make up everything! (A bit too sciencey?)
    *   *Idea:* Why did the scarecrow win an award? Because he was outstanding in his field! (Good, classic.)

7.  **Final Output Generation.** (Using the scarecrow joke.)Why don't scientists trust atoms?

Because they make up everything! 😄Why don't scientists trust atoms?

Because they make up everything! 😄
```
