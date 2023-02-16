from fastapi.templating import Jinja2Templates


def get_chart_template(TEMPLATES_PATH, request, info_dict):

    templates = Jinja2Templates(directory=TEMPLATES_PATH)

    return templates.TemplateResponse(
        "template.html",
        {
            "request": request,
            "ra": info_dict["ra"],
            "dec": info_dict["dec"],
            "oid": info_dict["oid"],
            "candid": info_dict["candid"],
            "stats": info_dict["stats"],
            "panstarrs_image": info_dict["img_str"],
        },
    )
