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
        # Render the blog.html template with the blogs data
    return render_template('blog.html', blogs=blogs)
@app.route('/food')
def food():
    try:
        if os.path.exists('food_data.json') and os.path.getsize('food_data.json') > 0:
            with open('food_data.json', 'r') as f:
                foods = json.load(f)
        else:
            foods = []
    except json.JSONDecodeError:
        foods = []
    return render_template('food.html', foods=foods)  # Ensure 'food.html' exists in the 'templates' folder

if __name__ == '__main__':
    app.run(debug=True)
