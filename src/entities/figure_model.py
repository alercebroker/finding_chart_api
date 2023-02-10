import matplotlib.pyplot as plt
import numpy as np


class FigureModel:
    def __init__(self, img, stats, size):
        self.img = img
        self.stats = stats
        self.size = size

    def create_figure(self):
        self.fig, self.axes = plt.subplots(1, figsize=(9, 9))
        self.axes.matshow(self.img, cmap="Greys_r", interpolation="nearest")
        self.color = "blue"
        alpha = 0.3
        # Adding cross
        #              --------------------modelo---------------------
        self.axes.plot([0, 300], [351, 351], c=self.color, alpha=alpha)
        self.axes.plot([701, 401], [351, 351], c=self.color, alpha=alpha)
        self.axes.plot([351, 351], [0, 300], c=self.color, alpha=alpha)
        self.axes.plot([351, 351], [701, 401], c=self.color, alpha=alpha)

        self.axes.arrow(
            701 - 30, 701 - 10, 0, -50, shape="full", width=3, color=self.color
        )
        self.axes.arrow(
            701 - 30, 701 - 10, -50, 0, shape="full", width=3, color=self.color
        )
        self.axes.text(701 - 110, 701 - 5, "E", color=self.color)
        self.axes.text(701 - 34, 701 - 80, "N", color=self.color)

    def add_figure_text(self):
        # Text
        string = "PanSTARRS DR1\nra: {} dec: {}\nscale: 0.25 arcsec/pix\nfield size: {} arcsec".format(
            np.round(self.stats.meanra, 5),
            np.round(self.stats.meandec, 5),
            self.size * 0.25,
        )
        self.axes.text(
            0.02,
            0.98,
            string,
            color=self.color,
            transform=self.axes.transAxes,
            fontsize=9,
            verticalalignment="top",
        )
        self.axes.axis("off")

        return self.fig
