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

2. Instale as dependências:
   ```bash
   pip install Flask
   ```

## Usage
Execute o script principal para iniciar o servidor.
```bash
py main.py
```
or
```bash
python main.py
```

## Routes

- `GET /<code>`: Redireciona para a URL longa associada ao código curto fornecido.
  - Exemplo de uso: `GET /abc123`
  - Resposta: Redireciona para a URL longa associada ao código curto.

- `GET /list`: Retorna todos os links encurtados.
  - Exemplo de uso: `GET /list`
  - Resposta: Todas as urls encurtadas.

- `POST /new`: Recebe uma URL longa e retorna uma URL curta.
  - Corpo da requisição (JSON):
    ```json
    {
      "url": "https://www.exemplo.com"
    }
    ```
  - Resposta (JSON):
    ```json
    {
      "shortUrl": "http://localhost:5000/abc123"
    }
    ```
