from flask import Flask, render_template, request, redirect, jsonify
import json
import os
import mysql.connector

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

# @app.route('/places')
# def places():
#     try:
#         if os.path.exists('places_data.json') and os.path.getsize('places_data.json') > 0:
#             with open('places_data.json', 'r') as f:
#                 places = json.load(f)
#         else:
#             places = []
#     except json.JSONDecodeError:
#         places = []
#     return render_template('places.html', places=places)  # Ensure 'places.html' exists in the 'templates' folder

@app.route('/stays')
def stays():
    try:
        if os.path.exists('stays_data.json') and os.path.getsize('stays_data.json') > 0:
            with open('stays_data.json', 'r') as f:
                stays = json.load(f)
        else:
            stays = []
    except json.JSONDecodeError:
        stays = []
    return render_template('stays.html', stays=stays)  # Ensure 'stays.html' exists in the 'templates' folder

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",        # Replace with your DB username
        password="Soumya@1234",    # Replace with your DB password
        database="contact_db"     # Replace with your DB name
    )
    cursor = conn.cursor()

    # Insert into table (make sure 'contacts' table exists)
    query = "INSERT INTO contacts (name, email, subject, message) VALUES (%s, %s, %s, %s)"
    values = (name, email, subject, message)
    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return redirect('/contact')




if __name__ == '__main__':
    app.run(host='localhost', port=5000)
    
    
    
    # app.run(host='0.0.0.0', port=10000)
