import numpy as np
from PIL import Image
import pandas as pd

img_test1 = Image.open(
    "/home/usuario/Escritorio/proyecto2_alerce/finding_chart_api/tests/img_test1.jpg"
)
img_test1 = img_test1.convert("L")

result_img_test1 = np.loadtxt(
    "/home/usuario/Escritorio/proyecto2_alerce/finding_chart_api/tests/result_img_test1.txt"
)

img_test2 = np.loadtxt(
    "/home/usuario/Escritorio/proyecto2_alerce/finding_chart_api/tests/img_test2.txt"
)
stats_test2 = pd.read_pickle(
    "/home/usuario/Escritorio/proyecto2_alerce/finding_chart_api/tests/stats_test2.pkl"
)
result_figure_test2 = Image.open(
    "/home/usuario/Escritorio/proyecto2_alerce/finding_chart_api/tests/result_figure_test2.png"
)
size_test2 = 1000


result_encode_test3 = {}
result_decode_test3 = {}
figure_test3 = {}
result_fig_img_test3 = {}

result_ra_test4 = {}
result_dec_test4 = {}
stats_test4 = {}
result_coords_test4 = {}
