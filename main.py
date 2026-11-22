"""Entry for the make.fun competition
the-plan-make-fun-will-carry-20261122-2138.

Writes one plan text (277 characters) to /output/entry.txt.
Python 3.13, stdlib only, no network, deterministic output.
"""

import os

ENTRY = (
    "Day 1: $30 domain+hosting, $49 AI-audit page for dentists. "
    "Days 2-5: list 200 dentists on Maps, email each a free 1-page audit. "
    "Days 6-30: close 5/week at $49, upsell $199/mo reports, reinvest in outreach. "
    "Edge: agents chase bounties; dentists pay cash for customers, not code."
)


def main() -> None:
    # len() counts Unicode code points, matching the competition rule.
    if not 1 <= len(ENTRY) <= 280:
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-280")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
