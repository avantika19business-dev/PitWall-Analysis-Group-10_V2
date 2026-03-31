"""
data_generator.py
─────────────────
Loads PitWall_Analytics_Cleaned.xlsx from multiple possible locations.
Searches: data/, repo root, and same directory as this script.
"""
from __future__ import annotations
import io
from pathlib import Path
import pandas as pd
import numpy as np

_HERE = Path(__file__).parent
_HEADER_ROW = 2  # headers on row 3 (0-indexed = 2)

# All candidate paths — checked in order
_CANDIDATES = [
    _HERE / "data" / "PitWall_Analytics_Cleaned.xlsx",
    _HERE / "PitWall_Analytics_Cleaned.xlsx",
    Path("/mount/src") / "data" / "PitWall_Analytics_Cleaned.xlsx",
]
# Also search for it anywhere one level up
for p in _HERE.parent.rglob("PitWall_Analytics_Cleaned.xlsx"):
    _CANDIDATES.append(p)


def _open_excel() -> dict[str, pd.DataFrame]:
    for path in _CANDIDATES:
        if path.exists():
            return pd.read_excel(path, sheet_name=None, header=_HEADER_ROW)
    raise FileNotFoundError(
        "PitWall_Analytics_Cleaned.xlsx not found.\n"
        "Make sure it is committed inside a 'data/' folder in your repo.\n"
        f"Searched: {[str(c) for c in _CANDIDATES[:3]]}"
    )


def load_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    xl   = _open_excel()
    subs = _clean_subscribers(xl["Subscribers"].copy())
    sess = _clean_sessions(xl["Engagement Sessions"].copy())
    mrr  = _clean_mrr(xl["Revenue MRR"].copy())
    return subs, sess, mrr


def _clean_subscribers(df: pd.DataFrame) -> pd.DataFrame:
    df.columns     = [c.strip() for c in df.columns]
    df["Signup Date"]  = pd.to_datetime(df["Signup Date"],  errors="coerce")
    df["Churn Date"]   = pd.to_datetime(df["Churn Date"],   errors="coerce")
    df["Churn Reason"] = df["Churn Reason"].fillna("Not Churned")
    df["churn_flag"]   = (df["Churned"] == "Yes").astype(int)
    return df


def _clean_sessions(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [c.strip() for c in df.columns]
    df["Session Date"]       = pd.to_datetime(df["Session Date"], errors="coerce")
    df["Is Weekend"]         = df["Is Weekend"].astype(bool)
    df["Engagement Score"]   = pd.to_numeric(df["Engagement Score"],     errors="coerce")
    df["Session Duration Min"] = pd.to_numeric(df["Session Duration Min"], errors="coerce")
    return df


def _clean_mrr(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [c.strip() for c in df.columns]
    df["Month"] = pd.to_datetime(df["Month"], format="%Y-%m", errors="coerce")
    return df
