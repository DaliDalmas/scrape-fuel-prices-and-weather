from libraries.fetch_data import FetchData

def fetch_kenyan_gasoline():
    url = 'https://www.accuweather.com/en/ug/kampala/318416/current-weather/318416'
    FetchData(url=url, file_name='kampala_weather').run()
