from flask import Flask, request
from setup import (
    SECRET_PASS, 
    CONFIRMATION_RESPONSE, 
    ACCESS_CODE
)


app = Flask(__name__)


def secret_is_valid(secret: str) -> bool:
    return secret == SECRET_PASS


def incoming_message(user_id: str, message_text: str):
    print(f"GET: from {user_id}: {message_text}")


@app.route("/callback", methods=['POST'])
def handle_callback():
    content = request.json
    
    if content['type'] == 'confirmation':
        return CONFIRMATION_RESPONSE, 200
    if content['type'] == 'message_new':
        if secret_is_valid(content['secret']):
            message = content['object']['message']
            incoming_message(message['from_id'], message['text'])
            return "Ok", 200
    
    return 'Unknown callback type', 400


@app.route("/message", methods=['POST'])
def send_message():
    content = request.json




app.run(debug=True, port=8070)