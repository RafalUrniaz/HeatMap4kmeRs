# -*- coding: utf-8 -*- 
"""Test script module for HeatMap4kmeRs package

Test module demonstrates the example charts for kmeRs package
and checks the package integrity

"""
# (C) Rafal Urniaz

# Import modules

try:
    import heatmap4kmers.kmers_heatmap as hmk

    # Graphics
    import matplotlib.pyplot as plt

    # Import matplotlib_heatmap_functions

    print("import: [-- OK --]")
except ImportError:
    print("Could not import heatmap4kmers package [-- Error --]")


if __name__ == '__main__':

    # --- Import sample_file

    x = hmk.read_file(filename=r"example_kmeRs_matrix.csv")
    print("Load demo dataframe [-- OK --]")

    # --- Prepare Quick HeatMap Demo
    try:
        # Standard
        hmk.kmers_heatmap(file_dataframe=x, show_legend=False,
                          save_file=True, file_name="Figure_1.png")
        print("Save demo plot as Figure_1.png [-- OK --]")

        # Categorised
        hmk.kmers_heatmap(file_dataframe=x, cmap=plt.cm.get_cmap(
            'Blues', 10), save_file=True, file_name="Figure_2.png")
        print("Save demo plot as Figure_2.png [-- OK --]")

        # RdBu positive vs. negative values
        hmk.kmers_heatmap(file_dataframe=x[x.columns.difference(
            ["score_total"])], cmap="RdBu", save_file=True,
            file_name="Figure_3.png")
        print("Save demo plot as Figure_3.png [-- OK --]")
    except (RuntimeError, TypeError, NameError):
        print("Test not pass [-- Error --]")
