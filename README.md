# ETL Pipeline Lab
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![ETL Pipeline](https://img.shields.io/badge/Focus-ETL_Pipeline_Development-2C3E50?style=for-the-badge)
![Modular Architecture](https://img.shields.io/badge/Architecture-3_Modules_+_Projects-0A66C2?style=for-the-badge)
![Extraction](https://img.shields.io/badge/Stage-Extraction_CSV_JSON_API-8E44AD?style=for-the-badge)
![Transformation](https://img.shields.io/badge/Stage-Transformation_Workflows-F39C12?style=for-the-badge)
![Loading](https://img.shields.io/badge/Stage-Loading_CSV_JSON_Excel-27AE60?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/danij4ne/etl-lab?style=for-the-badge)
![Commit Activity](https://img.shields.io/github/commit-activity/m/danij4ne/etl-lab?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-1D8348?style=for-the-badge)

The ETL Pipeline Lab is a structured repository focused on the implementation of Extract, Transform, and Load workflows using Python. The repository is organized into independent modules that isolate the functionality of each ETL stage and provide documentation, exercises, and datasets required for practical data-processing workflows.

---

## Purpose

The purpose of this repository is to provide a modular and well-defined structure for building ETL pipelines. It outlines how data is extracted from multiple formats, transformed through controlled transformation steps, and loaded into standardized output files. Each module documents the specific responsibilities and components associated with its stage in the workflow.

---

## Repository Structure

```
01_extract/
    README.md
    exercises_guided.ipynb
    exercises_unguided.py
    data/

02_transform/
    README.md
    exercises_guided.ipynb
    exercises_unguided.py
    data/

03_load/
    README.md
    exercises_guided.ipynb
    exercises_unguided.py
    data/

04_etl_projects/
    README.md
    guided_etl_notebook.ipynb
    mini_project_1.py
    mini_project_2.py
    final_project.py

README.md
```

Each module includes its own documentation and supporting files.

---

## Module Overview

### **01 — Extract**

This module focuses on controlled data acquisition from multiple source types:

- CSV ingestion
- JSON and JSON Lines ingestion
- API-based extraction using the `requests` library
- Multi-file processing using pattern matching through `glob.glob`
- Consolidation of extracted content into DataFrame structures

### **02 — Transform**

This module handles systematic transformation of structured data:

- Type normalization and conversion
- Missing-value management
- Duplicate detection and resolution
- Numeric transformations
- Text standardization workflows
- Validation logic for ensuring consistent output

### **03 — Load**

This module is responsible for output persistence:

- CSV file generation
- JSON file generation
- Excel export
- Output directory creation
- Timestamp-based file naming
- Error handling for file-write operations

### **04 — ETL Projects**

This directory contains integrated end-to-end pipelines that combine the Extract, Transform, and Load modules:

- Guided ETL notebook
- Independent mini projects
- Final ETL script performing the complete workflow

---

## Conventions and Standards

- All documentation uses English naming and file structure.
- Each module contains a `notes.md` file describing its structure and scope.
- Exercises are separated into:
  - `exercises_guided.ipynb` for structured tasks
  - `exercises_unguided.py` for independent tasks
- Each module stores its datasets inside its local `/data` directory.
- Scripts follow consistent naming and organizational conventions suitable for modular ETL development.

---

## Recommended Usage

- Explore the modules sequentially to review the ETL pipeline structure.
- Consult the module notes to understand the responsibilities and components of each stage.
- Use the project directory to examine full pipeline implementations.
- Modules can be integrated or extended for different datasets or workflows.

---

## Author

Daniel Jane Garcia (danij4ne)
