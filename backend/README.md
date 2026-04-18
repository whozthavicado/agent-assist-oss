# Backend Demo

This folder contains the first backend prototype for agent-assist-oss.

## Current files

- `demo_assist.py`: a simple rule-based prototype that detects basic conversation signals and generates:
  - detected signals
  - suggested replies
  - summaries
  - CRM-ready notes
- `run_batch_demo.py`: runs the same logic on a small test set
- `test_demo_assist.py`: basic unit tests for the current backend logic
- `test_messages.json`: sample customer messages for batch testing
- `api.py`: minimal local HTTP API for message analysis
- `sample_request.json`: example request payload for the API

## Why this exists

This is an intentionally simple first step.

The goal is to validate the workflow and structure before adding more advanced logic, model integrations, or real-time pipelines.

## How to run

Manual demo:

`python backend/demo_assist.py`

Batch demo:

`python backend/run_batch_demo.py`

Local API:

`python backend/api.py`

Run tests:

`python -m unittest backend/test_demo_assist.py`

## API routes

- `GET /health`
- `POST /analyze`

## Example request body

`{"message": "It's too expensive. I need to think about it."}`

## Example output

- detected signals: `price_objection`, `hesitation`
- suggested reply
- summary
- CRM note

## Extra references

- practical examples: [`docs/examples.md`](../docs/examples.md)

## Next steps

Possible next backend improvements:

- load larger datasets
- score conversation quality
- support configurable rules
- add prompt-based LLM mode
- expose a more complete API
