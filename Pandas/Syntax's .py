import pandas as pd

data = {
    "Name": ["Devansh", "Harsh","Poorvanshi", "Rajat", "Yashika"],
    "Age": [18 , 21 , 18, 12, 16],
    "City": ["Mumbai", "Delhi", "Jaipur", "Nagpur", "Delhi" ],
    "Salary": [1000000, 1000000, 1000000, 1000000, 1000000],
    "Performance_Score": [98, 97, 99, 93, 90]
}

df = pd.DataFrame(data)




#Selecting single Column- 
print(df["Name"])

#Selecting Multi Column
print(df[["City", "Age","Salary"]])



#BOOLEAN INDEXING

#Filterating Rows with single Condition-
single_cond = df[df["Age"] > 17]
print(single_cond)

#Filterating Rows with multi Condition-
multi_cond = df[ ( df["Age"] > 17 ) & ( df["Performance_Score"] > 95) ]
print(multi_cond)

# Using OR Condition- 
or_cond = df[ ( df["Age"] > 17 ) | ( df["Performance_Score"] > 95) ]
print(or_cond)  