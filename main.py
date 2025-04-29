from flask import Flask, request, redirect, jsonify
import json
import os
import random

app = Flask(__name__)
url_file = 'urls.json'
short_code_length = 16
def load_urls():
    if os.path.exists(url_file):
        with open(url_file, 'r') as file:
            return json.load(file)
    return {}

def save_urls(urls):
    with open(url_file, 'w') as file:
        json.dump(urls, file, indent=2)


def generate_short_code(url):

    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    short_code = ''.join(random.choice(chars) for _ in range(short_code_length))
    return short_code

@app.route('/new', methods=['POST'])
def create_short_url():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'error': 'URL is required'}), 400

    urls = load_urls()
    code = generate_short_code(url)
    

    if code in urls:
        return jsonify({'shortUrl': f'http://localhost:5000/{code}'}), 200


    urls[code] = url
    save_urls(urls)

    return jsonify({'shortUrl': f'http://localhost:5000/{code}'}), 201

@app.route('/<code>', methods=['GET'])
def redirect_to_url(code):
    urls = load_urls()

    if code in urls:
        return redirect(urls[code], 302)
    
    return jsonify({'error': 'Link not found'}), 404

@app.route('/list', methods=['GET'])

def list_url():
    data = load_urls()
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)

