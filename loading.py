import csv

class Trip:
    def __init__(self):
        self.trip_id = ""
        self.stop_name = ""
        self.stop_dict = {}
    
    def load(self, dict):
        self.stop_id = dict["stop_id"]
        self.stop_name = dict["stop_name"]
        self.stop_dict= {"stop_id":self.stop_id,"stop_name":self.stop_name}

class Route:
    def __init__(self):
        self.route_id = ""
        self.short_name = ""
        self.long_name = ""
        self.route_dict = {}
    
    def load(self, dict):
        self.route_id = dict["route_id"]
        self.short_name = dict["short_name"]
        self.long_name = dict["long_name"]
        self.stop_dict = {"route_id":self.route_id,"short_name":self.short_name,"long_name":self.long_name}

with open("routes.txt", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        stop = Route()
        stop.load(row)
        routes_all.append = {Route.route_id:[Route.long_name,Route.short_name]}