import pandas as pd

def analyze_csv(df: pd.DataFrame) -> dict:
    rows, cols = df.shape
    insights = [f'The dataset contains {rows:,} records and {cols:,} columns.',
                f'{int(df.isna().sum().sum()):,} missing cell(s) were found across the dataset.']
    numeric = df.select_dtypes(include='number')
    if len(numeric.columns):
        col = numeric.var().fillna(0).idxmax()
        s = numeric[col].dropna()
        insights.append(f"'{col}' average is {s.mean():,.2f} and median is {s.median():,.2f}." if len(s) else f"Numeric column '{col}' has no usable values.")
    else:
        insights.append('No numeric columns were detected; consider capturing measurable KPIs.')
    categorical = df.select_dtypes(include=['object', 'category', 'bool'])
    if len(categorical.columns):
        col = max(categorical.columns, key=lambda c: df[c].nunique(dropna=True))
        counts = df[col].dropna().astype(str).value_counts()
        insights.append(f"'{col}' has {df[col].nunique(dropna=True)} distinct values; most frequent is '{counts.index[0]}' ({counts.iloc[0]} records)." if len(counts) else f"'{col}' has no non-missing values.")
    else:
        insights.append('No categorical columns were detected for segment-level comparisons.')
    if len(numeric.columns):
        col = numeric.columns[0]; s = numeric[col].dropna()
        insights.append(f"'{col}' ranges from {s.min():,.2f} to {s.max():,.2f}; review the spread for outliers." if len(s) else 'Numeric fields need valid values before range analysis.')
    else:
        insights.append('Add numeric KPIs to support range, trend, and variability analysis.')
    return {'rows': int(rows), 'columns': [str(c) for c in df.columns], 'insights': insights[:5],
            'recommendations': ['Investigate missing values and standardize inconsistent fields.',
            'Compare key metrics across relevant business segments.',
            'Validate unusual values and confirm metric definitions with stakeholders.']}
