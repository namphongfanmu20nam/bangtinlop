from flask import Flask, render_template, jsonify, request
import json
import os

app = Flask(__name__)

# Data file for board posts
DATA_FILE = 'board_posts.json'

def load_posts():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_posts(posts):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/board', methods=['GET'])
def get_board():
    return jsonify(load_posts())

@app.route('/api/board', methods=['POST'])
def add_post():
    new_post = request.json
    posts = load_posts()
    posts.insert(0, new_post)
    save_posts(posts[:300]) # Keep last 300
    return jsonify({"status": "success"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
