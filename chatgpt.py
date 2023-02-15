import requests
from bs4 import BeautifulSoup
import json

# Define the URL of the website to scrape
url = "https://www.stfrancismedicalcenter.com/find-a-provider/"

# Send a GET request to the website
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Find the elements containing provider information
provider_elements = soup.find_all("div", class_="provider-info")

# Extract the provider details
providers = []
for provider_element in provider_elements:
    name = provider_element.find("h3").text.strip()
    specialty = provider_element.find("div", class_="provider-specialty").text.strip()
    location = provider_element.find("div", class_="provider-location").text.strip()
    providers.append({
        "name": name,
        "specialty": specialty,
        "location": location
    })

# Save the provider details in a JSON file
with open("providers.json", "w") as f:
    f.write(json.dumps(providers, indent=4))
