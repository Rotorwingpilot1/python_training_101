import pandas as pd
import cProfile as profile
import pstats

# Configuration
pd.set_option("display.precision", 1)
# Don't wrap repr(DataFrame) across additional lines
pd.set_option("display.expand_frame_repr", False)
# Set max rows displayed in output to 25
pd.set_option("display.max_rows", 100)
# Set max columns
pd.set_option("display.max_columns", None)

# Create a profile object
prof = profile.Profile()
prof.enable()

df = pd.read_csv('all_energy_statistics.csv');

df.info()

#print(df)
df.info()

def print_df(df):
    df.to_csv('output.zip', index=False)

print_df(df)

# Disable the profiler
prof.disable()

# Print profile output
stats = pstats.Stats(prof).strip_dirs().sort_stats("cumtime")
# Print top 10 rows
stats.print_stats(10)
