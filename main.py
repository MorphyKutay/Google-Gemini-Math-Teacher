from flask import Flask,render_template,request, jsonify,redirect

import pathlib
import textwrap
from PIL import Image
import io
import requests

import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown



GOOGLE_API_KEY= 'AIzaSyBPCqxr1MmUUyFzRR2zPaC2uM-Ku0tvohM'

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-pro')

"""response = model.generate_content("What is the meaning of life?")
cikti = to_markdown(response.text)"""


app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')



@app.route("/send_message", methods=['POST'])
def send_message():
        message = request.form['message']
        
        response =  model.generate_content(message)
        geminitext = response.text
        print(response.text)



        return jsonify({'gemini_response': geminitext})

@app.route("/send_photo",methods=['POST'])
def send_photo():
    photo = request.files['photo']
    if photo:
       
        img = Image.open(io.BytesIO(photo.read()))

        
        processed_text = img
        response = model.generate_content(processed_text)
        gemini_response = response.text

        return jsonify({'gemini_response': gemini_response})

    return jsonify({'error': 'No photo uploaded'})


if __name__ == '__main__':
    app.run(debug=True)