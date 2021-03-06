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
        ["π Whois π"],
        ["π€ Contact us π€","βΉοΈ Information βΉοΈ"],
        ["βοΈ Help βοΈ"]

    ],resize_keyboard=True
)
# ====================================================================
@app.on_message(filters.command("start"))
async def Start(client, message):
    await message.reply_text(f"""πHello <b>{message.from_user.mention}</b>, dear
Welcome to the robot Whois
This robot can retrieve site informationπ₯""",reply_markup=Keyboard,parse_mode="html")
# ====================================================================
async def Whois(client, message):
    UserSite = await app.ask(message.from_user.id,"πSend your message :) π₯")
    URL = f"https://api.whoisfreaks.com/v1.0/whois?apiKey=3144e5c770d74a09a4698ccca0058127&whois=live&domainName={UserSite.text}"
    request = requests.get(URL).json()
    request1 = dict(request)
    await message.reply_text(request["whois_raw_domain"]+f"\n\n\n**π {BOTID}**",reply_markup=Keyboard)

    await message.reply_text("Choose one of the options ππ",reply_markup=Keyboard)
# ====================================================================
async def Information(client, message):
    await message.reply_text(f"""
`ββ¬` __User info__
`ββ` First Name:  `{message.from_user.first_name}`
`ββ` Last Name:  `{message.from_user.last_name}`
`ββ` Username:  `@{message.from_user.username}`
`ββ` ID:  `{message.from_user.id}` """,reply_markup=Keyboard,parse_mode="markdown")
# ====================================================================
async def Contact_us(client, message):
    await message.reply_text(f"""π€ If you have a problem with an idea, you can contact the following IDπ₯
π **{ADMINID}**""",reply_markup=Keyboard,parse_mode="markdown")
# ====================================================================
async def Help(client, message):
    await message.reply_text(f"""πTo use the robot, you must first click the **π Whois π** button, then you must enter the site address, for example google.com π₯""",reply_markup=Keyboard,parse_mode="markdown")
# ====================================================================
@app.on_message()
async def Main(client, message):
    Text = message.text
    if Text == "π Whois π":
        await Whois(client, message)
    elif Text == "π€ Contact us π€":
        await Contact_us(client, message)
    elif Text == "βΉοΈ Information βΉοΈ":
        await Information(client, message)
    elif Text == "βοΈ Help βοΈ":
        await Help(client, message)
# ====================================================================
app.run()
