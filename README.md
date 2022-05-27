# pygame ISS tracker
---
A script that tracks the International Space Station implemented using Python and pygame for plotting its previous positions on a map in real time.

Originally made as a project to study the subject of APIs and how to process the retrieved data, with the goal of being as simple and straightforward as possible.


### Known issues and limitations
---
- Currently it only works with maps using equidistant projections, since the code maps the coordinates linearly.
- Since the program plots a polyline using the lines on a list as vertices, when the ISS exits one edge of the map and reappears on the other one the program plots a straight line across the map.
