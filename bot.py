from os import environ

session_string = environ.get("SESSION")
api_id = int(environ.get("API_ID"))
api_hash = environ.get("API_HASH")
bot_token = environ.get("BOT_TOKEN")

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import asyncio

C = [".", "/"]
CHANNELS = [int(chnel) for chnel in environ.get("CHANNELS", None).split()]       

authchat = filters.chat(CHANNELS) if CHANNELS else (filters.group | filters.channel)         

bot_client = Client("acceptUser", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)
)

@User.on_message(filters.command(["run", "approve"], C) & authchat)                     
async def approve(client: User, message: Message):
    chat=message.chat 
    try:
       try:
          await client.approve_all_chat_join_requests(chat.id)
          return
       except FloodWait as t:
          asyncio.sleep(t.value)
          await client.approve_all_chat_join_requests(chat.id)
          return    
    except Exception as e:
       print(e)
    hhh = await client.send_message(chat.id, "mission completed ✅️ approved all joinrequest")
    await asyncio.sleep(3)
    await hhh.delete()
 
@User.on_message(filters.command(["no", "remove", "decline"], C) & authchat)                     
async def decline(client: User, message: Message):
    chat=message.chat 
    try:
       try:
          await client.decline_all_chat_join_requests(chat.id)
          return   
       except FloodWait as t:
          asyncio.sleep(t.value)
          await client.decline_all_chat_join_requests(chat.id)
          return     
    except Exception as e:
       print(e)
    hhh = await client.send_message(chat.id, "mission completed ❌️ declined all joinrequest")  
    await asyncio.sleep(3)
    await hhh.delete()     

print("bot started....")
User.run()
