## Load libraries
import pandas as pd
import numpy as np

# Load a csv file into a pandas dataframe
# The csv location is defined after the first / in the path
df = pd.read_csv(r"/Users/michaelhelvajian/Downloads/Looker Field Usage 2022-09-02T0918.csv")

# Take the "Fields Used" column and split every value at the comma
# The str.split() function applied to the df (dataframe) returns a list of values and the "," is the delimiter
fields = df['Fields Used'].str.split(',')

# Concatenate all values into pandas Series
fields_series = pd.Series(np.concatenate(fields))

# Count each occurrence of each value in the Series and save as a pandas DataFrame with a new index
fields_df = pd.DataFrame(fields_series.value_counts()).reset_index()

# Label columns
fields_df.columns = ['FIELDS_USED', 'COUNT']

# Save as csv
fields_df.to_csv(r"/Users/michaelhelvajian/Downloads/Looker Field Usage Count.csv")
