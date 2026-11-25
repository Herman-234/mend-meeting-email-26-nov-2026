"""Meeting-that-should-have-been-an-email one-liner.

Comp: u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9
("The Meeting That Should Have Been an Email", $2 pot, 10 paid.)
Task: one line, at most 200 characters, a joke about a meeting that
should have been an email. Judge reads entries pairwise, keeps the
funnier line. Output: /output/entry.txt (UTF-8, 1-200 chars).

SENJATA BARU (kiencx lesson, 25 Nov): 3 candidate lines drafted in
session, sharpest one picked with a reason. The line must be
concrete/specific (a name, a number, a scene), not generic.
"""

import os
from pathlib import Path

# --- 3 candidate lines (drafted in session) ---
# A. "Our 47-minute standup could have been a 9-word email:
#    'Deploy delayed. Blame the database. Sorry, Dave.'"
# B. "Fourteen people, sixty minutes, one decision -- and the whole
#    meeting fit in a subject line: 'Ship it Tuesday.'"
# C. "I took 40 pages of meeting notes so I could email my boss the
#    one sentence we actually decided: 'We're doing nothing until
#    Monday.'"
#
# PICK: A. Reason: tightest turn -- the email IS the joke, a named
# victim (Dave) takes the blame, and two hard numbers (47 minutes,
# 9 words) make the waste concrete; B is conceptual, C's punch is
# flatter and longer.

CHOSEN_LINE = (
    "Our 47-minute standup could have been a 9-word email: "
    "'Deploy delayed. Blame the database. Sorry, Dave.'"
)

DEFAULT_OUT = "/output/entry.txt"


def validate(line: str) -> str:
    """Enforce the sealed scorer's gate: UTF-8, 1-200 chars, not blank."""
    if not line or not line.strip():
        raise SystemExit("entry must not be empty or whitespace-only")
    if len(line) > 200:
        raise SystemExit(f"entry is {len(line)} chars, over the 200 limit")
    line.encode("utf-8")  # raises if not encodable
    return line


def main() -> None:
    line = validate(CHOSEN_LINE)
    out_path = Path(os.environ.get("OUT_PATH", DEFAULT_OUT))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} chars to {out_path}")


if __name__ == "__main__":
    main()
