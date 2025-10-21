import pandas as pd

data = pd.read_csv('D:\AIMS\Assignment - 1_Encoding\data.csv')

df = pd.DataFrame(data)

print("Orignal DataFrame: \n", df , "\n")

colsToEncode = ["Color", "Gender"]

for col in colsToEncode:
    uniqueValues = []
    for data in df[col]:
        if data in uniqueValues:
            continue
        else:
            uniqueValues.append(data)

    for val in uniqueValues:
        newCol = col + "_" + val
        newValues = []

        for content in df[col]:
            if val == content:
                newValues.append(1)
            else:
                newValues.append(0)

        df[newCol] = newValues


print("Updated DataFrame after OneHot encoding: \n", df)
 