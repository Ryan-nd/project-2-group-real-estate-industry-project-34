# fetch_agency_data.py
import requests
import time

def fetch_agency_data(agency_id, access_token, params, api_url_base):
    """
    Fetch listings data for a given agency ID.

    Parameters:
        agency_id (str): The agency ID to fetch listings for.
        access_token (str): The access token for authenticating the request.
        params (dict): Dictionary containing request parameters.
        api_url_base (str): Base URL for the API.

    Returns:
        list: List of all listings retrieved for the given agency ID.
    """
    headers = {"Authorization": f"Bearer {access_token}"}
    all_listings = []
    
    # Iterate through pages to fetch listings
    for page_number in range(1, 300):  # Adjust range based on requirements
        params['pageNumber'] = page_number
        url_endpoint = f'{api_url_base}/agencies/{agency_id}/listings'

        response = requests.get(url_endpoint, headers=headers, params=params)
        
        if response.status_code == 200:
            listings = response.json()
            if not listings:  # Stop if no listings are found
                print(f"No more listings found at page {page_number} for agency {agency_id}.")
                break
            all_listings.extend(listings)
            print(f"Fetched {len(listings)} listings from page {page_number} for agency {agency_id}.")
        else:
            print(f"Failed to retrieve data for agency {agency_id} on page {page_number}: {response.status_code} - {response.reason}")
            break  # Stop fetching further pages if there's an error

        # Optional: Sleep between requests to avoid rate limiting
        time.sleep(1)
    
    return all_listings
