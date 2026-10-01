import pandas as pd
from autoviz.AutoViz_Class import AutoViz_Class

# Load dataset
df = pd.read_csv("C:\\Users\\MSI\\Desktop\\Internship\\AutoViz and SweetViz\\indian_data.csv")

print("Dataset loaded successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Create AutoViz object
AV = AutoViz_Class()

# Generate AutoViz report
report = AV.AutoViz(
    filename="",
    dfte=df,
    depVar="total_sales",
    verbose=2,
    chart_format="html"
)

print("AutoViz analysis completed!")