# excel-using-python

                       -------------------------------LOSTINCODE---------------------------------------

Problem Statement:

You have a directory of excel files with same format (like same number of columns, same type of columns).

Objective is to merge all the excel files into one large excel file.



SOLUTION:


import os
import pandas as pd

df = pd.DataFrame()

for f in ['academicsrecord.xlsx', 'academicsrecord.xlsx']:
    data = pd.read_excel(f, 'Sheet1')
    df = df.append(data)

df.to_excel("merged.xlsx")





