import os
from typing import List
import models.waypoint as models
from rich import print
from geopy.point import Point
import chevron


class WPT:
    def __init__(self, file: str = None):
        self._template_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../templates/wpt.mustache")
        if file:
            self._points = self.__load_file(file)
        else:
            self._points = []

    @property
    def waypoints(self) -> List[models.Waypoint]:
        return self._points

    @waypoints.setter
    def waypoints(self, waypoints: List[models.Waypoint]):
        self._points = waypoints

    def __load_file(self, file: str):
        raise RuntimeError(f"TODO")

    def to_file(self, file):
        # convert to values dict
        waypoints = []
        for p in self._points:
            lat, long = self.__to_dms(p)
            print(f"{p.name}")
            print(f"\t{p.lat} --> {lat[0]} {lat[1]} {lat[2]} {lat[3]}")
            print(f"\t{p.long} --> {long[0]} {long[1]} {long[2]} {long[3]}")
            print(f"\t{p.altitude} --> {p.altitude}")
            waypoints.append({
                "name": p.name,
                "description": p.description,
                "lat": {
                    "hemisphere": lat[0],
                    "degree": lat[1],
                    "minute": lat[2],
                    "second": lat[3],
                },
                "long": {
                    "hemisphere": long[0],
                    "degree": long[1],
                    "minute": long[2],
                    "second": long[3],
                },
                "altitude": round(max(0, p.altitude)),
            })
        values = {"waypoints": waypoints}

        print(f"rendering waypoints to [blue]{file}[/blue]")
        with open(self._template_file, "r") as template:
            content = chevron.render(template=template, data=values, warn=True)
            with open(file, "w") as output:
                output.write(content)


    @staticmethod
    def __to_dms(wpt: models.Waypoint):
        p = Point(wpt.lat, wpt.long).format(False, '', '', '')
        lat, long = p.split(",")
        lat = lat.strip().split(" ")
        long = long.strip().split(" ")
        return [
            (lat[3], lat[0], lat[1], round(float(lat[2]), 2)),
            (long[3], long[0], long[1], round(float(long[2]), 2)),
        ]
