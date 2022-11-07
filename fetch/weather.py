from libraries.fetch_data import FetchData

class Weather:
    def __init__(self, city_id: int, city: str):
        self.city_id = city_id
        self.city = city

    def fetch_weather(self):
        url = f'https://www.ventusky.com/{self.city.lower()}'
        print(url)
        FetchData(url=url, file_name=f'{self.city}_weather').run()

if __name__=='__main__':
    kampala = 1328
    nairobi = 251
    Weather(kampala, 'kampala').fetch_weather()
    Weather(nairobi,'nairobi').fetch_weather()