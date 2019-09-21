import requests
import json
import time
from PIL import Image
from io import BytesIO
import os

url = "api.gotinder.com"

headers = {
    'app_version': '6.9.4',
    'platform': 'ios',
    "content-type": "application/json",
    "User-agent": "Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00)",
    "Accept": "application/json",
    "X-Auth-Token":"2995b390-aa88-45c6-9821-6344366066bc"
}

#fb_auth_token = "EAALaH6pXhXcBAPdLSj5zZCIRkfhZAe62MMSQkjRk75qSM0dV1E0oNRBGTLDR5u4xAOSD51lRk5jt8XETYgWF2otRZBYUqLfxVMwyVUwBf2LZC9yOzlzAoaiZAV5yor3NLnQRLvazbPw3tnKoKdIm9Mmym5nlZCghU2nRAClTx9zanEx5dEejFHIZAqm2qSooFsilmOyW2dyYgZDZD"
#fb_user_id = "2331555803775033"



#req = requests.post("https://api.gotinder.com/auth",
#                    headers=headers,
#                    data=json.dumps(
#                        {'facebook_token': fb_auth_token, 'facebook_id': fb_user_id})
#                    )
#print(req.headers)
os.chdir("/Users/matthewbrun/Desktop/Tinder")
while 0 < 1:
    ids = []
    req = requests.get("https://api.gotinder.com/user/recs", headers=headers).json()
    for profile in req['results']:
        ids.append(profile["_id"])
        photo = requests.get(profile['photos'][0]['url'])
        img = Image.open(BytesIO(photo.content))
        img.save(str(profile["_id"])+".jpeg", "JPEG")
        for id in ids:
            left = requests.get("https://api.gotinder.com/pass/"+id, headers=headers)
    time.sleep(.5)