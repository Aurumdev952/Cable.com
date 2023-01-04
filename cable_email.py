import requests
import os
from dotenv import load_dotenv

load_dotenv()

MAILTRAP_API_TOKEN = os.getenv('MAILTRAP_API_TOKEN')
print(MAILTRAP_API_TOKEN)
url = "https://send.api.mailtrap.io/api/send"
def generate_html(data):
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>cable found</title>
</head>
<body style="background-color: rgb(237,241,245);">
    <pre style="color: rgb(92,114,138); font-size: 16px; text-align:left; margin: 0 auto; display: inline;">

        Hello,

        I wanted to let you know that your cable was found by {data['name']}. 
        
        If you would like to come by and pick it up, please contact {data['name']} via
        email: {data['email']}
        slack: {data['slack']}



        Thank you,


        Cable.com
    </pre>
</body>
</html>'''
    return html
def send_email(data):
    payload = {
        "to": [
            {
                "email": data['receiver']['email'],
                "name": data['receiver']['name'],
            }
        ],
        "from": {
            "email": "benjamugi2007@gmail.com",
            "name": "Cable.com"
        },
        "html": generate_html(data['sender']),
        "headers": {
            "X-Message-Source": "dev.mydomain.com",
            "X-MT-Category":"Notification"
        },
        "subject": "Found cable",
        "text": f'''
        Hello,

        I wanted to let you know that your cable was found by {data['sender']['name']}. 
        
        If you would like to come by and pick it up, please contact {data['sender']['name']} via
        email: {data['sender']['email']}
        slack: {data['sender']['slack']}



        Thank you,


        Cable.com
        ''',
        "category": "Notification"
    }
    headers = {
        "Content-Type": "application/json",
        "Api-Token": MAILTRAP_API_TOKEN
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)


send_email({
    "receiver": {
        "email": "benjamugi20072@gmail.com",
        "name": "benjamin"
    },
    "sender": {
        "email": "benjamugi20072@gmail.com",
        "name": "benjamin",
        "slack": "benjamin ishimwe"
    }
})