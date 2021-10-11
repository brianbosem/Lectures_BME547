import requests

server_name = "http://vcm-7631.vm.duke.edu:5002/"

r = requests.get(server_name + "get_patients/bab97")
print(r.text)
