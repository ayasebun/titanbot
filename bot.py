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



    if 'cancel' in message.content.lower():
        print('Cancel Found')
        emoji = '<:cmontan:854236706626076742>'
        await message.add_reaction(emoji)


    if message.content.startswith('!8balltan'):
        print('8 Ball Titan')
        titans = ['<:yestan:608551635844857856>',
                '<:notan:612894048990003200>',
                '<:doubtan:637821087987662856>',
                '<:thinktan:610471993619382328>',
                '<:thonktan:610474371672178713>',
                '<:thonktanry:610474396200599552>']

        emote = random.choice(titans)
        await message.reply(emote, mention_author=True)



    if "Heehee HAHA hahaha HEEHEE haha HEEEEEE!!!" in message.content:
        await message.reply("https://cdn.discordapp.com/attachments/564386972852813833/893279654281109575/ifritmood.png", mention_author=True)

#bot content END
#read config for token
client.run(config['discord']['token'])
