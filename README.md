# URL Shortener

A simple short URL generator written in Python using Flask.

## Features
- Generate short URLs from long URLs.
- Simple to use with no external dependencies.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/slyhax/shortURL.git
   ```

2. Install the dependencies:
   ```bash
   pip install Flask
   ```

## Usage
Run the main script to start the server.
```bash
py main.py
```
or
```bash
python main.py
```

## Routes

- `GET /<code>`: Redirects to the long URL associated with the provided short code.
  - Example: `GET /abc123`
  - Response: Redirects to the long URL associated with the short code.

- `GET /list`: Returns all shortened links.
  - Example: `GET /list`
  - Response: All the shortened URLs.

- `POST /new`: Receives a long URL and returns a shortened URL.
  - Request body (JSON):
    ```json
    {
      "url": "https://www.example.com"
    }
    ```
  - Response (JSON):
    ```json
    {
      "shortUrl": "http://localhost:5000/abc123"
    }
    ```
