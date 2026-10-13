from pathlib import Path
import pytest
from src.pandasai_runner import load_data, ask
from src.manual_analysis import answer_question
ROOT=Path(__file__).resolve().parents[1]
def test_dataset_shape():
    df=load_data(ROOT/"data"/"indian_retail_sales.csv")
    assert len(df)==600 and {"city","state","product","revenue_inr"}.issubset(df.columns)
def test_manual_revenue_positive():
    df=load_data(ROOT/"data"/"indian_retail_sales.csv")
    assert answer_question(df,"Q01")>0
def test_unknown_question():
    df=load_data(ROOT/"data"/"indian_retail_sales.csv")
    with pytest.raises(KeyError): answer_question(df,"bad")
def test_failed_ai_query_handled_and_logged(caplog):
    class Broken:
        def chat(self,q): raise RuntimeError("simulated failure")
    with caplog.at_level("ERROR",logger="pandasai_practical"):
        result=ask(Broken(),"test")
    assert not result["ok"] and "RuntimeError" in result["error"]
    assert "query_failed" in caplog.text
