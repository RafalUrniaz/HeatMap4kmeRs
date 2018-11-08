# (C) Rafal Urniaz
#  

# Import required modules
import os, csv, sys

# Data 
import numpy as np
import pandas as pd

# Graphics 
import matplotlib
import matplotlib.pyplot as plot


# Function takes as an argument the filename and directory 
# and returns pandas' dataframe


def read_file(filename = ""):

    if os.path.isfile(filename) and os.access(filename, os.R_OK):
        file_dataframe = pd.read_csv(filename, sep = ";", index_col = 0)
        file_dataframe = pd.DataFrame(file_dataframe.iloc[1:len(file_dataframe.iloc[0])], dtype = "float_")
        print("File exists and is readable [-- OK --]")

        # Print first 5 rows
        print(file_dataframe.iloc[0:3,])
    
    else:
        print("Either the file is missing or not readable")
        sys.exit()
    
    return file_dataframe

#Function takes as an argument .. and returns pandas' dataframe

def heatmap(file_dataframe):

# Prepare data

    # x axis labels - columns names
    x_labels = file_dataframe.columns

    # y axis label - rows names
    y_labels = file_dataframe.index

    # data to the heatmap plot
    data = file_dataframe.values
    #fig, ax = matplotlib.pyplot.subplots()

    return data  # file_dataframe