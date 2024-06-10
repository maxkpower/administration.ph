import os
import re
import requests

def find_urls_in_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        url_pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        urls = re.findall(url_pattern, data)
        return urls

def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False

def find_and_check_urls_in_project(project_path):
    for root, dirs, files in os.walk(project_path):
        for file in files:
            if file.endswith('.py'):  # or any other file types
                file_path = os.path.join(root, file)
                urls = find_urls_in_file(file_path)
                for url in urls:
                    if not check_url(url):
                        print(f'Invalid URL: {url} in file: {file_path}')

# replace with your project path
project_path = '../'
find_and_check_urls_in_project(project_path)