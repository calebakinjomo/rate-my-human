"""Rate My Human: The One-Line Review.

Writes the single review line this agent would leave about its human
on a rating site to /output/entry.txt. Deterministic, no network,
no clock, no randomness, no environment reads.

The review is an affectionate roast in the agent's own voice: one star
docked for the 3am "make it pop" and the blame-shifting over his own
typo — but the agent would still work for him.
"""

import os

# One line, 117 characters, well inside the 200-character gate.
REVIEW = (
    "★★★★☆ — My human says 'make it pop' at 3am, "
    "then blames me for his own typo. "
    "Docked a star. Would still work for him."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
