## **Forensics_PlotCoord**
---

### **Objective:** 
Plot GPS coordinates found in an iPhone's consolidated.db file using a Python script.

### **Introduction:**
There is a scenario used to introduce students to Digital Forensics called the **2012 National Gallery DC Attack**, the scenario was created as part of a joint collaboration between the US Naval Postgraduate School and the US Military Academy at West Point. More information about it can be found at [Digital Corpora](https://digitalcorpora.org/corpora/scenarios/national-gallery-dc-2012-attack). 


One of the artifacts to investigate is an iPhone image. From the iPhone image we can analyze the GPS data found in it by checking the `consolidated.db` database.

The goal usually is to find out the locations where the phone has been during certain days and times. Some tools may already offer this functionality, but in my case the tool that I was using did not offer it, so instead of going constantly to a mapping application to discover the locations stored in the database, we can plot those locations into a map using this python script. 

### **Prepare the input data:**
- The `consolidated.db` database has to be extracted from the iPhone image, then its data can be accessed with SQLite.
    - Example of the data found in the database:
      ![alt text](Images/consolidated-db.PNG "consolidated.db")

- This database contains several fields, but for this script we'll only use the `timestamp`, `latitude` and `logitude`. 
- For simplification purposes those three columns were exported to a `CSV file` in order to work with them in the python script.
- Take into consideration that the timestamp in `consolidated.db` is a `NSDate timestamp` (time interval relative to 00:00:00 UTC on 1 January 2001).

### **Script:**

The script uses the [Plotly Python Open Source Graphing Library](https://plotly.com/python/), specifically the Scatter Plots on Mapbox maps in Python. No Mapbox account or public Mapbox Access Token is needed in this case because no data from the *Mapbox service* is requested.

Description:
1. Read the CSV file and store its contents in a dataframe. 
    - The CSV contains the `timestamp`, `latitude`, and `longitude` as explained in the previous section.
2. Normalize the `timestamp` field. 
    - The timestamp is in `NSDate` format and we need to transform it into human readable `UTC` format. In order to accomplish that we need to change it first to Unix epoch Time, which can be done by adding the time interval from 00:00:00 UTC on January/1/1970 to 00:00:00 UTC on Jan/1/2001.
3. Map the data with mapbox.
    - Uses the `plotly.express` library, which is the high-level interface to *Plotly*. The method used is the `scatter_mapbox` method  with the *mapbox style* as *OpenStreetMap*, which is the option that allows the script to run without the need of a *Mapbox* account.

Usage:
1. Install the following libraries in your python environment:
    ```bash:
    $ pip install plotly
    $ pip install pandas
    $ pip install numpy
    ```
2. The CSV file should be passed as input to the script.
    ```bash:
    $ python3 MapGPSLocations.py <CSV_File>
    ```

Example of what the script plots:

![alt text](Images/locations_6_13.PNG "GPS coordinates")
