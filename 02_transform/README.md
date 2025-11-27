# Module 02 — Transform

The Transform module prepares datasets extracted from different sources by applying normalization, conversions, and cleaning operations. It produces consistent DataFrames suitable for downstream integration.

## Tools and Libraries Used
- pandas for DataFrame manipulation, calculations, conversions, and cleanup  
- os when referencing dataset paths

## Purpose
This module processes raw input into clean, standardized structures. It includes unit conversions, string normalization, missing-value handling, duplicate removal, and creation of derived metrics such as BMI.

## Concepts Addressed
- Metric conversions (height, weight)
- Text normalization (strip, lower, title-case)
- Missing-value strategies
- Duplicate removal
- Computed fields
- Preparation of final clean datasets

## Exercises Included
- exercises_guided.py  
- exercises_unguided.py  

## Module Summary
The Transform module enforces structural and semantic consistency across datasets. It acts as the main data preparation layer before loading or integration with additional systems.
