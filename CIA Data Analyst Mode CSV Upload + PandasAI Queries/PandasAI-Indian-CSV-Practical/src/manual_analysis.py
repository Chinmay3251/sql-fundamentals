def answer_question(df, qid):
    if qid == "Q01": return round(float(df["revenue_inr"].sum()), 2)
    if qid == "Q02": return df.groupby("product")["revenue_inr"].sum().sort_values(ascending=False).head(5)
    if qid == "Q03": return df.groupby("city")["revenue_inr"].sum().sort_values(ascending=False).head(1)
    if qid == "Q04": return df.groupby("category")["quantity"].sum().sort_values(ascending=False)
    if qid == "Q05": return df["payment_method"].value_counts().head(1)
    if qid == "Q06": return round(float(df["revenue_inr"].mean()), 2)
    if qid == "Q07": return df.groupby(df["order_date"].dt.to_period("M"))["revenue_inr"].sum().sort_index()
    if qid == "Q08": return df.groupby("region").size().sort_values(ascending=False)
    if qid == "Q09":
        x=df["discount_pct"].dropna()
        return round(float(x.gt(0).mean()*100), 2)
    if qid == "Q10": return df.groupby("customer_type")["revenue_inr"].sum().sort_values(ascending=False)
    raise KeyError(qid)
