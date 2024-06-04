from pathlib import Path
import json
import plotly.express as px

#Read data as a string and convert to a python object.
path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

#Create a more readable version of the data file.
path = Path('eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

#Eximine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

mags,lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

title = "Global Earthquakes"
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title, color=mags,
                     color_continuous_scale='Viridis', labels={'colors': 
                                                               'Magnitude'},
                                                               projection=
                                                               'natural earth',)

fig.show()