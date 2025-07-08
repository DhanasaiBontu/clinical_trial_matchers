import json
import matplotlib.pyplot as plt
import seaborn as sns
import os
from collections import Counter

# Load results
with open("data/results.json", "r", encoding="utf-8") as f:
    results = json.load(f)

# Load patient & trial data
with open("data/patients.json", "r", encoding="utf-8") as f:
    patients = {p["patient_id"]: p for p in json.load(f)}

with open("data/trials.json", "r", encoding="utf-8") as f:
    trials = {t["trial_id"]: t for t in json.load(f)}

# Ensure output folder
os.makedirs("plots", exist_ok=True)

# 1. Number of Trials Matched per Patient
match_counts = [len(r["matches"]) for r in results]
plt.figure()
sns.histplot(match_counts, bins=10, kde=True)
plt.title("Number of Trials Matched per Patient")
plt.xlabel("Trial Count")
plt.ylabel("Patient Count")
plt.savefig("plots/trials_per_patient.png")
plt.close()

# 2. Distribution of Match Scores
all_scores = []
for r in results:
    for m in r["matches"]:
        all_scores.append(m["score"])
plt.figure()
sns.histplot(all_scores, bins=20, kde=True)
plt.title("Distribution of Match Scores")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.savefig("plots/score_distribution.png")
plt.close()

# 3. Match Count by Condition
condition_counts = Counter()
for r in results:
    patient = patients.get(r["patient_id"])
    if patient:
        for cond in patient["conditions"]:
            condition_counts[cond] += len(r["matches"])
top_conditions = condition_counts.most_common(10)
labels, values = zip(*top_conditions)
plt.figure()
sns.barplot(x=list(values), y=list(labels))
plt.title("Match Count by Condition (Top 10)")
plt.xlabel("Matches")
plt.ylabel("Condition")
plt.savefig("plots/matches_by_condition.png")
plt.close()

# 4. Top 10 Most Matched Trials
trial_counter = Counter()
for r in results:
    for m in r["matches"]:
        trial_counter[m["trial_id"]] += 1
top_trials = trial_counter.most_common(10)
trial_names = [trials[t[0]]["title"][:40] + "..." for t in top_trials]
trial_values = [t[1] for t in top_trials]
plt.figure(figsize=(10, 6))
sns.barplot(x=trial_values, y=trial_names)
plt.title("Top 10 Most Matched Trials")
plt.xlabel("Match Count")
plt.ylabel("Trial Title")
plt.tight_layout()
plt.savefig("plots/top_matched_trials.png")
plt.close()

print("✅ Visualizations saved to 'plots/' folder.")
