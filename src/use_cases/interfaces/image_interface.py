import abc


class IImageRepo(abc.ABC):
    @abc.abstractmethod
    def get_gray_image(
        self,
        PANSTARR_FILE_PATH,
        PANSTARR_CUTOUT_PATH,
        ra,
        dec,
        size=240,
        output_size=None,
        filter="g",
        format="jpg",
    ):
        pass
