import requests
from bs4 import BeautifulSoup
import json
url = "https://www.stfrancismedicalcenter.com/find-a-provider/"

# Make a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Find the data you want to scrape
data = soup.find_all("div", class_="data-element")

# Extract the information you want from each data element
for element in data:
    name = element.find("div", class_="name").text
    specialty = element.find("div", class_="specialty").text
    address = element.find("div", class_="address").text
    city = element.find("div", class_="city").text
    state = element.find("div", class_="state").text
    zip_code = element.find("div", class_="zip-code").text
    phone = element.find("div", class_="phone").text

    # Print the extracted information
    print(f"Name: {name}")
    print(f"Specialty: {specialty}")
    print(f"Address: {address}")
    print(f"City: {city}")
    print(f"State: {state}")
    print(f"Zip code: {zip_code}")
    print(f"Phone: {phone}")
    
with open("element.json", "w") as f:
    f.write(json.dumps(element, indent=4))
