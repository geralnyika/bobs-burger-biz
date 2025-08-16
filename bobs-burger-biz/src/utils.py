import pandas as pd
import numpy as np

def audit(df, name="df"):
    print(f"\n== {name} ==")
    print("shape:", df.shape)
    print("dtypes:\n", df.dtypes)
    print("nulls:\n", df.isna().sum())
    print("duplicates:", df.duplicated().sum())
