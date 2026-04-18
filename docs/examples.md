# Examples

This page shows practical input and output examples for the current rule-based backend prototype.

## 1. Sales objection example

### Input

`It's too expensive. I need to think about it.`

### Detected signals

- `price_objection`
- `hesitation`

### Example behavior

- generate a more confident suggested reply
- summarize the customer intent
- create a CRM-ready note for follow-up

## 2. Support frustration example

### Input

`I've already explained this twice and nothing has changed.`

### Detected signals

- `frustration`
- `repeat_issue`

### Example behavior

- acknowledge frustration
- suggest a response focused on ownership and clarity
- create a structured summary for the next agent or reviewer

## 3. Collections delay example

### Input

`I can't pay today. Maybe next week.`

### Detected signals

- `payment_delay`
- `uncertain_commitment`

### Example behavior

- suggest a follow-up question to get a realistic date
- summarize the delay clearly
- generate a CRM note for collections follow-up

## 4. Information request example

### Input

`Can you send me the information first?`

### Detected signals

- `info_request`

### Example behavior

- suggest a reply that confirms next steps
- keep the interaction moving instead of ending with a passive handoff

## Why examples matter

Examples make the project easier to understand quickly.

They help contributors, potential users, and future maintainers see how the current logic behaves before the project expands into more advanced pipelines or model-based workflows.
