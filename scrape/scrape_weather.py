import json

from libraries.base_scrape import BaseScrape
from libraries.api_libs import PostToAPI
class ScrapeWeather(BaseScrape):

    def scrape(self, country: str):
        soup = self._read_file()
        elements = []
        temperature = soup.find('td', {"class": "temperature"}).text
        elements.append('temperature')
        elements.append(str(temperature).strip())
        wind = soup.find('b', {"class": "wind_ico"}).text
        elements.append('wind')
        elements.append(str(wind).strip())

        table_cell_elements = soup.find_all('div', {"class": "info_table"})[2].find_all('td')
        for cell_element in table_cell_elements:
            elements.append(str(cell_element.text).strip())

        data_dict = {}
        for index in range(len(elements)):
            if index%2!=0:
                key = str(elements[index-1].lower()).replace(" ", "_")
                data_dict[key] = float(elements[index].split(' ')[0])
                data_dict[f'{key}_unit'] = str(elements[index].split(' ')[1])
        data_dict['country'] = country

        PostToAPI('http://127.0.0.1:8000/add_weather/', json.dumps(data_dict)).api_post()

if __name__=='__main__':
    ScrapeWeather('tmp/kampala_weather.html').scrape('UG')
    ScrapeWeather('tmp/nairobi_weather.html').scrape('KE')