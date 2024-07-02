import requests

BACKEND_URL = 'http://localhost:5000'

def generate_code(description, language):
    try:
        response = requests.post(f'{BACKEND_URL}/generate-code', json={'description': description, 'language': language})
        response.raise_for_status()
        return response.json().get('code', 'Error generating code')
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return 'Error generating code'

def optimize_code(code, language):
    try:
        response = requests.post(f'{BACKEND_URL}/optimize-code', json={'code': code, 'language': language})
        response.raise_for_status()
        return response.json().get('optimizedCode', 'Error optimizing code')
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return 'Error optimizing code'

def correct_code(code, language):
    try:
        response = requests.post(f'{BACKEND_URL}/correct-code', json={'code': code, 'language': language})
        response.raise_for_status()
        return response.json().get('correctedCode', 'Error correcting code')
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return 'Error correcting code'

def explain_code(code, language):
    try:
        response = requests.post(f'{BACKEND_URL}/explain-code', json={'code': code, 'language': language})
        response.raise_for_status()
        return response.json().get('explanation', 'Error explaining code')
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return 'Error explaining code'
