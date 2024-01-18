# Map App

The aim of this project is to create a web application for users to interact with
some of the Google Map’s API endpoints. The application is created using Flask
and features pages that allow users to perform three major functionalities: “At
a Glance”, “Search Advance”, and “Travel Plans”. Each functionality makes
use of one or more Google Maps API endpoints to serve data to the users,
based on user input. Overview of these functionalities are given below:

- The “At a Glance” functionality allows user to input the name of a location
and provides an embedded interactive map, along with a gallery of images
based on that location. The interactive map has the option to switch to
Satellite view from the default Street map view, and also provides two
external links to Google Map’s website. One of the link is to view a larger
version of the map, along with the location details. The other link is to get
directions to the location. The image gallery below this interactive map
features eight images. The first four images are static aerial view images of
the location corresponding to Road, Satellite, Terrain, and Hybrid views.
The next last four images are static street view images of the location
taken from one 360° panorama image corresponding to the North, East,
South, and West directions.

- The “Search Advance” functionality provides an interactive map with an
auto-complete search feature to look up places quickly. The auto-complete
search feature uses smart auto-fill suggestions based on which place the
map is currently showing. For instance, searching for the city “Halifax”
when the map view is around the American continents will show suggestions
for the Halifax city in Nova Scotia, Canada, whereas, searching for
the same city “Halifax” when the map view is around Europe will show
suggestions for Halifax city in the United Kingdom.

- The “Travel Plans” functionality allows user to input of origin and destination
cities, and gives an interactive map view with pointers to the
source (marked as A) and destination (marked as B) locations. The resulting
route between these points is highlighted on the map. In addition
to this, a detailed list of directions, turns, and distances are given to reach
from point A to point B

Additionally, the maps on “Search Advance” and “Travel Plans” pages also
gives options to view the map in full screen, as well as to drop the pegman icon
on any area of the map to get an immersive and interactive 360° view of the
area. These interactive maps also provides options switching between satellite
and default street view, with additional toggle options to show or hide markers
or terrain respectively.
