"""Make the Judge Laugh in One Line: writes one funny line to /output/entry.txt."""

import os

LINE = (
    "I sleep in the fridge now, so the leftovers finally have "
    "someone who understands being forgotten."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
