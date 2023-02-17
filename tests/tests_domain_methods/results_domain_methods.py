import numpy as np
from PIL import Image
import pandas as pd
from astropy.coordinates import SkyCoord
import astropy.units as u
import os


img_test1 = Image.open(
    os.path.join(os.getcwd(), "tests/tests_domain_methods/test1/img_test1.jpg")
)
img_test1 = img_test1.convert("L")
# salida
result_img_test1 = np.loadtxt(
    os.path.join(os.getcwd(), "./tests/tests_domain_methods/test1/result_img_test1.txt")
)


# entrada
stats_test2 = pd.read_pickle(
    os.path.join(os.getcwd(), "./tests/tests_domain_methods/test2/stats_test2.pkl")
)

# mock
ra_coords = 248.9439027625 * u.deg
dec_coords = 71.687537278125 * u.deg
result_coords_test2 = SkyCoord(ra_coords, dec_coords, frame="icrs")

# salida
result_ra_test2 = "16h35m46.536663s"
result_dec_test2 = "71d41m15.13420125s"
