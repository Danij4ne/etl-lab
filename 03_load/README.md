
# Technical Documentation — Load Module (03_load)

## 1. Overview

The **Load** module represents the final stage of the ETL pipeline.  
Its purpose is to persist transformed data into one or more output systems:

- Local files (CSV, JSON, Excel)
- Databases
- External systems (APIs, cloud buckets)

This repository documents the standard local-file implementation.

---

## 2. Main responsibilities

- Ensure output directory exists.
- Export DataFrames without data loss.
- Support multiple output formats.
- Handle common file-writing errors.
- Provide a reusable and consistent interface.

---

## 3. Dependencies

```python
import pandas as pd
import os
from datetime import datetime
```

---

## 4. Output directory design

A single output directory is recommended:

```python
OUTPUT_DIR = "output"
```

All load functions write inside this directory.

---

## 5. Load functions

### 5.1. Ensure output directory

```python
def ensure_output_dir(path: str = OUTPUT_DIR) -> None:
    """Create the output directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)
```

---

### 5.2. Save as CSV

```python
def save_csv(df: pd.DataFrame, filename: str) -> str:
    """Save a DataFrame as CSV (no index) and return the file path."""
    ensure_output_dir()
    full_path = os.path.join(OUTPUT_DIR, filename)
    try:
        df.to_csv(full_path, index=False)
    except Exception as e:
        raise RuntimeError(f"Failed to save CSV '{filename}': {e}")
    return full_path
```

---

### 5.3. Save as JSON

```python
def save_json(df: pd.DataFrame, filename: str) -> str:
    """Save a DataFrame in JSON (records) format with indentation."""
    ensure_output_dir()
    full_path = os.path.join(OUTPUT_DIR, filename)
    try:
        df.to_json(full_path, orient="records", indent=2, force_ascii=False)
    except Exception as e:
        raise RuntimeError(f"Failed to save JSON '{filename}': {e}")
    return full_path
```

---

### 5.4. Save as Excel

```python
def save_excel(df: pd.DataFrame, filename: str) -> str:
    """Export a DataFrame to Excel (.xlsx)."""
    ensure_output_dir()
    full_path = os.path.join(OUTPUT_DIR, filename)
    try:
        df.to_excel(full_path, index=False)
    except Exception as e:
        raise RuntimeError(f"Failed to save Excel '{filename}': {e}")
    return full_path
```

---

### 5.5. Timestamped filenames

```python
def with_timestamp(base_name: str, extension: str = "csv") -> str:
    """Generate a timestamped filename: base_YYYYMMDD_HHMMSS.ext"""
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_{ts}.{extension}"
```

---

## 6. Load orchestration function

```python
def load_all(df: pd.DataFrame) -> dict[str, str]:
    """Generate multiple output files and return a dict with their paths."""
    results = {}
    results["csv"] = save_csv(df, with_timestamp("final_data", "csv"))
    results["json"] = save_json(df, with_timestamp("final_data", "json"))
    results["excel"] = save_excel(df, with_timestamp("final_data", "xlsx"))
    return results
```

---

## 7. ETL pipeline usage

```python
def run_load_phase(df: pd.DataFrame) -> None:
    files = load_all(df)
    print("Generated files:")
    for fmt, path in files.items():
        print(f" - {fmt}: {path}")
```

---

## 8. Expected outcomes

- The pipeline produces reproducible, timestamped output files.
- All transformed data is stored consistently.
- Standard support for CSV, JSON, and Excel formats.
- File system errors are properly handled.
