from linebot.models import (RichMenu, RichMenuArea,
                            RichMenuBounds, RichMenuResponse, RichMenuSize)
from linebot.models import URIAction, PostbackAction


def font_richmenu(line_bot_api):
    rich_menu_to_create = RichMenu(
        size=RichMenuSize(width=2500, height=843),
        selected=False,
        name="select font",
        chat_bar_text="Select font",
        areas=[RichMenuArea(
            bounds=RichMenuBounds(x=0, y=0,
                                  width=1250, height=843//2),
            action=URIAction(
                label='Mathematical bold',
                uri='https://line.me')
        ),
            RichMenuArea(
            bounds=RichMenuBounds(x=1250, y=0,
                                  width=1250, height=843//2),
            action=URIAction(
                label='Mathmatical italic',
                uri='https://line.me'
            )
        )
        ]
    )

    return rich_menu_to_create
