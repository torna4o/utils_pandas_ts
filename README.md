[![Project Status: Active - The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/)
# utils_pandas_ts for knowing what are you dealing while working with a Pandas.Series object
Utility functions for pandas time series data, currently chunk_sizer calculates NA and valid number chunks in a timeseries object, and also gives total number of NA and valid number rows.

Currently, pdts_utils.py code includes a 

chunk_sizer function:
  - Takes a Pandas.Series() object, such as a column from a time series dataframe.
  - It calculates number of NaN elements and valid elements in a given column.
  - It also counts the number of continuous NaN or valid chunks in the series.
  - Returns the chunk list where it records all chunks consecutively with their sizes
  - [Optional] endtrim True removes the last chunk in the series and return it, in case the last of the series is NaN.

valid_chunk function:
  - Takes a Pandas.Series() object, such as a column from a time series dataframe.
  - Calculates number of valid elements in a given column
  - Provides the length of the longest valid chunk
  - Provides histogram of the valid chunk sizes
  - Returns the chunk list of the valid chunk sizes in their order

nan_chunk function:
  - This function mirrors valid_chunk function to the NaN chunks.
