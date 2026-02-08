from pathlib import Path

def clear_log(log_path):
    Path(log_path).write_text("", encoding="utf-8")

def log_message(log_path, message):
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(message + "\n")
