import os
from dotenv import load_dotenv
import discord
import requests
import json
import certifi
import ssl
import random

load_dotenv()

def get_meme():
    response  =  requests.get('https://meme-api.com/gimme')
    json_data  = json.loads(response.text)
    return json_data['url']

def random_meme_source_picker():
    subreddits = ['ProgrammerHumor', 'codinghumor']
    randomPicker = random.choice(subreddits)
    return randomPicker

def get_coding_meme():
    response  =  requests.get(f'https://meme-api.com/gimme/{random_meme_source_picker()}')
    json_data  = json.loads(response.text)
    return [json_data['url'] ]

def generate_random_emote():
    response = 'https://emojicdn.elk.sh/random?style=google'
    # json_data = json.loads(response.text)
    return response 


class MyClient(discord.Client):
    # When bot login successful
    async def on_ready(self):
        print(f"Logged in as {self.user}!")

    # on_message method
    async def on_message(self, message):
        if message.author == self.user:
            # Bot should not respond to itself
            return
        
        # Command : $hello
        if message.content.startswith('$hello'):
            await message.channel.send("Hello world!")
            await message.channel.send(f"I am {self.user}!")
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())

        #  Command : $ssh
        if message.content.startswith('$ssh'):
            await message.channel.send(get_coding_meme()[0])
            
        # Command : $emote
        if message.content.startswith("$emote"):
            await message.channel.send(generate_random_emote())

        # Command : $help
        if message.content.startswith('$help'):
            await message.channel.send(
                """


**Commands:**
-----SSH Bot-----
`$hello` : To say Hello.
`$meme` : To get a random Meme.
`$ssh`: To say random Programming Meme.
`$help` : To get help.
"""
            )
intents = discord.Intents.default()
intents.message_content = True

# For Future Use
# intents.emojis_and_stickers = True


# Create a new client
client = MyClient(intents=intents)

client.run(os.getenv('DISCORD_BOT_TOKEN'))
