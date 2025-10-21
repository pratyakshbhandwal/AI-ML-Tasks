import pandas as pd

dataSet = pd.read_csv('D:\AIMS\Assignment - 1_Encoding\imputation_data.csv')

# mean imputation
df_mean  = pd.DataFrame(dataSet)

print("Orignal Dataframe: \n", df_mean, "\n")

for col in df_mean.columns:
    if df_mean[col].dtype in ["int64", "float64"]:
        validVal = [x for x in df_mean[col] if not pd.isna(x)]

        sum = 0
        for x in validVal:
            sum = sum + x
        mean = sum/len(validVal)
        
        newVals = []
        for data in df_mean[col]:
            if pd.isna(data):
                newVals.append(mean)
            else:
                newVals.append(data)
        df_mean[col] = newVals

print("Updated Dataframe after Mean imputation: \n", df_mean, "\n")


# median imputation
df_median  = pd.DataFrame(dataSet)


for col in df_median.columns:
    if df_median[col].dtype in ["int64", "float64"]:
        validVal = sorted([x for x in df_mean[col] if not pd.isna(x)])

        n = len(validVal)
        
        if n%2 == 1:
            median = validVal[n//2]
        else:
            median = ( validVal[n//2 -1] + validVal[n//2] ) / 2

        newVals = []
        for data in df_mean[col]:
            if pd.isna(data):
                newVals.append(median)
            else:
                newVals.append(data)
        df_median[col] = newVals
            

print("Updated Dataframe after Median imputation: \n", df_median, "\n")


# mode imputation
df_mode  = pd.DataFrame(dataSet)


for col in df_mode.columns:
    
    vals = [x for x in df_mode[col] if not pd.isna(x)]

    freq = {}

    for v in vals:
        if v in freq:
            freq[v] += 1
        else:
            freq[v] = 1

    mode = max(freq, key=freq.get)
    
    newVals = []
    for data in df_mode[col]:
        if pd.isna(data):
            newVals.append(mode)
        else:
            newVals.append(data)
    df_mode[col] = newVals
            

print("Updated Dataframe after Mode imputation: \n", df_mode, "\n")

 