import pandas as pd

profanity = None
with open('profane.txt', 'r') as fp:
    profanity = fp.readlines()
profanity = [word.strip() for word in profanity]

df = pd.read_csv('mukul_data.csv')
pattern = u"|".join(profanity)
bool_df = df["contents"].str.contains(pattern, regex=True)
clean_df = df[~bool_df]
clean_df.to_csv("mukul_cleaned_data.csv")
print(clean_df.shape)