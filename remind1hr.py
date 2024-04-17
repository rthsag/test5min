import time
import datetime
import requests

# Replace 'YOUR_LINE_NOTIFY_TOKEN' with your LINE Notify access token
LINE_NOTIFY_TOKEN = 'l38caB3QMJ5VjrZe5sDe49AS6Efcbn1JGSTbfRE94Fb'

def send_reminder():
    message = "It's time to take a break! Stand up, stretch, or take a quick walk around your room!"
    headers = {'Authorization': f'Bearer {LINE_NOTIFY_TOKEN}'}
    payload = {'message': message}
    requests.post('https://notify-api.line.me/api/notify', headers=headers, data=payload)

def main():
    while True:
        current_time = datetime.datetime.now().time()
        # Check if the current time is between 9 am and 1 pm
        if datetime.time(9, 0) <= current_time <= datetime.time(18, 0):
            # Send reminder
            send_reminder()
        # Wait for 60 minutes
        time.sleep(30*60)

if __name__ == "__main__":
    main()
