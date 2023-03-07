import pandas as pd
class CompareXlSheets():

    def compare(self,sheet1,sheet2,sheet1_name,sheet2_name):
        self.sheet1=sheet1
        self.sheet2=sheet2
        self.sheet1_name=sheet1_name
        self.sheet2_name = sheet2_name
        self.df1=pd.read_excel(self.sheet1,sheet_name=self.sheet1_name)
        self.df2=pd.read_excel(self.sheet2,sheet_name=self.sheet2_name)
        self.df3=self.df1.compare(self.df2)

        print(self.df3)
sheet1_path='C:/Users/user787/PycharmProjects/ADV_PYTHON/data/Arrival_Dates.xlsx'
sheet2_path='C:/Users/user787/PycharmProjects/ADV_PYTHON/data/Arrival_Dates_Final.xlsx'
sheet1_name='Sheet1'
sheet2_name='Sheet1'
obj=CompareXlSheets()
obj.compare(sheet1_path,sheet2_path,sheet1_name,sheet2_name)

