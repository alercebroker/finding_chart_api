from unittest import mock, TestCase
from results_domain_methods import (
    img_test1,
    result_img_test1,
    result_ra_test2,
    result_dec_test2,
    stats_test2,
    result_coords_test2,
)
from src.entities.domain_methods import img_to_np_array, get_ICRS_coords

import pandas as pd


class TestService(TestCase):
    def test_img_to_np_array(self):
        result = img_to_np_array(img_test1)
        self.assertEqual(result.tolist(), result_img_test1.tolist())

    @mock.patch("src.entities.domain_methods.ICRS")
    def test_get_ICRS_coords(self, ICRS_mock):
        ICRS_mock.return_value = result_coords_test2
        result_ra, result_dec = get_ICRS_coords(stats_test2)
        self.assertEqual((result_ra, result_dec), (result_ra_test2, result_dec_test2))
