# Juan Macias Vasquez
# Date 07/05/2025
# Module 9.2 APIs
# current_astronauts.py

import requests

# API endpoint for current astronauts
url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)

# Test connection
print("Status Code:", response.status_code)

# Raw output
print("Raw Response:", response.text)

# Pretty formatted output
if response.status_code == 200:  # to know its connecting right 
    data = response.json()
    print("\nThere are", data['number'], "people in space:\n")
    for person in data['people']:
        print(person['name'], "on", person['craft'])