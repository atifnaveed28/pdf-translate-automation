from pathlib import Path

MAX_SIZE_MB = 10

def get_valid_files(folder_path):
    folder = Path(folder_path)
    all_files = [f for f in folder.iterdir() if f.is_file()]
    valid_files = []
    skipped_files = []

    for f in all_files:
        if f.stat().st_size <= MAX_SIZE_MB * 1024 * 1024:
            valid_files.append(str(f.resolve()))
        else:
            skipped_files.append((f.name, f.stat().st_size / (1024 * 1024)))

    return valid_files, skipped_files
