from fastapi.testclient import TestClient
from app.main import app,DATASETS
import pytest
client=TestClient(app); CSV=b"region,sales,orders\\nNorth,100,4\\nSouth,200,5\\nNorth,150,3\\nEast,50,2\\n"
@pytest.fixture(autouse=True)
def clean():
 DATASETS.clear(); yield; DATASETS.clear()
def upload():
 r=client.post("/api/upload",files={"file":("sample.csv",CSV,"text/csv")}); assert r.status_code==200; return r.json()["dataset_id"]
def test_upload():
 r=client.post("/api/upload",files={"file":("sample.csv",CSV,"text/csv")}); assert r.status_code==200 and r.json()["rows"]==4
@pytest.mark.parametrize("q,expected",[("What is the row count?","4 rows"),("What is the sum of sales?","500.00"),("What is the average sales?","125.00"),("Show sales by region","North"),("What is the maximum orders?","5.00")])
def test_five_queries(q,expected):
 r=client.post("/api/query",json={"dataset_id":upload(),"question":q}); assert r.status_code==200; b=r.json(); assert expected.lower() in b["answer"].lower(); assert "data" in b["chart"] and "layout" in b["chart"]
def test_reject_txt(): assert client.post("/api/upload",files={"file":("a.txt",b"hi","text/plain")}).status_code==400
def test_missing_dataset(): assert client.post("/api/query",json={"dataset_id":"missing","question":"sum sales"}).status_code==404
