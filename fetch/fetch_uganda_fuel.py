from libraries.fetch_data import FetchData

def fetch_ugandan_gasoline():
    url = 'https://www.globalpetrolprices.com/Uganda/gasoline_prices/'
    FetchData(url=url, file_name='ugandan_gasoline_price').run()

if __name__=='__main__':
    fetch_ugandan_gasoline()