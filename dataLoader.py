import csv
import urllib.request

class DataLoader:
    def __init__(self, url):
        self.url = url

    def download_csv(self):
        urllib.request.urlretrieve(self.url, "task_rcs.csv")

    def parse_csv(self, variant_number):
        self.download_csv()
        with open('task_rcs.csv', 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Пропускаем заголовок
            for row in csv_reader:
                if int(row[0]) == variant_number:
                    D = float(row[1])
                    fmin = float(row[2])
                    fmax = float(row[3])
                    return D, fmin, fmax
        raise ValueError("Variant number not found in CSV file")

