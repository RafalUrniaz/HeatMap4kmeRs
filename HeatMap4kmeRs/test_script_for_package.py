# (C) Rafal Urniaz

# Test functions in heatmap4kmers package
# Import modules

try:
    from heat_map import heat_map
    print("import: [-- OK --]")
except ImportError:
    print("Could not import heatmap4kmers package")


# Import / test sample file 


# Prepare the HeatMap

x = heat_map()
print(x)
