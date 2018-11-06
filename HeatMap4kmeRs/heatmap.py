# (C) Rafal Urniaz
#  

import os
import os.path

def read_file(filename = ""):

    if os.path.isfile(filename) and os.access(filename, os.R_OK):
        print("File exists and is readable")
    else:
        print("Either the file is missing or not readable")

    return filename

def heatmap(matrix = ""):
    return matrix