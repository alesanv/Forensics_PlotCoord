## Forensics_PlotCoord

### Objective: Plot GPS coordinates found in an iPhone's consolidated.db file


For the digital forensics of an iPhone we can analyze the GPS data found in it by checking the `consolidated.db` database.
The goal usually is to find out the locations where the phone has been at during certain days and times, in the `consolidated.db` we can find a lot of location information and instead of going constantly to a mapping application to discover the location on the file, we can plot those locations into a map using this python script. 

- The infomation can be found in `root/Library/Caches/locationd/consolidated.db`
This database contains several fields, but for this script we'll only use the `timestamp`, `latitude` and `logitude`. 

- For simplification purposes those three columns were exported to a `CSV file` in order to work with them in the python script.

- Take into consideration that the timestamp in `consolidated.db` is a `NSDate timestamp` (time interval relative to 00:00:00 UTC on 1 January 2001).



Note: Right now the path to the CSV file is hardcoded into the script but can be changed to accept that information as parameter.


Example of what the script plots:

![alt text](Images/locations_6_13.PNG "GPS coordinates")
