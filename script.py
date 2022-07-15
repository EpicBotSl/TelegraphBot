from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

START_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton('❀ʜᴇʟᴘ❀', callback_data="gen")
                 ],
                 [
                 InlineKeyboardButton('❂ꜱᴜᴘᴘᴏʀᴛᴇᴅ ᴛʏᴘᴇꜱ❂', callback_data="Help"),
                 InlineKeyboardButton(text="✽ ᴀʙᴏᴜᴛ ✽", callback_data="about")
                 ],
                 [
                 InlineKeyboardButton(text="❦ ꜱʜᴀʀᴇ & ꜱᴜᴘᴘᴏʀᴛ ᴜꜱ ❦", callback_data="about")
                 ],
                 [
                 InlineKeyboardButton(text="</ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ</>🇱🇰", url="https://t.me/EpicBotsSl")
                 ]])
