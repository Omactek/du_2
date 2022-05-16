import csv

class Stop:
    def __init__(self):
        self.stop_id = ""
        self.stop_name = ""
        self.stop_dict = {}
    
    def load(self, dict):
        self.stop_id = dict["stop_id"]
        self.stop_name = dict["stop_name"]
        self.stop_dict= {"stop_id":self.stop_id,"stop_name":self.stop_name}

class Routes:
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



with open("stops.txt", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        stop = Stop()
        stop.load(row)
        
        
        
        
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


