import pandas as pd

with open('data/dec1.txt') as f:
    content = f.read().split("\n")

df = pd.DataFrame({"data":content})

df["num"] = df.data.str.findall('\d').str.join("").fillna(0)
df["num"] = df["num"].str[0] + df["num"].str[-1]

print(f'Answer: {df["num"].astype(int).sum()}')

