import requests
import json  

def get_auth_token():
    url = "https://reqres.in/api/login"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        token = response.json().get("token")
        
        # Simpan token ke dalam file JSON
        with open("token.json", "w") as file:
            json.dump({"token": token}, file, indent=4)
        
        return token
    else:
        raise Exception("Failed to get token")
    
try:
    token = get_auth_token()
    print("Token successfully retrieved:", token)
except Exception as e:
    print(e)
