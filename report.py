import json
import os
from datetime import datetime

# Path to your JSON file (same as tracker)
LOG_FILE = os.path.join(os.path.expanduser("~"), "Documents", "usage_log.json")

def load_logs():
    if not os.path.exists(LOG_FILE):
        print("⚠️ No log file found.")
        return {}
    with open(LOG_FILE, "r") as f:
        return json.load(f)

def seconds_to_hms(seconds):
    """Convert seconds to H:M:S format"""
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h}h {m}m {s}s"

def report(day=None):
    logs = load_logs()
    if not logs:
        return

    if day is None:
        day = datetime.now().strftime("%Y-%m-%d")

    if day not in logs:
        print(f"⚠️ No logs for {day}")
        return

    print(f"\n📊 Usage Report for {day}")
    print("-" * 40)

    total = 0
    for app, seconds in logs[day].items():
        print(f"{app:30} {seconds_to_hms(seconds)}")
        total += seconds

    print("-" * 40)
    print(f"Total: {seconds_to_hms(total)}")

if __name__ == "__main__":
    report()
