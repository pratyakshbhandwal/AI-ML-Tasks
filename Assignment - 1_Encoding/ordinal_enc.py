import pandas as pd


data = pd.read_csv('D:\AIMS\Assignment - 1_Encoding\data.csv')

df = pd.DataFrame(data)

print("Orignal DataFrame: \n", df , "\n")

sizes = ["Small", "Medium", "Large"]

encVal = []

for value in df['Size']:
    for i in range(len(sizes)):
        if sizes[i] == value:
            encVal.append(i + 1)
            break

df['Size_Encoding'] = encVal

print("Updated DataFrame after ordinal encoding: \n", df)

 


