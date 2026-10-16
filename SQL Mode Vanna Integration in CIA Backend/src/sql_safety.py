"""Small conservative guardrails for generated SQL. Not a full SQL parser."""
import re

# Reject SQL that can mutate data or alter privileges. This is defense-in-depth,
# not a substitute for a read-only database account or dialect-aware parsing.
FORBIDDEN = re.compile(
    r"\b(INSERT|UPDATE|DELETE|DROP|ALTER|CREATE|TRUNCATE|GRANT|REVOKE|COPY|CALL|EXECUTE|MERGE)\b",
    re.IGNORECASE,
)

def validate_read_only_sql(sql: str) -> str:
    """Return normalized SQL if it appears to be one read-only SELECT/WITH query."""
    if not isinstance(sql, str) or not sql.strip():
        raise ValueError("Generated SQL is empty.")
    query = sql.strip()
    # Permit one optional trailing semicolon, but reject any other statement separator.
    without_trailing = query[:-1] if query.endswith(";") else query
    if ";" in without_trailing:
        raise ValueError("Multiple SQL statements are not allowed.")
    if not re.match(r"^(SELECT|WITH)\b", without_trailing, re.IGNORECASE):
        raise ValueError("Only SELECT or WITH queries are allowed.")
    if FORBIDDEN.search(without_trailing):
        raise ValueError("Potentially mutating SQL keyword detected.")
    return without_trailing
