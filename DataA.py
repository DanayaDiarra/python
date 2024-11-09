import numpy as np
import pandas as pd

Inc= np.array([2000, 1500, 3001,1982, 7320, 2003,3001,1482, 7320, 3289])
Exp= np.array([200, 150, 300,198, 732, 200,300,198, 732, 200 ])
Inc_no_tax= Inc*0.7
months=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"]
data={"Income":Inc, "Expenses": Exp, "Income_without_tax": Inc_no_tax}
df1=pd.DataFrame(data, index= months)
print(df1)
print("=========================================")
print('\n' "================1st quarter===============")
print(df1.iloc[0:3:])
