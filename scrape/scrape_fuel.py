import json

from libraries.base_scrape import BaseScrape
from libraries.api_libs import PostToAPI
class ScrapeFuel(BaseScrape):

    def scrape(self, country: str):
        soup = self._read_file()
        table_rows = soup.find("div",{"id": "graphPageLeft"}).find('tbody').find_all('tr')
        data_dict = {}
        for row in table_rows:
            currency = str(row.find('th').text).strip().lower()
            prices = []
            for cell in row.find_all('td'):
                prices.append(cell.text)
            if currency in ['usd', 'eur']:
                data_dict[f'{currency}_price_per_litre'] = float(str(prices[0]).replace(',', ''))
                data_dict[f'{currency}_price_per_gallon'] = float(str(prices[1]).replace(',', ''))
            data_dict['country'] = country
        PostToAPI('http://127.0.0.1:8000/add_fuel/', json.dumps(data_dict)).api_post()



if __name__=='__main__':
    ScrapeFuel('tmp/kenya_fuel_price.html').scrape('KE')
    ScrapeFuel('tmp/uganda_fuel_price.html').scrape('UG')