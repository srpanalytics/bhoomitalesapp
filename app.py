from flask import Flask, render_template, request, redirect, jsonify
import json
import os

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')  # This loads your homepage

@app.route('/blog')
def blog():
    try:
        if os.path.exists('blog_data.json') and os.path.getsize('blog_data.json') > 0:
            with open('blog_data.json', 'r') as f:
                blogs = json.load(f)
        else:
            blogs = []
    except json.JSONDecodeError:
        blogs = []

    return render_template('blog.html', blogs=blogs)

if __name__ == '__main__':
    app.run(debug=True)
