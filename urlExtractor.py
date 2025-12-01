import requests
from bs4 import BeautifulSoup
import webbrowser
from urllib.parse import urljoin, urlparse
import os

MAX_TABS = 20  # Maximum number of tabs to open
LINKS_FILE = "extracted_links.txt"  # File to save links

def is_valid_link(href):
    """Check if a link is a valid HTTP/HTTPS URL or relative path."""
    if not href:
        return False
    href = href.strip()
    return href.startswith("http://") or href.startswith("https://") or href.startswith("/")

def save_links_to_file(links, filename):
    """Save all links to a text file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for link in links:
                f.write(link + "\n")
        print(f"\nAll links saved to '{os.path.abspath(filename)}'")
    except Exception as err:
        print(f"Error saving links to file: {err}")

def open_links_in_browser(links):
    """Open links in the browser with a progress counter."""
    if len(links) > MAX_TABS:
        print(f"Found {len(links)} links, opening only the first {MAX_TABS} to prevent overload.")
        links = links[:MAX_TABS]

    print(f"\nOpening {len(links)} links in browser...\n")
    for i, link in enumerate(links, start=1):
        try:
            webbrowser.open_new_tab(link)
            print(f"[{i}/{len(links)}] Opened: {link}")
        except Exception as err:
            print(f"[{i}/{len(links)}] Could not open: {link} ({err})")
    print("\nDone! All accessible links were opened.")

def open_all_links(url):
    # Validate URL format
    if not urlparse(url).scheme:
        print("Error: URL must start with http:// or https://")
        return

    print(f"Fetching page: {url}")

    # Fetch the page
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(f"Error fetching the page: {err}")
        return

    # Parse HTML
    try:
        soup = BeautifulSoup(response.text, "html.parser")
    except Exception as err:
        print(f"Error parsing HTML: {err}")
        return

    # Extract links
    links = set()
    for tag in soup.find_all("a", href=True):
        href = tag["href"]
        if is_valid_link(href):
            absolute_url = urljoin(url, href)
            links.add(absolute_url)

    if not links:
        print("No valid links found on this page.")
        return

    # Convert to list and save all links
    links = list(links)
    save_links_to_file(links, LINKS_FILE)

    # Ask user what to do
    print("\nDo you want to open the links in your browser or only save them?")
    print("1. Open links in browser")
    print("2. Only save to file")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        open_links_in_browser(links)
    elif choice == "2":
        print("Links have been saved. No tabs opened.")
    else:
        print("Invalid choice. Links have been saved but not opened.")

if __name__ == "__main__":
    try:
        target_url = input("Enter a URL: ").strip()
        open_all_links(target_url)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as err:
        print(f"Unexpected error: {err}") 
