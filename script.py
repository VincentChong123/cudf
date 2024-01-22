import pandas as pd

URL = "https://github.com/plotly/datasets/raw/master/tips.csv"
df = pd.read_csv(URL)  # uses the GPU
df["size"].value_counts()  # uses the GPU
df.groupby("size").total_bill.mean()  # uses the GPU
df.apply(list, axis=1)  # uses the CPU (fallback)
