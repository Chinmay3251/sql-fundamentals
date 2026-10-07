
import requests


API_URL = "http://127.0.0.1:8000/cia/sql-analyst"

QUESTIONS = [
    "Which products are low in stock?",
    "Which five products have the highest price?",
    "Which products have the highest units sold?",
    "How many orders are in the database?",
    "How many orders has each customer placed?",
    "What are the total sales for each month?",
    "Who are the top five customers by total spending?",
    "What is the average order value?",
    "How many products are in each category?",
    "Which orders were placed most recently?",
]


def main():
    passed = 0
    failed = 0

    for index, question in enumerate(QUESTIONS, start=1):
        print("\n" + "=" * 70)
        print(f"TEST {index}: {question}")

        try:
            response = requests.post(
                API_URL,
                json={"question": question},
                timeout=180,
            )

            print("HTTP status:", response.status_code)

            if response.status_code != 200:
                print("ERROR:", response.text)
                failed += 1
                continue

            result = response.json()
            sql = result.get("sql", "")

            print("Generated SQL:")
            print(sql)
            print("Validation:", result.get("validation_message"))

            if result.get("valid") and sql:
                print("RESULT: SQL generated and passed structural checks")
                print("MANUAL REVIEW: Confirm tables, columns and logic.")
                passed += 1
            else:
                print("RESULT: REJECTED")
                failed += 1

        except requests.RequestException as exc:
            print("REQUEST FAILED:", exc)
            failed += 1

    print("\n" + "=" * 70)
    print(f"Passed structural checks: {passed}/{len(QUESTIONS)}")
    print(f"Failed: {failed}/{len(QUESTIONS)}")
    print("Passing a structural check does not prove SQL correctness.")


if __name__ == "__main__":
    main()
