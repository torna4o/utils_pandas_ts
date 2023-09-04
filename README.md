[![Project Status: Active - The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/)
# utils_pandas_ts for knowing what are you dealing while working with a Pandas.Series object
Utility functions for pandas time series data, currently chunk_sizer calculates NA and valid number chunks in a timeseries object, and also gives total number of NA and valid number rows.

Currently, pdts_utils.py code includes a chunk_sizer function. This function:
  - Takes a Pandas.Series() object, such as a column from a time series dataframe.
  - It calculates number of NaN elements and valid elements in given column.
  - It also counts the number of continuous NaN or valid chunks in the series.
