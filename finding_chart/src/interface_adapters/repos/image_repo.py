from __future__ import print_function
from finding_chart.src.use_cases.interfaces.image_interface import IImageRepo
import numpy
from astropy.table import Table
import requests
from PIL import Image
from io import BytesIO


class ImageRepo(IImageRepo):
    def getimages(self, ra, dec, size=240, filters="grizy"):
        """Query ps1filenames.py service to get a list of images

        ra, dec = position in degrees
        size = image size in pixels (0.25 arcsec/pixel)
        filters = string with filters to include
        Returns a table with the results
        """
        url = (
            "{self.PANSTARR_FILE_PATH}?ra={ra}&dec={dec}&size={size}&format=fits"
            "&filters={filters}"
        ).format(**locals())
        table = Table.read(url, format="ascii")
        return table

    def geturl(
        self,
        ra,
        dec,
        size=240,
        output_size=None,
        filters="grizy",
        format="jpg",
        color=False,
    ):
        """Get URL for images in the table

        ra, dec = position in degrees
        size = extracted image size in pixels (0.25 arcsec/pixel)
        output_size = output (display) image size in pixels (default = size).
                    output_size has no effect for fits format images.
        filters = string with filters to include
        format = data format (options are "jpg", "png" or "fits")
        color = if True, creates a color image (only for jpg or png format).
                Default is return a list of URLs for single-filter grayscale images.
        Returns a string with the URL
        """

        if color and format == "fits":
            raise ValueError("color images are available only for jpg or png formats")
        if format not in ("jpg", "png", "fits"):
            raise ValueError("format must be one of jpg, png, fits")
        table = self.getimages(ra, dec, size=size, filters=filters)
        url = (
            "{self.PANSTARR_CUTOUT_PATH}?ra={ra}&dec={dec}&size={size}&format={format}"
        ).format(**locals())
        if output_size:
            url = url + "&output_size={}".format(output_size)
        # sort filters from red to blue
        flist = ["yzirg".find(x) for x in table["filter"]]
        table = table[numpy.argsort(flist)]
        if color:
            if len(table) > 3:
                # pick 3 filters
                table = table[[0, len(table) // 2, len(table) - 1]]
            for i, param in enumerate(["red", "green", "blue"]):
                url = url + "&{}={}".format(param, table["filename"][i])
        else:
            urlbase = url + "&red="
            url = []
            for filename in table["filename"]:
                url.append(urlbase + filename)
        return url

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
        """Get grayscale image at a sky position

        ra, dec = position in degrees
        size = extracted image size in pixels (0.25 arcsec/pixel)
        output_size = output (display) image size in pixels (default = size).
                      output_size has no effect for fits format images.
        filter = string with filter to extract (one of grizy)
        format = data format (options are "jpg", "png")
        Returns the image
        """
        self.PANSTARR_FILE_PATH = PANSTARR_FILE_PATH
        self.PANSTARR_CUTOUT_PATH = PANSTARR_CUTOUT_PATH

        if format not in ("jpg", "png"):
            raise ValueError("format must be jpg or png")
        if filter not in list("grizy"):
            raise ValueError("filter must be one of grizy")
        url = self.geturl(
            ra, dec, size=size, filters=filter, output_size=output_size, format=format
        )
        r = requests.get(url[0])
        im = Image.open(BytesIO(r.content))
        return im
