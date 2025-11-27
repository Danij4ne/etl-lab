# Module 01 — Extract

The Extract module focuses on retrieving raw data from different sources and converting them into structured pandas DataFrames suitable for the next stages of the ETL workflow.

## Tools and Libraries Used
- pandas for file-based data loading
- requests for HTTP API requests
- os for path handling when applicable

## Purpose
This module centralizes data ingestion operations. It loads datasets from local storage or external endpoints and ensures that the resulting structures are valid for transformation. Its scope is limited to safe ingestion, without applying business logic or cleaning layers.

## Concepts Addressed
- CSV, JSON, and JSON Lines extraction  
- API-based extraction (GET requests returning JSON)
- Basic structural validation  
- Multi-source extraction coordination

## Exercises Included
- exercises_guided.ipynb  
- exercises_unguided.py  

## Module Summary
The Extract module provides consistent entry points for obtaining raw datasets in predictable structures. It supports heterogeneous formats while maintaining separation from transformation and loading responsibilities.
