import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return self.session.get(url, timeout=10)

    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return self.session.post(url, json=data, timeout=10)

    def put(self, endpoint, data):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return self.session.put(url, json=data, timeout=10)

    def delete(self, endpoint):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return self.session.delete(url, timeout=10)
