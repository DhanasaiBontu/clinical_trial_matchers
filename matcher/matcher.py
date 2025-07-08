import re

def normalize(text):
    return text.lower().strip() if isinstance(text, str) else ""

def match_patient_to_trial(patient, trial):
    score = 0
    reasons = []

    # Match condition
    trial_condition = normalize(trial.get("condition", ""))
    patient_conditions = [normalize(cond) for cond in patient.get("conditions", [])]
    if trial_condition in patient_conditions:
        score += 30
        reasons.append("✅ Condition matched")

    # Match location (partial match)
    if normalize(patient["location"]) in normalize(trial.get("location", "")):
        score += 20
        reasons.append("✅ Location matched")

    # Match age (basic check via eligibility criteria text)
    age = patient["age"]
    eligibility = normalize(trial.get("inclusion", ""))
    if any(keyword in eligibility for keyword in ["18 years", "above 18", "adult"]):
        if age >= 18:
            score += 20
            reasons.append("✅ Age eligible")

    # Keyword overlap (basic NLP-style bonus)
    overlap_keywords = ["non-smoker", "type 2", "obese", "pregnant", "hypertension", "metformin"]
    matches = [kw for kw in overlap_keywords if kw in eligibility]
    score += len(matches) * 5
    if matches:
        reasons.append(f"✅ Keyword match: {', '.join(matches)}")

    return {
        "trial_id": trial["trial_id"],
        "trial_title": trial["title"],
        "score": score,
        "match_reasons": reasons
    }
