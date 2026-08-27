# Saucedemo Automation Project

A Selenium + Python + pytest test suite for saucedemo.com, built using the Page Object Model.

## Structure
- `pages/` — page object classes (LoginPage, ProductsPage)
- `tests/` — test files, organized by feature
- `conftest.py` — shared pytest fixtures (browser setup/teardown)

## Running the tests
pip install -r requirements.txt
python -m pytest -v

## Status
Work in progress — built as part of a 5-week Selenium learning project.
