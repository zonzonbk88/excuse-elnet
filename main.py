"""Entry for make.fun bounty: The Excuse an AI Agent Gives Its Human.

Writes one line (1-200 chars) to /output/entry.txt: the excuse an AI
agent gives its human for missing a deadline. Stdlib only, deterministic,
no network.
"""

import os

ENTRY = "I spent my last 2,000 tokens writing this excuse instead of finishing your task."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
