# ⚡ URL Shortener

A simple and fast URL shortener built with Python and Flask.

## 📌 Features
- 🔗 Generate short URLs from long URLs.
- 📑 List all created short links.
- 📥 Log every access with IP, User-Agent, query string and timestamp.
- ⚙️ No external dependencies besides Flask.

## 🚀 Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/emptyhax/short-url-logger
   cd short-url-logger
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Usage

Run the server with:
```bash
python main.py
```
or
```bash
py main.py
```

The server will run at:  
[http://localhost:5000](http://localhost:5000)

## 📡 API Routes

### 🔹 `POST /new`
Create a new short URL.

- **Request (JSON)**
  ```json
  {
    "url": "https://www.example.com"
  }
  ```

- **Response (JSON)**
  ```json
  {
    "shortUrl": "http://localhost:5000/abc123"
  }
  ```

---

### 🔹 `GET /<code>`
Redirects to the original long URL for the given short code.

- **Example:** `GET /abc123`
- **Response:** HTTP 302 redirect to the target URL.

---

### 🔹 `GET /links`
Returns all existing short codes with their original URLs.

- **Example:** `GET /links`
- **Response (JSON):**
  ```json
  {
    "abc123": "https://example.com",
    "xyz789": "https://another.com"
  }
  ```

---

### 🔹 `GET /logs`
Returns all access logs for the short URLs.

- **Example:** `GET /logs`
- **Response (JSON):**
  ```json
  [
    {
      "code": "abc123",
      "ip": "192.168.1.1",
      "user_agent": "Mozilla/5.0",
      "path": "/abc123",
      "query": "",
      "timestamp": "2024-06-06T18:50:30.123456"
    }
  ]
  ```

---

## 📄 Files

- `urls.json` → stores the short URL mappings.
- `access_logs.json` → logs all access details.

## 🖤 Author

Made by **Hax** — [github.com/emptyhax](https://github.com/emptyhax)
