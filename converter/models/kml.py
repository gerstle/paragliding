import xml.etree.ElementTree as ET
from models.waypoint import Waypoint
import re
from typing import List
import os
import chevron
from rich import print

def get_namespace(element):
  m = re.match('\{.*}', element.tag)
  return m.group(0) if m else ''


class KML:
    def __init__(self, file: str = None):
        self._template_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../templates/kml.mustache")
        if file:
            self._points = self.__load_file(file)
        else:
            self._points = []
    
    @property
    def waypoints(self) -> List[Waypoint]:
        return self._points


    @waypoints.setter
    def waypoints(self, waypoints: List[Waypoint]):
        self._points = waypoints

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

    def to_file(self, file):
        waypoints = []
        for p in self._points:
            waypoints.append({
                "name": p.name,
                "lat": p.lat,
                "long": p.long,
                "altitude": p.altitude,
            })
        values = {
            "name": os.path.basename(file),
            "waypoints": waypoints
        }

        print(f"rendering waypoints to [blue]{file}[/blue]")
        with open(self._template_file, "r") as template:
            content = chevron.render(template=template, data=values, warn=True)
            with open(file, "w") as output:
                output.write(content)

    @staticmethod
    def __parse_placemark(namespace, placemark) -> Waypoint:
        name = placemark.find(f"{namespace}name").text
        lookat = placemark.find(f"{namespace}Point")
        coordinates = lookat.find(f"{namespace}coordinates").text
        long, lat, alt = coordinates.split(',')

        return Waypoint(name, lat, long, alt)