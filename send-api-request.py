import requests
import json
import time
from shutil import copyfile

API_KEY='Enter your API key here'
URL='https://vision.googleapis.com/v1/images:annotate?key=' + API_KEY

REQUEST_DIR='target/requests/'
REQUEST_FILE=REQUEST_DIR + 'request.json'

def call_api():
    # Read the request data we generated on previous step
    with open(REQUEST_FILE, 'r') as request_data:
        data = request_data.read()
    # Send the request to the Google Vision API
    response = requests.post(url = URL, data = data, headers = {'Content-Type':'application/json'})
    # Load the JSON response
    json_obj = json.loads(response.text)
    textAnn = json_obj['responses'][0]['textAnnotations']
    # Get only the description from textAnnotations
    words = map(lambda x: x['description'].encode('UTF-8'), textAnn)
    # Write the result in file, separating the words with whitespaces
    timestamp = str(time.time())
    with open('target/results/result.' + timestamp, 'w+') as result:
        for word in words:
            result.write(word + ' ')
    # Copy and mark the request file with the timestamp of the response to keep the relation.
    copyfile(REQUEST_FILE, REQUEST_DIR + 'request.' + timestamp + '.json')


if __name__ == '__main__':
    call_api()
