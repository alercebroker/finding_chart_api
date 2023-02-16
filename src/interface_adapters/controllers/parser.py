from src.entities.dtos import RequestDto


def parse_controller_info_to_dto(
    object_repo, api, oid, img_repo, PANSTARR_FILE_PATH, PANSTARR_CUTOUT_PATH, size
):
    return RequestDto(
        object_repo, api, oid, img_repo, PANSTARR_FILE_PATH, PANSTARR_CUTOUT_PATH, size
    )
