import pandas as pd
d1={'Name':['don','vems','gopi','idiot'],'country':['india','USA','UK','canada']}
df1=pd.DataFrame(d1)
print(df1)
df2=pd.DataFrame({'ID':[1,2,3,4],'Name':['don','idiot','pavan','ajay']})
print(df2)
df_merged=df1.merge(df2,how='right',on=df2['ID'])
print(df_merged)