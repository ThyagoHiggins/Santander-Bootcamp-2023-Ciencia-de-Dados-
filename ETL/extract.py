import pandas as pd 
import requests
import json 


#Nesse trecho estamos configurando o leitura de dados no arquivo
df = pd.read_csv('santander.csv')
user_ids = df['UserID'].tolist()

print(user_ids)

#Função para acessar os dados do user no API 

def get_user(id):
    
    response = requests.get(f'https://sdw-2023-prd.up.railway.app/users/{id}')

    return response.json() if response.status_code == 200 else None



users =[ user for id in user_ids if(user := get_user(id))is not None]

print(json.dumps(users, indent=2))

