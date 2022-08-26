import json
import logging
import os

import requests
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv('WEBHOOK_URL')


def send_notification(text):
    message = f'*Notification using Webhook*\n{text}'  # *(asterisk) to make title bold
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({'text': message})

    response = requests.post(WEBHOOK_URL, data=data, headers=headers)
    if response.status_code == 200:
        logging.info(f'"{text}" has been notified.')
    else:
        logging.info(f'Error: "{text}" has been not been notified due to {response.reason}')


if __name__ == '__main__':
    logging.basicConfig(filename='log/notification.txt', format='%(asctime)s %(message)s', level=logging.INFO)

    send_notification('Have a good day')
