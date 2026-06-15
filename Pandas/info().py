import pandas as pd

data = {
    "Name": ["Devansh", "Harsh","Rajat"],
    "Age": [18 , 21 , 12],
    "City": ["Mumbai", "Delhi", "Jaipur"]
}

df = pd.DataFrame(data)
print(df.info())