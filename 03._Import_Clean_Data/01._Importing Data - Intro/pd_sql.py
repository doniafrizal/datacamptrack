#%%

import sqlite3
from pathlib import Path
#%%

import pandas as pd

#%%
file = str(Path().joinpath('data', 'Chinook.sqlite'))
conn = sqlite3.connect(file)

#%%

df = pd.read_sql_query('select * from Employee', conn)

#%%

df.head()

#%%
