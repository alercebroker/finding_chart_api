from src.entities.dtos import RequestDto


def parse_controller_info_to_dto(oid, size):
    return RequestDto(oid, size)
