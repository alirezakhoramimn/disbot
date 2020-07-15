# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 23:53:41 2020

@author: j.khorami
"""


import discord 

Adding a Bot to a Guild
A bot can’t accept invites like a normal user can. Instead, you’ll add your bot using the OAuth2 protocol.

Technical Detail: OAuth2 is a protocol for dealing with authorization, where a service can grant a client application limited access based on the application’s credentials and allowed scopes.

To do so, head back to the Developer Portal and select the OAuth2 page from the left-hand navigation:
    '''

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('mamad dadashemone!')

client.run()
