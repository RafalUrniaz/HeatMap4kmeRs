# (C) Rafal Urniaz
#  

# Import required modules
import os, csv, sys

# Data 
import numpy as np
import pandas as pd

# Graphics 
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# External
import general_heatmap_functions


def read_file(filename = ""):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Arguments:
        data       : A 2D numpy array of shape (N,M)
        row_labels : A list or array of length N with the labels
                     for the rows
        col_labels : A list or array of length M with the labels
                     for the columns
    Optional arguments:
        ax         : A matplotlib.axes.Axes instance to which the heatmap
                     is plotted. If not provided, use current axes or
                     create a new one.
        cbar_kw    : A dictionary with arguments to
                     :meth:`matplotlib.Figure.colorbar`.
        cbarlabel  : The label for the colorbar
    All other arguments are directly passed on to the imshow call.
    """

    if os.path.isfile(filename) and os.access(filename, os.R_OK):
        file_dataframe = pd.read_csv(filename, sep = ";", index_col = 0)
        file_dataframe = pd.DataFrame(file_dataframe.iloc[1:len(file_dataframe.iloc[0])], dtype = "float_")
        print("File exists and is readable [-- OK --]")

        # Print first 5 rows
        print(file_dataframe.iloc[0:3,])
    
    else:
        print("Either the file is missing or not readable")
        sys.exit()
    
    return file_dataframe


# Prepare data function takes as an argument the read_file() function
# output and returns list of dataframe

def prepare_data(file_dataframe):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Arguments:
        data       : A 2D numpy array of shape (N,M)
        row_labels : A list or array of length N with the labels
                     for the rows
        col_labels : A list or array of length M with the labels
                     for the columns
    Optional arguments:
        ax         : A matplotlib.axes.Axes instance to which the heatmap
                     is plotted. If not provided, use current axes or
                     create a new one.
        cbar_kw    : A dictionary with arguments to
                     :meth:`matplotlib.Figure.colorbar`.
        cbarlabel  : The label for the colorbar
    All other arguments are directly passed on to the imshow call.
    """
    # x axis labels - columns names
    x_labels = file_dataframe.columns

    # y axis label - rows names
    y_labels = file_dataframe.index

    # data to the heatmap plot
    data = file_dataframe.values

    return [x_labels, y_labels, data]


# Save heatmap in location defined by filename 
def save_or_show_heatmap(plt, show = True, file_name = ""):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Arguments:
        data       : A 2D numpy array of shape (N,M)
        row_labels : A list or array of length N with the labels
                     for the rows
        col_labels : A list or array of length M with the labels
                     for the columns
    Optional arguments:
        ax         : A matplotlib.axes.Axes instance to which the heatmap
                     is plotted. If not provided, use current axes or
                     create a new one.
        cbar_kw    : A dictionary with arguments to
                     :meth:`matplotlib.Figure.colorbar`.
        cbarlabel  : The label for the colorbar
    All other arguments are directly passed on to the imshow call.
    """
    # Show = True
    if show == True:
        plt.savefig(file_name)
    if show == False:
        plt.show()
    return ""


def kmeRs_annotated_heatmap(file_dataframe, show_values = False, cmap="viridis", title = "Example GATTACA HeatMap", 
                            title_alignment ="Bottom", show_legend= True, legend_label = "Similarity Score", 
                            save_file = False, file_name = "Figure_1"):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Arguments:
        data       : A 2D numpy array of shape (N,M)
        row_labels : A list or array of length N with the labels
                     for the rows
        col_labels : A list or array of length M with the labels
                     for the columns
    Optional arguments:
        ax         : A matplotlib.axes.Axes instance to which the heatmap
                     is plotted. If not provided, use current axes or
                     create a new one.
        cbar_kw    : A dictionary with arguments to
                     :meth:`matplotlib.Figure.colorbar`.
        cbarlabel  : The label for the colorbar
    All other arguments are directly passed on to the imshow call.
    """

    x = prepare_data(file_dataframe)

    x_labels = x[0]
    y_labels = x[1]
    data = x[2]

# Prepare HeatMap

    #matplotlib.style.use("classic") # ['dark_background']
    plt
    fig, ax = plt.subplots()
    im = ax.imshow(data, cmap = cmap)

# -- Create colorbar / legend --
    if show_legend == True:
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
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",rotation_mode="anchor")

# -- Title --
    if title_alignment == "Bottom":
        ax.set_xlabel(title)
        # Let the horizontal axes labeling appear on top.
        ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)
        # Rotate the tick labels and set their alignment.
        plt.setp(ax.get_xticklabels(), rotation=-30, ha="right", rotation_mode="anchor")
    else:
        ax.set_title(title)
        #ax.tick_params(top=False, bottom=True, labeltop=False, labelbottom=True)

    # Loop over data dimensions and create text annotations.
    if show_values == True:
        for i in range(len(y_labels)):
            for j in range(len(x_labels)):
                ax.text(j, i, data[i, j],ha="center", va="center", color="w")

    fig.tight_layout()

# Save or show the plot

    save_or_show_heatmap(plt, save_file, file_name)

    return "Done!"



# Have colormaps separated into categories:
# http://matplotlib.org/examples/color/colormaps_reference.html