# Search Engine
## Setup
Ensure you have Python 3.x installed on your system.
Clone this repository:
text
```git clone https://github.com/Suzaalx/search_engine.git```
```cd python-search-project ```

Install the required dependencies:

```pip install -r requirements.txt ```

Running the Project
To run the search functionality:

```python search.py ```

This will prompt you for a search keyword and offer advanced search options.

Running Tests
To run the tests:

```python -m unittest search_test.py ```

## Main Functions
The main search functions in search.py include:

- search(keyword):
Performs a basic search by keyword.
Returns a list of article titles containing the given keyword (case insensitive).
Returns an empty list if the keyword is empty or no results are found.

- title_length(max_length, titles):
Filters articles by title length.
Returns a list of article titles from given titles with a length that does not exceed max_length characters.

- article_count(count, titles):
Limits the number of returned articles.
Returns a list of articles from given titles, starting from the beginning, that do not exceed the given count.

- random_article(index, titles):
Gets a random article by index.
Returns the article title at the given index. If the index is not valid, returns an empty string.

- favorite_article(favorite, titles):
Checks if a favorite article is in the results.
Returns True if the favorite article is in the given articles (case insensitive), False otherwise.

- multiple_keywords(keyword, titles):
Searches with multiple keywords.
Searches for article titles from the entire list of available articles and adds those articles to the list of article titles from the basic search.


## File Descriptions
- search.py:
Contains the main search functions and display logic.
Implements the core search functionality and advanced search options.
- wiki.py:
Provides article data and helper functions for user input.
Contains a list of Wikipedia articles and their metadata.
Implements functions to get article titles and information.
- search_test.py:
Contains unit and integration tests for the search functionality.
Tests each main function in search.py.
- search_tests_helper.py:
Helper functions for testing.
Provides utilities for mocking user input and capturing output during tests.
## Testing
The project includes both unit tests and integration tests:
Unit tests check individual functions for correct behavior.
Integration tests simulate user input and check the overall functionality of the search system.

