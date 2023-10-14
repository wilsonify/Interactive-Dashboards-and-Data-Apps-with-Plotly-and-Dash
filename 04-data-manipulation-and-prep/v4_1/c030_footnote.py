"""

Chapter 4 - Data Manipulation and Preparation, Paving the Way to `Plotly Express`

* Understanding long format (tidy) data
* Understanding the role of data manipulation skills
* Learning Plotly Express

"""

import pandas as pd
import plotly.express as px

# ## Footnote

footnote = pd.read_csv('../../data/PovStatsFootNote.csv')
footnote = footnote.drop('Unnamed: 4', axis=1)
footnote['Year'] = footnote['Year'].str[2:].astype(int)
footnote.columns = ['Country Code', 'Series Code', 'year', 'footnote']
print(f"footnote = {footnote}")

