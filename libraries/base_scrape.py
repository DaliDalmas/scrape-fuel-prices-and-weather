from bs4 import BeautifulSoup

class BaseScrape:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def _read_file(self):
        with open(self.file_path, 'r') as f:
            file = f.read()
        soup = BeautifulSoup(file)
        return soup