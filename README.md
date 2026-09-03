# Saucedemo Automation Project

A Selenium + Python test automation suite for saucedemo.com, built using the Page Object Model, alongside a separate API testing module demonstrating requests + pytest fundamentals.

## What this project tests

- Login flows: valid login, invalid credentials, and edge cases (empty fields), including a parametrized test covering multiple scenarios with distinct expected error messages
- Inventory page: product sorting (price low-to-high, high-to-low), adding items to the cart, and verifying the cart badge updates correctly
- API fundamentals (separate module): GET/POST requests, status code verification, and response body assertions

## Scope and limitations

saucedemo.com is a UI-only demo application with no real backend API. The API tests in tests/test_api.py run against reqres.in, a public test API, purely to demonstrate requests + pytest skills - they are NOT testing saucedemo itself. This is documented directly in that file's docstring.

## Project structure

    saucedemo-automation/
    |-- conftest.py              (Shared pytest fixtures)
    |-- pages/                   (Page Object Model classes)
    |   |-- login_page.py
    |   `-- products_page.py
    |-- tests/                   (Test files, organized by feature)
    |   |-- test_login.py
    |   |-- test_inventory.py
    |   `-- test_api.py
    |-- requirements.txt
    `-- README.md

## Running the tests

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python -m pytest -v

## Status

Built as a 5-week self-directed learning project (Aug-Sep 2026), covering locator strategies, explicit waits, assertions, pytest fixtures/parametrization, and Page Object Model design. Work in progress - actively maintained.

## What I'd add next

- CI/CD integration (e.g., GitHub Actions) to run the suite automatically on each push
- Test reporting with pytest-html for a readable pass/fail summary

These were deliberately scoped out of this project to stay focused on core Selenium, pytest, and Page Object Model fundamentals within the timeline.
