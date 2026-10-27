
import requests
from bs4 import BeautifulSoup


def get_page_title(url):
    try:
        # Fetch the webpage
        response = requests.get(url, timeout=10)

        # Raise an error if the server returns an HTTP error
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract the webpage title
        title_tag = soup.find("title")
        if title_tag:
            title = title_tag.get_text(strip=True)
        else:
            title = "No title found"

        print(f"\nWebpage title: {title}")

        # Extract and display all hyperlinks
        print("\nHyperlinks found:")

        links = soup.find_all("a", href=True)

        if links:
            for link in links:
                link_text = link.get_text(strip=True)
                link_url = link["href"]

                print(f"- {link_text or '[No link text]'}: {link_url}")
        else:
            print("No hyperlinks found.")

    except requests.exceptions.Timeout:
        print("Error: The request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the website.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Network error: {error}")


# Get the URL from the user
url = input("Enter a webpage URL: ").strip()

# Add https:// if the user leaves out the scheme
if url and not url.startswith(("http://", "https://")):
    url = "https://" + url

if url:
    get_page_title(url)
else:
    print("Error: URL cannot be empty.")
