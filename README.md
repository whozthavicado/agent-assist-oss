# agent-assist-oss

Open-source AI framework for real-time agent assistance, objection handling, summaries, and QA support.

## Overview

agent-assist-oss is an open-source project for building tools that help human agents perform better during and after conversations.

It is designed for workflows in:

- call centers
- sales teams
- customer support
- collections
- internal QA operations

The goal is not to replace human agents. The goal is to give them better support, faster context, and more consistent outputs.

## Why this exists

Many teams still rely on static scripts, scattered documentation, manual notes, and inconsistent follow-up.

That creates common problems such as:

- uneven customer experiences
- slower agent response quality
- repetitive after-call work
- weak CRM notes
- poor visibility into objections and conversation quality

agent-assist-oss aims to provide a practical open-source base for building agent-assist systems that solve those problems.

## Core capabilities

The project is being built around workflows such as:

- objection detection
- suggested replies
- real-time guidance
- automatic summaries
- CRM-ready notes
- QA support and conversation review

## Version 1 focus

The first version focuses on assisting human agents, not replacing them.

Initial scope:

- detect common objections
- suggest better replies
- generate post-conversation summaries
- create clean CRM-ready notes

## Example use cases

### Sales

Help agents respond to objections such as:

- "It's too expensive."
- "I need to think about it."
- "Send me the information."

### Support

Help teams summarize issues faster and keep notes more consistent.

### Collections

Help agents detect payment intent signals, handle refusal patterns, and improve follow-up structure.

### QA

Help reviewers generate structured summaries and identify quality signals more efficiently.

## Backend demo

The repository already includes a simple rule-based backend prototype.

Current backend demo features:

- detect common conversation signals
- generate suggested replies
- generate summaries
- generate CRM-ready notes
- run single-message and batch demos

Manual demo:

`python backend/demo_assist.py`

Batch demo:

`python backend/run_batch_demo.py`

See [backend/README.md](backend/README.md) for backend details.

## Quick start

### Requirements

- Python 3.10 or newer recommended
- No external dependencies required for the current backend demo

### Run the manual demo

`python backend/demo_assist.py`

### Run the batch demo

`python backend/run_batch_demo.py`

### Run the local API

`python backend/api.py`

### Test the API

Health check:

`curl http://127.0.0.1:8000/health`

Analyze a message:

`curl -X POST http://127.0.0.1:8000/analyze -H "Content-Type: application/json" -d "{\"message\":\"It's too expensive. I need to think about it.\"}"`

You can also use the sample payload in:

`backend/sample_request.json`

## Project structure

```text
agent-assist-oss/
├─ README.md
├─ CONTRIBUTING.md
├─ .gitignore
├─ backend/
│  ├─ README.md
│  ├─ demo_assist.py
│  ├─ run_batch_demo.py
│  ├─ api.py
│  ├─ test_messages.json
│  └─ sample_request.json
├─ frontend/
├─ docs/
│  ├─ architecture.md
│  ├─ roadmap.md
│  ├─ use-cases.md
│  └─ vision.md
├─ examples/
│  └─ objection-handling-demo.md
├─ datasets/
│  └─ synthetic-call-examples.json
└─ screenshots/

```

## Current project status

This is an early-stage open-source project.

The current repository includes:

- project documentation
- initial architecture
- use cases
- roadmap
- vision
- a first synthetic dataset
- a simple backend prototype
- a batch test runner
- a minimal local API
- a sample API request payload
- a simple objection-handling example

## Documentation

- [Architecture](docs/architecture.md)
- [Roadmap](docs/roadmap.md)
- [Use Cases](docs/use-cases.md)
- [Vision](docs/vision.md)
- [Backend Demo](backend/README.md)
- [Example Demo](examples/objection-handling-demo.md)
- [Contributing](CONTRIBUTING.md)

## Long-term vision

Build a practical open-source foundation for agent-assist systems that can later connect to:

- voice pipelines
- chat workflows
- CRM systems
- QA processes
- multiple LLM providers

## Contributing

Contributions are welcome, especially in:

- documentation
- synthetic datasets
- prompt design
- backend logic
- frontend prototypes
- workflow ideas based on real agent operations

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

Apache License 2.0
