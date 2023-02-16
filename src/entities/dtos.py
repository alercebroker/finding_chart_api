class RequestDto:
    def __init__(
        self,
        object_repo,
        api,
        oid,
        img_repo,
        PANSTARR_FILE_PATH,
        PANSTARR_CUTOUT_PATH,
        size,
    ):
        self.object_repo = object_repo
        self.api = api
        self.oid = oid
        self.img_repo = img_repo
        self.PANSTARR_FILE_PATH = PANSTARR_FILE_PATH
        self.PANSTARR_CUTOUT_PATH = PANSTARR_CUTOUT_PATH
        self.size = size
