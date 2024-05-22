
import json
import requests
import os


def UploadScore(score: int):
    url = "https://prog1942remake-d9fb.restdb.io/rest/score"

    headers = {
    'content-type': "application/json",
    'x-apikey': "901fa6859afb6617b3fd1ec3b265f15e0e04c",
    'cache-control': "no-cache"
    }

    payload = "{\"Name\":\"" + os.path.expanduser("~").replace("/Users/", "") + "\", \"Score\":" + str(score) +"}"
    print(payload)
    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.status_code)
