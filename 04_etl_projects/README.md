
# 04_ETL_Projects — Documentation

This module provides a set of practical projects designed to implement complete ETL pipelines using Python.
Its purpose is to consolidate extraction, transformation, and loading concepts and apply them to scenarios closer to real-world data engineering workflows.

---

## 1. Module Objective

The goals of this module are:

- Designing reproducible ETL structures in Python.
- Integrating data from multiple sources (CSV, JSON, APIs).
- Applying consistent and coherent data transformations.
- Defining output formats following best practices.
- Documenting each phase of the process clearly.

---

## 2. Module Components

### 2.1 Mini Project 1
Simple ETL pipeline based on local sources (CSV and JSON).
Covers extraction, transformation, and loading.

### 2.2 Mini Project 2
API-oriented ETL pipeline.
Includes data normalization, error handling, and multi-format export.

### 2.3 Guided ETL Notebook
Interactive notebook describing general ETL structure, modular design, and basic checks.

### 2.4 Final Project
Complete ETL pipeline integrating multiple sources, advanced transformations, and structured loading.

---

## 3. Prerequisites

To complete this module, the following knowledge is required:

- Reading data from CSV, JSON, and HTTP requests.
- Basic proficiency with pandas.
- Understanding of cleaning, normalization, and data typing.
- Basic knowledge of saving data (CSV, JSON, Excel).

---

## 4. Module Structure

```
04_etl_projects/
│── notes.md
│── mini_project_1.py
│── mini_project_2.py
│── guided_etl_notebook.ipynb
│── final_project.py
```

---

## 5. Implementation Guidelines

- Each project should be organized in functions grouped by ETL phase (extract, transform, load).
- Basic validation steps are recommended before the loading phase.
- Code should be reproducible in any Python environment with pandas installed.
- Paths and filenames must remain consistent across the pipeline.

---

## 6. Next Steps

Once all projects are completed, it is recommended to review:

- Full code modularization.
- Basic logging.
- Error handling and exception control.
- Improvements to data read/write efficiency.
