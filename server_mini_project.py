import requests


# server_name = "http://vcm-21170.vm.duke.edu:5000/student"

# my_dict = {
#     "name": "Brian Bosem",
#     "net_id": "bab97",
#     "e-mail": "brian.bosem@duke.edu"
# }
# r6 = requests.post(server_name, json=my_dict)
# sum_result = r6.json()
# print(sum_result)

# server_name = "http://vcm-21170.vm.duke.edu:5000/list"
# r = requests.get(server_name)
# print(r.json())

server_name = "http://vcm-21170.vm.duke.edu:5000/sum"
request_json = {
    "a": 1,
    "b": 2
}
r = requests.post(server_name, json=request_json)
if r.status_code != 200:
    print(r.text)
else:
    print(r.json())