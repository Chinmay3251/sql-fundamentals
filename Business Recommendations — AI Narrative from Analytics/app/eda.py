import pandas as pd

def analyze_csv(df: pd.DataFrame) -> dict:
    if df.empty:
        raise ValueError("CSV has no data rows.")
    numeric = list(df.select_dtypes(include="number").columns)
    categorical = [c for c in df.columns if c not in numeric]
    insights = [f"The dataset contains {len(df):,} rows and {len(df.columns)} columns."]
    if numeric:
        col = numeric[0]
        insights.append(f"{col}: mean {df[col].mean():,.2f}, median {df[col].median():,.2f}, minimum {df[col].min():,.2f}, maximum {df[col].max():,.2f}.")
        if len(numeric) > 1:
            corr = df[numeric].corr()
            pairs = [(a,b,float(corr.loc[a,b])) for i,a in enumerate(numeric) for b in numeric[i+1:] if pd.notna(corr.loc[a,b])]
            if pairs:
                a,b,v = max(pairs,key=lambda x:abs(x[2]))
                insights.append(f"Strongest pairwise numeric correlation is {a} vs {b} (correlation {v:.2f}).")
            else: insights.append(f"The dataset contains {len(numeric)} numeric columns for quantitative comparison.")
        else: insights.append("Only one numeric column is available, so cross-metric correlation is not applicable.")
        insights.append(f"Total of {col} is {df[col].sum():,.2f}; rows with missing {col} values: {int(df[col].isna().sum())}.")
    else:
        insights.extend(["No numeric columns were detected; numeric aggregation is unavailable.",f"There are {len(categorical)} non-numeric columns to inspect for category patterns."])
    if categorical:
        col=categorical[0]; counts=df[col].fillna("(missing)").astype(str).value_counts()
        insights.append(f"Most frequent value in {col} is '{counts.index[0]}' ({int(counts.iloc[0])} rows)." if len(counts) else f"No non-empty categories were found in {col}.")
    else: insights.append("No categorical columns were detected for segment-level analysis.")
    insights=insights[:5]
    while len(insights)<5: insights.append("Additional segmentation may reveal patterns not captured by available columns.")
    return {"rows":int(len(df)),"columns":list(map(str,df.columns)),"numeric_columns":list(map(str,numeric)),"missing_values":{str(k):int(v) for k,v in df.isna().sum().items()},"insights":insights}
