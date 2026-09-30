import csv
import os
import requests

API_URL = "https://openlibrary.org/search.json"
BOOK_COUNT = 50
MIN_YEAR = 2000
OUTPUT_FILE = "output/books.csv"

def fetch_books():
    """Fetch at least 50 books published after 2000."""
    books = []
    page = 1
    limit = 100

    while len(books) < BOOK_COUNT:
        params = {
            "q": f"first_publish_year:[{MIN_YEAR + 1} TO *]",
            "page": page,
            "limit": limit,
            "fields": "key,title,author_name,first_publish_year",
        }

        response = requests.get(
            API_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()
        page_books = data.get("docs", [])

        if not page_books:
            break

        for book in page_books:
            publish_year = book.get("first_publish_year")

            if publish_year and publish_year > MIN_YEAR:
                books.append(book)

            if len(books) == BOOK_COUNT:
                break

        page += 1

    return books


def save_to_csv(books):
    """Save books to a CSV file."""

    os.makedirs(
        os.path.dirname(OUTPUT_FILE),
        exist_ok=True
    )

    fieldnames = [
        "title",
        "author",
        "publish_year",
        "openlibrary_key",
    ]

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for book in books:
            writer.writerow({
                "title": book.get(
                    "title",
                    "Unknown"
                ),
                "author": ", ".join(
                    book.get(
                        "author_name",
                        []
                    )
                ),
                "publish_year": book.get(
                    "first_publish_year"
                ),
                "openlibrary_key": book.get(
                    "key",
                    ""
                ),
            })


def main():
    """Run the complete data collection process."""

    print("Fetching books from Open Library...")

    books = fetch_books()

    print(
        f"Collected {len(books)} books "
        f"published after {MIN_YEAR}."
    )

    if len(books) < BOOK_COUNT:
        raise RuntimeError(
            f"Only {len(books)} valid books were found."
        )

    save_to_csv(books)

    print(
        f"Successfully saved {len(books)} books "
        f"to {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()
