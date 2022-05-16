import csv

stops_all = {} #dict for all stops objects, key is stop ID
routes_all = {} #dict for all route objects, key is route ID
trips_all = {} #dict for all trip objects, key is trip ID
stop_seq_all = {} #dict of lists of stop time object with same trip ID, key is trip ID
stopsegments_dict = {} #dict of all segments


class Stop:
    def __init__(self):
        self.stop_id = "" #initialize string value
        self.stop_name = ""
    
    def load(self, dict):
        self.stop_id = dict["stop_id"] #gets attribute from stop id column
        self.stop_name = dict["stop_name"]

    def getStopId(self): #getter for stop_id
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
        self.route = Route #initializes as Route class
    
    def load(self, dict):
        self.trip_id = dict["trip_id"]
        self.route = routes_all.get(dict["route_id"]) #loads route object with the same route ID as this row
    
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

class StopSegment:
    def __init__(self):
        self.stop_dep = Stop
        self.stop_ariv = Stop
        self.occurrences = 0

    def load(self, dep, ariv, occ):
        self.stop_dep = dep
        self.stop_ariv = ariv
        self.occurrences = occ

    def getOcc(self):
        return self.occurrences

    def create_segments(stop_times): #creates segments
        for i in stop_times:
            for v in stop_times[i]:
                    if v.getStopSeq() == "1":
                        stop_1 = v.stop
                        continue

                    elif v.getStopSeq() == "2":
                        stop_2 = v.stop

                    else:
                        #bigger than the two stops -> second changes to first and the newly loaded one follows as stop_2
                        stop_1 = stop_2
                        stop_2 = v.stop

                    #sorting based on ID, so the same segment is identified in both directions
                    if stop_1.getStopId() <= stop_2.getStopId():
                        first = stop_1
                        second = stop_2
                    else:
                        first = stop_2
                        second = stop_1

                    segment_key = (first.getStopId(), second.getStopId())

                    if segment_key not in stopsegments_dict:
                        occurrences = 1
                        sgmnt = StopSegment()
                        sgmnt.load(first,second,occurrences)
                        stopsegments_dict[(segment_key)] = sgmnt

                    else:
                        stopsegments_dict[segment_key].occurrences += 1

        return stopsegments_dict

try:
    with open("stops.txt", newline='', encoding="utf-8") as csvfile: #opens file
        reader = csv.DictReader(csvfile) #reads file as dict
        for row in reader:
            stop = Stop() #initializes as Stop
            stop.load(row) #loads specific row
            stops_all.update({stop.getStopId():stop}) #creates dict of all stops, uses stop ID as key

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
            if stop_seq.trip.getTripID() not in stop_seq_all.keys(): #creates dict of lists of stop time objects with same trip ID, key is trip ID
                stop_seq_all[stop_seq.trip.getTripID()] = [stop_seq]
            elif stop_seq.trip.getTripID() in stop_seq_all.keys(): #if there already is this trip ID as key appends this StopTime objects to list with the same trip ID
                stop_seq_all[stop_seq.trip.getTripID()].append(stop_seq)
except FileNotFoundError as error:
    print("File {:s} not found.".format(error.filename))
except PermissionError as error:
    print("You don´t have permission for file {:s}".format(error.filename))
        
data = StopSegment
data = StopSegment.create_segments(stop_seq_all)
sorted_segment_dict = sorted(data.values(), key = lambda x: x.getOcc(), reverse=True) #sorts segments based on occurrences

i = 1
for item in sorted_segment_dict[:5]: #prints five stops with the highest occurrences
    print(f"{i}.: Spojení je mezi zastávkou {item.stop_dep.getStopName()} a zastávkou {item.stop_ariv.getStopName()}. Počet spojů: {item.getOcc()}.")
    i+=1