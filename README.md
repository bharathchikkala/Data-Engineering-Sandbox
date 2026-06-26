# Automated Job Market Intelligence Pipeline

This repository contains the architecture and production code for an end-to-end Data Engineering pipeline. The project focuses on extracting unstructured job market data, applying rigorous data cleaning and normalization techniques, and persisting the processed data into a structured MySQL database for business intelligence.

## Pipeline Architecture
This pipeline follows a standard ETL (Extract, Transform, Load) workflow:

Extraction (E): Utilizes `Selenium` and `BeautifulSoup` to bypass web dynamic-loading constraints and scrape unstructured job postings.
*   Transformation (T):Leverages `Pandas` and `NumPy` to perform complex data wrangling. This includes:
    *   Normalizing inconsistent salary and experience metrics.
    *   Handling null-value data imputation to ensure 95%+ data integrity.
    *   Resolving delimiter inconsistencies.
*   Loading (L):Implements a robust connection to `MySQL`, bypassing memory constraints by generating optimized SQL instruction scripts for native execution.

## Tech Stack
*   Languages: Python, Advanced SQL
*   Data Processing: Pandas, NumPy
*   Web Scraping: Selenium, BeautifulSoup, Requests
*   Storage: MySQL
*   Visualization: Power BI, Streamlit

## Key Achievements
*   Successfully engineered a pipeline to handle and clean 42,000+ job listings.
*   Solved complex system-level memory conflicts (Access Violation errors) by refactoring the load process from bulk-streaming to native SQL script generation.
*   Designed a relational database schema optimized for query performance and trend analysis.

---
*Developed by Chikkala Venkata Bharath*
