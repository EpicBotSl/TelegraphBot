import os
from config import *
from pyrogram import *
from pyrogram.types import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from pyrogram.types import Message
import logging
from telegraph import upload_file
from urllib.parse import quote
import asyncio

app = Client(
    "Team Epic",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("webss"))
async def take_ss(_, message: Message):
    try:
        if len(message.command) != 2:
            return await message.reply_text(
                "Give A Url To Fetch Screenshot."
            )
        url = message.text.split(None, 1)[1]
        m = await message.reply_text("**Taking Screenshot**")
        await m.edit("**Uploading**")
        try:
            await message.reply_photo(
                photo=f"https://webshot.amanoteam.com/print?q={url}",
                quote=False,
            )
        except TypeError:
            return await m.edit("No Such Website.")
        await m.delete()
    except Exception as e:
        await message.reply_text(str(e))

#---------------------------Gen Logo Epic-------------------------------------#

@app.on_message(filters.media & filters.private)
def ul(_, message):
    reply = message.reply_to_message
       reply.media:
        i = message.reply("**ᴘʀᴏᴄᴇꜱꜱɪᴏɴ...**")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x
        i.edit("**ᴄᴏᴠᴇʀᴛɪᴏɴ..**")
        i.edit("**🙂එතකම් සිම්දුවක් අහමුත**")
        i.edit("**වැඩ**")
        i.edit("**කරන**")
        i.edit("**අපේ**")
        i.edit("**විරුවා**")
        i.edit("**ටාගෝබය😂😂**") 
        i.edit("**😪හරි හරි ඉ‍‍ඳාම් ලිම්ක් එක දෙම්නම්**") 
        i.edit("**⛀⛀⛀⛀⛀⛀⛀**")
        i.edit("**⛁⛀⛀⛀⛀⛀⛀**")
        i.edit("**⛁⛁⛀⛀⛀⛀⛀**")
        i.edit("**⛁⛁⛁⛀⛀⛀⛀**")
        i.edit("**⛁⛁⛁⛁⛀⛀⛀**")
        i.edit("**⛁⛁⛁⛁⛁⛀⛀**")
        i.edit("**⛁⛁⛁⛁⛁⛁⛀**")
        i.edit("**⛁⛁⛁⛁⛁⛁⛁**")
        xy = 't.me/share/url?url=' + quote(url)
        i.edit(f'ʏᴏᴜʀ ᴏᴅᴇʀ🖨️ ⇰ `{url}`', reply_markup=InlineKeyboardMarkup([[
                 InlineKeyboardButton('🎊 ᴏᴘᴇɴ', url=url),
                 InlineKeyboardButton('📤 ꜱʜᴀʀᴇ', url=xy),
                 ]]), disable_web_page_preview=True)




#╔════╗────────╔═══╗
#║╔╗╔╗║────────║╔══╝
#╚╝║║╠╩═╦══╦╗╔╗║╚══╦══╦╦══╗
#──║║║║═╣╔╗║╚╝║║╔══╣╔╗╠╣╔═╝
#──║║║║═╣╔╗║║║║║╚══╣╚╝║║╚═╗
#──╚╝╚══╩╝╚╩╩╩╝╚═══╣╔═╩╩══╝
#──────────────────║║
#──────────────────╚╝

print("""
╔════╗────────╔═══╗
║╔╗╔╗║────────║╔══╝
╚╝║║╠╩═╦══╦╗╔╗║╚══╦══╦╦══╗
──║║║║═╣╔╗║╚╝║║╔══╣╔╗╠╣╔═╝
──║║║║═╣╔╗║║║║║╚══╣╚╝║║╚═╗
──╚╝╚══╩╝╚╩╩╩╝╚═══╣╔═╩╩══╝
──────────────────║║
──────────────────╚╝""")

app.run()
