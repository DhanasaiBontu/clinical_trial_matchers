import json
import random
import uuid

diseases = ["Diabetes", "Hypertension", "Cancer", "Asthma"]

locations = [
    "India", "Delhi", "Mumbai", "Hyderabad", "Chennai", "Bangalore", "Pune"
]

ages = list(range(18, 80))
genders = ["Male", "Female", "Other"]

def generate_patients(n=50, out_file="data/patients.json"):
    patients = []

    for _ in range(n):
        patient = {
            "patient_id": str(uuid.uuid4()),
            "age": random.choice(ages),
            "gender": random.choice(genders),
            "location": random.choice(locations),
            "conditions": random.sample(diseases, k=random.randint(1, 2))  # Multi-condition support
        }
        patients.append(patient)

    with open(out_file, "w") as f:
        json.dump(patients, f, indent=2)

    print(f"✅ Generated {n} synthetic patients in {out_file}")


if __name__ == "__main__":
    generate_patients()
