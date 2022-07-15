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
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton,
    CallbackQuery, InlineQuery, Message)
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton,
    CallbackQuery, InlineQuery, Message)
import random

app = Client(
    "Team Epic",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)



@app.on_message(filters.photo)
async def uploadphoto(client, message):
  msg = await message.reply_text("Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ...")
  userid = str(message.chat.id)
  img_path = (f"./Download....!/{userid}.jpg")
  img_path = await client.download_media(message=message, file_name=img_path)
  await msg.edit_text("Uploading..... ")
  try:
    tlink = upload_file(img_path)
    link = https://telegra.ph{tlink[0]}
  except:
    await msg.edit_text("`Something went wrong join` @septemberfilms") 
  else:
    await msg.edit_text(f"https://telegra.ph{tlink[0]}", reply_markup=InlineKeyboardMarkup([[
                   InlineKeyboardButton('🎊 ᴏᴘᴇɴ', url="link"),
                   InlineKeyboardButton('📤 ꜱʜᴀʀᴇ', url="link"),
                   ]]), disable_web_page_preview=True) 
    os.remove(img_path) 
    
            

@app.on_message(filters.animation)
async def uploadgif(client, message):
  if(message.animation.file_size < 5242880):
    msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ join` @septemberfilms")
    userid = str(message.chat.id)
    gif_path = (f"./DOWNLOADS/{userid}.mp4")
    gif_path = await client.download_media(message=message, file_name=gif_path)
    await msg.edit_text("`Tʀʏɪɴɢ Tᴏ Uᴘʟᴏᴀᴅ.....`")
    try:
      tlink = upload_file(gif_path)
      await msg.edit_text(f"`https://telegra.ph{tlink[0]}`")   
      os.remove(gif_path)   
    except:
      await msg.edit_text("Something really Happend Wrong... join @septemberfilms") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb join @septemberfilms")

@app.on_message(filters.video)
async def uploadvid(client, message):
  if(message.video.file_size < 5242880):
    msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ join` @septemberfilms")
    userid = str(message.chat.id)
    vid_path = (f"./DOWNLOADS/{userid}.mp4")
    vid_path = await client.download_media(message=message, file_name=vid_path)
    await msg.edit_text("`Tʀʏɪɴɢ Tᴏ Uᴘʟᴏᴀᴅ.....`")
    try:
      tlink = upload_file(vid_path)
      await msg.edit_text(f"`https://telegra.ph{tlink[0]}`")     
      os.remove(vid_path)   
    except:
      await msg.edit_text("Something really Happend Wrong... join @septemberfilms") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb join @septemberfilms")


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

@app.on_message(filters.command("tg"))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("**Downloading....**")
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
