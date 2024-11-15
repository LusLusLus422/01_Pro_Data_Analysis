import pandas as pd
import numpy as np
from pandas.testing import assert_series_equal
import pytest
from scripts.data_processing import is_greater_than_average


def test_is_greater_than_average():
    input_series = pd.Series([1, 2, 3, 2.5, 4])
    expected_series = pd.Series([0, 0, 1, 0, 1])

    output_series = is_greater_than_average(series=input_series)

    assert_series_equal(output_series, expected_series)


def test_is_greater_than_average_empty():
    input_series = pd.Series([])
    expected_series = pd.Series([], dtype="int64")
    output_series = is_greater_than_average(series=input_series)
    assert_series_equal(output_series, expected_series)


# uncomment this test to see what happens if you have missing values and you don't deal with them before transforming the data
@pytest.mark.skip(reason="it fails")
def test_is_greater_than_average_with_nan():
    input_series = pd.Series([1, 2, np.nan])
    expected_series = pd.Series([0, 1, np.nan])  # or exception
    output_series = is_greater_than_average(series=input_series)
    assert_series_equal(output_series, expected_series)


# test for type
def test_is_greater_than_average_returns_series():
    input_series = pd.Series([1, 2, 3, 2.5, 4])
    output_series = is_greater_than_average(series=input_series)
    assert type(output_series) is pd.core.series.Series
