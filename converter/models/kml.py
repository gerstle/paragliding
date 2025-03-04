import xml.etree.ElementTree as ET
import models.waypoint as models
import re
from typing import List

def get_namespace(element):
  m = re.match('\{.*}', element.tag)
  return m.group(0) if m else ''


class KML:
    def __init__(self, file: str = None):
        if file:
            self._points = self.__load_file(file)
        else:
            self._points = []
    
    @property
    def waypoints(self) -> List[models.Waypoint]:
        return self._points
    
    def __load_file(self, file: str):
        tree = ET.parse(file)
        root = tree.getroot()
        namespace = get_namespace(root)
        doc = root.find(f"{namespace}Document")
        points = []
        for it in doc.findall(f"{namespace}Placemark"):
            pt = self.__parse_placemark(namespace, it)
            points.append(pt)
        
        return points
    
    @staticmethod
    def __parse_placemark(namespace, placemark) -> models.Waypoint:
        name = placemark.find(f"{namespace}name").text
        lookat = placemark.find(f"{namespace}Point")
        coordinates = lookat.find(f"{namespace}coordinates").text
        long, lat, alt = coordinates.split(',')

        return models.Waypoint(name, lat, long, alt)