from alerce.core import Alerce
from flask import jsonify
from src.interface_adapters.controllers.parser import parse_controller_info_to_dto
from src.interface_adapters.presenters.presenter import get_chart_template
from src.interface_adapters.repos.image_repo import ImageRepo
from src.interface_adapters.repos.object_repo import ObjectRepo
from src.use_cases.gather_template_info import gather_template_info

api = Alerce()
img_repo = ImageRepo()
object_repo = ObjectRepo()

PANSTARR_FILE_PATH = "http://ps1images.stsci.edu/cgi-bin/ps1filenames.py"
PANSTARR_CUTOUT_PATH = "http://ps1images.stsci.edu/cgi-bin/fitscut.cgi"


def controller_get_chart(request, logo_path):
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

    request_dto = parse_controller_info_to_dto(oid, size)

    info_dict = gather_template_info(
        request_dto,
        object_repo,
        img_repo,
        api,
        PANSTARR_FILE_PATH,
        PANSTARR_CUTOUT_PATH,
    )

    info_dict["candid"] = candid

    return get_chart_template(info_dict)
