#%%
import pandas as pd
from pandas import Series,DataFrame

#Series
series_sample = pd.Series([10,20,30,40,50])

# print(series_sample)

#Index
series_index_sample = pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])

# print(series_index_sample)

print('データの値：',series_index_sample.values)
print('インデックス：',series_index_sample.index)

attri_data1 = {'id':['100','101','102','103','104'],
                'city':['Tokyo','Osaka','Kyoto','Hokkaido','Tokyo'],
                'Birth_year':['1990','1989','1992','1997','1982'],
                'Name':['Hiroshi','Akiko','Yuki','Satoru','Steve']}

attri_data_frame1 = DataFrame(attri_data1)
print(attri_data_frame1)



# %%
