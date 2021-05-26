import pandas as pd
import numpy as np
from scipy.stats import shapiro



"""
Method to compute the Shapiro normality criterion for each column in a dataframe
"""
def shapiro_columns(df, progress = False):

    shapiro_out = []

    count = 0
    for col in df.columns:

        stat, p = shapiro(df[col])

        if (progress & count % 100 == 0):
            print("count " + str(count))
            print("stat, p %s %s" % (stat, p))
            print(df[col])

        count = count + 1
        shapiro_out.append([stat,p])

    shapiro_out_df = pd.DataFrame(shapiro_out, columns=["shapiro_stat", "shapiro_p"], dtype=np.float64)
    if (progress):
        print("done shapiro, shape")
        print(shapiro_out_df.shape)
    shapiro_out_df


def row_sum(df):
    """
    This function takes a pandas data framework and calculates each row's summation, only for numerical
    columns
    Args:
        df: a pandas data framework

    Returns:
        new : new pandas data framework containing the non-numerical columns and a new "row sum" column for row sum
    """
    # select columns that are not numerical
    res = df.select_dtypes(include=[object, bool])
    res =res.assign(**{"row sum": df.sum(axis=1)})
    return res


def row_non_zero_count(df):
    """
    This function counts non-zero numerical values for each row
    Args:
        df: a pandas data framework

    Returns:
        res : new pandas data framework containing the non-numerical columns and a new "row non-zero value count" column for row non-zero
        values count
    """
    # select columns that are not numerical
    res = df.select_dtypes(include=[object, bool])
    # add a new column to res
    res = res.assign(**{"row non-zero value count": df.select_dtypes(include=np.number).astype(bool).sum(axis=1)})
    return res


def col_sum(df):
    """
    This function
    Args:
        df: a pandas data framework

    Returns:
        res: new pandas data framework containing 2 columns. First column - 'column name' is numerical columns' names,
        second column - 'column sum' is the sum of that column.
    """
    # select df numerical column names and convert from series to frame
    res = df.select_dtypes(include=np.number).columns.to_frame(name="column name")
    # sum values column-wise and add them to be the second column
    res['column sum'] = df.select_dtypes(include=np.number).sum(axis=0)
    return res


def col_non_zero_count(df):
    """
    This function counts non-zero numerical values for each column
    Args:
        df: a pandas data framework

    Returns:
        res : new pandas data framework containing 2 columns. First column - 'column name' is numerical columns' names,
        second column - 'column non-zero value count' is the count of non-zero values in that column.
    """
    # select df numerical column names and convert from series to frame
    res = df.select_dtypes(include=np.number).columns.to_frame(name="column name")
    # count non-zero values in column and add them to second column
    res['column non-zero value count'] = df.select_dtypes(include=np.number).astype(bool).sum(axis=0).to_frame(name="column name")
    return res
