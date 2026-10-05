# EDA Methods and Tool Notes

| Method | What it contributes | Limitation |
|---|---|---|
| Pandas profiling and summary statistics | Checks shape, data types, missing values, duplicates, and distributions | Requires interpretation and manual selection of useful findings |
| Matplotlib / Seaborn | Creates focused charts for category, state, monthly, and transaction-level patterns | Chart choices can hide or overstate patterns if poorly designed |
| Sweetviz | Generates an interactive automated HTML EDA report | Automated patterns still need business context and validation |
| Optional Ollama model | Drafts a natural-language interpretation of computed metrics | Can misinterpret or invent explanations; validate all claims |
| Rule-based fallback | Generates reproducible insights when the AI model is unavailable | Less flexible than an LLM and limited to programmed rules |

## Recommended approach

Use Pandas to calculate metrics, visualisations to inspect patterns, Sweetviz to speed up initial profiling, and AI only to help explain already-computed results. The dataset and code should remain the source of truth.
