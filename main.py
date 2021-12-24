from pyrogram import *
from pyrogram.types import *
import requests
from pyromod import listen
# ====================================================================
app = Client("MrTak",config_file="config.ini")
# ====================================================================
ADMINID = "@MrTakDev"
BOTID = "@WhoisMrTakBot"
# ====================================================================
Keyboard = ReplyKeyboardMarkup(
    [
        ["🗂 Whois 🗂"],
        ["👤 Contact us 👤","ℹ️ Information ℹ️"],
        ["❗️ Help ❗️"]

    ],resize_keyboard=True
)
# ====================================================================
@app.on_message(filters.command("start"))
async def Start(client, message):
    await message.reply_text(f"""😃Hello <b>{message.from_user.mention}</b>, dear
Welcome to the robot Whois
This robot can retrieve site information🔥""",reply_markup=Keyboard,parse_mode="html")
# ====================================================================
async def Whois(client, message):
    UserSite = await app.ask(message.from_user.id,"😃Send your message :) 🔥")
    URL = f"https://api.whoisfreaks.com/v1.0/whois?apiKey=3144e5c770d74a09a4698ccca0058127&whois=live&domainName={UserSite.text}"
    request = requests.get(URL).json()
    request1 = dict(request)
    await message.reply_text(request["whois_raw_domain"]+f"\n\n\n**🆔 {BOTID}**",reply_markup=Keyboard)

    await message.reply_text("Choose one of the options 😃👇",reply_markup=Keyboard)
# ====================================================================
async def Information(client, message):
    await message.reply_text(f"""
`┌┬` __User info__
`│├` First Name:  `{message.from_user.first_name}`
`│├` Last Name:  `{message.from_user.last_name}`
`│├` Username:  `@{message.from_user.username}`
`│├` ID:  `{message.from_user.id}` """,reply_markup=Keyboard,parse_mode="markdown")
# ====================================================================
async def Contact_us(client, message):
    await message.reply_text(f"""👤 If you have a problem with an idea, you can contact the following ID🔥
🆔 **{ADMINID}**""",reply_markup=Keyboard,parse_mode="markdown")
# ====================================================================
async def Help(client, message):
    await message.reply_text(f"""😃To use the robot, you must first click the **🗂 Whois 🗂** button, then you must enter the site address, for example google.com 🔥""",reply_markup=Keyboard,parse_mode="markdown")
# ====================================================================
@app.on_message()
async def Main(client, message):
    Text = message.text
    if Text == "🗂 Whois 🗂":
        await Whois(client, message)
    elif Text == "👤 Contact us 👤":
        await Contact_us(client, message)
    elif Text == "ℹ️ Information ℹ️":
        await Information(client, message)
    elif Text == "❗️ Help ❗️":
        await Help(client, message)
# ====================================================================
app.run()
