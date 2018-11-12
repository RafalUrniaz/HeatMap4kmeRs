## (C) Rafal Urniaz
#

# Test functions in heatmap4kmers package
# Import modules

try:
    # Graphics 
    import matplotlib.pyplot as plt

    from kmers_heatmap import kmers_heatmap
    from kmers_heatmap import read_file

    #import matplotlib_heatmap_functions
    print("import: [-- OK --]")
except ImportError:
    print("Could not import heatmap4kmers package")


# Import sample_file 
x = read_file(filename = r"example_data\example_kmeRs_matrix.csv")

# Prepare the Quick HeatMap Demo

# Standard
#kmers_heatmap(file_dataframe = x, show_legend = False)

# Categorised
#kmers_heatmap(file_dataframe = x, cmap = plt.cm.get_cmap('Blues', 10))

# RdBu positive vs. negative values
kmers_heatmap(file_dataframe = x[x.columns.difference(["score_total"])], cmap="RdBu")

