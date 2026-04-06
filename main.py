import json
import requests
import time
import os

def post_to_facebook(message, page_id, token):
    url = f"https://graph.facebook.com/{page_id}/feed"
    payload = {'message': message, 'access_token': token}
    r = requests.post(url, data=payload)
    return r.json()

def start_bot():
    print("AutoPost Myanmar Bot is running...")
    # ဒီနေရာမှာ နောက်ပိုင်း Webhook နဲ့ ချိတ်ဆက်ဖို့ logic တွေ ထပ်ထည့်ပါမယ်
    while True:
        # စာသားဖတ်မည့် အပိုင်း
        time.sleep(10) 

if __name__ == "__main__":
    start_bot()
