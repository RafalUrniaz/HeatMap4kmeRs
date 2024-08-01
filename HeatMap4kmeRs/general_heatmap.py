# -*- coding: utf-8 -*-
"""Test module contains universal heatmap function"""

# (C) Rafal Urniaz,PhD

# Data
import numpy as np

# Graphics
import matplotlib
import matplotlib.pyplot as plt

# General matplotlib HeatMap Functions


def heatmap(data, row_labels, col_labels, cbar_kw, ax=None, cbarlabel="",
            **kwargs):
    """Create a heatmap from a numpy array and two lists of labels

    Extended description of function.

    Args:
        data (arr): A 2D numpy array of shape (N,M)
        row_labels (arr): A list or array of length N with the
            labels for the rows
        col_labels (arr): A list or array of length M with the
            labels for the columns
        ax (str): A matplotlib.axes.Axes instance to which the
            heatmap is plotted. If not provided, use current
            axes or create a new one
        cbar_kw (str): A dictionary with arguments to
            :meth:`matplotlib.Figure.colorbar`

        cbarlabel (str): The label for the colorbar

    Returns:
        plot (im, cbar)
    """

    if not ax:
        ax = plt.gca()

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # We want to show all ticks...
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    # ... and label them with the respective list entries.
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    for spine in ax.spines.items():
        spine.set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


def annotate_heatmap(im, data=None, valfmt="",
                     textcolors=["black", "white"],
                     threshold=None, **textkw):
    """A function to annotate a heatmap

    A function to annotate a heatmap

    Args:
        im (): The AxesImage to be labeled
        data (str): Data used to annotate. If None, the image's data is used.
        valfmt (int): The format of the annotations inside the heatmap.
            This should either use the string format method, e.g.
            "$ {x:.2f}", or be a :class:`matplotlib.ticker.Formatter`.
        textcolors (int): A list or array of two color specifications. The
            first is used for values below a threshold, the second for those
            above.
        threshold (int): Value in data units according to which the colors from
            textcolors are applied. If None (the default) uses the
            middle of the colormap as separation.

    Returns:
        bool: Description of return value

    """

    valfmt = "{x:.2f}"

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[im.norm(data[i, j]) > threshold])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts
