

```plaintext

## Setup

1. Ensure you have Python 3.x installed on your system.
2. Clone this repository:
```plaintext

git clone [https://github.com/Suzaalx/search_engine.git](https://github.com/Suzaalx/search_engine.git)
cd python-search-project

```
3. Install the required dependencies:
```

pip install -r requirements.txt

```plaintext

## Running the Project

To run the search functionality:

```

python search.py

```plaintext

This will prompt you for a search keyword and offer advanced search options.

## Running Tests

To run the tests:

```

python -m unittest search_test.py

```plaintext

## Main Functions

The main search functions in `search.py` include:

1. `search(keyword)`: 
   - Performs a basic search by keyword.
   - Returns a list of article titles containing the given keyword (case insensitive).
   - Returns an empty list if the keyword is empty or no results are found.

2. `title_length(max_length, titles)`:
   - Filters articles by title length.
   - Returns a list of article titles from given titles with a length that does not exceed `max_length` characters.

3. `article_count(count, titles)`:
   - Limits the number of returned articles.
   - Returns a list of articles from given titles, starting from the beginning, that do not exceed the given count.

4. `random_article(index, titles)`:
   - Gets a random article by index.
   - Returns the article title at the given index. If the index is not valid, returns an empty string.

5. `favorite_article(favorite, titles)`:
   - Checks if a favorite article is in the results.
   - Returns True if the favorite article is in the given articles (case insensitive), False otherwise.

6. `multiple_keywords(keyword, titles)`:
   - Searches with multiple keywords.
   - Searches for article titles from the entire list of available articles and adds those articles to the list of article titles from the basic search.

## Advanced Search Options

1. Filter by article title length
2. Limit number of returned articles
3. Get a random article
4. Check for a favorite article
5. Search with multiple keywords

## File Descriptions

1. `search.py`:
   - Contains the main search functions and display logic.
   - Implements the core search functionality and advanced search options.

2. `wiki.py`:
   - Provides article data and helper functions for user input.
   - Contains a list of Wikipedia articles and their metadata.
   - Implements functions to get article titles and information.

3. `search_test.py`:
   - Contains unit and integration tests for the search functionality.
   - Tests each main function in `search.py`.

4. `search_tests_helper.py`:
   - Helper functions for testing.
   - Provides utilities for mocking user input and capturing output during tests.

## Testing

The project includes both unit tests and integration tests:

- Unit tests check individual functions for correct behavior.
- Integration tests simulate user input and check the overall functionality of the search system.

