import csv

with open("stops.txt", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        stop = Stop()

class Stop:
    def __init__(self):
        self.stop_id = ""
        self.stop_name = ""
        self.stop_dict = {}
    
    def load(self):
        self.stop_id = 