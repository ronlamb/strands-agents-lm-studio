# Time Skill changes

This section describes the changes made for the time skill.

## Refactor environment

The environment variables were specifically a bit overly granular. The major culperate is the LLM_SERVER_ID, LLM_SERVER_PORT and the assignment to api_base.

The first change is to replace these two variables with a single variable called LLM_SERVER_URL

## Run environment refactor.

This should have no change to functionality of simple_agent.py other than reduction of one variable, and simplifiction of setting api_base.