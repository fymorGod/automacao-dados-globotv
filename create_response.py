import schedule 
import time as tm
import requests
import json

# Função para buscar e criar o response.json
def job():

  # Caminho para o arquivo JSON
  file_name  = "response.json"
  directory_path = "C:\DataSets\Auxiliar SISCOM"
  file_path = f"{directory_path}/{file_name}"

  apí_url = 'http://127.0.0.1:5000/get_data'
  response = requests.post(apí_url)

  if response.status_code == 200:
      data = response.json()
      
      with open(file_path, "w") as json_file:
        json.dump(data, json_file)
      print(f"Dados foram salvos no arquivo '{file_path}'.")
  else:
      print(f"Erro ao consumir a API: {response.status_code}")

schedule.every().day.at("08:00").do(job)

while  True:
    schedule.run_pending()
    tm.sleep(1)