import numpy as np
from PIL import Image
import pandas as pd
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
import astropy.units as u
import os


img_test1 = Image.open(
    os.path.join(os.getcwd(), "tests/tests_service/test1/img_test1.jpg")
)
img_test1 = img_test1.convert("L")
# salida
result_img_test1 = np.loadtxt(
    os.path.join(os.getcwd(), "./tests/tests_service/test1/result_img_test1.txt")
)
# entrada
img_test2 = np.loadtxt(
    os.path.join(os.getcwd(), "./tests/tests_service/test2/img_test2.txt")
)
stats_test2 = pd.read_pickle(
    os.path.join(os.getcwd(), "./tests/tests_service/test2/stats_test2.pkl")
)
size_test2 = 1000
# salida
result_figure_test2 = os.path.join(
    os.getcwd(), "./tests/tests_service/test2/result_figure_test2.png"
)


# entrada
figure_test3_img = mpimg.imread(
    os.path.join(os.getcwd(), "./tests/tests_service/test3/figure_test3.png")
)
fig, ax = plt.subplots()
figure_test3 = fig


# salida
with open(
    os.path.join(os.getcwd(), "./tests/tests_service/test3/result_test3.txt"),
    "r",
) as f:
    result_test3 = f.read()


# entrada
stats_test4 = pd.read_pickle(
    os.path.join(os.getcwd(), "./tests/tests_service/test4/stats_test4.pkl")
)

# mock
ra_coords = 248.9439027625 * u.deg
dec_coords = 71.687537278125 * u.deg
result_coords_test4 = SkyCoord(ra_coords, dec_coords, frame="icrs")

# salida
result_ra_test4 = "16h35m46.536663s"
result_dec_test4 = "71d41m15.13420125s"
