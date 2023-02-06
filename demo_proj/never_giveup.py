import pandas as pd
import numpy as np
class ReadCSV():
    def create_df(self,path):
        self.path=path
        self.df=pd.DataFrame(self.path)

        #self.df['Total']=self.df['m1']+self.df['m2']+self.df['m3']+self.df['m4']+self.df['m5']
obj=ReadCSV()
obj.create_df("..//data/demo_proj.csv")
'''data=pd.read_csv('../data/demo_proj.csv')
data['Total']=data.iloc[:].sum(axis=1)
data['Avg']=data['Total']/5
data['Rank']=data['Avg'].rank()
data['Pass']=np.where((data['m1']>=35)&(data['m2']>=35)&(data['m3']>=35)&(data['m4']>=35)&(data['m5']>=35),'pass','fail')
#for i in data.iloc[1:2,[2,3,4,5,6]]:
    #data['pass']=((data[i]>='35').replace({True:'pass',False:'Fail'}))#.replace({True:'Pass',False:'fail'})
    #if data.iloc[:,[2,3,4,5,6]]=='pass':
        #data['pass']=((data['pass']=='pass').replace({True:'pass',False:'fail'}))
    #data['Pass']=((data[i]>=35).replace({True:'pass',False:'fail'}))
#data['pass']=(data['Avg']>=35.0).replace({True:'pass',False:'fail'})
print(data.sort_values(by=['Rank']))'''