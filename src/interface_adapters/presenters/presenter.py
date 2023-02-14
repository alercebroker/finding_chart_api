from fastapi.templating import Jinja2Templates


def get_chart_template(TEMPLATES_PATH, request, ra, dec, oid, candid, stats, img_str):

    templates = Jinja2Templates(directory=TEMPLATES_PATH)

    return templates.TemplateResponse(
        "template.html",
        {
            "request": request,
            "ra": ra,
            "dec": dec,
            "oid": oid,
            "candid": candid,
            "stats": stats,
            "panstarrs_image": img_str,
        },
    )
