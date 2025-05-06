import requests

class AuthAPI:
    def __init__(self, url, verify_ssl=True):
        self.url = url
        self.access_token = None
        self.expires_in = None
        self.verify_ssl = verify_ssl

    def login(self, email, password):
        payload = {"email": email, "password": password}
        response = requests.post(self.url, json=payload, verify=self.verify_ssl)
        response.raise_for_status()
        data = response.json()
        if data.get("code") == 201 and "data" in data:
            self.access_token = data["data"].get("accessToken")
            self.expires_in = data["data"].get("expiresIn")
        return data

    def refresh(self, refresh_url, token=None):
        access_token = token or self.access_token
        if not access_token:
            raise ValueError("Access token não informado.")
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.post(refresh_url, headers=headers, verify=self.verify_ssl)
        response.raise_for_status()
        data = response.json()
        if data.get("code") == 201 and "data" in data:
            self.access_token = data["data"].get("accessToken")
            self.expires_in = data["data"].get("expiresIn")
        return data
