import pandas as pd 
import numpy as np
df = pd.DataFrame([['A', 'B', 2], ['B', 'A', 2], ['C','A', 5]], columns= ['Bor', 'Lend', 'Amt'])
print(df)
df_add = df.copy()
df_add['Add_Amt'] = -1*df['Amt']
df_add['Lend_Amt'] = df['Amt']

df_lend = df_add[['Lend', 'Lend_Amt']].copy()
df_bor = df_add[['Bor', 'Add_Amt']].copy()

df_pos = df_lend.groupby('Lend').agg({'Lend_Amt':'sum'}).reset_index().rename({'Lend_Amt':'Lend_Amt_total'})
df_neg = df_bor.groupby('Bor').agg({'Add_Amt':'sum'}).reset_index().rename({'Add_Amt':'Add_Amt_total'})

df_all = pd.merge(df_neg, df_pos,left_on= 'Bor', right_on = 'Lend',how= 'outer')

df_all = df_all[['Bor', 'Add_Amt', 'Lend_Amt']]
df_all=df_all.replace(np.nan,0)
df_all['net_value'] = df_all['Add_Amt']+ df_all['Lend_Amt']

print(df_all)

df_all_net = df_all[['Bor', 'net_value']]

df_all_net = df_all_net.sort_values([ 'net_value','Bor',] ,ascending= (True, True))
print(df_all_net)