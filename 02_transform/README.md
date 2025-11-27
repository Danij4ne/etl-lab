
# Technical Documentation — Transform Module (02_transform)

## 1. Overview

The **Transform** module implements the data transformation phase in the ETL pipeline.  
Its purpose is to clean, normalize, type-cast, and enrich the data previously extracted, ensuring it is in a consistent and usable state for downstream systems (files, databases, data warehouses, etc.).

Unlike the Extract module, this stage applies basic business rules, format conversions, and data quality checks.

---

## 2. Main responsibilities

Typical transformations include:

- Data type conversions (e.g. text to numeric or datetime).
- Handling of missing values and basic outlier treatment.
- Normalization of categorical values (countries, states, codes).
- String cleaning (trimming, case normalization, formatting).
- Duplicate removal.
- Creation of derived columns (metrics, flags, combined fields).
- Final validation of dataset consistency.

---

## 3. Dependencies

Transform functions are primarily built on `pandas`:

```python
import pandas as pd
from typing import Iterable
```

Additional libraries such as `datetime` may be used depending on business requirements.

---

## 4. Transformation function interfaces

Below are recommended patterns for reusable transformation functions.

---

### 4.1. Numeric type conversion

Example function to safely convert a column to numeric:

```python
def to_numeric(df: pd.DataFrame, column: str, errors: str = "coerce") -> pd.DataFrame:
    """Convert a column to numeric type with configurable error handling."""
    df = df.copy()
    df[column] = pd.to_numeric(df[column], errors=errors)
    return df
```

Typical use:
- Force conversion of columns such as `age`, `amount`, `score`.
- With `errors="coerce"`, invalid values become `NaN`.

---

### 4.2. Datetime conversion

Example function to convert a text column into datetime:

```python
def to_datetime(df: pd.DataFrame, column: str, fmt: str | None = None) -> pd.DataFrame:
    """Convert a column to datetime."""
    df = df.copy()
    df[column] = pd.to_datetime(df[column], format=fmt, errors="coerce")
    return df
```

Allows:
- Supporting multiple date formats.
- Returning `NaT` for invalid entries.

---

### 4.3. String normalization

Example function normalizing a string column by trimming spaces and lowercasing:

```python
def normalize_str_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Normalize a string column: trim and lower-case."""
    df = df.copy()
    df[column] = (
        df[column]
        .astype("string")
        .str.strip()
        .str.lower()
    )
    return df
```

Useful for:
- Columns such as `email`, `country`, `city`, etc.

---

### 4.4. Categorical normalization

Example function to map multiple variants to standard country values:

```python
def normalize_country(df: pd.DataFrame, column: str = "country") -> pd.DataFrame:
    """Normalize country values to a standard set."""
    df = df.copy()
    df[column] = (
        df[column]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    mapping = {
        "spain": "spain",
        "españa": "spain",
        "es": "spain",
        "france": "france",
        "fr": "france",
    }

    df[column] = df[column].map(lambda x: mapping.get(x, x))
    return df
```

The same pattern can be extended to other fields (states, plan types, etc.).

---

### 4.5. Missing value handling

Generic function to fill missing values:

```python
def fill_missing(
    df: pd.DataFrame,
    column: str,
    strategy: str = "mean",
    value: float | int | str | None = None,
) -> pd.DataFrame:
    """Fill missing values using a given strategy: mean, median, constant."""
    df = df.copy()

    if strategy == "constant":
        if value is None:
            raise ValueError("A 'value' must be provided for strategy='constant'.")
        df[column] = df[column].fillna(value)
    elif strategy == "mean":
        df[column] = df[column].fillna(df[column].mean())
    elif strategy == "median":
        df[column] = df[column].fillna(df[column].median())
    else:
        raise ValueError(f"Unsupported strategy: {strategy}")

    return df
```

---

### 4.6. Duplicate removal

Recommended pattern:

```python
def drop_duplicates(
    df: pd.DataFrame,
    subset: Iterable[str] | None = None,
    keep: str = "first",
) -> pd.DataFrame:
    """Drop duplicate rows based on selected columns."""
    df = df.copy()
    df = df.drop_duplicates(subset=subset, keep=keep)
    return df
```

`subset` allows specifying keys such as `["email"]` or `["user_id"]`.

---

### 4.7. Derived columns

Example: `full_name` from `first_name` and `last_name`:

```python
def add_full_name(df: pd.DataFrame) -> pd.DataFrame:
    """Create a full_name column from first_name and last_name."""
    df = df.copy()
    df["full_name"] = (
        df["first_name"].astype("string").str.strip()
        + " "
        + df["last_name"].astype("string").str.strip()
    )
    return df
```

Example: `is_adult` boolean flag:

```python
def add_is_adult(df: pd.DataFrame, age_column: str = "age") -> pd.DataFrame:
    """Add a boolean is_adult column based on age."""
    df = df.copy()
    df["is_adult"] = df[age_column] >= 18
    return df
```

---

## 5. Main transformation function

In a real pipeline, a central function is recommended:

```python
def transform_users(df: pd.DataFrame) -> pd.DataFrame:
    """Apply agreed transformations to the users DataFrame."""
    df = df.copy()

    # Type conversions
    df = to_numeric(df, "age", errors="coerce")

    # Dates
    if "signup_date" in df.columns:
        df = to_datetime(df, "signup_date")

    # String normalization
    if "email" in df.columns:
        df = normalize_str_column(df, "email")
    if "country" in df.columns:
        df = normalize_country(df, "country")

    # Missing values
    if "age" in df.columns:
        df = fill_missing(df, "age", strategy="median")

    # Duplicates
    if "email" in df.columns:
        df = drop_duplicates(df, subset=["email"])

    # Enrichment
    if {"first_name", "last_name"}.issubset(df.columns):
        df = add_full_name(df)
    if "age" in df.columns:
        df = add_is_adult(df, age_column="age")

    return df
```

This centralizes transformation rules for a specific dataset (e.g., users) and makes the logic easier to test and maintain.

---

## 6. Expected ETL pipeline usage

The Transform module is called after Extract and before Load.

Typical pattern:

```python
def run_transform_phase(data_sources: dict[str, pd.DataFrame]) -> pd.DataFrame:
    # Example: select a single source to transform
    df_users = data_sources.get("csv")  # or "api", "json", etc.
    if df_users is None:
        raise ValueError("No users DataFrame provided in data_sources.")

    df_transformed = transform_users(df_users)
    return df_transformed
```

The output is a clean, typed, and normalized `DataFrame` ready to be persisted or served to downstream systems.

---

## 7. Expected outcomes

Once the Transform module is implemented, the following should be available:

- Reusable functions for type conversion, date parsing, and string normalization.
- Defined strategies for missing-value handling and deduplication.
- Basic normalization of key categories (e.g. country).
- Derived fields that add analytical value.
- A single orchestration function applying all transformations consistently to the target dataset.
