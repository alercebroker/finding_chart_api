from flask import render_template


def get_fig_template(ra, dec, oid, candid, logo_path, stats, img_str):
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
