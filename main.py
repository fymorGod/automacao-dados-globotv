from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

url = 'https://accounts.mybackstage.globo.com/token'
api_url = 'https://api-afiliadas.mybackstage.globo.com/afiliadas/relatorio/spotnet/exibidora?pagesize=400&pagenumber=1&dataCompetenciaInicio=2023/06/01&dataCompetenciaFim=2023/06/30'
client_id = '7iBj3LfAGq12FCh5bcEySw=='
client_secret = 'OoWu14zKE53WOXcYiCopcA=='

user_credentials = {
    "grant_type": "grant_type",
    "value": "client_credentials"
}

@app.route('/get_data', methods=['POST'])
def get_data():
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    token_response = requests.post(url, data=payload)
    token_data = token_response.json()
    if 'access_token' in token_data:
        access_token = token_data['access_token']

        headers = {
             'Authorization': f'Bearer {access_token}'
        }
        
        payload = {
            'grant_type': 'client_credentials',
        }

        api_response = requests.get(api_url, headers=headers, data=payload)
        api_data = api_response.json()
        print(api_data)
        return jsonify(api_data)
    else:
        return jsonify({'error': 'Unable to get access token'})
    
if __name__ == '__main__':
    app.run(debug=True)
