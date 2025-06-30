import requests
import json

url = 'https://api.the-odds-api.com/v4/sports?apiKey=92a0209828337b02e378101efc68d6f9' 
response = requests.get(url)
print (response)
