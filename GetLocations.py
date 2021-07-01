# importing necessary libraries
import reverse_geocoder as rg
import pprint
import plotly.express as px
import pandas as pd
import numpy as np




  
def reverseGeocode(coordinates):
    result = rg.search(coordinates)
      
    # result is a list containing ordered dictionary.
    pprint.pprint(result) 
  
# Driver function
if __name__=="__main__":
      
    # Coorinates tuple.Can contain more than one pair.
    coordinates = (51.5214588,-0.1729636),(9.936033, 76.259952),(38.82908231,-77.08571225)
      
    reverseGeocode(coordinates) 



