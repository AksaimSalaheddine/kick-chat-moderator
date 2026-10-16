# Kick Chat Moderator

A small Python chat-moderation engine for detecting inappropriate messages. It is currently a command-line project with JSON-configured moderation rules; it is not yet connected to Kick's API.

## What it does

- Detects configured insults, spam, and harassment terms.
- Detects simple obfuscation, including `s-p-a-m`, `s.p.a.m`, `s p a m`, `s/p/a/m`, `s_p_a_m`, and `s@p@a@m`.
- Matches words case-insensitively.
- Avoids false positives inside larger words, such as `newspam` and `spamming`.
- Chooses the most severe matching action: `warn`, `timeout`, or `ban`.
- Loads rules from a JSON configuration file.

## Project structure

```text
kick-chat-moderator/
├── config/
│   └── moderation_rules.json  # Editable moderation rules
├── tests/                     # Automated pytest suite
├── filter.py                  # Moderation decision logic
├── main.py                    # Interactive command-line program
├── rule_loader.py             # JSON loading and validation
├── text_detection.py          # Word and obfuscation matching
└── README.md
```

## Requirements

- Python 3
- `pytest` for running the test suite

The project currently includes a local virtual environment in `.venv`.

## Run the moderator

From the project directory, run:

```bash
.venv/bin/python main.py
```

Enter a chat message at the prompt. Type `exit` to quit.

For example, a message containing a configured spam term returns its matching word and action. A message with no match is allowed.

## Run the tests

Use Python to launch pytest so the project modules are found correctly:

```bash
.venv/bin/python -m pytest -q
```

Latest local verification: **38 tests passed**.

## Configure moderation rules

Rules live in [`config/moderation_rules.json`](config/moderation_rules.json). Each action must have a list of non-empty words or phrases:

```json
{
  "ban": ["harassment"],
  "timeout": ["spam", "stop spamming"],
  "warn": ["idiot", "shut up", "sucks"]
}
```

To add a rule, add a word or phrase to the list for its intended action, then run the tests. The supported actions are:

- `warn` — lowest severity
- `timeout` — medium severity
- `ban` — highest severity

When several rules match one message, the highest-severity action is selected.

## Current limitations

- Each moderation decision returns the same structured result with `allowed`, `action`, `severity`, and `matches` fields.
- No HTTP API, database, authentication, rate limiting, logging, Docker configuration, or cloud deployment exists yet.
- The project is not connected to Kick and does not take real moderation actions.
- Matching is intentionally simple and should continue to gain false-positive and Unicode coverage.

## Next steps

The next milestone is a FastAPI service with `POST /moderate` and `GET /health` endpoints.
