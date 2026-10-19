import pandas as pd
import plotly.graph_objects as go

def answer_question(df, question):
    q=question.lower(); cols=list(map(str,df.columns)); nums=list(map(str,df.select_dtypes(include="number").columns))
    if df.empty: return {"answer":"The uploaded dataset has no rows.","chart":{"data":[],"layout":{"title":{"text":"No data"}}}}
    if any(x in q for x in ["row count","how many rows","number of rows","count rows"]):
        return {"answer":f"The dataset contains {len(df)} rows and {len(cols)} columns.","chart":{"data":[],"layout":{"title":{"text":"Dataset size"}}}}
    num=next((c for c in sorted(nums,key=len,reverse=True) if c.lower() in q),None)
    cat=next((c for c in sorted([c for c in cols if c not in nums],key=len,reverse=True) if c.lower() in q),None)
    if num and cat and any(x in q for x in ["by ","per ","group","compare","top"]):
        s=df.groupby(cat,dropna=False)[num].sum().sort_values(ascending=False).head(20)
        title=f"Sum of {num} by {cat}"; fig=go.Figure(go.Bar(x=[str(x) for x in s.index],y=[float(x) for x in s.values])); fig.update_layout(title=title,xaxis_title=cat,yaxis_title=f"Sum of {num}",template="plotly_white")
        return {"answer":title+": "+", ".join(f"{k}: {v:,.2f}" for k,v in s.items()),"chart":fig.to_dict()}
    if num:
        if any(x in q for x in ["average","avg","mean"]): label="average"; val=float(df[num].mean())
        elif any(x in q for x in ["maximum","max","highest","largest"]): label="maximum"; val=float(df[num].max())
        elif any(x in q for x in ["minimum","min","lowest","smallest"]): label="minimum"; val=float(df[num].min())
        else: label="sum"; val=float(df[num].sum())
        fig=go.Figure(go.Bar(x=[label.title()],y=[val])); fig.update_layout(title=f"{label.title()} of {num}",xaxis_title="Metric",yaxis_title=num,template="plotly_white")
        return {"answer":f"The {label} of {num} is {val:,.2f}.","chart":fig.to_dict()}
    return {"answer":f"Loaded {len(df)} rows and {len(cols)} columns. Ask for row count, a numeric sum/average, or a numeric total grouped by category.","chart":{"data":[],"layout":{"title":{"text":"Ask an aggregate question"}}}}
