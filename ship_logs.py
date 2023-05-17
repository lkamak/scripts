#!/Users/lucas.kamakura/opt/anaconda3/bin

import json
import requests
import os
import sys

# Define your Datadog API key here
DD_API_KEY = 'API-KEY-GOES-HERE'

# Define the source of your logs
source = 'test'

# Path to your file
file_path = sys.argv[1]

# Check the file extension
_, file_extension = os.path.splitext(file_path)

# Load your file
if file_extension.lower() == '.json':
    with open(file_path, 'r') as f:
        log_data = json.load(f)
        log_data['ddsource'] = source
elif file_extension.lower() == '.txt':
    with open(file_path, 'r') as f:
        log_data = {
            'message': f.read(),
            'ddsource': source,
        }
else:
    raise ValueError('Unsupported file type. Only .json and .txt files are supported.')

# Define the header for your request
headers = {
    'Content-Type': 'application/json',
    'DD-API-KEY': DD_API_KEY,
}

# Define the endpoint
url = 'https://http-intake.logs.datadoghq.com/v1/input'

# Make the POST request
response = requests.post(url, headers=headers, json=log_data)

# Print the response
print(f'Response HTTP Status Code: {response.status_code}')
print(f'Response HTTP Content: {response.content}')