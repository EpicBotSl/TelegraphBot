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

@Client.on_callback_query()  
async def tgm(bot, update):  
    if update.data == "add": 
        await update.answer(
             text="β»οΈAdding Soon.....",
        )
    elif update.data == "gen":
         await update.message.edit_text(
             text=HELP_TXT,
             reply_markup=M_BACK,
             disable_web_page_preview=True
         )
         await update.answer(
             text="ποΈ Welcome to Help menu ποΈ Join @EpicBotsSl",
         )
    elif update.data == "M_B":
         await update.message.edit_text(
             text=BA_TXT,
             reply_markup=START_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="ποΈ Welcome back ποΈ Join @EpicBotsSl",
         )
    elif update.data == "Help":
         await update.message.edit_text(
             text=SUP_TYPE,
             reply_markup=M_BACK,
             disable_web_page_preview=True
         )
         await update.answer(
             text="ποΈ Welcome to Types menu ποΈ Join @EpicBotsSl",
         )
    elif update.data == "about":
         await update.message.edit_text(
             text=ABOUT_TXT,
             reply_markup=M_BACK,
             disable_web_page_preview=True
         )
         await update.answer(
             text="ποΈ Welcome to About menu ποΈ Join @EpicBotsSl",
         )


