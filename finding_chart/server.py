from flask import Flask, request, jsonify, render_template
from alerce.core import Alerce
from .panstarrs import *
from astropy.coordinates import ICRS
from astropy import units as u
from astropy.time import Time

import base64
import PIL.ImageOps
import os
import numpy as np
import matplotlib.pyplot as plt


PANSTARR_FILE_PATH = "http://ps1images.stsci.edu/cgi-bin/ps1filenames.py"
PANSTARR_CUTOUT_PATH = "http://ps1images.stsci.edu/cgi-bin/fitscut.cgi"

STATIC_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "static")
CSS_PATH = [
    os.path.join(STATIC_PATH, "css/template.css"),
    os.path.join(STATIC_PATH, "css/bootstrap.min.css"),
]


app = Flask(__name__, instance_relative_config=True)
api = Alerce()


@app.route("/")
def index():
    return "ALeRCE Finding Chart Generator"


@app.route("/get_chart")
def get_chart():
    oid = request.args.get("oid")
    candid = request.args.get("candid")
    size = request.args.get("size", default=1000)

    if oid is None:
        return jsonify({"error": "Missing oid parameter"}), 400

    if candid is None:
        dets = api.query_detections(oid, format="pandas")
        if len(dets) > 0:
            candid = dets[dets.has_stamp].iloc[0].candid
        else:
            return jsonify({"error": "object doesn't have detections"}), 400

    stats = api.query_objects(oid=oid, format="pandas")
    magstats = api.query_magstats(oid=oid)
    stats = stats.iloc[0]
    stats["mean_magpsf_r"] = magstats[1]["magmean"]
    stats["mean_magpsf_g"] = magstats[0]["magmean"]
    logo_path = os.path.join(STATIC_PATH, "img/logo.png")

    # Getting image
    img = getgrayim(ra=stats.meanra, dec=stats.meandec, size=size, output_size=701)
    img = PIL.ImageOps.invert(img)
    img = np.asarray(img)

    fig, axes = plt.subplots(1, figsize=(9, 9))
    axes.matshow(img, cmap="Greys_r", interpolation="nearest")
    color = "blue"
    alpha = 0.3
    # Adding cross
    axes.plot([0, 300], [351, 351], c=color, alpha=alpha)
    axes.plot([701, 401], [351, 351], c=color, alpha=alpha)
    axes.plot([351, 351], [0, 300], c=color, alpha=alpha)
    axes.plot([351, 351], [701, 401], c=color, alpha=alpha)

    axes.arrow(701 - 30, 701 - 10, 0, -50, shape="full", width=3, color=color)
    axes.arrow(701 - 30, 701 - 10, -50, 0, shape="full", width=3, color=color)
    axes.text(701 - 110, 701 - 5, "E", color=color)
    axes.text(701 - 34, 701 - 80, "N", color=color)

    # Text
    string = "PanSTARRS DR1\nra: {} dec: {}\nscale: 0.25 arcsec/pix\nfield size: {} arcsec".format(
        np.round(stats.meanra, 5), np.round(stats.meandec, 5), size * 0.25
    )
    axes.text(
        0.02,
        0.98,
        string,
        color=color,
        transform=axes.transAxes,
        fontsize=9,
        verticalalignment="top",
    )

    axes.axis("off")

    buf = BytesIO()
    plt.savefig(buf, format="jpg", bbox_inches="tight", transparent=True)
    buf.seek(0)
    im = buf.read()
    img_str = base64.b64encode(im).decode("utf-8")

    plt.cla()
    plt.clf()
    plt.close()

    c = ICRS(stats.meanra * u.degree, stats.meandec * u.degree)
    ra = c.ra.to_string(u.hour)
    dec = c.dec.to_string()
    stats["first_detection"] = Time(stats["firstmjd"], format="mjd")
    stats["first_detection"].format = "datetime"
    stats["last_detection"] = Time(stats["lastmjd"], format="mjd")
    stats["last_detection"].format = "datetime"

    html = render_template(
        "template.html",
        ra=ra,
        dec=dec,
        oid=oid,
        candid=candid,
        logo_path=logo_path,
        stats=stats,
        panstarrs_image=img_str,
    )
    return html, 200


if __name__ == "__main__":
    app.run(debug=True)
