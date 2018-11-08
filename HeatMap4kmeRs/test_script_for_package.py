# (C) Rafal Urniaz

# Test functions in heatmap4kmers package
# Import modules

try:
    from heatmap import heatmap
    from heatmap import read_file
    print("import: [-- OK --]")
except ImportError:
    print("Could not import heatmap4kmers package")


# Import sample_file 
x = read_file(filename = r"example_data\example_kmeRs_matrix.csv")


# Prepare the HeatMap
x = heatmap(file_dataframe = x)
print(x)
