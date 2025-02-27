import requests

def fetch_match_data(api_url, mp, api_key):
    params = {
        "k": api_key,
        "mp": mp
    }
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        return response.json()  # return the match data if successful
    else:
        print(f"\nError: {response.status_code} trying to check match {mp}")
        print(response.text)
        return None
