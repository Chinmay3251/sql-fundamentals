from io import BytesIO
import os
import pandas as pd
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import StreamingResponse
from .analytics import analyze_csv
from .groq_summary import generate_executive_summary
from .ppt_export import create_presentation

app = FastAPI(title='W8D2 Business Recommendations', version='1.0.0')

@app.get('/')
def root():
    return {'message': 'CSV upload -> EDA -> AI summary -> PPT export', 'docs': '/docs'}

@app.get('/health')
def health():
    return {'status': 'ok'}

async def load_csv(file: UploadFile):
    if not file.filename or not file.filename.lower().endswith('.csv'):
        raise HTTPException(400, 'Please upload a .csv file.')
    raw = await file.read()
    if not raw:
        raise HTTPException(400, 'Uploaded CSV is empty.')
    try:
        df = pd.read_csv(BytesIO(raw))
    except Exception as exc:
        raise HTTPException(400, f'Could not read CSV: {exc}')
    if df.empty:
        raise HTTPException(400, 'CSV must contain at least one data row.')
    return df

@app.post('/analyze')
async def analyze(file: UploadFile = File(...)):
    df = await load_csv(file)
    report = analyze_csv(df)
    summary = generate_executive_summary(report['insights'])
    return {'filename': file.filename, **report, 'executive_summary': summary,
            'ai_summary_provider': 'Groq' if os.getenv('GROQ_API_KEY') else 'local_fallback'}

@app.post('/export-ppt')
async def export_ppt(file: UploadFile = File(...)):
    df = await load_csv(file)
    report = analyze_csv(df)
    summary = generate_executive_summary(report['insights'])
    content = create_presentation(file.filename or 'uploaded.csv', report['rows'], report['columns'],
                                  report['insights'], summary, report['recommendations'])
    name = (file.filename or 'analytics.csv').rsplit('.', 1)[0] + '_recommendations.pptx'
    return StreamingResponse(BytesIO(content), media_type='application/vnd.openxmlformats-officedocument.presentationml.presentation',
        headers={'Content-Disposition': f'attachment; filename="{name}"'})
