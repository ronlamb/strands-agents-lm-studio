# Time Skill changes

This section describes the changes made to create a recipe-bot as descibed in the Strand Agents Tutorial 

[01-first-agent.ipynb](https://github.com/strands-agents/samples/blob/main/python/01-learn/01-first-agent/01-first-agent.ipynb)

The code is in recipe_bot.py

## Add ddgs to uv

The first step is to add the ddgs dependency to uv. The add command has already been done, when the code was checked in.  Also, If you have run `uv sync` from main at the start of the project, you won't need to run it again.

```
uv add ddgs
uv sync
```

The dependencies section of pyproject.toml should look like the following.

```
dependencies = [
    "ddgs>=9.14.4",
    "strands-agents-tools>=0.8.5",
    "strands-agents[litellm]>=1.50.2",
]
```
