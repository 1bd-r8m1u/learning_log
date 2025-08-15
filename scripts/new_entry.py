import os
from datetime import date
import subprocess

# Paths
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
entries_dir = os.path.join(base_dir, "entries")
today_file = os.path.join(entries_dir, f"{date.today()}.md")

# Template
template = f"""# {date.today()} — Learning Log

**Title:**  

**Goal:**  

**Time Spent:**  

**Learnings:**  

**Next Steps:**  
"""

os.makedirs(entries_dir, exist_ok=True)

if not os.path.exists(today_file):
    with open(today_file, "w") as f:
        f.write(template)
    print(f"Created: {today_file}")
else:
    print(f"File already exists: {today_file}")

# Opens the file in Termux's nano (you can also use vim or micro)
try:
    subprocess.call(["nano", today_file])
except FileNotFoundError:
    print("Nano not found. Edit the file manually or install nano in Termux.")
