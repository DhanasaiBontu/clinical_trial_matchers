import json
from statistics import mean

def evaluate(results_path="data/results.json"):
    with open(results_path, "r") as f:
        results = json.load(f)

    total_patients = len(results)
    matched_patients = sum(1 for r in results if r["matches"])
    total_matches = sum(len(r["matches"]) for r in results)
    all_scores = [match["score"] for r in results for match in r["matches"]]

    print("📊 Evaluation Metrics")
    print(f"Total Patients         : {total_patients}")
    print(f"Patients Matched       : {matched_patients}")
    print(f"Match Coverage         : {matched_patients / total_patients * 100:.2f}%")
    print(f"Total Matches Found    : {total_matches}")
    print(f"Avg. Matches/Patient   : {total_matches / total_patients:.2f}")
    print(f"Avg. Match Score       : {mean(all_scores):.2f}" if all_scores else "Avg. Match Score: N/A")

if __name__ == "__main__":
    evaluate()
