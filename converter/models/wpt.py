import os
from typing import List
from typing import Optional
from models.waypoint import Waypoint
from rich import print
from geopy.point import Point
import chevron
import re


class WPT:
    def __init__(self, file: str = None):
        self._template_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../templates/wpt.mustache")
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
        points = []
        with open(file, "r") as f:
            for it in f:
                if it.startswith("$FormatGEO"):
                    continue
                pt = self.__parse_line(it)
                if pt:
                    points.append(pt)

        return points

    def __parse_line(self, line: str) -> Optional[Waypoint]:
        pattern = re.compile(
            r'([^ ]*) {4}([NS]) (\d*) (\d*) (\d*\.\d*) {4}([EW]) (\d*) (\d*) (\d*\.\d*) {3}(\d*)( {2}?(.*))?')
        if match := re.search(pattern, line):
            name = match.group(1)
            lat, long = self.__from_dms(
                '''{} {}' {}" {} {} {}' {}" {}'''
                .format(
                    match.group(3),
                    match.group(4),
                    match.group(5),
                    match.group(2),
                    match.group(7),
                    match.group(8),
                    match.group(9),
                    match.group(6)
                )
            )
            alt = float(match.group(10))
            description = match.group(12)
            return Waypoint(name, lat, long, alt, description)

    def to_file(self, file):
        waypoints = []
        for p in self._points:
            lat, long = self.__to_dms(p)
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
    def __from_dms(dms: str) -> {float, float}:
        p = Point(dms)
        return p.latitude, p.longitude

    @staticmethod
    def __to_dms(wpt: Waypoint):
        p = Point(wpt.lat, wpt.long).format(False, '', '', '')
        lat, long = p.split(",")
        lat = lat.strip().split(" ")
        long = long.strip().split(" ")
        return [
            (lat[3], lat[0], lat[1], round(float(lat[2]), 2)),
            (long[3], long[0], long[1], round(float(long[2]), 2)),
        ]
