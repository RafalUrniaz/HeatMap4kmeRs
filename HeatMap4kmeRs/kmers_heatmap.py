# -*- coding: utf-8 -*-
"""Test module contains specific heatmap functions for HeatMap4kmeRs package"""

# (C) Rafal Urniaz

# Import required modules
import os
import sys

# Data
import numpy as np
import pandas as pd

# Graphics
import matplotlib as mpl
import matplotlib.pyplot as plt

# External
import heatmap4kmers.general_heatmap

# Read Data


def read_file(filename=""):
    """Function reads kmeRs package output

    Function reads csv output from kmeRs package and returns
    file content in a pandas data frame

    Args:
        filename (str): full or abstract file path

    Returns:
        dataframe: file content in a pandas data frame
    """

    if os.path.isfile(filename) and os.access(filename, os.R_OK):
        file_dataframe = pd.read_csv(filename, sep=";", index_col=0)
        file_dataframe = pd.DataFrame(
            file_dataframe.iloc[1:len(file_dataframe.iloc[0])], dtype="float_")
        print("File exists and is readable [-- OK --]")

        # Print first 3 rows
        print(file_dataframe.iloc[0:3, ])

    else:
        print("Either the file is missing or not readable [-- Error --]")
        sys.exit()

    return file_dataframe


# Prepare Data

def prepare_data(file_dataframe):
    """Function separates data frame to axes and data

    Function takes pandas data frame and separates the
    cols and rows names as x and y axis and matrix values

    Args:
        file_dataframe (str): data frame from read_file()

    Returns:
        list: list of x_labels, y_labels, data, respectively
    """
    # x axis labels - columns names
    x_labels = file_dataframe.columns

    # y axis label - rows names
    y_labels = file_dataframe.index

    # data to the heatmap plot
    data = file_dataframe.values

    return [x_labels, y_labels, data]


# Save heatmap in location defined by filename
def save_or_show_heatmap(plt, show=True, file_name=""):
    """Function shows the heatmap or saves it

    Function shows the kmeRs heatmap or saves it
    into the file

    Args:
        plt (str): pyplot returns from kmeRs_heatmap()
        show (bool): if True the plot will be show
        file_name (str): full or abstract file path
            and file name where the plot should be saved

    Returns:
        bool: True if successful
    """
    # Show = True
    try:
        if show is True:
            plt.savefig(file_name)
        if show is False:
            plt.show()
        return True
    except:
        return False


def kmers_heatmap(file_dataframe, show_values=False, cmap="viridis",
                  title="Example GATTACA HeatMap", title_alignment="Bottom",
                  show_legend=True, legend_label="Similarity Score",
                  save_file=False, file_name="Figure_1"):
    """Function generates heatmap

    Function generates heatmap with predefined kmeRs style values,
    some parameters can be specified by the user

    Args:
        file_dataframe (str): result of prepare_data function
        show_values (bool): if True values lables will be vivisble on the graph
        cmap (str): matlab color map style, 'viridis' by default
            more at
            http://matplotlib.org/examples/color/colormaps_reference.html
        title (str): graph title
        title_alignment (str): graph title location; 'Bottom' or 'Top'
            available
        show_legend (bool): if True the legend is visible on the graph
        legend_label (str): legend tittle
        save_file (bool): if True the file will be save to name given by
            file_name variable
        file_name (str): full or abstract file path

    Returns:
        bool: True if successful
    """
    try:
        x = prepare_data(file_dataframe)

        x_labels = x[0]
        y_labels = x[1]
        data = x[2]

# Prepare HeatMap

    # matplotlib.style.use("classic") # ['dark_background']

        fig, ax = plt.subplots()
        im = ax.imshow(data, cmap=cmap)

# -- Create colorbar / legend --
        if show_legend is True:
            cbar = ax.figure.colorbar(im, ax=ax)
            cbar.ax.set_ylabel(legend_label, rotation=-90, va="bottom")

# -- Lablels --

    # Show all ticks
        ax.set_xticks(np.arange(len(x_labels)))
        ax.set_yticks(np.arange(len(y_labels)))

    # Label with the respective list entries
        ax.set_xticklabels(x_labels)
        ax.set_yticklabels(y_labels)

    # Rotate 45 degrees the labels and set their alignment
        plt.setp(ax.get_xticklabels(), rotation=45,
                 ha="right", rotation_mode="anchor")

# -- Title --
        if title_alignment == "Bottom":
            ax.set_xlabel(title)
        # Let the horizontal axes labeling appear on top.
            ax.tick_params(top=True, bottom=False,
                           labeltop=True, labelbottom=False)
        # Rotate the tick labels and set their alignment.
            plt.setp(ax.get_xticklabels(), rotation=-30,
                     ha="right", rotation_mode="anchor")
        else:
            ax.set_title(title)
            # ax.tick_params(top=False, bottom=True, labeltop=False,
            # labelbottom=True)

    # Loop over data dimensions and create text annotations.
        if show_values is True:
            for i in range(len(y_labels)):
                for j in range(len(x_labels)):
                    ax.text(j, i, data[i, j], ha="center",
                            va="center", color="w")

        fig.tight_layout()

# Save or show the plot

        save_or_show_heatmap(plt, save_file, file_name)
        return True

    except:
        return False
