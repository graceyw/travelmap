'''Folium python map'''

import folium   # library for data visualization on maps
import json
from time import sleep

def plot_places():
    """
    INPUT: database containing places w/ long, lat, name, comment, and visited status
    OUTPUT: map with pins on locations
    """
    colors = ['red','green','blue','purple','orange','darkred','lightred','beige','darkblue','darkgreen','gray','black','lightgray']

    # Creates map
    p = folium.Map(zoom_start=2, tiles='Mapbox bright')
    # folium.Marker(location=[5,6]).add_to(placesMap)

    p.save('testMap.html')

if __name__ == '__main__':
    plot_places()
