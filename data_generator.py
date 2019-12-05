from dataframe_generator import Create
import pandas as pd
import os
df=pd.read_csv('dow30.csv')
symbols=list(df['Symbol'].values)

create=Create()
for i in symbols:
    df=create.create_data(i,'20190919','20190930')
    file_name=i+'.csv'
    df.to_csv(file_name,index=False)