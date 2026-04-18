# Backend Demo

This folder contains the first backend prototype for agent-assist-oss.

## Current files

- `demo_assist.py`: a simple rule-based prototype that detects basic conversation signals and generates:
  - detected signals
  - suggested replies
  - summaries
  - CRM-ready notes
- `signal_rules.json`: configurable signal detection rules loaded by the backend demo
- `run_batch_demo.py`: runs the same logic on a small test set
- `test_demo_assist.py`: unit tests for the rule-based backend logic and rule loading
- `test_api.py`: tests for the local API endpoints and input validation
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

`python -m unittest discover -s backend -p "test_*.py"`

## Configurable rules

The backend now loads signal rules from:

`backend/signal_rules.json`

This makes it easier to extend signals, keywords, and language coverage without editing the core logic every time.

If the rules file is missing or invalid, the backend falls back to the built-in default rules.

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
- support more configurable workflow layers
- add prompt-based LLM mode
- expose a more complete API
