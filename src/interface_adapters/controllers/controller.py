from alerce.core import Alerce
from flask import jsonify
import os
from src.use_cases.services.service import (
    get_chart_image,
    get_object_stats,
    get_gray_img,
    get_ICRS_coords,
    format_first_and_last_detection,
)
from src.interface_adapters.presenters.presenter import get_chart_template
from src.interface_adapters.repos.image_repo import ImageRepo
from src.interface_adapters.repos.object_repo import ObjectRepo

api = Alerce()
img_repo = ImageRepo()
object_repo = ObjectRepo()

PANSTARR_FILE_PATH = "http://ps1images.stsci.edu/cgi-bin/ps1filenames.py"
PANSTARR_CUTOUT_PATH = "http://ps1images.stsci.edu/cgi-bin/fitscut.cgi"


def controller_get_chart(request, params, TEMPLATES_PATH):
    oid = params.oid
    candid = params.candid
    size = 1000

    if candid is None:
        dets = api.query_detections(oid, format="pandas")
        if len(dets) > 0:
            candid = dets[dets.has_stamp].iloc[0].candid
        else:
            return jsonify({"error": "object doesn't have detections"}), 400

    stats = get_object_stats(object_repo, api, oid, "pandas")
    img = get_gray_img(
        img_repo,
        PANSTARR_FILE_PATH,
        PANSTARR_CUTOUT_PATH,
        ra=stats.meanra,
        dec=stats.meandec,
        size=size,
        output_size=701,
    )
    img_str = get_chart_image(img, stats, size)
    ra, dec = get_ICRS_coords(stats)
    format_first_and_last_detection(stats)

    return get_chart_template(
        TEMPLATES_PATH, request, ra, dec, oid, candid, stats, img_str
    )
