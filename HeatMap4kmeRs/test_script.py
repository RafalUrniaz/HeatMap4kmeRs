# -*- coding: utf-8 -*-
"""Test script module for heatmap4kmers package

This module demonstrates the example charts for kmeRs package

"""
## (C) Rafal Urniaz

# Import modules
try:
    from kmers_heatmap import kmers_heatmap
    from kmers_heatmap import read_file

    # Graphics 
    import matplotlib.pyplot as plt

    #import matplotlib_heatmap_functions
    print("import: [-- OK --]")
except ImportError:
    print("Could not import heatmap4kmers package [-- Error --]")


if __name__ == '__main__':

# --- Import sample_file 

    x = read_file(filename = r"example_data\example_kmeRs_matrix.csv")

# --- Prepare Quick HeatMap Demo

# Standard
    #kmers_heatmap(file_dataframe = x, show_legend = False)

# Categorised
    #kmers_heatmap(file_dataframe = x, cmap = plt.cm.get_cmap('Blues', 10), save_file = True, file_name = "Figure_2")

# RdBu positive vs. negative values
    kmers_heatmap(file_dataframe = x[x.columns.difference(["score_total"])], cmap="RdBu")

