from libraries.fetch_data import FetchData

def fetch_kenyan_gasoline():
    url = 'https://worldweather.wmo.int/en/city.html?cityId=251'
    FetchData(url=url, file_name='nairobi_weather').run()

if __name__=='__main__':
    fetch_kenyan_gasoline()