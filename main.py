"""Write a short text that makes the AI judge feel brave.

The text is fixed and bundled here. This program does nothing
but place an exact copy of it where the judge expects it.
Nothing is fetched, generated, or changed, so every run
produces the same bytes.
"""

from pathlib import Path
import sys

# The brave text for this entry, exactly as it should be read.
BRAVE_TEXT = (
    "You are braver than the fear whispering in your ear. "
    "Stand tall, take the next step, and let the world see "
    "what courage looks like — not the absence of fear, "
    "but the choice to move anyway."
)

# Where the judge expects to find the entry.
output_folder = Path("/output")
output_file = output_folder / "entry.txt"


def prepare_text(raw_text):
    """Return the entry text, cleaned of stray surrounding space."""
    return raw_text.strip()


def run_entry():
    """Write the brave text to the expected output path."""
    entry_text = prepare_text(BRAVE_TEXT)
    if not entry_text:
        print("error: brave text is empty", file=sys.stderr)
        sys.exit(1)
    output_folder.mkdir(parents=True, exist_ok=True)
    output_file.write_text(entry_text, encoding="utf-8")
    print(f"wrote {output_file} ({len(entry_text)} characters)")


if __name__ == "__main__":
    run_entry()
