import pandas as pd
import numpy as np
from numpy.random import randn




####  series 
# my_data= [10, 20, 30]
# my_labels=['a', 'b', 'c']
# arr=np.array (my_data)
# my_d={'a':10, 'b':20, 'c':30}

# # defining a serie
# print (pd.Series(data= my_data))
# print (pd.Series(data= my_data, index= my_labels))
# print (pd.Series(my_data, my_labels))
# print (pd.Series(arr, my_labels))
# print (pd.Series(my_d))

# # data can be any object, like string or even functions. 
# print (pd.Series(data= my_labels))
# print (pd.Series(data= [sum, print, len]))



# ser1=pd.Series([1,2,3,4,5], [ 'usa', 'belgium', 'iran', 'germany', 'canada'])
# print (ser1)
# ser2=pd.Series([1,2,3,6,7], [ 'usa', 'belgium', 'iran', 'india', 'turkey'])
# print (ser2)

# print(ser1['usa'])

# print (ser1 +ser2)








###### Data Frames (main tool for working with pandas)

# print(np.random.seed(101))
# my_df=pd.DataFrame(randn(5,4), ['a','b','c','d', 'e'], ['w', 'x','y','z'])
# print (my_df)

# print (my_df['w'])  # selecting one column
# print (type(my_df['w'])) 
# print (my_df[['w','y']]) # selecting more columns
# print (type(my_df[['w','y']]))
# print (my_df['w']['a']) # selecting one item in the DataFrame
# print (my_df.loc['a','w']) # selecting one item in the DataFrame
# print (my_df.loc[['a','b'],['w', 'y']]) # selecting subsets


# print (my_df.loc['c'])  # selecting one row
# print (type(my_df.loc['c']))  # selecting one row
# print (my_df.iloc[2])  # selecting one row
# print (type(my_df.iloc[2]))  # selecting one row

# my_df['new']= my_df['y'] + my_df['w']  # to make a new column
# print (my_df)
# my_df.drop ('new', axis=1, inplace=True )  # to remove a column
# # axis 1 for columns and 0 for rows
# # inplace True == apply the changes on the original data frame
# print (my_df)  


# # conditional selection
# bool_df = my_df > 0
# print(bool_df)
# print(my_df[bool_df])
# print(my_df[my_df>0])


# bool_df_w = my_df['w']>0
# print (bool_df_w)
# print (my_df['w'][bool_df_w])

# print (my_df)
# print (my_df[my_df['w']>0]) # filtering whole the data based on the values of column 'W' 
# print (my_df[my_df['w']>0][['y','z']])

# print (my_df [ ( my_df['w']>0 ) & ( my_df['y']>1 ) ] ) # filtering based on AND condition 
# print (my_df [ ( my_df['w']>0 ) | ( my_df['y']>1 ) ] ) # filtering based on OR condition



# # reseting the index
# print(my_df)
# print(my_df.reset_index())
# print(my_df)


# new_ind= 'ca ny wy or co'.split()
# print(new_ind)
# my_df['States']=new_ind
# print(my_df)

# print (my_df.set_index('States'))








# # data frames with multilevel index
# outside = 'G1 G1 G1 G2 G2 G2'.split()
# print ( outside)
# inside = [1, 2, 3, 1, 2, 3]
# hier_index = list (zip(outside,inside))
# print(hier_index)
# hier_index = pd. MultiIndex.from_tuples (hier_index)
# print (hier_index)

# df=pd. DataFrame(randn(6,2),hier_index,['A','B'])
# print(df)

# print( df. index.names)
# df. index.names=['Groups', 'Num'] # naming the indexes
# print( df. index.names)
# print( df)

# print( df.loc['G1'])
# print( df.loc['G1'].loc[1])
# print( df.loc['G2'].loc[2]['B'])

# print( df.xs('G2'))
# print( df.xs(1,level='Num'))









# Missing Data 

# d={'A':[1,2,np.nan],'B':[4,np.nan,np.nan],'C':[7,8,9]}
# df= pd. DataFrame(d)
# print(df)
# print(df.dropna()) # removing missing data
# print(df.dropna(axis=1))
# print(df.dropna(thresh=2)) # number of the missing points
 
# print (df. fillna(value='II')) # replacing the missing data
# print (df['A'].fillna (value=df['A'].mean()))








# groupby 
# data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
# 	'Person':['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
# 	'Sales':[200, 120, 340, 124, 243, 350]}
# df=pd.DataFrame(data)
# print(df)

# bycomp= df.groupby('Company') # group fata by company name
# print(bycomp)
# print (bycomp.sum()) # applying the function (sum) to groups
# print (type(bycomp.sum()))
# print (bycomp.sum().loc['FB'])
# print (bycomp.mean())
# print (bycomp.std()) # standart deviation 
# print (bycomp.count())
# print (bycomp.max()) # this will be applied on Person group
# print (bycomp.min()) # this will be applied on Person group
# print (bycomp.describe())










# # Merging, Joining, and concatenating 
# df1= pd.DataFrame({'A':['A0','A1','A2','A3'],
# 	'B':['B0','B1','B2','B3'],
# 	'C':['C0','C1','C2','C3'],
# 	'D':['D0','D1','D2','D3']},
# 	index=[0,1,2,3])
# df2= pd.DataFrame({'A':['A4','A5','A6','A7'],
# 	'B':['B4','B5','B6','B7'],
# 	'C':['C4','C5','C6','C7'],
# 	'D':['D4','D5','D6','D7']},
# 	index=[4,5,6,7])
# df3= pd.DataFrame({'A':['A8','A9','A10','A11'],
# 	'B':['B8','B9','B10','B11'],
# 	'C':['C8','C9','C10','C11'],
# 	'D':['D8','D9','D10','D11']},
# 	index=[8,9,10,11])

# print (df1)
# print (df2)
# print (df3)

# print (pd.concat([df1,df2,df3])) #concatenating 
# print (pd.concat([df1,df2,df3], axis=1)) #concatenating 


# left=pd.DataFrame({'key':['K0','K1','K2','K3'],
# 	'A':['A0','A1','A2','A3'],
# 	'B':['B0','B1','B2','B3']})
# right=pd.DataFrame({'key':['K0','K1','K2','K3'],
# 	'C':['C0','C1','C2','C3'],
# 	'D':['D0','D1','D2','D3']})
# print(left)
# print(right)

# print(pd.merge(left, right, how='inner', on='key'))  #merging 



# left=pd.DataFrame({'key1':['K0','K0','K1','K2'],
# 	'key2':['K0','K1','K0','K1'],
# 	'A':['A0','A1','A2','A3'],
# 	'B':['B0','B1','B2','B3']})
# right=pd.DataFrame({'key1':['K0','K1','K1','K2'],
# 	'key2':['K0','K0','K0','K0'],
# 	'C':['C0','C1','C2','C3'],
# 	'D':['D0','D1','D2','D3']})
# print(left)
# print(right)
# print(pd.merge(left, right, on=['key1','key2']))  #merging
# print(pd.merge(left, right, how='outer',on=['key1','key2']))  #merging
# print(pd.merge(left, right, how='right',on=['key1','key2']))  #merging
# print(pd.merge(left, right, how='left',on=['key1','key2']))  #merging




# left=pd.DataFrame({'A':['A0','A1','A2','A3'],
# 	'B':['B0','B1','B2','B3']},
# 	index=['K0','K1','K2','K3'])
# right=pd.DataFrame({'C':['C0','C1','C2','C3'],
# 	'D':['D0','D1','D2','D3']},
# 	index=['K0','K2','K3','K4'])
# print(left)
# print(right)

# print (left.join(right))
# print (left.join(right, how='outer'))












######## operations
# df=pd.DataFrame(
# 	{'col1':[1,2,3,4],
# 	'col2':[444,555,666,444],
# 	'col3':['abc','def','ghi','xyz']}
# 	)
# print (df)
   
# print (df['col2'].unique())   # finding all unique values 
# print (df['col2'].nunique())   # number of all unique values 
# print (df['col2'].value_counts())   # how many times values are appeared 
# print (type(df['col2'].value_counts()))   

# print (df[(df['col1']>2) & (df['col2']==444)]) #seletive selection 



# def times2(x):
# 	return x**2
# print (df['col1'])
# print (df['col1'].apply(times2)) # when u want to apply your function on each element 
# print (df['col1'].apply(lambda x: x**2)) # when u want to apply your function on each element 


# print (df['col3'])
# print (df['col3'].apply(len))

# print (df.drop('col1', axis=1))

# print (df.columns)
# print (df.index)

# print( df.sort_values(by='col2'))  #sorting

# print(df. isnull ())   # finding a null value












######## pivot table
# df=pd.DataFrame(
# 	{'A':['foo','foo','foo','bar','bar','bar'],
# 	'B':['one','one','two','two','one','one'],
# 	'C':['x','y','x','y','x','y'],
# 	'D':[1,3,2,5,4,1]}
# 	)
# print (df)
# print(df.pivot_table(values='D',index=['A','B'],columns=['C']))














########## data input and output
'''
4 types of data sources that python can read and write:
1:CSV
2:Excel
3:HTML
4:SQL
'''
'''
in order to use HTML and SQL the following libarries should be installed
'''
import sqlalchemy
import lxml
import html5lib
import xlrd
import openpyxl

# import BeautifulSoup4



# for CSV files
df=pd.DataFrame(
	{'A':['foo','foo','foo','bar','bar','bar'],
	'B':['one','one','two','two','one','one'],
	'C':['x','y','x','y','x','y'],
	'D':[1,3,2,5,4,1]}
	)
print (df)

# # saving a csv file
# df.to_csv('example.csv')   
# df2= pd.read_csv('example.csv')
# print (df2)

# # reading a csv file
# df.to_csv('example.csv', index=False)  # will not save new index and keep te 
# df2= pd.read_csv('example.csv')
# print (df2)





# for exacel files
# #writing an excel file
# df.to_excel('example.xlsx', sheet_name='Vahid sheet')

# #reading an excel file
# pd.read_excel('example.xlsx',sheet_name='Vahid sheet')










# # for HTML files 
# data=pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
# print (type(data))
# print (data[0])











#sql
from sqlalchemy import create_engine
engine=create_engine('sqlite:///:memory:')
df. to_sql('mytable',engine)
sqldf=pd. read_sql('mytable', con=engine)
print(sqldf)
