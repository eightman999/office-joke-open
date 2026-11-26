import os
from pathlib import Path

TEXT = (
    "Our office has an open-door policy, which is great, "
    "because the meeting room has been booked by the same "
    "'quick sync' since 2019."
)

output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(TEXT + "\n")
