import os
import discord
from dotenv import load_dotenv
import translate

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

class DevPSUBot(discord.Client):
    async def on_ready(self):
        print("logged on!")
    
    async def on_message(self, message):
        print(f"message found!: {message.content} from {message.author} in {message.channel}")
        if message.author == client.user:
            return
        if "hello" in message.content.lower():
            print(f"command recognized: hello")
            await message.channel.send("Hello!")    # Seek command from channel
        if client.user in message.mentions:
            print("Bot mentioned!")
            await message.channel.send("Mentioned!")
        if "react" in message.content.lower():
            print("react command recognized")
            await message.add_reaction("😀")
        
        # Translate
        if "translate" in message.content.lower():
            message_list = message.content.split()
            i = 1
            msg = ""
  
            if "to" in message.content:
                while message_list[i] != "to":
                    msg += message_list[i]
                    i += 1
                
                lang = message_list[i+1]

                await message.channel.send(translator.translator_func(msg, lang))
            
            else:
                while i < len(message_list):
                    msg += message_list[i+1]
                    i += 1
                
                await message.channel.send(translator.translator_func(msg))

    
    async def on_typing(self, channel, user, when):
        print(f"{user} is typing in {channel} at {when}")
        await channel.send(f"I see you typing, {user}")

client = DevPSUBot(intents=intents)
client.run(token)
