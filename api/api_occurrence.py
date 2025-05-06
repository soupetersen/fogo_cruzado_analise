import requests
import os
import json

class OccurrenceAPI:
    def __init__(self, token_file="access_token.txt", verify_ssl=True):
        self.token_file = token_file
        self.verify_ssl = verify_ssl
        self.base_url = "https://api-service.fogocruzado.org.br/api/v2/occurrences"
        self.access_token = self._load_token()

    def _load_token(self):
        try:
            with open(self.token_file, "r") as f:
                return f.read().strip()
        except FileNotFoundError:
            raise Exception("Token file not found.")

    def get_occurrences(self, initial_date, final_date, id_cities, id_state=None, order="ASC", save_json=True):
        headers = {"Authorization": f"Bearer {self.access_token}"}
        params = {
            "initialdate": initial_date,
            "finaldate": final_date,
            "idCities": id_cities,
            "order": order.upper() if order else "ASC"
        }
        # Remove empty or None parameters
        params = {k: v for k, v in params.items() if v}
        if id_state:
            params["idState"] = id_state
        response = requests.get(self.base_url, headers=headers, params=params, verify=self.verify_ssl)
        response.raise_for_status()
        data = response.json()
        if save_json:
            os.makedirs("data", exist_ok=True)
            file_path = os.path.join(
                "data",
                f"occurrences_city_{id_cities}.json"
            )
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        return data

    def get_occurrences_by_state(self, initial_date, final_date, id_state, save_json=True):
        headers = {"Authorization": f"Bearer {self.access_token}"}
        params = {
            "initialdate": initial_date,
            "finaldate": final_date,
            "idState": id_state
        }
        response = requests.get(self.base_url, headers=headers, params=params, verify=self.verify_ssl)
        response.raise_for_status()
        data = response.json()
        if save_json:
            os.makedirs("data", exist_ok=True)
            file_path = os.path.join("data", f"occurrences_state_{id_state}.json")
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        return data
