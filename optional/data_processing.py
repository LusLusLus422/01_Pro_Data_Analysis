import pandas as pd
import numpy as np


## data imputation


def impute_mean(series: pd.Series) -> pd.Series:
    """Filling missing values with the average of the series.

    Args:
        series (pd.Series): input series

    Returns:
        pd.Series: new series with 0 and 1
    """
    mean_val = series.mean()
    return series.fillna(mean_val)


# data transformation and feature generation


def is_greater_than_average(series: pd.Series) -> pd.Series:
    """For values smaller than average in the series return 0, for greater than average return 1.

    Args:
        series (pd.Series): input series

    Returns:
        pd.Series: new series with 0 and 1
    """
    avg = series.mean()
    new_series = [0 if x <= avg else 1 for x in series]
    # return new_series   wrong but it would work with dataframes
    return pd.Series(new_series, dtype="int64")
