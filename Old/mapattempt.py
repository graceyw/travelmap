'''Folium python map'''

import folium   # library for data visualization on maps
import json
from time import sleep

def plot_places():
    """
    INPUT: database containing places w/ long, lat, name, comment, and visited status
    OUTPUT: map with pins on locations
    """

    # Creates map
    placesMap = folium.Map(zoom_start=2, tiles='Mapbox bright')
    # folium.Marker(location=[356915.68,482043.25],icon=folium.Icon(color='green'),popup='hi').add_to(placesMap)

    # Loads database from json file 'placesdb.json'
    with open('placesdb.json') as f:
        PlacesDB = json.load(f)

    # TEST PRINT STATMENTS
    # location=[PlacesDB["places"][0]["lat"],PlacesDB["places"][0]["long"]]
    # icon = folium.Icon(color=colors[0])
    # popup = {PlacesDB["places"][0]["name"],                           # name
    #          PlacesDB["places"][0]["comment"],                        # comment
    #          PlacesDB["places"][0]["visited"]}
    # print(location, icon, popup)

    # Loops through placesDB and drops pins i.e. 'markers'
    # for i in range(len(PlacesDB["places"])):
    #     # if PlacesDB[i] == []:
    #     #     pass
    #     # else:
    #     if PlacesDB["places"][i]["visited"]:                                              # if "visited" == true, make icon blue
    #         folium.map.Marker(location=[PlacesDB["places"][i]["lat"],PlacesDB["places"][i]["long"]],     # lat, long (northing, easting)
    #                           icon=folium.Icon(color='blue'),                                  # blue if visited
    #                           popup=PlacesDB["places"][i]["name"]+': '+                        # name
    #                                 PlacesDB["places"][i]["comment"]                           # comment
    #                                  ).add_to(placesMap)
    #     else:                                                                             # if "visited" == false or doesn't exist, make icon red
    #         folium.map.Marker(location=[PlacesDB["places"][i]["lat"],PlacesDB["places"][i]["long"]],     # lat, long (northing, easting)
    #                           icon=folium.Icon(color='red'),                                   # red if not yet visited
    #                           popup=PlacesDB["places"][i]["name"]+': '+                        # name
    #                                 PlacesDB["places"][i]["comment"]                           # comment
    #                                  ).add_to(placesMap)
        # sleep(1)  # Delays calls to open cage geocoder
    # keep_in_front(marker)
    folium.ClickForMarker(popup='place').add_to(placesMap)
    placesMap.save('map2.html')

if __name__ == '__main__':
    plot_places()
