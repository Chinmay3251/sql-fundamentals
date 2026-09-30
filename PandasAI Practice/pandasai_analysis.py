import pandas as pd
import logging
from pandasai import SmartDataframe

# ==========================================
# LOGGING
# ==========================================

logging.basicConfig(
    filename="error_log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ==========================================
# LOAD DATA
# ==========================================

try:
    df = pd.read_csv("C:\\Users\\MSI\\Desktop\\Internship\\PandasAI Practice\\indian_data.csv")

    print("Dataset loaded successfully!")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])
    print("\nColumns:")
    print(df.columns.tolist())

except Exception as e:
    logging.error("Dataset loading failed: %s", e)
    print("Error loading dataset:", e)
    exit()

# ==========================================
# CREATE PANDASAI DATAFRAME
# ==========================================

try:
    smart_df = SmartDataframe(df)

except Exception as e:
    logging.error("PandasAI initialization failed: %s", e)
    print("PandasAI initialization failed:", e)
    exit()

# ==========================================
# NATURAL LANGUAGE QUESTIONS
# ==========================================

questions = [
    "How many rows are in the dataset?",
    "What are the column names?",
    "Show the first 5 rows.",
    "What is the average value of the numeric columns?",
    "Which category has the highest count?",
    "Which category has the lowest count?",
    "What is the maximum value of the main numeric column?",
    "What is the minimum value of the main numeric column?",
    "Show the top 10 records by the main numeric column.",
    "What are the main insights from this dataset?"
]

print("\n========== PANDASAI QUESTIONS ==========")

for i, question in enumerate(questions, start=1):

    print(f"\nQuestion {i}: {question}")

    try:
        answer = smart_df.chat(question)
        print("Answer:")
        print(answer)

    except Exception as e:
        logging.error(
            "Question failed: %s | Error: %s",
            question,
            e
        )

        print("Query failed.")
        print("Error:", e)

print("\n========================================")
print("PANDASAI ANALYSIS COMPLETED")
print("========================================")