# Python API Test Automation Framework

## Overview
A Python-based API automation framework using Pytest and Requests.

## Tech Stack
- Python
- Pytest
- Requests
- Pytest HTML

## Test Cases
1. Get a single user
2. Get all users
3. Create a post
4. Get a nonexistent post
5. Test an invalid endpoint
6. Create a post with an empty payload

## Project Structure
- api_client.py - Reusable API methods
- tests/test_get.py - GET API tests
- tests/test_post.py - POST API tests
- tests/test_api_negative.py - Negative API tests
- pytest.ini - Pytest configuration
- requirements.txt - Project dependencies

## Run Tests
Install dependencies:

pip install -r requirements.txt

Run all tests:

python -m pytest -v

Generate HTML report:

python -m pytest --html=reports/report.html --self-contained-html

## API
JSONPlaceholder: https://jsonplaceholder.typicode.com

Note: JSONPlaceholder is a demo API. POST responses are simulated and data is not permanently stored.

## Author
Mayank Tarneja
