PDF Translation Automation

Overview:
This project automates the translation of PDF documents using Google Translate via a SeleniumBase + Python automation framework.
It is designed using the Page Object Model (POM) for maintainability and modularity.
The project supports logging, PDF validation, and headless execution for CI/CD workflows.

Features:
Upload PDFs to Google Translate automatically.
Download translated PDFs.
Validate PDFs to ensure size ≤ 10 MB.
Retry translations up to 10 times per file if processing is slow.
Logs translation results in UTF-8 encoded logs/logs.txt.
Fully structured with Page Objects, Utils, and pytest.
Supports headless browser execution for CI/CD (GitHub Actions).

Project Structure:
PDF_Translation/
├── page_objects/         # Page Object classes
│   └── google_translate_page.py
├── tests/                # pytest test scripts
│   └── test_translate_docs.py
├── utils/                # Helper modules
│   ├── file_manager.py
│   └── logger.py
├── data/attachments/   # PDF files to translate
├── logs/                 # Logs generated during execution
│   └── logs.txt
├── .github/workflows/    # GitHub Actions CI workflow
│   └── pytest.yml
├── pytest.ini            # Pytest configuration
└── requirements.txt      # Python dependencies


Running Locally:
Run the PDF translation script in a headless browser:
pytest -s tests/test_translate_docs.py

Customizing:
PDF Folder: Change FOLDER = Path("data/attachments") in the test file or utils.
Log Path: Modify LOG_FILE = Path("logs/logs.txt").
Max File Size: Modify MAX_SIZE_MB = 10 in utils/file_manager.py.

GitHub Actions CI:
Automatically runs tests on push or pull request.
Uses headless Chrome on Ubuntu runners.
Uploads logs/logs.txt as an artifact for review.
Run workflow manually or push to main to trigger CI/CD.

Project Workflow:
Load PDF files from data/attachments.
Filter out files larger than 10 MB.
Open Google Translate in SeleniumBase.
Upload PDF and click Translate(French to English)
Wait for translation, then click Download.
Retry up to 10 times if processing is slow.
Log results in logs/logs.txt.

Clone the repository:
git clone https://github.com/atifnaveed28/pdf-translate-automation.git
cd PDF_Translation

Install dependencies:
pip install -r requirements.txt