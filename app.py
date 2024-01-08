import os
import requests
import time
import os


from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
api_base = 'https://rcgth-hackathon-aoai-eu2.openai.azure.com/'  # Enter your endpoint here
api_key = 'c7a1c79eb07d4ff380f09938640f774c'        # Enter your API key here

api_version = '2023-12-01-preview'

app = Flask(__name__)

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
def image_gen():
    url = f"{api_base}/openai/deployments/<dalle3>/images/generations?api-version={api_version}"
    headers= { "api-key": api_key, "Content-Type": "application/json" }
    body = {
        # Enter your prompt text here
        "prompt": "A multi-colored umbrella on the beach, disposable camera",
        "size": "1024x1024", # supported values are “1792x1024”, “1024x1024” and “1024x1792” 
        "n": 1,
        "quality": "hd", # Options are “hd” and “standard”; defaults to standard 
        "style": "vivid" # Options are “natural” and “vivid”; defaults to “vivid”
    }
    submission = requests.post(url, headers=headers, json=body)
    
    image_url = submission.json()['data'][0]['url']
    
    print(image_url)

if __name__ == '__main__':
   app.run()
