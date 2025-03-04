class Waypoint:
    def __init__(self, name: str, lat: float, long: float, altitude: float, description: str=''):
        self.name = name 
        self.lat = float(lat)
        self.long = float(long)
        self.altitude = float(altitude)
        self.description = description
    
    def __str__(self):
        return f"{self.name}:\n\tlat: {self.lat}\n\tlong: {self.long}\n\talt: {self.altitude}\n\tdesc: {self.description}"