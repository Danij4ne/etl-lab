
# Technical Documentation — Extract Module (01_extract)

## 1. Overview

The **Extract** module implements the data ingestion phase of the ETL pipeline.  
Its primary responsibility is to read data from different sources (files and APIs), perform basic structural validation, and return homogeneous in-memory structures (mainly `pandas.DataFrame`) ready for transformation.

This module should not contain complex cleaning or business logic; its focus is on safe ingestion and minimum structural guarantees.

---

## 2. Supported data sources

The following source types are considered:

- CSV files
- JSON files (including JSON Lines)
- HTTP APIs (GET requests returning JSON)

Each source type is encapsulated in a dedicated function to promote maintainability and reuse.

---

## 3. Dependencies

The core functions rely on:

```python
import pandas as pd
import requests
from typing import Dict
```

Additional modules such as `logging` can be integrated depending on project needs.

---

## 4. Extraction function interfaces

### 4.1. CSV extraction

Recommended pattern:

```python
def extract_from_csv(path: str, required_columns: set | None = None) -> pd.DataFrame:
    """Read a CSV file and validate minimal structure."""
    try:
        df = pd.read_csv(path)
    except Exception as e:
        raise RuntimeError(f"Failed to read CSV '{path}': {e}")

    if df.empty:
        raise ValueError(f"CSV file '{path}' is empty.")

    if required_columns:
        missing = required_columns.difference(df.columns)
        if missing:
            raise ValueError(
                f"CSV '{path}' is missing required columns: {missing}"
            )

    return df
```

Key aspects:
- Explicit read error handling.
- Empty-file validation.
- Optional required-column validation.

---

### 4.2. JSON extraction

Both standard JSON and JSON Lines (JSONL) are supported.

Recommended function:

```python
def extract_from_json(path: str, lines: bool = False) -> pd.DataFrame:
    """Read a JSON or JSON Lines file and return a DataFrame."""
    try:
        df = pd.read_json(path, lines=lines)
    except Exception as e:
        raise RuntimeError(f"Failed to read JSON '{path}': {e}")

    if df.empty:
        raise ValueError(f"JSON file '{path}' contains no data.")

    return df
```

Usage:
- `lines=False` for regular JSON.
- `lines=True` for JSONL inputs.

---

### 4.3. API extraction

Recommended pattern for simple GET-based JSON APIs:

```python
def extract_from_api(url: str, timeout: int = 10) -> pd.DataFrame:
    """Perform a GET request to an API and convert the JSON response into a DataFrame."""
    try:
        response = requests.get(url, timeout=timeout)
    except requests.RequestException as e:
        raise RuntimeError(f"Connection error calling API '{url}': {e}")

    if response.status_code != 200:
        raise RuntimeError(
            f"Invalid response from API '{url}'. Status code: {response.status_code}"
        )

    try:
        payload = response.json()
    except ValueError as e:
        raise RuntimeError(f"API response is not valid JSON: {e}")

    # Adapt this part to the API's structure
    if isinstance(payload, dict) and "users" in payload:
        data = payload["users"]
    else:
        data = payload

    df = pd.DataFrame(data)

    if df.empty:
        raise ValueError(f"API '{url}' returned no usable data.")

    return df
```

Key aspects:
- Network error handling.
- HTTP status validation.
- Safe JSON parsing.
- Adaptation to typical API payload structures.

---

### 4.4. Aggregation of sources: `extract_all`

In multi-source scenarios, a single orchestrating function is recommended:

```python
def extract_all(
    csv_path: str | None = None,
    json_path: str | None = None,
    api_url: str | None = None,
) -> Dict[str, pd.DataFrame]:
    """Coordinate extraction from multiple sources and return a dictionary of DataFrames."""
    results: Dict[str, pd.DataFrame] = {}

    if csv_path:
        results["csv"] = extract_from_csv(csv_path)

    if json_path:
        results["json"] = extract_from_json(json_path)

    if api_url:
        results["api"] = extract_from_api(api_url)

    if not results:
        raise ValueError("No data sources were provided for extraction.")

    return results
```

Benefits:
- Single entry point for the Extract phase.
- Easier orchestration from a `main()` or upper-level script.
- Configurable use of each data source.

---

## 5. Expected ETL pipeline usage

These functions are intended to be used by higher-level orchestration components, such as:

- main pipeline scripts,
- project-level modules (for example, `final_project.py`),
- external schedulers (e.g., Airflow, cron jobs).

Example usage:

```python
def run_extract_phase() -> Dict[str, pd.DataFrame]:
    csv_path = "data/users.csv"
    json_path = "data/users_extra.json"
    api_url = "https://dummyjson.com/users?limit=10"

    data_sources = extract_all(
        csv_path=csv_path,
        json_path=json_path,
        api_url=api_url,
    )

    return data_sources
```

The output of this phase should be a well-defined set of `DataFrame` objects, structurally consistent and ready for the Transform module. No advanced cleaning or business rules should be applied at this stage.

---

## 6. Expected outcomes

Once this module is implemented, the following should be available:

- Robust, reusable, and testable extraction functions.
- Consistent support for CSV, JSON, and basic REST APIs.
- Minimal validation to avoid propagating empty or structurally invalid datasets.
- A clear contract towards the Transform phase, based on well-structured DataFrames.
