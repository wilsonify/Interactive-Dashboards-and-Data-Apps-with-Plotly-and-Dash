"""

Chapter 4 - Data Manipulation and Preparation, Paving the Way to `Plotly Express`

* Understanding long format (tidy) data
* Understanding the role of data manipulation skills
* Learning Plotly Express

"""
import os

import pandas as pd

pd.options.display.max_columns = None
os.listdir('../../data/')

# ## Series

series = pd.read_csv('../../data/PovStatsSeries.csv')
print(series.shape)
series.head()

series['Topic'].value_counts()

series['Short definition'].notna().apply(['sum', 'mean'])

series['Unit of measure'].value_counts(dropna=False)

result_series = (
    series.groupby('Topic')['Limitations and exceptions']
    .agg(['count', pd.Series.nunique])
    .style.set_caption('Limitations and Exceptions')
)
