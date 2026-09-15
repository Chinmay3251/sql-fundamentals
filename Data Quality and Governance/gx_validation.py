import pandas as pd
import great_expectations as gx
from great_expectations.expectations import (
    ExpectColumnToExist,
    ExpectColumnValuesToNotBeNull,
    ExpectColumnValuesToBeUnique,
    ExpectColumnValuesToBeBetween,
    ExpectColumnValuesToBeInSet,
)

# ==================================================
# 1. Load the clean dataset
# ==================================================

df = pd.read_csv("C:\\Users\\MSI\\Desktop\\Internship\\Data Quality and Governance\\cleaned_sales.csv")

print("Original dataset:")
print(df)


# ==================================================
# 2. Intentionally inject 3 data quality errors
# ==================================================

bad_data = df.copy()

# Error 1: Missing customer
bad_data.loc[0, "customer"] = None

# Error 2: Negative quantity
bad_data.loc[1, "quantity"] = -10

# Error 3: Duplicate order_id
bad_data.loc[2, "order_id"] = bad_data.loc[3, "order_id"]

bad_data.to_csv("sales_with_errors.csv", index=False)

print("\nThree intentional errors were added:")
print("1. Missing customer")
print("2. Negative quantity")
print("3. Duplicate order ID")


# ==================================================
# 3. Create Great Expectations context
# ==================================================

context = gx.get_context()


# ==================================================
# 4. Create Pandas Data Source
# ==================================================

data_source = context.data_sources.add_pandas(
    name="sales_data_source"
)

data_asset = data_source.add_dataframe_asset(
    name="sales_asset"
)

batch_definition = data_asset.add_batch_definition_whole_dataframe(
    "sales_batch"
)

batch = batch_definition.get_batch(
    batch_parameters={
        "dataframe": bad_data
    }
)


# ==================================================
# 5. Create Expectation Suite
# ==================================================

suite = gx.ExpectationSuite(
    name="sales_data_quality_suite"
)


# ==================================================
# 6. Add 8 Expectations
# ==================================================

suite.add_expectation(
    ExpectColumnToExist(
        column="order_id"
    )
)

suite.add_expectation(
    ExpectColumnToExist(
        column="customer"
    )
)

suite.add_expectation(
    ExpectColumnValuesToNotBeNull(
        column="customer"
    )
)

suite.add_expectation(
    ExpectColumnValuesToBeUnique(
        column="order_id"
    )
)

suite.add_expectation(
    ExpectColumnValuesToBeBetween(
        column="quantity",
        min_value=1,
        max_value=100
    )
)

suite.add_expectation(
    ExpectColumnValuesToBeBetween(
        column="price",
        min_value=0
    )
)

suite.add_expectation(
    ExpectColumnValuesToBeInSet(
        column="region",
        value_set=[
            "South",
            "North",
            "East",
            "West"
        ]
    )
)

suite.add_expectation(
    ExpectColumnValuesToBeInSet(
        column="category",
        value_set=[
            "Electronics",
            "Furniture",
            "Clothing"
        ]
    )
)


# ==================================================
# 7. Save the expectation suite
# ==================================================

context.suites.add(suite)

print("\nExpectation suite created successfully.")

print("Total expectations:", len(suite.expectations))


# ==================================================
# 8. Create validation definition
# ==================================================

validation_definition = gx.ValidationDefinition(
    data=batch_definition,
    suite=suite,
    name="sales_validation"
)

context.validation_definitions.add(validation_definition)


# ==================================================
# 9. Run validation
# ==================================================

print("\n========== VALIDATION RESULTS ==========")

results = validation_definition.run(
    batch_parameters={
        "dataframe": bad_data
    }
)


# ==================================================
# 10. Display results
# ==================================================

print("\nOverall validation result:")

if results.success:
    print("PASSED")
else:
    print("FAILED")


print("\n========== FAILED EXPECTATIONS ==========")

failed_count = 0

for result in results.results:

    if not result.success:
        failed_count += 1

        expectation_type = result.expectation_config.type

        print("FAILED:", expectation_type)


print("\nTotal failed expectations:", failed_count)

print("\nExpected errors detected:")
print("1. Missing customer")
print("2. Duplicate order ID")
print("3. Invalid negative quantity")

print("\n====================================")
print("GREAT EXPECTATIONS VALIDATION COMPLETE")
print("====================================")