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

    def getStopId(self):
        return self.stop_id

    def getStopName(self):
        return self.stop_name

class Route:
    def __init__(self):
        self.route_id = ""
        self.short_name = ""
        self.long_name = ""
    
    def load(self, dict):
        self.route_id = dict["route_id"]
        self.short_name = dict["route_short_name"]
        self.long_name = dict["route_long_name"]

    def getRouteID(self):
        return self.route_id

    def getShortName(self):
        return self.short_name

    def getLongName(self):
        return self.long_name

class Trip:
    def __init__(self):
        self.trip_id = ""
        self.route = Route
    
    def load(self, dict):
        self.trip_id = dict["trip_id"]
        self.route = routes_all.get(dict["route_id"])
    
    def getTripID(self):
        return self.trip_id

class StopTime:
    def __init__(self):
        self.trip = Trip
        self.stop = Stop
        self.stop_sequence = 0

    def load(self, dict):
        self.trip = trips_all.get(dict["trip_id"])
        self.stop = stops_all.get(dict["stop_id"])
        self.stop_sequence = dict["stop_sequence"]
    
    def getStopSeq(self):
        return self.stop_sequence

with open("stops.txt", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        stop = Stop()
        stop.load(row)
        stops_all.update({stop.getStopId():stop})

with open("routes.txt", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        route = Route()
        route.load(row)
        routes_all.update({route.getRouteID():route})

with open("trips.txt", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        trip = Trip()
        trip.load(row)
        trips_all.update({trip.getTripID():trip})

with open("stop_times.txt", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        stop_seq = StopTime()
        stop_seq.load(row)
        if stop_seq.trip.getTripID() not in stop_seq_all.keys():
            stop_seq_all[stop_seq.trip.getTripID()] = [stop_seq]
        elif stop_seq.trip.getTripID() in stop_seq_all.keys():
            stop_seq_all[stop_seq.trip.getTripID()].append(stop_seq)
        
class StopSegment:
    def __init__(self):
        self.stop_dep = Stop
        self.stop_ariv = Stop
        self.occurences = 0

    #@classmethod
    def load_stops(cls,stop_times):
        for i in stop_times:
            for v in stop_times[i]:
                print(v.stop.getStopId())


data = StopSegment.load_stops(StopSegment,stop_seq_all)