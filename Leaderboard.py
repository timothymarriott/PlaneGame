
import json
import requests
import os
from types import SimpleNamespace
import httpx

def UploadScore(score: int):
    url = "https://prog1942remake-d9fb.restdb.io/rest/score"

    headers = {
    'content-type': "application/json",
    'x-apikey': "901fa6859afb6617b3fd1ec3b265f15e0e04c",
    'cache-control': "no-cache"
    }

    get = requests.request("GET", url, headers=headers)
    getData = json.loads(get.text, object_hook=lambda d: SimpleNamespace(**d))
    for user in getData:
        print(user.Name + " has score " + str(user.Score))
        if user.Name == os.path.expanduser("~").replace("/Users/", ""):
            requests.request("DELETE", url + "/" + str(user._id), headers=headers)

    payload = "{\"Name\":\"" + os.path.expanduser("~").replace("/Users/", "") + "\", \"Score\":" + str(score) +"}"
    response = requests.request("POST", url, data=payload, headers=headers)

    

    print(response.status_code)
