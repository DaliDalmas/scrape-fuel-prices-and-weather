from libraries.fetch_data import FetchData

def fetch_kampala_weather():
    url = 'https://worldweather.wmo.int/en/city.html?cityId=1328'
    FetchData(url=url, file_name='kampala_weather').run()

if __name__=='__main__':
    fetch_kampala_weather()