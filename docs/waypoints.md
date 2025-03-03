# Waypoint tutorial

The idea here is to document how to create waypoint files that can be imported into XCTrack. The ultimate goal is to
teach newer XC pilots how to navigate and complete tasks.

# Creating waypoint files

The easiest way that I've found to manage waypoints is to do it visually in [google earth](https://earth.google.com/),
export it as a KML file, and then convert it to a waypoint file (.wpt). All of the tools I've found to do this so far
are not great, so I forged my own path and made my own tool.

1. Create a project in [google earth](https://earth.google.com/) and drop pins where you want them
    - For example, my [sand city project](https://earth.google.com/earth/d/1X3ToC1Kt2kLXc0vw8LZcZgNbkZDY9afE?usp=sharing)
2. Export as `KML` file
3. Run the `converter` included in this repo to convert the KML file to a `.wpt` waypoint file
    - [see here for how](../converter/README.md)
4. Transfer the waypoint file to your phone
    - I usually put the file in a google drive folder
    - If you want to use Android File Transfer or some other tool, drop it directly into
      `/Android/data/org.xcontest.XCTrack/files/Waypoints`

# Examples

- [sand city google earth project](https://earth.google.com/earth/d/1X3ToC1Kt2kLXc0vw8LZcZgNbkZDY9afE?usp=sharing)
- [exported KML file](../sandcity/sand-city.kml)
- [Converted waypoint (.wpt) file](../sandcity/sand-city.wpt)