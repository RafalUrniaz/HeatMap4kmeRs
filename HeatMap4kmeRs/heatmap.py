# (C) Rafal Urniaz
#  

# Import required modules
import os, csv, sys, pandas

def read_file(filename = ""):

    if os.path.isfile(filename) and os.access(filename, os.R_OK):
        file_array = pandas.read_csv(filename, sep = ";", index_col = 0)
        file_array = pandas.DataFrame(file_array.iloc[1:len(file_array.iloc[0])], dtype = "float_")
        print(file_array.iloc[0,])
        # col number print(len(file_array.iloc[0]))
        print("File exists and is readable [-- OK --]")

    else:
        print("Either the file is missing or not readable")
        sys.exit()
    
    return filename

def heatmap(matrix = ""):
    return matrix