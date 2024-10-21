python-search-project/
│
├── search.py
├── wiki.py
├── search_test.py
├── search_tests_helper.py
├── README.md
└── requirements.txt

```plaintext

## Setup

1. Ensure you have Python 3.x installed on your system.
2. Clone this repository:
```

git clone [https://github.com/yourusername/python-search-project.git](https://github.com/yourusername/python-search-project.git)
cd python-search-project

```plaintext
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

To add new tests:
1. Open `search_test.py`
2. Add new test methods to the `TestSearch` class
3. Use assertions to check expected outcomes

## Contributing

Contributions to this project are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit them (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

Please ensure that your code passes all tests and follows the existing coding style.
```

This more detailed README.md provides a comprehensive overview of the project, including:

1. A table of contents for easy navigation
2. A visual representation of the project structure
3. More detailed setup instructions
4. Expanded descriptions of each main function
5. A dedicated section describing each file in the project
6. More information about the testing process and how to contribute new tests
7. A more detailed contribution guide


This README should give users and potential contributors a thorough understanding of the project, its structure, and how to use and extend it.