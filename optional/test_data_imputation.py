import pandas as pd
import numpy as np
import pytest
from pandas.testing import assert_frame_equal
from pandas.testing import assert_series_equal

from scripts.data_processing import impute_mean


def test_impute_mean_one_value():
    data = pd.Series([1.0, np.nan, 3.0])  # 1. Define some input data
    expected = pd.Series([1.0, 2.0, 3.0])  # 2. Define what is expected to happen
    actual = impute_mean(data)  # 3. Run function and record what happens
    assert_series_equal(expected, actual)  # 4. Make sure expected and actual are equal
