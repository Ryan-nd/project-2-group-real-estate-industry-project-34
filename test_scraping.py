import requests
from bs4 import BeautifulSoup
import os

# URL of the page containing the DataPacks
url = 'https://www.abs.gov.au/census/find-census-data/datapacks/download/2021_GCP_SA2_for_VIC_short-header.zip'

# Send a GET request to fetch the page content
response = requests.get(url)
response.raise_for_status()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the link for the Victoria DataPack
victoria_link = None
for link in soup.find_all('a'):
    if 'Victoria' in link.text:
        victoria_link = link.get('href')
        break

if victoria_link:
    # Create the output directory if it doesn't exist
    output_dir = 'data/raw'
    os.makedirs(output_dir, exist_ok=True)

    # Download the Victoria DataPack
    victoria_response = requests.get(victoria_link)
    victoria_response.raise_for_status()

    # Extract the filename from the link and save it to the output directory
    filename = os.path.join(output_dir, 'Victoria_DataPack')
    with open(filename, 'wb') as f:
        f.write(victoria_response.content)

    print(f'Victoria DataPack downloaded and saved to {filename}')
else:
    print('Victoria DataPack link not found.')