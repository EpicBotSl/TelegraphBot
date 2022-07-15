import re
import uuid
import socket
import platform
import os
import random
import time
import math
import json
import string
import traceback
import psutil
import asyncio
import wget
import motor.motor_asyncio
import pymongo
import aiofiles
import datetime
from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *
from helper.decorators import humanbytes
from config import *
from database.db import Database
from asyncio import *
import heroku3
import requests
from script import *
from helper.fsub import forcesub
from database.check_user import *
#--------------------------------------------------Db-------------------------------------------------#


async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : user is blocked\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"
        
#------------------------------Db End---------------------------------------------------------#       

DATABASE_URL=MONGO_URI
db = Database(DATABASE_URL, "telegraph_bot")

#╔════╗────────╔═══╗
#║╔╗╔╗║────────║╔══╝
#╚╝║║╠╩═╦══╦╗╔╗║╚══╦══╦╦══╗
#──║║║║═╣╔╗║╚╝║║╔══╣╔╗╠╣╔═╝
#──║║║║═╣╔╗║║║║║╚══╣╚╝║║╚═╗
#──╚╝╚══╩╝╚╩╩╩╝╚═══╣╔═╩╩══╝
#──────────────────║║
#──────────────────╚╝
#---------------------------Commands Start Epic-------------------------------------#

client = Client

@Client.on_message(filters.command("start"))
async def start(client, message):
    if await forcesub(client, message):
       return
    chat_id = message.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await client.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        if LOG_CHANEL:
            await client.send_message(
                LOG_CHANEL,
                f"#NEWUSER: \n\n**User:** [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n\**ID:**{message.from_user.id}\n Started @{BOT_USERNAME} !!",
            )
        else:
            logging.info(f"#NewUser :- Name : {message.from_user.first_name} ID : {message.from_user.id}")
    await message.delete()
    await message.reply_photo("https://telegra.ph/file/886c2db8d9ec4e8057176.jpg", caption=f"""
    ❧ʜɪ ❦{message.from_user.mention} ❦
    ✪ɪ ᴀᴍ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ✪
❍ɪ ᴄᴀɴ ᴄᴏɴᴠᴇʀᴛ :
        ✯**ᴘʜᴏᴛᴏ**
        ✯**ɢɪꜰᴛ**
        ✯**ᴠɪᴅᴇᴏ ʟᴇꜱꜱ ᴛʜᴀɴ 5ᴍʙ**
ᴍᴇᴅɪᴀ ᴛʏᴘᴇꜱ✓
❍ᴘᴏᴡᴇʀᴅ ʙʏ : [ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ](https://t.me/EpicBotsSl)""", reply_markup=START_BUTTON)


#---------------------------Gen Logo Epic-------------------------------------##╔════╗────────╔═══╗
#║╔╗╔╗║────────║╔══╝
#╚╝║║╠╩═╦══╦╗╔╗║╚══╦══╦╦══╗
#──║║║║═╣╔╗║╚╝║║╔══╣╔╗╠╣╔═╝
#──║║║║═╣╔╗║║║║║╚══╣╚╝║║╚═╗
#──╚╝╚══╩╝╚╩╩╩╝╚═══╣╔═╩╩══╝
#──────────────────║║
#──────────────────╚╝
