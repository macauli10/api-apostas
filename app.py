import os
import requests
import pandas as pd
import psycopg2
from dotenv import load_dotenv


load_dotenv()


conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS odds (
        key TEXT,
        group_name TEXT,
        active BOOLEAN,
        has_outrights BOOLEAN
    )
''')


url = f"https://api.the-odds-api.com/v4/sports?apiKey={os.getenv('API_KEY')}"
response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    df = pd.DataFrame(dados)

    for _, row in df.iterrows():
        cursor.execute('''
            INSERT INTO odds (key, group_name, active, has_outrights)
            VALUES (%s, %s, %s, %s)
        ''', (
            row['key'],
            row['group'],
            row['active'],
            row['has_outrights']
        ))

    conn.commit()
    print("✅ Dados inseridos com sucesso no PostgreSQL da Render!")
else:
    print("❌ Erro ao acessar API:", response.status_code)

cursor.close()
conn.close()
