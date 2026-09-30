# OpenLibrary Books Data Collector

A Python project that collects book information from the public Open Library API, filters books published after 2000, and saves the results into a CSV file.

## Features

* Fetches book information from Open Library API
* Collects 50 books
* Filters books published after 2000
* Saves the results in CSV format
* Uses Python and the `requests` library
* Handles API response errors
* Creates the output directory automatically

## Project Structure

```text
openlibrary_books/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── output/
    └── books.csv
```

## Requirements

* Python 3.9 or newer
* Internet connection
* `requests`

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/openlibrary-books.git
cd openlibrary-books
```

Install the required package:

```bash
pip install -r requirements.txt
```

## Usage

Run the Python script:

```bash
python main.py
```

The program will collect 50 books published after 2000 and save them to:

```text
output/books.csv
```

## CSV Columns

The generated CSV file contains:

| Column            | Description                  |
| ----------------- | ---------------------------- |
| `title`           | Book title                   |
| `author`          | Author name                  |
| `publish_year`    | First publication year       |
| `openlibrary_key` | Open Library work identifier |

## API

This project uses the Open Library Search API:

https://openlibrary.org/search.json

## Filtering

Only books with a `first_publish_year` greater than 2000 are included.

For example:

* 2000 → Not included
* 2001 → Included
* 2010 → Included
* 2025 → Included

## Output

The final result is saved as:

```text
output/books.csv
```

The CSV contains exactly 50 books that satisfy the filtering condition.

## License

This project was created for educational purposes.
