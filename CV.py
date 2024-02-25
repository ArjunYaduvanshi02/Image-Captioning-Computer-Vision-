import requests

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

for i in range(1,11):
    loc="Sample_images/"+"img"+str(i)+".jpeg"
    print(query(loc))