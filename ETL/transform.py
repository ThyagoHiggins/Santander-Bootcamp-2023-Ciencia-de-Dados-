import openai
import pandas as pd 
import requests
import json 

openai_key= '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'

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




openai.api_key = openai_key

def generate_ai_news (user):

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
          "role": "system",
          "content": "Você é um especialista em markting bancário."
      },
      {
          "role": "user",
          "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"
      }
    ]
  )  
  return completion.choices[0].message.content.strip('\"')

for user in users:
    news = generate_ai_news(user)
    print(news)

    user['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": news
    })
    print(user)


def update_user(user):
  response = requests.put(f"https://sdw-2023-prd.up.railway.app/users/{id}", json=user)
  return True if response.status_code == 200 else False

for user in users:
  success = update_user(user)
  print(f"User {user['name']} updated? {success}!")