# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 16:02:45 2023

@author: vaish
"""
#loan.csv.xls
import pandas as pd
import numpy as np
df=pd.read_csv('loan.csv.xls')
df

df.dtypes

df.shape 
#(39717, 111)
df.size 
#4408587
df.columns 
    
df.columns.values

df.index 

df.describe()

df['tax_liens']
#display tax_liens column
df['tax_liens'][3]
#0.0
df2=df.rename({'id':'A','member_id':'B'},axis=1)
df2
df2=df.rename({'term':'C','grade':'D'},axis='columns')
df2
df2.columns


df.dtypes['id']
#raise error
df.astype({"id":chr},errors='raise')
#ignore error *check it once
df.astype({'id':chr},errors='ignore')

df['member_id']

df[['id','member_id']]

df[6:]

df['member_id'][9]

#rename
df2=df.rename(columns={"member_id":"MemID"})

#drop
df2=df.drop(0)
df2=df.drop(df.index[1:2])
df1=df.drop(range(0,2)) #it will delete 0 and 1
df1
df2=df.drop(df.columns[0],axis=1)

#iloc & loc
df2=df.iloc[:3,:5]
df2=df.loc[:,["id","member_id","term"]]
df2=df.loc[:,'term']


#-------------------------------------------------------------------------------

#crime_data.csv.xls
import pandas as pd
import numpy as np
df=pd.read_csv('crime_data.csv.xls')
df

df.dtypes

df.shape 
#(50,5)
df.size 
#250
df.columns 

df.columns.values

df.index 

df.describe()

df['Murder']
#display tax_liens column
df['Murder'][3]
#0.0
df2=df.rename({'Rape':'R','Murder':'M'},axis=1)
df2

df2.columns

df.dtypes["Murder"]

df2=df[["Murder","Rape"]]

df2=df[5:]

df['Assault'][10]

df2=df.drop(df.columns[-1],axis=1)

df2=df.iloc[:3,1:]
df2=df.iloc[:,:3]
df2=df.loc[:,['Murder',"Rape","Assault"]]
df2=df.loc[:,"Murder":]



#---------------------------------------------------------------


import pandas as pd
import numpy as np
df=pd.read_csv('bank_data.csv.xls')
df

df.dtypes

df.shape 
#(45211, 32)
df.size 
#1446752
df.columns 

df.columns.values

df.index 

df.describe()

df['balance']
#display tax_liens column
df['balance'][3]
#0.0
df2=df.rename({'age':'a','default':'d'},axis=1)
df2

df2.columns
#rename id ,member_id ,term and grade
df2=df.loc[:,'default':]
df2

df2=df.loc[:,'age':'default']
df2

df2=df.iloc[-1:]
df2

df2=df.iloc[:,1:5]
df2

df2=df.iloc[1:5]
df2

df.describe()

df.dtypes['pdays']

df2=df['balance']

df2=df[['balance','loan','duration']]

df2=df.drop(0)
df2=df.drop(df.columns[0],axis=1)


#----------------------------------------------------------
import pandas as pd
import numpy as np
df=pd.read_csv('Seeds_data.csv.xls')
df

df.index
# RangeIndex(start=0, stop=210, step=1)

df.columns

df.size
#1680

df.shape   
#(210, 8)

#access first 3 rows
df.iloc[:3]

#access col
df.iloc[:,:4]

df2=df.loc[:,["Area","Width",'length']]

df2=df["Area"]

df2=df.rename(columns={"length":"Len"})

df2=df.drop(df.columns[1],axis=1)

#Summary of data basic information about dataframe
df.describe()
df.info()

#select area and perimeter col from given dataframe
#df[["Area","Perimeter"]]
df["Area"]

#program to select row where area are less than 15
df2=df[df["Area"]<15]
df2

#row count
row_cnt=df.shape[0]
row_cnt
#210

#col count
col_cnt=df.shape[1]
col_cnt
#8

#print row where length is between 18-20
df2=df[df['length'].between(3,5)]
df2

df2=df.query("Area==15.26")
df2


df2=df.query("Area!=15.26")
df2


 