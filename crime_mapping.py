
import pandas as pd
import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
from datetime import timedelta

# Mapping
import geopandas
import geopy
from geopy.geocoders import Nominatim
import folium
from geopy.extra.rate_limiter import RateLimiter
from folium import plugins
from folium.plugins import MarkerCluster
from folium.plugins import Search




df = pd.read_csv("baltimore_crime_data.csv")
df = df.set_index("case_number")
df['date and time'] = pd.to_datetime(df['date and time'], format="%d-%m-%Y %H:%M")
df['date'] = [d.date() for d in df['date and time']]
df = df[~df['date and time'].isnull()] # remove rows with null values in OCCURED column
df['time'] = [d.time() for d in df['date and time']]
df['day'] = df['date and time'].dt.day_name()

# Find Fractions of Day
df['timeint'] = (df['date and time']-df['date and time'].dt.normalize()).dt.total_seconds()/timedelta(days=1).total_seconds()
locator = Nominatim(user_agent='myGeocoder', timeout=100)
location = locator.geocode('Baltimore,USA')
geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
df['location'] = df['address'].apply(geocode)
df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)

# 4 - split point column into latitude, longitude and altitude columns and remove empty points
df = df[df['point'].notnull()]
df[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df['point'].tolist(), index=df.index)
df.head()

# Mark events with names on map
m = folium.Map([ 39.299236,-76.609383], zoom_start=14)


# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# 1 - Create a list of sorted years
years = sorted(df['date'].dt.year.unique())

# 2 - Create a dictionary to hold the markers for each year
year_markers = {}

# 3 - Iterate over the years, creating a marker cluster for each year
for year in years:
    year_data = df[df['date'].dt.year == year]
    marker_cluster = MarkerCluster().add_to(m)
    
    # 4 - Add a label to each marker cluster with the year
    label = folium.Marker(location=[year_data['latitude'].mean(), year_data['longitude'].mean()], 
                          icon=None, 
                          popup=str(year))
    label.add_to(marker_cluster)
    
    # Add markers for each event
    for index, row in year_data.iterrows():
        popup_text = f"Date and Time: {row['date and time']}<br>" \
                     f"Crime: {row['crime']}<br>" \
                    
        folium.Marker([row['latitude'], row['longitude']],
                            radius=3,
                            popup=popup_text,
                            fill_color="#3db7e4",
                           ).add_to(marker_cluster)
    
    # 5 - Add the marker cluster to the map
    year_markers[year] = marker_cluster




# convert to (n, 2) nd-array format for heatmap
dfmatrix = df[['latitude', 'longitude']].values
# plot heatmap
m.add_child(plugins.HeatMap(dfmatrix, radius=15))

# Show the map
m

# save the file
m.save('map.html')


