import os
import json

# Load data
with open("data/patients.json", "r", encoding="utf-8") as f:
    patients = {p["patient_id"]: p for p in json.load(f)}

with open("data/trials.json", "r", encoding="utf-8") as f:
    trials = {t["trial_id"]: t for t in json.load(f)}

with open("data/results.json", "r", encoding="utf-8") as f:
    results = json.load(f)

# Create reports directory
os.makedirs("reports", exist_ok=True)

# Generate reports
for result in results:
    patient_id = result["patient_id"]
    patient = patients.get(patient_id)

    report_lines = [
        f"Patient ID: {patient_id}",
        f"Age: {patient['age']}",
        f"Gender: {patient['gender']}",
        f"Conditions: {', '.join(patient['conditions'])}",
        "-" * 40,
        "Top Matched Trials:\n"
    ]

    if not result["matches"]:
        report_lines.append("No suitable trials found.\n")
    else:
        for idx, match in enumerate(result["matches"], 1):
            trial = trials.get(match["trial_id"], {})
            report_lines.extend([
                f"{idx}. {trial.get('title', 'N/A')}",
                f"   Location: {trial.get('location', 'N/A')}",
                f"   Score: {match['score']:.2f}",
                f"   Inclusion Snippet: {trial.get('inclusion', 'N/A')[:200]}...",
                ""
            ])

    # Save to file
    with open(f"reports/{patient_id}.txt", "w", encoding="utf-8") as report_file:
        report_file.write("\n".join(report_lines))

print("✅ All patient reports generated in 'reports/' folder.")
