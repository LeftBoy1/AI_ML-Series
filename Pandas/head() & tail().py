import pandas as pd
#Displaying Head & Tail in Rows-

df = pd.read_json("F:\Devansh_Gupta\AI + ML\Pandas\sample_Data.json", encoding="latin1")    

'''

Encoding tells Pandas how to correctly read characters from a file so text data doesn’t break or show errors
    
   Example -> encoding="latin1"
                ✔ Prevents UnicodeDecodeError
                ✔ Reads special characters safely
                ✔ Ensures the file loads correctly
'''

print(f"First 10 Rows: \n{df.head(10)}")  #Showing starting 10 rows of file
print(f"Last 10 Rows: \n{df.tail(10)}")  #Showing last 10 rows of file