#!/usr/bin/python36

import discord
import asyncio
import configparser
import re
import string
import random

config = configparser.ConfigParser()
config.read('settings.ini')

#adding activity message in parenthesis

client = discord.Client(activity=discord.Game(name='*snap*'))

#Commands
@client.event
async def on_ready():
    print('Bot ready')

@client.event

async def on_message(message):

#ignore bot

    if message.author.bot: return

#bot content

    if message.content.startswith('!titan'):
        print('Random Titan')
        with open('emotes') as emotes:
            titans = emotes.read().splitlines()
        randomtitan = random.choice(titans)
        await message.reply(randomtitan, mention_author=True)

    if message.content.startswith('!teetan'):
        print('Random Teetan')
        with open('teetans') as teetanlist:
            teetans = teetanlist.read().splitlines()
        randomteetan = random.choice(teetans)
        await message.reply(randomteetan, mention_author=True)


    if 'wide' in message.content.lower():
        await message.reply('<:wide:623782094723743744><:ti:623782116089659402><:tan:623782142014390272><:hap:623782160049897502><:py:623782183429210122>')

    if 'u3u' in message.content.lower():
        print('u3u Found')
        emoji = '<:u3utan:873129678544703518>'
        await message.add_reaction(emoji)


client.run(config['discord']['token'])qq^Ciscordapp.com/attachments/564386972852813833/893279654281109575/ifritmood.png", mention_author=True)
