# -*- coding: utf-8 -*-

import os
import sys

from flask import Flask, request, abort, session
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextSendMessage, TextMessage, PostbackEvent,
)

from textgen import transform
from richmenu import font_richmenu

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('YOUR_CHANNEL_SECRET', None)
channel_access_token = os.getenv('YOUR_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify YOUR_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify YOUR_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

rich_menu_id = line_bot_api.create_rich_menu(rich_menu=font_richmenu())
with open("img/menu.png", "rb") as f:
    line_bot_api.set_rich_menu_image(rich_menu_id, 'image/png', f)

line_bot_api.set_default_rich_menu(rich_menu_id)


@app.route('/')
def hello():
    name = "Hello world"
    return name


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(PostbackEvent)
def change_font(event):
    session['font'] = event.postback.data
    LineBotApi.reply_message(
        event.reply_token,
        TextSendMessage(text=transform("font changed", session['font']))
    )


@handler.add(MessageEvent, message=TextMessage)
def transform_text(event):
    if session['font']:
        result = transform(event.message.text, session['font'])
    else:
        result = transform(event.message.text, "MATHEMATICAL_BOLD")
    if result is not None:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=result)
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Error has occured. Please retry.")
        )


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
