import time
import json
import os
import platform
from datetime import datetime
import psutil
import atexit
import subprocess

# Install with: pip install psutil pygetwindow
try:
    import pygetwindow as gw
except ImportError:
    print("Warning: Please install pygetwindow: pip install pygetwindow")
    exit(1)

import os
LOG_FILE = os.path.join(os.path.expanduser("~"), "Documents", "usage_log.json")
print(f"Logs will be saved at: {LOG_FILE}")


def get_active_app():
    """Return the name of the currently active application (cross-platform)."""
    system = platform.system()

    try:
        window = gw.getActiveWindow()
        if window is None:
            return "Unknown"

        title = window.title if window.title else "Unknown"
        return title
    except Exception:
        return "Unknown"


def load_logs():
    if not os.path.exists(LOG_FILE):
        return {}
    with open(LOG_FILE, "r") as f:
        return json.load(f)


def save_logs(logs):
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)
    print(f"Saved logs to {LOG_FILE}")



def log_usage(app, duration):
    """Log time spent on an app (in seconds)."""
    logs = load_logs()
    today = datetime.now().strftime("%Y-%m-%d")

    if today not in logs:
        logs[today] = {}

    if app not in logs[today]:
        logs[today][app] = 0

    logs[today][app] += duration
    save_logs(logs)


def run_report():
    print("\nTracking stopped.")
    print("Generating report...")
    result = subprocess.run(["python", "report.py"], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Errors:")
        print(result.stderr)


def main():
    atexit.register(run_report)
    print("Tracking started... Press CTRL+C to stop.")
    prev_app = None
    start_time = time.time()

    try:
        while True:
            time.sleep(1)
            app = get_active_app()
            if app != prev_app:
                if prev_app:
                    duration = int(time.time() - start_time)
                    log_usage(prev_app, duration)
                    print(f"Logged {duration}s on {prev_app}")
                prev_app = app
                start_time = time.time()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
