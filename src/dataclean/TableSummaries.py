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