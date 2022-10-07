from libraries.fetch_data import FetchData

def fetch_kampala_weather():
    url = 'https://www.accuweather.com/en/ug/kampala/318416/current-weather/318416'
    FetchData(url=url, file_name='kampala_weather').run()

if __name__=='__main__':
    fetch_kampala_weather()