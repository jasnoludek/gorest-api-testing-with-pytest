# GoRest API Testing with Pytest

This mini-project performs testing on the GoRest API (http://gorest.co.in/) using pytest. The tests cover functionality related to users, posts, comments, and todos.

## Getting Started

### Prerequisites

- Python 3.11
- Pip (Python package installer)

### Installation

1. **Clone the repository:**

```bash
git clone http://github.com/jasnoludek/gorest-api-testing-with-pytest.git
```

2. **Navigate to the project directory:**

```bash
cd gorest-api-testing-with-pytest
```

3. **Create and activate a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `ven/Scripts/activate`
```

### API Access Token

Before running the tests, you'll need to obtain an access token from the [GoRest API](http://gorest.co.in/). Follow these steps to create and store your access token in your project directory.

1. **Get Your [GoRest API Access Token](https://gorest.co.in/my-account/access-tokens)**


2. **Create `auth.ini` File:**

  - In the project's root directory, create a file named `auth.ini`.


  - Open `auth.ini` in a text editor and paste the following, replacing `youraccesstokenhere` with your actual access token:

```bash
[API]
ACCESS_TOKEN = youraccesstokenhere
```

3. **Add `auth.ini` to `.gitignore`:**
- To prevent your access token from being exposed in version control, add `auth.ini` to your project's `.gitignore` file. If you don't have one, create a new file named `.gitignore` in the project's root directory and add the following line:
```bash
auth.ini
```
## Running Tests

To run the tests, execute the following command:

```bash
pytest -v
```

### Test Structure

- `tests/test_comments_api.py`: Tests related to comments functionality.


- `tests/test_posts_api.py`: Tests related to posts functionality.


- `tests/test_todos_api.py`: Tests related to to-dos functionality.


- `tests/test_user_api.py`: Tests related to user functionality.

## HTML Test Report

After running the tests, an HTML report is generated. To view the detailed test results, open the `report.html` file in your web browser using the following command:

```bash
open report.html # on MacOS
```

Replace `open` with your system's command for opening files in a browser (e.g., `start` on Windows or `xdg-open` on Linux).

This command will launch the default web browser and display the HTML test report, allowing you to analyze the outcomes of the test suite.

## Contributing

Feel free to contribute by opening issues or pull requests. Your contributions are greatly appreciated!

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.