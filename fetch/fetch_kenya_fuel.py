from libraries.fetch_data import FetchData

def fetch_kenyan_gasoline():
    url = 'https://www.globalpetrolprices.com/Kenya/gasoline_prices/'
    FetchData(url=url, file_name='kenyan_gasoline_price').run()
