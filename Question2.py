import requests
import time
import json

def get_weather(url, headers=None, params=None, retries=3, backoff_factor=1.5, timeout=10):
    for attempt in range(1, retries + 1):
        try:
            print(f"Attempt {attempt} to fetch {url}")
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            if attempt == retries:
                raise
            sleep_time = backoff_factor ** attempt
            print(f"Retries in {sleep_time}")
            time.sleep(sleep_time)

def save_response(data, file_path):

    with open(file_path, 'w') as f:
        json.dump(data, f, index=4)
    print(f"Responsesaved to {file_path}")

if __name__ == "__main__":
    API_URL = "http://localhost:8000/weather_list/"

    try:
        response_data = get_weather(API_URL)
        save_response(response_data, "api_response.json")
    except Exception as e:
        print(f"Failed to fetch and save data: {e}")
    

    