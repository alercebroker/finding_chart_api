import numpy as np
import base64
import matplotlib.pyplot as plt
from io import BytesIO
import PIL.ImageOps
from src.entities.figure_model import FigureModel
from astropy.coordinates import ICRS
from astropy import units as u
from astropy.time import Time
from src.use_cases.interfaces.object_interface import IObjectRepo
from src.use_cases.interfaces.image_interface import IImageRepo
import pandas as pd


def get_object_stats(object_repo: IObjectRepo, api, oid, format):
    return object_repo.get_stats(api, oid, format)


def get_gray_img(
    image_repo_interface: IImageRepo,
    PANSTARR_FILE_PATH,
    PANSTARR_CUTOUT_PATH,
    ra,
    dec,
    size,
    output_size,
):
    return image_repo_interface.get_gray_image(
        PANSTARR_FILE_PATH, PANSTARR_CUTOUT_PATH, ra, dec, size, output_size
    )


# tests esto.
def img_to_np_array(img):
    # img.save("results/original_image.jpg", "JPEG")
    img = PIL.ImageOps.invert(img)
    img = np.asarray(img)
    # np.savetxt("results/result_img_test1.txt", img)
    return img


# tests esto.
def get_figure(img, stats, size):
    # np.savetxt("results/img_test2.txt", img)
    model = FigureModel(img, stats, size)
    fig, axes = model.create_figure()
    fig = model.add_figure_text(fig, axes)
    # fig.savefig("results/result_figure_test2.png")

    # stats.to_pickle("results/stats_test2.pkl")
    return fig


# tests esto con mock de base64 o de bytesIO ¡consultar!
def fig_img_to_string(figure):
    # f = open("figure_test3.txt", "w")
    # print(figure, file=f)
    # f.close()
    buf = BytesIO()
    # f = open("buf.txt", "w")
    # print(buf, file=f)
    # f.close()
    figure.savefig(buf, format="jpg", bbox_inches="tight", transparent=True)
    buf.seek(0)
    im = buf.read()
    img_str = base64.b64encode(im)
    # f = open("encoder_test3.txt", "w")
    # print(img_str, file=f)
    # f.close()
    img_str = base64.b64decode("utf-8")
    # f = open("decoder_test3.txt", "w")
    # print(img_str, file=f)
    # f.close()

    return img_str


# tests esto con mock de ICRS
def get_ICRS_coords(stats):
    coords = ICRS(stats.meanra * u.degree, stats.meandec * u.degree)
    # f = open("result_ICRS_test4.txt", "w")
    # print(coords, file=f)
    # f.close()
    # f = open("stats_test4.txt", "w")
    # print(stats, file=f)
    # f.close()
    ra = coords.ra.to_string(u.hour)
    dec = coords.dec.to_string()
    # f = open("ra_test4.txt", "w")
    # print(ra, file=f)
    # f.close()
    # f = open("dec_test4.txt", "w")
    # print(dec, file=f)
    # f.close()
    return ra, dec


def format_first_and_last_detection(stats):
    stats["first_detection"] = Time(stats["firstmjd"], format="mjd")
    stats["first_detection"].format = "datetime"
    stats["last_detection"] = Time(stats["lastmjd"], format="mjd")
    stats["last_detection"].format = "datetime"


def get_chart_image(img, stats, size):
    img_array = img_to_np_array(img)
    fig = get_figure(img_array, stats, size)
    img_str = fig_img_to_string(fig)

    return img_str
