import pandas as pd

#Read Data from csv file into a dataframe
df = pd.read_csv("F:\Devansh Gupta\AI + ML\Pandas\sales_data_sample.csv", encoding = "latin1")
print(df)

#Read Data from xlsx file into a dataframe
df2 = pd.read_excel("F:\Devansh Gupta\AI + ML\Pandas\SampleSuperstore.xlsx")
print(df2)

#Read Data from json file into a dataframe
df3 = pd.read_json("F:\Devansh Gupta\AI + ML\Pandas\sample_Data.json", encoding="latin1")
print(df3)


'''
if data is stored in Google Cloud Storage (GCS), not just “any cloud” , we can use ===>>>  gcsfs
        Example -   import pandas as pd

                    df = pd.read_csv("gs://my-bucket/data.csv", storage_options={"token": "cloud"})
'''