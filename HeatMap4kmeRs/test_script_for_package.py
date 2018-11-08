# (C) Rafal Urniaz

# Test functions in heatmap4kmers package
# Import modules

try:
    from heatmap import kmeRs_heatmap
    from heatmap import quick_kmeRs_heatmap
    from heatmap import read_file
    print("import: [-- OK --]")
except ImportError:
    print("Could not import heatmap4kmers package")


# Import sample_file 
x = read_file(filename = r"example_data\example_kmeRs_matrix.csv")

# Prepare the Quick HeatMap
quick_kmeRs_heatmap(file_dataframe = x)

kmeRs_heatmap(file_dataframe = x)
