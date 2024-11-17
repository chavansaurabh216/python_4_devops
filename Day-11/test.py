import requests



response_url = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_response = response_url.json()

# print (complete_response[0]["user"]["login"])


for users in range(len(complete_response)):
    output = complete_response[users]["user"]["login"]
    print(output)