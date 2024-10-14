# auth.py
import requests

def get_access_token(client_id, client_secret, scopes, auth_url):
    """
    Retrieve the access token for a given API client.
    
    Parameters:
        client_id (str): The client ID provided by the API.
        client_secret (str): The client secret provided by the API.
        scopes (list): List of scopes for accessing specific API endpoints.
        auth_url (str): The authentication URL for the API.
    
    Returns:
        str: The access token for the client.
    """
    response = requests.post(auth_url, data={
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials',
        'scope': ' '.join(scopes),
        'Content-Type': 'application/x-www-form-urlencoded'
    })
    
    if response.status_code == 200:
        json_response = response.json()
        return json_response.get('access_token')
    else:
        raise Exception(f"Failed to retrieve access token: {response.status_code} - {response.text}")
