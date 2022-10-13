import requests

class PostToAPI:
    def __init__(self, end_point, data) -> None:
        self.url = end_point
        self.data = data

    def api_post(self):
        results = requests.post(self.url, self.data)
        print(results.status_code)
        print('posted', self.data)
        