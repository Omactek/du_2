import csv

stops_all = {} #dict for all the stops objects
routes_all = {}
trips_all = {}
stop_seq_all = {} #{"trip_id1":[{"stop_id1":stop_seq1},{"stop_id1":stop_seq2...],...]}

class Stop:
    def __init__(self):
        self.stop_id = ""
        self.stop_name = ""
    
    def load(self, dict):
        self.stop_id = dict["stop_id"]
        self.stop_name = dict["stop_name"]

class Route:
    def __init__(self):
        self.route_id = ""
        self.short_name = ""
        self.long_name = ""
    
    def load(self, dict):
        self.route_id = dict["route_id"]
        self.short_name = dict["route_short_name"]
        self.long_name = dict["route_long_name"]

class Trip:
    def __init__(self):
        self.trip_id = ""
        self.route = {}
    
    def load(self, dict):
        self.trip_id = dict["trip_id"]
        self.route = routes_all.get(dict["route_id"])

class Stop_time:
    def __init__(self):
        self.trip = {}
        self.stop = {}
        self.stop_sequence = 0

    def load(self, dict):
        self.trip = trips_all.get(dict["trip_id"])
        self.stop = stops_all.get(dict["stop_id"])
        print(self.trip)
        self.stop_sequence = dict["stop_sequence"]

with open("stops.txt", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        stop = Stop()
        stop.load(row)
        stops_all[stop.stop_id] = stop.stop_name

with open("routes.txt", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        route = Route()
        route.load(row)
        routes_all[route.route_id] = {"short_name":route.short_name,"long_name":route.long_name}

with open("trips.txt", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        trip = Trip()
        trip.load(row)
        trips_all[trip.trip_id] = {"route":trip.route}  

with open("stop_times.txt", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        stop_seq = Trip()
        stop_seq.load(row)
        #if stop_seq_all.get(stop_seq.trip[, default])
        
 #část 2 - vytvoření úseků - potřeba otestovat

class StopSegment:
    def __init__(self):
        self.stop_1 = stop_1
        self.stop_2 = stop_2
        self.occurrences = occurrences
    
    @classmethod
    def loading_segments(cls, stoptime_seznam):
        stopsegments_dict = {}

        for stop_time in stoptime_seznam:
            if stop_time.stop_sequence == "1":
                stop_1 = stop_time.stop
                continue
            elif stop_time.stop_sequence == "2":
                stop_2 = stop_time.stop

            else:
                #vyšší než první dvě zastávky -> druhá jde za první a nově načetlá následuje jako stop_2
                stop_1 = stop_2
                stop_2 = stop_time.stop

                
            # následující podmínka: seřazení dle id, tak aby stejný úsek byl stejně identifikován v obou směrech
            if stop_1.id <= stop_2.id:
                first = stop_1
                second = stop_2
            else:
                first = stop_2
                second = stop_1

            segment_key = (first.id, second.id)

            if segment_key not in stopsegments_dict:
                occurrences = 1
                sgmnt = StopSegment(first, second, occurrences)
                stopsegments_dict[(segment_key)] = sgmnt

            else:
                stopsegments_dict[segment_key].occurrences += 1

            return stopsegments_dict


