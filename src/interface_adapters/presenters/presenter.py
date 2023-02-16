from flask import render_template


def get_chart_template(info_dict):
    html = render_template(
        "template.html",
        ra=info_dict["ra"],
        dec=info_dict["dec"],
        oid=info_dict["oid"],
        candid=info_dict["candid"],
        stats=info_dict["stats"],
        panstarrs_image=info_dict["img_str"],
    )
    return html, 200
