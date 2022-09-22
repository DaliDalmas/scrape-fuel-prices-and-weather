import requests
class FetchData:
    def __init__(self, url: str, file_name):
        self.web_link = url
        self.file_name = file_name

        if not url:
            raise Exception("You have to provide a url to fetch the data")

        if not isinstance(url,str):
            raise ValueError(f"The type of url should be string but you have provided type = {type(url)}")

    def fetch(self):
        html_data = requests.get(self.web_link).content
        return html_data

    def run(self):
        data = self.fetch()
        with open(f'tmp/{self.file_name}.html', 'wb') as file:
            file.write(data)
            file.close()
        

if __name__=="__main__":
    FetchData('https://sports.ndtv.com/english-premier-league/news', 'ndtv').run()