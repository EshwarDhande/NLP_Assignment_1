import pandas as pd
from datasketch import MinHash

df = pd.read_csv("mukul_cleaned_data.csv")
df["hash"] = "NA"
df["id"] = df.index + 1

for i in range(len(df)):
    m1 = MinHash()
    for token in df.iloc[i,2].split():
        m1.update(token.encode("utf-8"))
    df.iloc[i,3] = m1

threshold = 0.2
i = 0
while True:
    if i > len(df):
        break

    ## Register duplicate rows except current row
    index_list = []
    for j in range(i + 1, len(df)):
        if df.iloc[i,3].jaccard(df.iloc[j,3]) >= threshold:
            index_list.append(df.iloc[j,0])

    ## Delete the duplicate rows
    df = df[~df["id"].isin(index_list)]
    print(index_list)

    i += 1

df.to_csv("mukul_dedup_data.csv")