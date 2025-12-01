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

### Example Workflow
```bash
$ python urlExtractor.py
Enter a URL: https://news.ycombinator.com

Fetching page: https://news.ycombinator.com
Found 150 links, saving to file...

All links saved to '/path/to/extracted_links.txt'

Do you want to open the links in your browser or only save them?
1. Open links in browser
2. Only save to file
Enter 1 or 2: 1

Found 150 links, opening only the first 20 to prevent overload.

Opening 20 links in browser...

[1/20] Opened: https://news.ycombinator.com/item?id=12345678
[2/20] Opened: https://example.org/article1
...
[20/20] Opened: https://github.com/topics/python

Done! All accessible links were opened.
```

### File Output Format
The script creates `extracted_links.txt` with one URL per line:
```
https://example.com/page1
https://example.com/page2
https://subdomain.example.com/article
https://external-site.com/resource
```

### Customization
- **Maximum browser tabs**:
  ```python
  MAX_TABS = 20  # Change this number to adjust maximum tabs
  ```
- **Links output file name**:
  ```python
  LINKS_FILE = "extracted_links.txt"  # Change this if you want a different filename
  ```

### Safety Features
1. **Tab Limit:** Automatically limits opened tabs to prevent browser/computer overload
2. **URL Validation:** Only processes valid HTTP/HTTPS URLs and relative paths
3. **Error Handling:** Gracefully handles network errors, timeouts, and invalid HTML
4. **Duplicate Prevention:** Uses sets to avoid opening duplicate links
5. **Absolute URL Conversion:** Converts relative URLs to absolute URLs

### Error Handling
The script handles the following errors gracefully:
- Invalid or malformed URLs
- Connection errors
- HTTP errors (404, 500, etc.)
- Timeout errors
- Parsing errors
- KeyboardInterrupt (Ctrl+C)

### Common Issues & Solutions
| Issue | Solution |
|-------|----------|
| "ModuleNotFoundError: No module named 'requests'" | Run `pip install requests beautifulsoup4` |
| "Error fetching the page: [SSL: CERTIFICATE_VERIFY_FAILED]" | Update your Python certificates or use a trusted URL |
| Links not opening in browser | Check default browser settings or browser compatibility |
| Script stops after entering URL | URL may be invalid - ensure it starts with `http://` or `https://` |
| Too many tabs opened | Reduce `MAX_TABS` value in the script |

### Code Structure 
```text
open_all_links(url)
├── URL validation
├── Fetch webpage (requests.get)
├── Parse HTML (BeautifulSoup)
├── Extract all <a href> links
├── Validate and convert to absolute URLs
├── Save all links to file
└── User choice: open or just save
    ├── Option 1: open_links_in_browser()
    └── Option 2: Just save confirmation
```

### Important Notes
1. **Browser Behavior:** The script uses webbrowser.open_new_tab() which respects your system's default browser settings
2. **Rate Limiting:** Opening many tabs quickly might be blocked by some websites
3. **Privacy:** The script only reads public webpages and doesn't handle authentication
4. **Legal Use:** Only use on websites you have permission to scrape
5. **Network Dependency:** Requires active internet connection
