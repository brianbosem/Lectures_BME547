import requests

patient1 = {"name": "Ann Ables", "id_no": 201, "blood_type": "A+",
            "dob": "1/23/00"}
# patient1 = ["Hello"]
r = requests.post("http://127.0.0.1:5000/new_patient", json=patient1)
print(r.status_code)
print(r.text)
