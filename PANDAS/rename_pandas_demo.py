import pandas as pd
list={'counrty':['india','USA','Uk','canada','srilanka'],
        'rank':[1,2,3,4,5],
      '%':['82%','89%','65%','75%','70%']}
p=pd.DataFrame(list)
#d=p.rename(columns={'rank':'ranking'})
print(p.iloc[4:5,[0,1]])
#print(d.loc[d['ranking']>=3])
#p.drop([0,1],axis=0,inplace=True)
print(p)