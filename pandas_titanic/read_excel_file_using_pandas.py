import pandas as pd
data=pd.read_excel("../data/Book1.xlsx",sheet_name='Sheet2')
#print(data)
data2=pd.read_excel("../data/Book1.xlsx",sheet_name='Sheet3')
#print(data2)
#data1=pd.concat([data2,data],axis=1,join='outer')
#print(data1)
print(data.compare(data2))