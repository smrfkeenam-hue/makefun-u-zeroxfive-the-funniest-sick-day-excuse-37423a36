import os

# One-line sick-day excuse: a snooze-button injury, half believable,
# with the joke landing on the body's "official filing" near the end.
ENTRY = "I pulled a muscle reaching for the snooze button, so my body has officially filed for a rest day and I'm just the messenger."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
