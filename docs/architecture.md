# Architecture

## Project goal

Build a modular open-source framework that helps human agents perform better during and after conversations.

## Core idea

The system takes conversation input and turns it into useful assistance outputs.

## High-level flow

1. Conversation input
   - live transcript
   - chat messages
   - post-call transcript

2. Signal detection
   - objection detection
   - intent cues
   - urgency cues
   - compliance-sensitive phrases

3. Assistance engine
   - suggested replies
   - objection-handling support
   - next-step suggestions

4. Post-conversation outputs
   - summary
   - CRM-ready note
   - QA support
   - follow-up recommendation

## Proposed modules

### Input layer
Handles transcripts, chat messages, or conversation chunks.

### Detection layer
Identifies patterns such as:
- price objections
- hesitation
- information requests
- refusal signals
- escalation cues

### Assistance layer
Generates:
- short reply suggestions
- objection-handling ideas
- clearer phrasing
- next-step guidance

### Output layer
Formats results for:
- CRM notes
- summaries
- QA review
- internal dashboards

## Version 1 scope

The first version focuses on:

- text-based inputs
- simple objection detection
- suggested replies
- post-call summaries
- CRM notes

## Non-goals for version 1

The first version does not aim to:

- replace human agents
- run a full telephony stack
- act as a fully autonomous sales agent
- provide production-grade compliance guarantees
