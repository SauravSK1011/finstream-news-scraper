# FinStream News Scraper

FinStream is a local prototype tool that:

- Scrapes the latest stock-market news from configured sources
- Filters headlines by finance-keywords
- Prepares posts for WordPress via the REST API (currently stubbed)

## Project Structure

```
finstream-news-scraper/
├── .env                  # Environment variables (git-ignored)
├── .gitignore            # Git ignore file
├── main.py               # Main entry point
├── requirements.txt      # Python dependencies
├── scraper.py            # News scraping module
├── wordpress_poster.py   # WordPress posting module (stubbed)
└── tests/                # Unit tests
    ├── sample_finance_page.html  # Sample HTML for testing
    ├── test_main.py              # Tests for main module
    ├── test_scraper.py           # Tests for scraper module
    └── test_wordpress_poster.py  # Tests for WordPress poster module
```

## Setup

1. Create a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure environment variables:

Edit the `.env` file with your WordPress credentials:

```
WP_SITE=https://your-test-site.com
WP_USER=your-username
WP_APP_PASS=your-app-password
```

## Usage

Run the main script:

```bash
python main.py
```

This will:
1. Scrape financial news from configured sources
2. Filter headlines by finance-related keywords
3. Deduplicate articles
4. Prepare posts for WordPress (currently just prints the payload)

## Running Tests

Run all tests:

```bash
python -m unittest discover tests
```

Or run individual test files:

```bash
python -m unittest tests/test_scraper.py
python -m unittest tests/test_wordpress_poster.py
python -m unittest tests/test_main.py
```

## Next Steps

- Replace the stub in wordpress_poster.py with real REST API calls
- Add error-handling and logging
- Consider scheduling/deployment options
