import os
from pathlib import Path

TEXT = "I love our open-plan office: zero privacy, full visibility, and somehow nobody can find the person who ate my yogurt."

output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(TEXT + "\n")
