from os import environ
import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import asyncio

logging.basicConfig(level=logging.ERROR)

C = [".", "/"]

CHANNELS = [int(CHANNEL) for CHANNEL in environ.get("CHANNELS", None).split()]       

AuthChat = filters.chat(CHANNELS) if CHANNELS else (filters.group | filters.channel)         

User = Client(
    name = "AcceptUser",
    session_string = environ.get("SESSION"),
    api_id = int(environ.get("API_ID")),
    api_hash = environ.get("API_HASH")
)

@User.on_message(filters.command(["run", "approve", "start"], C) & AuthChat)                     
async def approve(client: User, message: Message):
    chat = message.chat 
    try:
       try:
          await client.approve_all_chat_join_requests(chat.id)
          return
       except FloodWait as t:
          asyncio.sleep(t.value)
          await client.approve_all_chat_join_requests(chat.id)
          return    
    except Exception as e:
        logging.error(str(e))
    msg = await client.send_message(chat.id, "**Task Completed** ✓ **Approved Pending All Join Request**")
    await asyncio.sleep(3)
    await msg.delete()
 
@User.on_message(filters.command(["no", "remove", "decline"], C) & AuthChat)                     
async def decline(client: User, message: Message):
    chat = message.chat 
    try:
       try:
          await client.decline_all_chat_join_requests(chat.id)
          return   
       except FloodWait as t:
          asyncio.sleep(t.value)
          await client.decline_all_chat_join_requests(chat.id)
          return     
    except Exception as e:
        logging.error(str(e))
    msg = await client.send_message(chat.id, "**Task Completed** ✓ **Declined All Join Request**")  
    await asyncio.sleep(3)
    await msg.delete()     

logging.info("Bot Started....")
User.run()
