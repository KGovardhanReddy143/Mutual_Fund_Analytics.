# Mutual Fund Analytics

## Project Overview

This project focuses on Mutual Fund Data Analytics. The objective is to ingest, validate, and analyze mutual fund datasets for further reporting and dashboard development.

## Day 1 Tasks Completed

### Project Setup

* Created project folder structure
* Initialized Git repository
* Pushed project to GitHub
* Created requirements.txt

### Data Ingestion

* Loaded 10 mutual fund datasets using Pandas
* Checked dataset shape, data types, and sample records
* Identified basic data anomalies

### Live NAV Fetch

* Fetched live NAV data from MFAPI
* Saved NAV history as CSV files
* Retrieved NAV data for multiple mutual fund schemes

### Fund Master Exploration

* Analyzed unique fund houses
* Analyzed categories and sub-categories
* Reviewed risk categories
* Studied AMFI scheme code structure

### Data Validation

* Validated AMFI codes between fund_master and nav_history datasets
* Confirmed all AMFI codes exist in NAV history
* Generated data quality report

## Technologies Used

* Python
* Pandas
* NumPy
* Requests
* Matplotlib
* Seaborn
* Plotly
* SQLAlchemy

## Project Structure

* data/raw
* data/processed
* scripts
* reports
* notebooks
* sql
* dashboard

## Status

Day 1: Data Ingestion Complete
