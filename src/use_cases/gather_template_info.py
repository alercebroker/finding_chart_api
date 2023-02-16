from src.entities.domain_methods import (
    get_chart_image,
    get_object_stats,
    get_gray_img,
    get_ICRS_coords,
    format_first_and_last_detection,
)

from src.interface_adapters.controllers.parser import RequestDto


def gather_template_info(request_dto: RequestDto):

    info_dict = {}

    stats = get_object_stats(
        request_dto.object_repo, request_dto.api, request_dto.oid, "pandas"
    )

    img = get_gray_img(
        request_dto.img_repo,
        request_dto.PANSTARR_FILE_PATH,
        request_dto.PANSTARR_CUTOUT_PATH,
        ra=stats.meanra,
        dec=stats.meandec,
        size=request_dto.size,
        output_size=701,
    )
    img_str = get_chart_image(img, stats, request_dto.size)
    ra, dec = get_ICRS_coords(stats)
    format_first_and_last_detection(stats)

    info_dict["ra"] = ra
    info_dict["dec"] = dec
    info_dict["oid"] = request_dto.oid
    info_dict["stats"] = stats
    info_dict["img_str"] = img_str

    return info_dict
