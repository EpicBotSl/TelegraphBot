from pyrogram import Client, filters
import os
from pyrogram.types import*

client = Client

@Client.on_message(filters.command("write"))
async def handwriting(_, message):
    if len(message.command) < 2:
        return await message.reply_text("» Gɪᴠᴇ Sᴏᴍᴇ Tᴇxᴛ Tᴏ Wʀɪᴛᴇ Iᴛ Oɴ Mʏ Cᴏᴩʏ...")
    m = await message.reply_text("» Wᴀɪᴛ A Sᴇᴄ, Lᴇᴛ Mᴇ Wʀɪᴛᴇ Tʜᴀᴛ Tᴇxᴛ...")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    hand = "https://apis.xditya.me/write?text=" + name
    await m.edit("Uᴩʟᴏᴀᴅɪɴɢ...")
    await client.send_photo(message.chat_id, hand, caption="Wʀɪᴛᴛᴇɴ Wɪᴛʜ 🖊 Bʏ [ɴᴀᴠᴀɴᴊᴀɴᴀ](t.me/ImNavanjana)")

print("""
#╔════╗────────╔═══╗
#║╔╗╔╗║────────║╔══╝
#╚╝║║╠╩═╦══╦╗╔╗║╚══╦══╦╦══╗
#──║║║║═╣╔╗║╚╝║║╔══╣╔╗╠╣╔═╝
#──║║║║═╣╔╗║║║║║╚══╣╚╝║║╚═╗
#──╚╝╚══╩╝╚╩╩╩╝╚═══╣╔═╩╩══╝
#──────────────────║║
#──────────────────╚╝
""")
