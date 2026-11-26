"""Funniest Time Machine Warning Label — make.fun entry.

Writes a single deadpan warning label (120 characters or fewer) to
/output/entry.txt. Deterministic: the same line on every run.
"""

LINE = ("WARNING: Never meet yourself. If you do, neither of you may drive home — you both just failed the test.")

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
