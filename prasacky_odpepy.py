import csv

stops_all = {} #dict for all the stops objects
routes_all = {}
trips_all = {}
stop_times_all = []

class Stop:
    def __init__(self, stop_id, stop_name):
        self.stop_id = stop_id
        self.stop_name = stop_name

class Route:
    def __init__(self, route_id, route_short_name, route_long_name):
        self.route_id = route_id
        self.short_name = route_short_name
        self.long_name = route_long_name
    
    def load(self, dict):
        self.route_id = dict["route_id"]
        self.short_name = dict["route_short_name"]
        self.long_name = dict["route_long_name"]

class Trip:
    def __init__(self, trip_id, route):
        self.trip_id = trip_id
        self.route = route

class Stop_time:
    def __init__(self, trip, stop, stop_sequence):
        self.trip = trip
        self.stop = stop
        self.stop_sequence = stop_sequence

with open("gtfs/stops.txt", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        stop = Stop(row["stop_id"], row["stop_name"])
        stops_all[stop.stop_id] = stop

with open("gtfs/routes.txt", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        route = Route(row["route_id"], row["route_short_name"], row["route_long_name"])
        routes_all[route.route_id] = route

with open("gtfs/trips.txt", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        route_vymenna = row['route_id']
        trip = Trip(row['trip_id'], routes_all[route_vymenna])
        trips_all[trip.trip_id] = trip

with open("gtfs/stop_times.txt", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        trip_vymenna = row['trip_id']
        stop_vymenna = row['stop_id']
        stop_time = Stop_time(trips_all[trip_vymenna], stops_all[stop_vymenna], row['stop_sequence'])
        stop_times_all.append(stop_time)
    
 #část 2 - vytvoření úseků - potřeba otestovat

class StopSegment:
    def __init__(self, stop_1, stop_2, occurrences):
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
            if stop_1.stop_id <= stop_2.stop_id:
                first = stop_1
                second = stop_2
            else:
                first = stop_2
                second = stop_1

            segment_key = (first.stop_id, second.stop_id)

            if segment_key not in stopsegments_dict:
                occurrences = 1
                sgmnt = StopSegment(first, second, occurrences)
                stopsegments_dict[(segment_key)] = sgmnt

            else:
                stopsegments_dict[segment_key].occurrences += 1

        return stopsegments_dict


    @classmethod
    def print_segments(cls, stopsegments_dict):
        sorted_segment_dict = sorted(stopsegments_dict.values(), key = lambda x: x.occurrences, reverse=True)
        i = 1
        for item in sorted_segment_dict[:5]:
            print(f"{i}.: Spojení je mezi zastávkou {item.stop_1.stop_id} a zastávkou {item.stop_2.stop_id}. Počet spojů: {item.occurrences}.")
            i+=1

StopSegment.print_segments(StopSegment.loading_segments(stop_times_all))
