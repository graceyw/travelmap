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
    map1 = folium.Map(zoom_start=2, tiles='Mapbox bright')
    # map1.Marker(location=[46.8354,-121.7325], popup='Camp Muir')
    # folium.Marker(location=[-100,-60]).add_to(map1)
    folium.ClickForMarker(popup='test point').add_to(map1)
    map1.save('emptymap.html')

if __name__ == '__main__':
    plot_places()


'''
Leaflet is the JS library being used
Folium is Python library

Put in an event listener: document.addEventListener('click', myfunction, false);
When event (marker getting put down) happens, run this function

Function gets the data we need based on the event

Then we figure out how to add custom js to send the data to dark
'''
