# Juan Macias Vasquez
# Date 07/05/2025
# Module 9.2 APIs
# api_test_connection.py

import requests

response = requests.get('http://www.google.com')
print("Status Code:", response.status_code)

