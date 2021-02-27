# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 15:32:55 2021

@author: Vlad
"""

import discord
from programme import price_list
from discord.ext import commands
client = commands.Bot(command_prefix='--')

@client.command(name='check')
async def check(context, query, country):
    general_channel = client.get_channel(815231056491839511)

    top_five = price_list(query, country)

    for a in top_five:
        myEmbed = discord.Embed(title=query, description="", color=0x0779e4)
        myEmbed.add_field(name=a['title'], value=a['source'])
        myEmbed.add_field(name="Price", value=a['price'])
        myEmbed.add_field(name="Reviews", value=a['reviews'])
        #myEmbed.set_footer(text=a['source'])
        await context.send(embed=myEmbed)

@client.event
async def on_ready():
    general_channel = client.get_channel(815231056491839511)
    await general_channel.send("Hello world")


client.run('ODE1MjI2NzE2NTUyMjk4NTM2.YDpVCw.1F2Ipv-YAYBdnHvWA3dy17Jm1qg')
