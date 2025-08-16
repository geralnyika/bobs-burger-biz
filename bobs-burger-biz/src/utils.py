import pandas as pd
import numpy as np

def audit(df, name="df"):
    print(f"\n== {name} ==")
    print("shape:", df.shape)
    print("dtypes:\n", df.dtypes)
    print("nulls:\n", df.isna().sum())
    print("duplicates:", df.duplicated().sum())

def cap_outliers(series, q_low=0.01, q_high=0.99):
    try:
        low, high = series.quantile([q_low, q_high])
        return series.clip(lower=low, upper=high)
    except Exception:
        return series

def to_float_maybe_money(s):
    # handles 12.5, "15", "$13.0", None
    return pd.to_numeric(
        pd.Series(s).astype(str).str.replace(r"[^0-9\.\-]", "", regex=True),
        errors="coerce"
    )

def normalize_str(s):
    return pd.Series(s).astype(str).str.strip().str.replace(r"\s+", " ", regex=True)

def clip_scale(x, lo=None, hi=None):
    x = pd.to_numeric(x, errors="coerce")
    if lo is not None and hi is not None:
        return x.clip(lower=lo, upper=hi)
    if lo is not None:
        return x.clip(lower=lo)
    if hi is not None:
        return x.clip(upper=hi)
    return x
