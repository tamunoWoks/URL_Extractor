## Web Link Extractor & Browser Opener 

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
