import os
import json

def extract_trial_data(raw_folder="data/raw_trails", out_file="data/trials.json"):
    trials = []

    for subfolder in os.listdir(raw_folder):
        subfolder_path = os.path.join(raw_folder, subfolder)
        if os.path.isdir(subfolder_path):
            for filename in os.listdir(subfolder_path):
                if filename.endswith(".json"):
                    file_path = os.path.join(subfolder_path, filename)
                    with open(file_path, "r", encoding="utf-8") as f:
                        try:
                            data = json.load(f)
                            section = data.get("protocolSection", {})

                            trial = {
                                "trial_id": section.get("identificationModule", {}).get("nctId", "N/A"),
                                "title": section.get("identificationModule", {}).get("briefTitle", "N/A"),
                                "inclusion": section.get("eligibilityModule", {}).get("eligibilityCriteria", "N/A"),
                                "exclusion": "",  # Optional: Extract from exclusion criteria if available separately
                                "location": (
                                    section.get("contactsLocationsModule", {})
                                    .get("locations", [{}])[0]
                                    .get("country", "N/A")
                                ),
                                "condition": (
                                    section.get("conditionsModule", {})
                                    .get("conditions", ["N/A"])[0]
                                )
                            }

                            trials.append(trial)
                        except Exception as e:
                            print(f"⚠️ Error processing {filename}: {e}")

    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(trials, f, indent=2)

    print(f"✅ Extracted {len(trials)} trials to {out_file}")


if __name__ == "__main__":
    extract_trial_data()
