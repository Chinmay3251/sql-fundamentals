import os
import httpx
GROQ_URL="https://api.groq.com/openai/v1/chat/completions"

def _fallback(insights):
    text="Executive Summary. The dataset review highlights these findings: "+" ".join(insights)+" Recommended next steps are to validate data quality, investigate major variations, and track key measures over time."
    return " ".join(text.split()[:200])

def generate_summary(insights):
    if len(insights)!=5: raise ValueError("Exactly five insights are required.")
    key=os.getenv("GROQ_API_KEY","").strip()
    if not key:
        s=_fallback(insights); return {"summary":s,"provider":"local-fallback","word_count":len(s.split())}
    prompt="Write a business executive summary in no more than 200 words. Use only these five insights; do not invent facts or numbers. Include implications and priorities.\n"+"\n".join(f"{i+1}. {v}" for i,v in enumerate(insights))
    r=httpx.post(GROQ_URL,headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"},json={"model":os.getenv("GROQ_MODEL","llama-3.3-70b-versatile"),"messages":[{"role":"system","content":"You are a careful business data analyst. Never invent findings."},{"role":"user","content":prompt}],"temperature":0.2,"max_tokens":350},timeout=45)
    r.raise_for_status(); summary=r.json()["choices"][0]["message"]["content"].strip(); summary=" ".join(summary.split()[:200])
    return {"summary":summary,"provider":"groq","word_count":len(summary.split())}
