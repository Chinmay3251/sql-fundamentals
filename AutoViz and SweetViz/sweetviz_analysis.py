import pandas as pd
import sweetviz as sv

# Load dataset
df = pd.read_csv("C:\\Users\\MSI\\Desktop\\Internship\\AutoViz and SweetViz\\indian_data.csv")

print("Dataset loaded successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Create SweetViz report
report = sv.analyze(df)

# Export HTML
report.show_html(
    "sweetviz_report.html",
    open_browser=False
)

print("SweetViz report created successfully!")
print("File: sweetviz_report.html")