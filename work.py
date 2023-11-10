import requests
from bs4 import BeautifulSoup

def download_book(book_title):
    url = f"https://www.pdfdrive.com/search?q={book_title}&searchin=&page=1"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        soup = BeautifulSoup(response.content, "html.parser")
        book_link = soup.find("a", {"class": "ai-search"}).get("href")

        if book_link:
            book_title = book_title.replace(" ", "_")
            pdf_url = f"https://www.pdfdrive.com{book_link}"
            response = requests.get(pdf_url)
            
            with open(f"{book_title}.pdf", "wb") as f:
                f.write(response.content)
            print(f"Book downloaded as {book_title}.pdf")
        else:
            print("Book not found.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    book_title = input("Enter the title of the book: ")
    download_book(book_title)
