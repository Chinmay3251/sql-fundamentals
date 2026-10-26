from io import BytesIO
import pandas as pd
from pptx import Presentation
from app.analytics import analyze_csv
from app.groq_summary import generate_executive_summary
from app.ppt_export import create_presentation

def test_five_insights_and_recommendations():
    r = analyze_csv(pd.DataFrame({'sales':[10,20,30], 'region':['East','West','East']}))
    assert len(r['insights']) == 5 and len(r['recommendations']) >= 3

def test_fallback_summary_under_200_words(monkeypatch):
    monkeypatch.delenv('GROQ_API_KEY', raising=False)
    assert len(generate_executive_summary(['a','b']).split()) <= 200

def test_ppt_has_seven_slides():
    ppt = create_presentation('sample.csv', 3, ['sales','region'], [f'Insight {i}' for i in range(5)], 'Summary', ['Do A','Do B','Do C'])
    prs = Presentation(BytesIO(ppt))
    assert len(prs.slides) == 7
    assert prs.slides[0].shapes.title.text == 'Business Recommendations'
