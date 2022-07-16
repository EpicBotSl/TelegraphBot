from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *
from pyrogram.types import Message
from urllib.parse import quote

SHARE_BUTTON_TEXT = "🙂Hey my dear Friend ! See this amazing bot @EtelegraphBot"

abc = 't.me/share/url?url=' + quote(SHARE_BUTTON_TEXT.format(username=username))

START_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton('🕊️ ʜᴇʟᴘ 🕊️', callback_data="gen")
                 ],
                 [
                 InlineKeyboardButton('🔰ꜱᴜᴘᴘᴏʀᴛᴇᴅ ᴛʏᴘᴇꜱ🔰', callback_data="Help"),
                 InlineKeyboardButton(text="🎊ᴀʙᴏᴜᴛ🎊", callback_data="about")
                 ],
                 [
                 InlineKeyboardButton(text="❦ ꜱʜᴀʀᴇ & ꜱᴜᴘᴘᴏʀᴛ ᴜꜱ ❦", url="abc")
                 ],
                 [
                 InlineKeyboardButton(text="</ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ</>🇱🇰", url="https://t.me/EpicBotsSl")
                 ]])

SHARE_BUTTON_TEXT = "🙂Hey my dear Friend ! See this amazing bot @EtelegraphBot"

ABOUT_TXT = f"""
╭╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╮
 ┍
   ◈ᴛʜɪꜱ ʙᴏᴛ ʙʏ ⎚ [ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ](https://t.me/EpicBotsSl)
                                  ┚        
  ⌭ᴅᴇᴠᴇʟᴏᴘᴇʀ : [ɴᴀᴠᴀɴᴊᴀɴᴀ](https://t.me/NA_VA_N_JA_NA1)
  ⌭ᴍᴀᴅᴇ ᴡɪᴛʜ : [ᴘʏᴛʜᴏɴ](https://python.org)
  ⌭ʜᴏꜱᴛᴇᴅ ᴏɴ : [ʜᴇʀᴏᴋᴜ](https://heroku.com)
  ⌭ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : [ɢɪᴛʜᴜʙ](https://github.com/EpicBotSl/TelegraphBot)
╰╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╴╴╴╶╶╶╶╶╯
"""

M_BACK = InlineKeyboardMarkup([[
   InlineKeyboardButton('⏎', callback_data="M_B")
  ]])

BA_TXT = f"""
    ❧ʜɪ ❦dear❦
    ✪ɪ ᴀᴍ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ✪
❍ɪ ᴄᴀɴ ᴄᴏɴᴠᴇʀᴛ :
        ✯**ᴘʜᴏᴛᴏ**
        ✯**ɢɪꜰᴛ**
        ✯**ᴠɪᴅᴇᴏ**
ᴍᴇᴅɪᴀ ᴛʏᴘᴇꜱ✓
❍ᴘᴏᴡᴇʀᴅ ʙʏ : [ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ](https://t.me/EpicBotsSl)
"""

HELP_TXT = f"""
**┏
  ʜᴇʟᴘ ᴍᴇɴᴜ 
            ┛**
**⋆ ꜱᴇɴᴅ ᴍᴇ ʏᴏᴜʀ ᴠɪᴅᴇᴏ, ɢɪꜰᴛ ᴏʀ ᴘʜᴏᴛᴏ
 ɪ ᴄᴀɴ ᴄᴏɴᴠᴇʀᴛ ɪᴛ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ
⋋                              ⋌**
⊱ ᴜꜱᴇ ᴄᴏᴍᴍᴀɴᴅ /about
  ⊷ ꜰᴏʀ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ʙᴏᴛ
⊱ ᴜꜱᴇ ᴄᴏᴍᴍᴀɴᴅ /types
  ⊷ ꜰᴏʀ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ꜱᴜᴘᴘᴏʀᴛᴇᴅ ᴛʏᴘᴇꜱ

⋆⋆ᴛʜɪꜱ ʙᴏᴛ ʙʏ [ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ](https://t.me/EpicBotsSl)
"""

SUP_TYPE = f"""
**┏
  ꜱᴜᴘᴘᴏʀᴛᴇᴅ ᴛʏᴘᴇꜱ
                ┛**
◈ᴘʜᴏᴛᴏꜱ 
◈ɢɪꜰᴛꜱ
◈ᴠɪᴅᴇᴏ **(ʟᴇꜱꜱ ᴛʜᴀɴ 5 ᴍʙ)**

ᴛʜɪꜱ ʙᴏᴛ ʙʏ ◐ [ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ](https://t.me/EpicBotsSl)
"""
