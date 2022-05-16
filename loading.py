class Trip:
    def __init__(self):
        self.trip_id = ""
        self.stop_name = ""
        self.stop_dict = {}
    
    def load(self, dict):
        self.stop_id = dict["stop_id"]
        self.stop_name = dict["stop_name"]
        self.stop_dict= {"stop_id":self.stop_id,"stop_name":self.stop_name}