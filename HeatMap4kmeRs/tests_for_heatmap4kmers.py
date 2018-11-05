# (C) Rafal Urniaz

# Test functions in heatmap4kmers package
# Import modules

try:
    from heatmap4kmers import heatmap4kmers
    print("import: [-- OK --]")
except ImportError:
    print("Could not import heatmap4kmers package")


# Import / test sample file 


# Prepare the HeatMap

x = heatmap4kmers()
print(x)
