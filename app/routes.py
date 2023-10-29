from flask import render_template, request, redirect, url_for
from app import app

# Import the OpenAI library here
import openai

# Load the OpenAI API key from the .env file
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a software engineering expert and excellent at explaining complex programming concepts in simple terms."},
                {"role": "user", "content": user_input}
            ]
        )
        
        # Process the API response and store the result
        result = completion.choices[0].message
        
        return render_template('result.html', result=result)
    
    return render_template('index.html')