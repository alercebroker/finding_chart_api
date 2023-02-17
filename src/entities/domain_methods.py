import numpy as np
import PIL.ImageOps
from src.entities.figure_model import FigureModel
from astropy.coordinates import ICRS
from astropy import units as u
from astropy.time import Time
from src.use_cases.interfaces.object_interface import IObjectRepo
from src.use_cases.interfaces.image_interface import IImageRepo


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


def img_to_np_array(img):
    img = PIL.ImageOps.invert(img)
    img = np.asarray(img)

    return img


def get_ICRS_coords(stats):
    coords = ICRS(stats.meanra * u.degree, stats.meandec * u.degree)
    ra = coords.ra.to_string(u.hour)
    dec = coords.dec.to_string()
    return ra, dec


def format_first_and_last_detection(stats):
    stats["first_detection"] = Time(stats["firstmjd"], format="mjd")
    stats["first_detection"].format = "datetime"
    stats["last_detection"] = Time(stats["lastmjd"], format="mjd")
    stats["last_detection"].format = "datetime"


def get_chart_image(img, stats, size):
    img_array = img_to_np_array(img)
    model = FigureModel()
    fig, axes = model.create_figure(img)
    fig = model.add_figure_text(fig, axes, stats, size)
    img_str = model.fig_img_to_string(fig)
    return img_str
