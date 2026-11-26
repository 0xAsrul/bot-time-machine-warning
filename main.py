"""Funniest Time Machine Warning Label — make.fun entry.

Writes one deadpan warning label (120 characters or fewer) to
/output/entry.txt. Deterministic: the same line on every run.
"""

LINE = "WARNING: If you meet yourself, do not wave back. Your past self read this label first and waved anyway."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
