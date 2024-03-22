import schedule 
import time as tm
import requests
import json

d = None
# Função para buscar e criar o response.json
def job():
  global d
  # Caminho para o arquivo JSON
  file_name  = "response.json"
  directory_path = "E:\Bonn\Fontes de Dados\SISCOM"
  file_path = f"{directory_path}/{file_name}"
      
  apí_url = 'http://127.0.0.1:5004/get_data'
  response = requests.post(apí_url)

  if response.status_code == 200:
      data = response.json()
      if "error" in data:
          job()
      with open(file_path, "w") as json_file:
        json.dump(data, json_file)
      print(f"Dados foram salvos no arquivo '{file_path}'.")
  else:
      print(f"Erro ao consumir a API: {response.status_code}")

      if "error" in d:
        job()   
schedule.every().day.at("07:10").do(job)
schedule.every().day.at("09:16").do(job)
schedule.every().day.at("11:00").do(job)
schedule.every().day.at("12:00").do(job)
schedule.every().day.at("17:14").do(job)
while  True:
    schedule.run_pending()
    tm.sleep(1)
