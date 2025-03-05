# Waypoint tutorial

The idea here is to document how to create waypoint files that can be imported into XCTrack. The ultimate goal is to
teach newer XC pilots how to navigate and complete tasks.

# Creating waypoint files

The easiest way that I've found to manage waypoints is to do it visually in [Google Earth](https://earth.google.com/),
export it as a KML file, and then convert it to a waypoint file (.wpt). All of the tools I've found to do this so far
are not great, so I forged my own path and made my own tool.

1. Create a project in [Google Earth](https://earth.google.com/) and drop pins where you want them
    - For example,
      my [sand city project](https://earth.google.com/earth/d/1X3ToC1Kt2kLXc0vw8LZcZgNbkZDY9afE?usp=sharing)
2. Export as `KML` file
3. Run the `converter` included in this repo to convert the KML file to a `.wpt` waypoint file
    - [see here for how](../converter/README.md)
4. Transfer the waypoint file to your phone
    - I usually put the file in a google drive folder
    - If you want to use Android File Transfer or some other tool, drop it directly into
      `/Android/data/org.xcontest.XCTrack/files/Waypoints`

# Examples

- [sand city Google Earth project](https://earth.google.com/earth/d/1X3ToC1Kt2kLXc0vw8LZcZgNbkZDY9afE?usp=sharing)
- [sand city exported KML file](../sites/sandcity/sand-city-v1.kml)
- [sand city Converted waypoint (.wpt) file](../sites/sandcity/sand-city-v1.wpt)
- Others
    - [NorCal XC league 2024](../examples/XC%20league%202024.wpt)
    - [Torrey Ridge Race Holiday Special](../examples/TorreyRR_HolidaySpecial.txt)
    - [Torrey Ridge Race SepOct24](../examples/TorreyRR_SepOct24.txt)
