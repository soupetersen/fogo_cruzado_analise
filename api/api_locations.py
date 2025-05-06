import requests
import os
import json

class LocationAPI:
    def __init__(self, token_file="access_token.txt", verify_ssl=True):
        self.token_file = token_file
        self.verify_ssl = verify_ssl
        self.access_token = self._load_token()

    def _load_token(self):
        try:
            with open(self.token_file, "r") as f:
                return f.read().strip()
        except FileNotFoundError:
            raise Exception("Token file not found.")

    def get_city_data(self, city_name, save_json=True):
        url = "https://api-service.fogocruzado.org.br/api/v2/cities"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        params = {"cityName": city_name}
        response = requests.get(url, headers=headers, params=params, verify=self.verify_ssl)
        response.raise_for_status()
        data = response.json()
        if save_json:
            os.makedirs("data", exist_ok=True)
            file_path = os.path.join("data", f"{city_name.lower()}.json")
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        return data

    def get_all_states(self, save_json=True):
        url = "https://api-service.fogocruzado.org.br/api/v2/states"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.get(url, headers=headers, verify=self.verify_ssl)
        response.raise_for_status()
        data = response.json()
        if save_json:
            os.makedirs("data", exist_ok=True)
            file_path = os.path.join("data", "states.json")
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        return data
