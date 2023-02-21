import numpy as np
from PIL import Image
import pandas as pd
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
import astropy.units as u
import os

img_test1 = np.loadtxt(
    os.path.join(os.getcwd(), "tests/tests_figure_model/test1/img_test1.txt")
)
result_figure_test1 = os.path.join(
    os.getcwd(), "tests/tests_figure_model/test1/result_figure_test1.png"
)


figure_test2_img = mpimg.imread(
    os.path.join(os.getcwd(), "tests/tests_figure_model/test2/figure_test2.png")
)
fig, ax = plt.subplots()
fig_test2 = fig
axes_test2 = ax
stats_test2 = pd.read_pickle(
    os.path.join(os.getcwd(), "tests/tests_figure_model/test2/stats_test2.pkl")
)
size_test2 = 1000
result_figure_test2 = os.path.join(
    os.getcwd(), "tests/tests_figure_model/test2/result_figure_test2.png"
)


# entrada
figure_test3_img = mpimg.imread(
    os.path.join(os.getcwd(), "tests/tests_figure_model/test3/figure_test3.png")
)
fig, ax = plt.subplots()
figure_test3 = fig


# salida
with open(
    os.path.join(os.getcwd(), "tests/tests_figure_model/test3/result_test3.txt"),
    "r",
) as f:
    result_test3 = f.read()
