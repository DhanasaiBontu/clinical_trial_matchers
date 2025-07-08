# Clinical Trial Patient Matching System

## Overview

This project aims to build an intelligent system that matches patient profiles to relevant clinical trials based on eligibility criteria. It leverages real-world datasets from ClinicalTrials.gov and simulates patient data to perform eligibility-based matching and ranking.

## Problem Statement

Develop a system that:
- Parses real clinical trial data and extracts eligibility criteria.
- Generates synthetic patient profiles.
- Scores and ranks clinical trials for each patient based on match quality.
- Outputs a ranked list of suitable clinical trials for each patient.

## Project Structure

clinical_trial_matchers/
├── data/
│ ├── raw_trails/
│ │ ├── Asthama_India/
│ │ ├── Cancer_India/
│ │ ├── Diabetes_India/
│ │ └── Hypertension_India/
│ ├── patients.json # Synthetic patient profiles
│ ├── trials.json # Extracted trial data from raw_trails
│ └── results.json # Matching results (patient ↔ trials)
│
├── matcher/
│ └── matcher.py # Trial-patient matching logic
│
├── plots/ # Output folder for visual graphs (created by visualize.py)
├── reports/ # Summary reports and evaluation metrics output
│
├── extract_trials.py # Parses raw JSON from raw_trails into trials.json
├── generate_patients.py # Creates synthetic patient data into patients.json
├── generate_reports.py # Creates reports from results.json (optional/extendable)
├── main.py # Main execution script that performs trial matching
├── visualize.py # Visualization of match statistics
├── evaluation.py # Match performance metrics (e.g., coverage, scores)
├── requirements.txt # Required Python packages
└── README.md # Project overview, instructions, and documentation

## Features

- Parses real clinical trial eligibility from JSON.
- Simulates realistic patient data (demographics, conditions).
- Performs criteria-based matching with scoring.
- Outputs results in structured format (JSON).
- Provides visualizations (bar charts, distributions).
- Calculates evaluation metrics.

## Evaluation Metrics

The system computes performance metrics after matching to assess the quality of recommendations.

| Metric                 | Description                                                   |
|------------------------|---------------------------------------------------------------|
| Match Coverage (%)     | Percentage of patients with at least one matched trial        |
| Avg. Matches/Patient   | Average number of trials matched per patient                  |
| Avg. Match Score       | Average score of matched trials (0 to 1)                      |

Run the evaluation script to view metrics

## Setup Instructions

1. **Clone the repository**
   git clone https://github.com/DhanasaiBontu/clinical_trial_matchers.git
   cd clinical_trial_matchers

2. **Set Up a Virtual Environment (Windows)**
    python -m venv venv
    venv\Scripts\activate

3. **Install Dependencies**
    pip install -r requirements.txt

4. **Extract Trial Data**
    Make sure folders like Asthama_India/, Cancer_India/, etc. are inside data/raw_trails/.
    python extract_trials.py

5. **Generate Synthetic Patients**
    python generate_patients.py

6. **Run the Matching Pipeline**
    python main.py

7. **Visualize Results**
    python visualize.py

8. **Evaluate Matching Performance**
    python evaluation.py
