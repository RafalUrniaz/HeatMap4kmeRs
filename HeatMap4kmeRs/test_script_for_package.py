# (C) Rafal Urniaz

# Test functions in heatmap4kmers package
# Import modules

try:
    from heatmap import heatmap
    from heatmap import read_file
    print("import: [-- OK --]")
except ImportError:
    print("Could not import heatmap4kmers package")


# Import / test sample file 

x = read_file()
print(x)

# Prepare the HeatMap

x = heatmap()
print(x)
