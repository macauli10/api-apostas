import requests
import json
import pandas as pd
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("API_KEY")
url = f'https://api.the-odds-api.com/v4/sports?apiKey={api_key}'


response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    df = pd.DataFrame(dados)
    print(df.head())
else:
    print("Erro ao acessar API:", response.status_code)
