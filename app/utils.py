import pandas as pd
import numpy as np

def calculate_zscores(df, columns):
    """Calculate Z-scores for specified columns."""
    return df[columns].apply(stats.zscore)

def handle_outliers(df, columns, threshold=3):
    """Flag rows with outliers based on Z-score threshold."""
    from scipy import stats
    z_scores = np.abs(stats.zscore(df[columns].dropna()))
    return (z_scores > threshold).any(axis=1)
