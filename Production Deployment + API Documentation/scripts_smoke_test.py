"""Production smoke test. Usage: python scripts_smoke_test.py https://your-app.onrender.com"""
import sys
import requests

if len(sys.argv) != 2:
    raise SystemExit("Usage: python scripts_smoke_test.py https://your-deployment-url")
base = sys.argv[1].rstrip("/")
session = requests.Session()

for path in ("/", "/health", "/docs"):
    response = session.get(base + path, timeout=30)
    print(f"GET {path}: {response.status_code}")
    response.raise_for_status()

with open("data/sample_sales.csv", "rb") as csv_file:
    response = session.post(base + "/analyze", files={"file": ("sample_sales.csv", csv_file, "text/csv")}, timeout=90)
print(f"POST /analyze: {response.status_code}")
response.raise_for_status()
data = response.json()
assert len(data.get("insights", [])) == 5, "Expected five insights"
assert data.get("executive_summary"), "Missing executive summary"
print("Analysis response: 5 insights and executive summary OK")

with open("data/sample_sales.csv", "rb") as csv_file:
    response = session.post(base + "/export-ppt", files={"file": ("sample_sales.csv", csv_file, "text/csv")}, timeout=90)
print(f"POST /export-ppt: {response.status_code}")
response.raise_for_status()
assert response.headers.get("content-type", "").startswith("application/vnd.openxmlformats-officedocument.presentationml.presentation")
assert response.content[:2] == b"PK", "PPTX response is not a ZIP-based Office file"
with open("smoke_test_output.pptx", "wb") as out:
    out.write(response.content)
print("PowerPoint download: OK (saved as smoke_test_output.pptx)")
