from PIL import Image
import filecmp
import os
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
from unittest import mock, TestCase
from results_figure_model import (
    img_test1,
    result_figure_test1,
    fig_test2,
    axes_test2,
    size_test2,
    stats_test2,
    result_figure_test2,
    figure_test3,
    result_test3,
)
import pandas as pd
from src.entities.figure_model import FigureModel

model = FigureModel()


class TestService(TestCase):
    def test_create_figure(self):
        result_fig, result_axes = model.create_figure(img_test1)
        result_fig.savefig("result_temporal.png")
        self.assertTrue(
            filecmp.cmp(
                "result_temporal.png",
                result_figure_test1,
            )
        )
        os.remove("result_temporal.png")

    def test_add_figure_text(self):
        result = model.add_figure_text(fig_test2, axes_test2, stats_test2, size_test2)
        result.savefig("result_temporal.png")
        self.assertTrue(
            filecmp.cmp(
                "result_temporal.png",
                result_figure_test2,
            )
        )
        os.remove("result_temporal.png")

    # listo
    def test_fig_img_to_string(self):
        result = model.fig_img_to_string(figure_test3)
        self.assertEqual(result, result_test3)
