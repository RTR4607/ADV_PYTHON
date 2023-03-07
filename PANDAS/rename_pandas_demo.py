import pandas as pd
list={'country':['india','USA','Uk','canada','srilanka'],
        'rank':[1,2,3,4,5],
      '%':['82%','89%','65%','75%','70%']}
p=pd.DataFrame(list,index=['a','b','c','d','e'])
d=p.rename(columns={'rank':'ranking'})
print(d)
#print(p.iloc[4:5,[0,1]])
#print(p.iloc[:,[]])
#p.drop(['country'],axis=1,inplace=True)
print(p)