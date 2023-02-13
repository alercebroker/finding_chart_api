from unittest import mock, TestCase
from results_service import (
    img_test1,
    result_img_test1,
    img_test2,
    stats_test2,
    size_test2,
    result_figure_test2,
    result_encode_test3,
    result_decode_test3,
    figure_test3,
    result_fig_img_test3,
    result_ra_test4,
    result_dec_test4,
    stats_test4,
    result_coords_test4,
)
from src.use_cases.services.service import (
    img_to_np_array,
    get_figure,
    fig_img_to_string,
    get_ICRS_coords,
)


class TestService(TestCase):
    def test_img_to_np_array(self):
        result = img_to_np_array(img_test1)
        self.assertEqual(result, result_img_test1)

    def test_get_figure(self):
        result = get_figure(img_test2, stats_test2, size_test2)
        self.assertEqual(result, result_figure_test2)

    @mock.patch("src.use_cases.services.service.base64.encode")
    @mock.patch("src.use_cases.services.service.base64.decode")
    def test_fig_img_to_string(self, decode_mock, encode_mock):
        encode_mock.return_value = result_encode_test3
        decode_mock.return_value = result_decode_test3

        result = fig_img_to_string(figure_test3)
        self.asserEqual(result, result_fig_img_test3)

    @mock.patch("src.use_cases.services.service.ICRS")
    def test_get_ICRS_coords(self, ICRS_mock):
        ICRS_mock.return_value = result_coords_test4
        result_ra, result_dec = get_ICRS_coords(stats_test4)
        self.assertEqual((result_ra, result_dec), (result_ra_test4, result_dec_test4))
