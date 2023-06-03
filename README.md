# POM_testsuite
Multi-platform sample web test suite designed according with page-object model using PyTest and Selenium

# Pytest and Selenium Test Suite

This repository contains a Pytest and Selenium test suite for testing the login form of [https://the-internet.herokuapp.com](https://the-internet.herokuapp.com)

The testing process in this repository is implemented using the Page Object Model (POM) design pattern. 

## Prerequisites

- Python 3
- pip (Python package installer)
- selenium
- pytest
- Web browser (Chrome, Firefox)

## Setup

1. Clone the repository:
```bash
git clone git@github.com:NastassiaRabkina/POM_testsuite.git
```

2. Install the necessary Python packages:
```bash
pip3 install -r requirements.txt
```

## Running the Tests

To execute the test suite, use the following command:
```bash
pytest verify_login_form.py
```
This command will run the Pytest suite to verify the login form.

## Author

- Nastassia Rabkina

---

Happy testing!
