# This is another example of profiling for the methods within the code that is done a little differently. Not
# a good example of coding with magic strings but focus on the profile and time example.

# This file will be evaluated as a complete file and profiler run from the command line in the root dir of the file
# This will write stats to a stat file in same directory
# py -m cProfile -o profile_training3.stats profile_training3.py
# This will read the stats file in that directory
# py -m pstats profile_training3.stats

import pstats
import numpy as np
import pandas as pd
import cProfile as profile
import io
from pstats import SortKey
import re
import csv

# Configuration
pd.set_option("display.precision", 1)
# Don't wrap repr(DataFrame) across additional lines
pd.set_option("display.expand_frame_repr", False)
# Set max rows displayed in output to 25
pd.set_option("display.max_rows", 100)
# Set max columns
pd.set_option("display.max_columns", None)

# First test function
def combine_columns(df_input):
    df = df_input
    df = df.reset_index()

    df["amount"] = ""
    for index in range(len(df)):
        unit = df.iloc[index,4]
        #print(unit)
        if 'Metric tons,  thousand' in unit:
            df.iloc[index, 8] = 'test'
        elif 'Terajoules' in unit:
            df.iloc[index, 8] = 'unit'
        elif 'Kilowatts, thousand' in unit:
            df.iloc[index, 8] = 'Kilowatts'
        elif 'Kilowatt-hours, million' in unit:
            df.iloc[index, 8] = 'KWH'
        elif 'Cubic metres, thousand' in unit:
            df.iloc[index, 8] = 'CM'
        elif 'Metric Tons' in unit:
            df.iloc[index, 8] = 'Metric Tons'
        else:
            df.iloc[index, 8] = 'catch all'
    return df

# Second test function
def combine_columns1(df_input):
    df = df_input
    df = df.reset_index()
    df["amount"] = ""
    for index in range(len(df)):
        unit = df.iloc[index,4]
        df.iloc[index, 8] = switch_unit(unit)
    return df

# Function called by the second test function to look up values
def switch_unit(unit):
    unit_value = {
        #case 1
        "Metric tons,  thousand": "test",
        "Terajoules": "unit",
        "Kilowatts, thousand": "Kilowatts",
        "Kilowatt-hours, million": "KWH",
        "Cubic metres, thousand": "CM",
        "Metric Tons": "Metric Tons"
    }

    return unit_value.get(unit, "catch all")


# Read the csv file All Energy Statistics retrieved from kaggle.com UNdata is the reference for Machine Learning datasets
df = pd.read_csv('all_energy_statistics.csv');

df_combined = combine_columns(df)
df_combined1 = combine_columns1(df)


# If you uncomment these, it will display the data in the dataframes
#print(df_combined)
#print(df_combined1)





