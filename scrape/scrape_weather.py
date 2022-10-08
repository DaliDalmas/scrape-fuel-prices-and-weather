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
        soup = BeautifulSoup(file, features="lxml")
        present_temp_value_div = soup.find_all('div', {"class": "present_temp_value"})
        present_rh_value_div = soup.find_all('div', {"class": "present_rh_value"})
        print(present_temp_value_div, present_rh_value_div)

if __name__=='__main__':
    ScrapeWeather('tmp/kampala_weather.html').scrape()
    ScrapeWeather('tmp/nairobi_weather.html').scrape()