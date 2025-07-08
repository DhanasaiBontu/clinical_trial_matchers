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

```
clinical_trial_matchers/
├── data/
│   ├── raw_trails/
│   │   ├── Asthama_India/
│   │   ├── Cancer_India/
│   │   ├── Diabetes_India/
│   │   └── Hypertension_India/
│   ├── patients.json          # Synthetic patient profiles
│   ├── trials.json            # Extracted trial data from raw_trails
│   └── results.json           # Matching results (patient ↔ trials)
├── matcher/
│   └── matcher.py             # Trial-patient matching logic
├── plots/                     # Output folder for visual graphs
├── reports/                   # Summary reports and evaluation metrics
├── extract_trials.py          # Parses raw JSON into trials.json
├── generate_patients.py       # Creates synthetic patients into patients.json
├── generate_reports.py        # Creates reports from results.json
├── main.py                    # Main execution script
├── visualize.py               # Visualize match statistics
├── evaluation.py              # Match performance metrics (coverage, scores)
├── requirements.txt           # Required Python packages
└── README.md                  # Project overview and documentation
```


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

3. **Set Up a Virtual Environment (Windows)**
    python -m venv venv
    venv\Scripts\activate

4. **Install Dependencies**
    pip install -r requirements.txt

5. **Extract Trial Data**
    Make sure folders like Asthama_India/, Cancer_India/, etc. are inside data/raw_trails/.
    python extract_trials.py

6. **Generate Synthetic Patients**
    python generate_patients.py

7. **Run the Matching Pipeline**
    python main.py

8. **Visualize Results**
    python visualize.py

9. **Evaluate Matching Performance**
    python evaluation.py
