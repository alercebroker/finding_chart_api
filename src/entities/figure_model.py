import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64


class FigureModel:
    def __init__(self):
        self.color = "blue"

    def create_figure(self, img):
        fig, axes = plt.subplots(1, figsize=(9, 9))
        axes.matshow(img, cmap="Greys_r", interpolation="nearest")
        alpha = 0.3
        # Adding cross
        #              --------------------modelo---------------------
        axes.plot([0, 300], [351, 351], c=self.color, alpha=alpha)
        axes.plot([701, 401], [351, 351], c=self.color, alpha=alpha)
        axes.plot([351, 351], [0, 300], c=self.color, alpha=alpha)
        axes.plot([351, 351], [701, 401], c=self.color, alpha=alpha)

        axes.arrow(701 - 30, 701 - 10, 0, -50, shape="full", width=3, color=self.color)
        axes.arrow(701 - 30, 701 - 10, -50, 0, shape="full", width=3, color=self.color)
        axes.text(701 - 110, 701 - 5, "E", color=self.color)
        axes.text(701 - 34, 701 - 80, "N", color=self.color)
        return fig, axes

    def add_figure_text(self, fig, axes, stats, size):
        # Text
        string = "PanSTARRS DR1\nra: {} dec: {}\nscale: 0.25 arcsec/pix\nfield size: {} arcsec".format(
            np.round(stats.meanra, 5),
            np.round(stats.meandec, 5),
            size * 0.25,
        )
        axes.text(
            0.02,
            0.98,
            string,
            color=self.color,
            transform=axes.transAxes,
            fontsize=9,
            verticalalignment="top",
        )
        axes.axis("off")
        return fig

    def fig_img_to_string(self, figure):
        buf = BytesIO()
        figure.savefig(buf, format="jpg", bbox_inches="tight", transparent=True)
        buf.seek(0)
        im = buf.read()
        img_str = base64.b64encode(im).decode("utf-8")

        return img_str
