import os
import pandas as pd

df = pd.DataFrame()

for f in ['academicsrecord.xlsx', 'academicsrecord.xlsx']:
    data = pd.read_excel(f, 'Sheet1')
    df = df.append(data)

df.to_excel("merged.xlsx")
