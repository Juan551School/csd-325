# Juan Macias Vasquez
# Date 07/05/2025
# Module 9.2 APIs
# ice_and_fire_api_example.py

import requests

# Ice and Fire API - Get data about Jon Snow (character 583)
url = "https://anapioficeandfire.com/api/characters/583"

# Step 1: Test the connection
response = requests.get(url)
print("Status Code:", response.status_code)

# Step 2: Print raw JSON response
print("\nRaw Response:")
print(response.text)

# Step 3: Print formatted output
if response.status_code == 200:
    data = response.json()
    print("\nFormatted Response:")
    print("Name:", data['name'])
    print("Gender:", data['gender'])
    print("Culture:", data['culture'])
    print("Born:", data['born'])
    print("Died:", data['died'] if data['died'] else "Still alive")
    print("Titles:", ", ".join(data['titles']) if data['titles'] else "No titles")
    print("Aliases:", ", ".join(data['aliases']) if data['aliases'] else "No aliases")

