import pandas as pd
from bs4 import BeautifulSoup
class ScrapeWeather:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def _read_file(self):
        with open(self.file_path, 'r') as f:
            file = f.read()
        return file

    def scrape(self):
        file = self._read_file()
        soup = BeautifulSoup(file, 'html')
        print(soup)

if __name__=='__main__':
    sobj = ScrapeWeather('tmp/kampala_weather.html')
    sobj.scrape()