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

app = Client



@app.on_message(filters.video)
async def uploadvid(client, message):
  if(message.video.file_size < 5242880):
    msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ....")
    userid = str(message.chat.id)
    vid_path = (f"./DOWNLOADS/{userid}.mp4")
    vid_path = await client.download_media(message=message, file_name=vid_path)
    await msg.edit_text(f"""
⚫⚫⚫
⚫⚫⚫
⚫⚫⚫
""")
  await msg.edit_text(f"""
🔴🔴🔴
🔴🔴🔴
🔴🔴🔴
""")
  await msg.edit_text(f"""
🔵🔵🔵
🔵🔵🔵
🔵🔵🔵
""")
  await msg.edit_text(f"""
⚪⚪⚪
⚪⚪⚪
⚪⚪⚪
""")
  await msg.edit_text(f"""
⚫⚫⚫
⚫⚫⚫
⚫⚫⚫
""")
  await msg.edit_text(f"""
🔴🔴🔴
🔴🔴🔴
🔴🔴🔴
""")
  await msg.edit_text(f"""
🔵🔵🔵
🔵🔵🔵
🔵🔵🔵
""")
  await msg.edit_text(f"""
⚪⚪⚪
⚪⚪⚪
⚪⚪⚪
""")
  await msg.edit_text(f"""
⚫⚫⚫
⚫⚫⚫
⚫⚫⚫
""")
  await msg.edit_text(f"""
🔴🔴🔴
🔴🔴🔴
🔴🔴🔴
""")
  await msg.edit_text("⚫🔴🔵⚪")
  await msg.edit_text("⚫⚪🔵🔴")
  await msg.edit_text("⚫🔵🔴⚪")
  await msg.edit_text("⚫⚪🔵🔴")
  await msg.edit_text("🆂 ▍🔴⚫")
  await msg.edit_text("🅴 ▍⚫🔴")
  await msg.edit_text("🅽 ▍🔴⚫")
  await msg.edit_text("🅳 ▍⚫🔴")
  await msg.edit_text("🅸 ▍🔴⚫")
  await msg.edit_text("🅽 ▍⚫🔴")
  await msg.edit_text("🅶 ▍🔴⚫")
  await msg.edit_text("🆂")
  await msg.edit_text("🆂🅴")
  await msg.edit_text("🆂🅴🅽")
  await msg.edit_text("🆂🅴🅽🅳")
  await msg.edit_text("🆂🅴🅽🅳🅸")
  await msg.edit_text("🆂🅴🅽🅳🅸🅽")
  await msg.edit_text("🆂🅴🅽🅳🅸🅽🅶")
  await msg.edit_text("🆂🅴🅽🅳🅸🅽")
  await msg.edit_text("🆂🅴🅽🅳🅸")
  await msg.edit_text("🆂🅴🅽🅳")
  await msg.edit_text("🆂🅴🅽")
  await msg.edit_text("🆂🅴")
  await msg.edit_text("🆂")
  await msg.edit_text("🆂🅴")
  await msg.edit_text("🆂🅴🅽")
  await msg.edit_text("🆂🅴🅽🅳")
  await msg.edit_text("🆂🅴🅽🅳🅸")
  await msg.edit_text("🆂🅴🅽🅳🅸🅽")
  await msg.edit_text("🆂🅴🅽🅳🅸🅽🅶")
  await msg.edit_text("**yeehaa!**")

  try:
    tlink = upload_file(vid_path)
    await msg.edit_text(f"`https://telegra.ph{tlink[0]}`")     
      os.remove(vid_path)   
  except:
    await msg.edit_text("Something really Happend Wrong... join @EpicChats") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb join @EpicChats")

print(f"""
Telegraph Vision Convert Section Powerd Up..
""")
