import os
import json
import requests

from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv('WEBHOOK_URL')

class CustomException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

def send_notification(text):
    message = f'*Notification using Webhook*\n{text}' # *(asterisk) to make title bold
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({'text': message})

    response = requests.post(WEBHOOK_URL, data=data, headers=headers)
    if response.status_code != 200:
        raise CustomException(response.reason)

if __name__ == '__main__':
    send_notification('Have a good day')
