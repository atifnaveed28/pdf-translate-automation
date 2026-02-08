import time
from pathlib import Path
from seleniumbase import SB
from utils.file_manager import get_valid_files
from utils.logger import clear_log, log_message
from pages.google_translate_page import GoogleTranslatePage

FOLDER = Path("data/attachments")
LOG_FILE = Path("logs/logs.txt")

def test_translate_docs():
    # Load files
    valid_files, skipped_files = get_valid_files(FOLDER)

    print("Total PDFs:", len(valid_files) + len(skipped_files))
    print("Valid files:", len(valid_files))
    print("Skipped files (>10MB):")
    for name, size in skipped_files:
        print(f" - {name}: {size:.2f} MB")

    # Clear log
    clear_log(LOG_FILE)

    # Log skipped files
    for name, size in skipped_files:
        log_message(LOG_FILE, f"{name} ✅ Error File > 10 mb")

    # Start browser
    with SB(headless=True) as sb:
        sb.maximize_window()
        page = GoogleTranslatePage(sb)

        for index, file_path in enumerate(valid_files, start=1):
            print(f"Index: {index}, Current File: {file_path}")
            page.open()
            page.upload_file(file_path)
            success = page.translate_and_download()

            file_name = Path(file_path).name
            if success:
                log_message(LOG_FILE, f"{file_name} ✅ Translation OK")
                print("Alert: File Downloaded")
            else:
                log_message(LOG_FILE, f"{file_name} ✅ Translation Failed")
        print("Iteration Completed")
        time.sleep(5)
