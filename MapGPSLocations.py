
import sys
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime

#Check the input
if len(sys.argv) != 2:
    raise ValueError('Please provide the name of the CSV file')
 
#Create a dataframe with the coordinate data from a CSV file
try:
    csvFile = sys.argv[1]
    df = pd.read_csv(csvFile)
except IOError:
    raise ValueError('Error reading the File')


# --- Normalize the timestamp to Unix epoch time ---
#variables to help us manage the timestamp info and add them to the dataframe
ts = []
unixTS = 978307200 
#iterate through each row of the dataframe 
for index, row in df.iterrows():
   
    # Try to,
    try:
        #get the iphone timestamp
        iphoneTS = int(row['Timestamp'])
        #convert that iphone timestamp to UTC
        ts.append(str(datetime.utcfromtimestamp(unixTS + iphoneTS)))
                                      
    # But if you get an error
    except Exception:
        # append a missing value 
        ts.append(np.NaN)

#Add the new timestamp (UTC) data to the dataframe
df['UTC'] = ts



#Map the data with mapbox
fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_name="UTC",
                        color_discrete_sequence=["red"], zoom=10, height=1000)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
