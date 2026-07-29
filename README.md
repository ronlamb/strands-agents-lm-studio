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