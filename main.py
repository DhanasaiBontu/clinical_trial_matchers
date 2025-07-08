import json
from matcher.matcher import match_patient_to_trial

def load_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def run_matching():
    patients = load_json("data/patients.json")
    trials = load_json("data/trials.json")
    all_results = []

    for patient in patients:
        patient_results = []
        for trial in trials:
            match = match_patient_to_trial(patient, trial)
            if match["score"] > 0:
                patient_results.append(match)
        
        # Sort matches by descending score
        top_matches = sorted(patient_results, key=lambda x: x["score"], reverse=True)[:5]  # Top 5 only
        all_results.append({
            "patient_id": patient["patient_id"],
            "matches": top_matches
        })

    save_json("data/results.json", all_results)
    print(f"✅ Matching completed. Results saved to data/results.json")

if __name__ == "__main__":
    run_matching()
