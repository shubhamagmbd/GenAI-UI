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

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')
   client = AzureOpenAI(
      api_version="2023-12-01-preview",  
      api_key='c7a1c79eb07d4ff380f09938640f774c',  
      azure_endpoint='https://rcgth-hackathon-aoai-eu2.openai.azure.com/'
   )

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
