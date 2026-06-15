import pandas as pd

#To saving files (in - csv, json, xlsx and more)
data = {
    "Name": ["Devansh", "Harsh","Rajat"],
    "Age": [18 , 21 , 12],
    "City": ["Mumbai", "Delhi", "Jaipur"]
}

df = pd.DataFrame(data)
print(df)

df.to_csv("Output.csv", index = False) #Saving File in csv format
df.to_excel("Output.xlsx", index = False) #Saving File in xlsx format
df.to_json("Output.json", index = False) #Saving File in json format
