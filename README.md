## URL Extractor & Browser Opener 

### Overview
A Python script that extracts all valid links from a given webpage and provides options to either open them in your browser or save them to a file. The script includes safeguards to prevent browser overload by limiting the number of tabs opened.

### Features
- Fetches and parses webpages using `requests` and `BeautifulSoup`.
- Extracts only valid HTTP/HTTPS or relative links.
- Removes duplicate links.
- Saves all extracted links to a text file (`extracted_links.txt`).
- Opens a limited number of links in browser tabs (default max: 20) to prevent overload.
- Displays a progress counter when opening links.
- Graceful error handling for invalid URLs, connection issues, timeouts, and parsing errors.
- User-friendly interface to choose whether to open links or just save them.

### File Structure
```text
url_extractor/
├── urlExtractor.py        # Main script
├── extracted_links.txt    # Generated file containing all links
└── README.md              # This documentation
```

### Requirements
- Python 3.6 or higher
- Required libraries:
  - `requests`
  - `beautifulsoup4`

You can install the required libraries using pip:
```bash
pip install requests beautifulsoup4
```

### Usage
1. **Run the script**:
```bash
python urlExtractor.py
```
2. **Enter a valid URL** when prompted (must start with `http://` or `https://`).
3. The script will fetch and parse the webpage, extract links, and save them to `extracted_links.txt`.
4. You will be prompted:
```
Do you want to open the links in your browser or only save them?
1. Open links in browser
2. Only save to file
```
- Enter `1` to open links in your default browser (up to 20 tabs).
- Enter `2` to only save the links to the text file without opening browser tabs.

### File Output
- **extracted_links.txt**: Contains all the extracted links, one per line.
