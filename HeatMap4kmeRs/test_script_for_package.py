# (C) Rafal Urniaz

# Test functions in heatmap4kmers package
# Import modules

try:
    from kmeRs_annotated_heatmap import kmeRs_annotated_heatmap
    from kmeRs_annotated_heatmap import read_file
    #import matplotlib_heatmap_functions
    print("import: [-- OK --]")
except ImportError:
    print("Could not import heatmap4kmers package")



# Import sample_file 
x = read_file(filename = r"example_data\example_kmeRs_matrix.csv")

# Prepare the Quick HeatMap
kmeRs_annotated_heatmap(file_dataframe = x)



