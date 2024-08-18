import requests

def read_blood_test_report(file_path_or_url):
    if file_path_or_url.startswith('http://') or file_path_or_url.startswith('https://'):
        response = requests.get(file_path_or_url)
        response.raise_for_status()  
        return response.text
    else:
        with open(file_path_or_url, 'r') as file:
            return file.read()