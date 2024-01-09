import os
from openai import AzureOpenAI
import requests
from PIL import Image
import json

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
app = Flask(__name__)

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route()
def gen_img():
  client = AzureOpenAI(
      api_version="2023-12-01-preview",  
      api_key='c7a1c79eb07d4ff380f09938640f774c',  
      azure_endpoint='https://rcgth-hackathon-aoai-eu2.openai.azure.com/'
  )
  result = client.images.generate(
      model="dalle3", # the name of your DALL-E 3 deployment
      prompt="a close-up of a bear walking throughthe forest",
      n=1
  )
  json_response = json.loads(result.model_dump_json())

  # Set the directory for the stored image
  image_dir = os.path.join(os.curdir, 'images')
  
  # If the directory doesn't exist, create it
  if not os.path.isdir(image_dir):
      os.mkdir(image_dir)
  
  # Initialize the image path (note the filetype should be png)
  image_path = os.path.join(image_dir, 'generated_image.png')
  
  # Retrieve the generated image
  image_url = json_response["data"][0]["url"]  # extract image URL from response
  generated_image = requests.get(image_url).content  # download the image
  with open(image_path, "wb") as image_file:
      image_file.write(generated_image)
  
  # Display the image in the default image viewer
  image = Image.open(image_path)
  image.show()

"""
@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))
"""

if __name__ == '__main__':
   app.run()
