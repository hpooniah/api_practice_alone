"""
Requests module provides access to websites or API's so that you can get data
"""
import requests

breed_name = input("What dog breed? ").strip().lower()

# Generate the URL needed for the API call
URL = f"https://dog.ceo/api/breed/{breed_name}/images/random"

# Use request module to make an API call and get the data 
# Note: data will come back as a JSON object
json_data = requests.get(URL, timeout=10).json()

# Get the dog image URL
dog_image = json_data["message"]

print(dog_image)









