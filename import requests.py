import requests
from bs4 import BeautifulSoup
import json

# Define the base URL of the website to scrape
base_url = "https://www.stfrancismedicalcenter.com/find-a-provider/"

# Initialize variables to keep track of the page number and provider details
page_num = 1
providers = []

# Loop through all pages until no more pages are found
while True:
    # Construct the URL for the current page
    url = f"{base_url}page/{page_num}/"

    # Send a GET request to the website
    response = requests.get(url)

    # Use BeautifulSoup to parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the elements containing provider information
    provider_elements = soup.find_all("div", class_="provider-info")

    # Extract the provider details
    for provider_element in provider_elements:
        name = provider_element.find("h3").text.strip()
        specialty = provider_element.find("div", class_="provider-specialty").text.strip()
        location = provider_element.find("div", class_="provider-location").text.strip()
        providers.append({
            "name": name,
            "specialty": specialty,
            "location": location
        })

    # Increment the page number
    page_num += 1

    # Check if there are more pages
    if not provider_elements:
        break

# Save the provider details in a JSON file
with open("providers.json", "w") as f:
    f.write(json.dumps(providers, indent=4))
