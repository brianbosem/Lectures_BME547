import requests

server_name = "http://vcm-7631.vm.duke.edu:5002/"
ID_dict = requests.get(server_name + "get_patients/bab97")
# print(ID_dict.text)
donor_ID = ID_dict.text[10] + ID_dict.text[11]
recipient_ID = ID_dict.text[27] + ID_dict.text[28]
# print(donor_ID)
# print(recipient_ID)

donor_bloodtype = requests.get(server_name + "get_blood_type/" + donor_ID)
# print(donor_bloodtype.text)
recipient_bloodtype = requests.get(server_name + "get_blood_type/" + recipient_ID)
# print(recipient_bloodtype.text)

if donor_bloodtype == recipient_bloodtype:
    type_match = True
else:
    type_match = False
print(type_match)

# request_json = {"Name": "bab97", "Match": "No"}
# r = requests.post(server_name + "match_check", json=request_json)
# if r.status_code != 200:
#     print(r.text)
# else:
#     print(r.json())