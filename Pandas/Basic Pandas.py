# DATAFRAME

#case 1 
import pandas as pd

data = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
})

print(data,"\n")

print(data['Age'] + 5)  # Adds 5 to each age

print(data.to_string(index=False))  #remove indexing 




#case2
import pandas as pd
df = pd.DataFrame({ "Name":["Poorvanshi", "Devansh", "Harsh"], "Surname" : ["Bhardwaj", "Gupta", "Gupta"]})
print(f"{df}\n")

'''.head() = used to show first 5 rows of dataframe
   .head(2) = used to show first 2 rows of dataframe
   .tail() = used to show last 5 rows of dataframe
   .tail(2) = used to show last 2 rows of dataframe
'''

print(f"{df.head()}\n")
print(f"{df.tail(1)}\n")        #show last 1 row
print(f"{df.describe()}\n")
print(f"{df.info()}\n")





#case 3
import pandas as pd

#Case 1
a = pd.DataFrame({ "Name":["Poorvanshi", "Devansh", "Harsh"], "Surname" : ["Bhardwaj", "Gupta", "Gupta"]})
print(f"\n{a}")

'''.iloc[] is used for integer-location based indexing — that means you access rows and columns by their positions (numbers) rather than their labels. It’s very flexible for selecting, slicing, or filtering data.
'''
print(a.iloc[0])
print(a.head())
print(a.tail())
print(a.describe())
print(a.info())



#   (in CSV file)
import pandas as pd
df = pd.read_csv("F:\Devansh Gupta\AI + ML\Pandas\Data.csv")
print(df)

''' 1. dropna() = Removes rows that contain missing values (NaN)
            Example - df.dropna()             # Removes rows with any NaN
                      df.dropna(inplace=True)  # Permanently removes from df , ( Without inplace=True, original dataframe is not changed.)
                      
    2. fillna() = Replaces missing values (NaN) with a value (here 0)
            Example - df.fillna(0)                  # Temporary replacement
                      df.fillna(0, inplace=True)    # Permanent replacement
                      
                      
    3. rename(columns={}) = Renames column names
            Example - df.rename(columns={"OldName": "NewName"}, inplace=True)
                            (Without inplace=True, it only prints renamed version)


    4. astype(int) = Converts column data type
            Example -   astype(int)      # float → int
                        astype(float)    # int → float
                        astype(str)      # number → string
    
'''
print(df.iloc[0])
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
print(df.dropna())
print(df.fillna(0))       
print(df.rename(columns = {"SepalLenghtCm": "SL"}))






# SERIES

#case 2
'''
SERIES - A Series is a 1-dimensional labeled data structure
    Example - 
                import pandas as pd
                s = pd.Series([25, 30], index=['Alice', 'Bob'])
                print(s)

DATAFRAME - A DataFrame is a 2-dimensional labeled data structure.
    Example - 
                import pandas as pd
                df = pd.DataFrame({
                    'Name': ['Alice', 'Bob'],
                    'Age': [25, 30]
                })
                print(df)
'''
import pandas as pd
a = pd.DataFrame([1,2,3,4,5]) 
b = pd.Series([1,2,3,4,5]) 
c = pd.Series([1,2,3,4,5], index = ['a','b','c','d','e']) 

print(a)
print(b)
print(c)
