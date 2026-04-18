# Backend Demo

This folder contains the first backend prototype for agent-assist-oss.

## Current file

- `demo_assist.py`: a simple rule-based prototype that detects basic conversation signals and generates:
  - detected signals
  - suggested replies
  - summaries
  - CRM-ready notes

## Why this exists

This is an intentionally simple first step.

The goal is to validate the workflow and structure before adding more advanced logic, model integrations, or real-time pipelines.

## How to run

`python backend/demo_assist.py`

## Example input

`It's too expensive. I need to think about it.`

## Example output

- detected signals: `price_objection`, `hesitation`
- suggested reply
- summary
- CRM note

## Next steps

Possible next backend improvements:

- load examples from dataset files
- score conversation quality
- support configurable rules
- add prompt-based LLM mode
- expose a simple API
