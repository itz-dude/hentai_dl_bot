from pyrogram import *
from pyrogram.types import *

def start(client, message):
    message.reply_text("""**/search <hentai name> to search**\n Powered By @MangaX_updates [🥳](https://telegra.ph/file/8dd8cc843ae45ebc5b4b5.png)""", parse_mode="markdown")
