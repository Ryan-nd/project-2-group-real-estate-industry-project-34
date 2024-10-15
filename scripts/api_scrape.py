import requests
import json

client_id = client_92b8c3462a03b7d8afdc35575cca6769
client_secret = secret_0904e5094cc2d5018412957e84e83b44
scopes = ['api_listings_read']
auth_url = 'https://auth.domain.com.au/v1/connect/token'
url_endpoint = 'https://api.domain.com.au/sandbox/''

agency_id = "11842"

def get_property_info():
    response = requests.post(auth_url, data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials',
        'scope': scopes,
        'Content-Type': 'text/json'
    }
    )
    
    json_response = response.json()
    access_token = json_response['access_token']
    print(access_token)
    auth = {"Authorization": "Bearer " + access_token}
    url = url_endpoint + agency_id
    response = requests.get(url, headers=auth)
    r = response.json()
    print(r)
    
get_property_info()
    
