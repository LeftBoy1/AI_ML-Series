import pandas as pd

data = {
    "Name": ["Devansh", "Harsh","Rajat"],
    "Age": [18 , 21 , 12],
    "City": ["Mumbai", "Delhi", "Jaipur"],
    "Marks": [99, 98, 97]
}

df = pd.DataFrame(data)




print(f"Shape: {df.shape}")   #showing shape

print(f"Columns: {df.columns}") #showing Columns
