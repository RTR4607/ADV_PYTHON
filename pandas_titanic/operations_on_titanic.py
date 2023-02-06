import pandas as pd
data=pd.read_csv('../data/tested.csv') # load dataset by using read_csv
print(data)
print(data.shape) # to print no.of rows and columns
print(data.isna().sum()) # isna() functions to find number of fields not assign a value
data.drop(['Cabin'],axis=1,inplace=True) # To delete a particular column or row in the dataset
data.fillna(method='ffill',inplace=True) # to fill emptyt cell with zeros
data.fillna(0)  # to fill emptyt cell with zeros
print(data.isna().any())
print(data['Embarked'])# it categorize the data set to groups
data['Survived']=data['Survived'].map({1:'yes',0:'no'})
print(pd.crosstab(index=data['Sex'],columns=data['Survived']))
#print(data)
print(data.sort_values(by=['PassengerId'],ascending=True))
