import requests
import os
from dotenv import load_dotenv


load_dotenv()
# GET
request = requests.get(os.getenv('FIREBASE'))  # This .json at the end of URL is a requirement of Firebase. Not needed in other databases.
print(request)
print(request.json())

# POST
information = '{"Age":"58", "Last_Name":"Stone", "Name":"Peter"}'
request = requests.post(os.getenv('FIREBASE'), data = information)
print(request)
print(request.json())

# PATCH
information = '{"Age":"40"}'
request = requests.patch(os.getenv('FIREBASE_2ND_DATA'), data = information)
print(request)
print(request.json())

# DELETE
request = requests.delete(os.getenv('FIREBASE_DELETE'), data = information)
print(request)
print(request.json())