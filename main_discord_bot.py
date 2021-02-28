import discord
from discord.ext import commands
from shopping import price_list
import requests
from bs4 import BeautifulSoup as sorter
import re

Bot = commands.Bot(command_prefix='.')


@Bot.command(name='check')
async def check(context, query, country):
""" Lists the top 5 products of the given input"""
    general_channel = Bot.get_channel(815231056491839511)

    top_five = price_list(query, country)

    for a in top_five:
        myEmbed = discord.Embed(title=query, description="", color=0x0779e4)
        myEmbed.add_field(name=a['title'], value=a['source'])
        myEmbed.add_field(name="Price", value=a['price'])
        myEmbed.add_field(name="Reviews", value=a['reviews'])
        await context.send(embed=myEmbed)
        
        
@Bot.command(name = 'history', pass_context = True)                                    # Overriding the Bot command with history
async def get_hist(context, limit):
""" Takes an int as input, sends that amount of messages as a csv to the user who
    wrote the command"""    
    general = Bot.get_channel(815231056491839511)                                      # Getting the general channel with its ID

    if not isinstance(limit, int):                                                     # Checking if the parameter is not a number
        await context.send('limit not a number')
    else:
        with open('result.csv', mode='w', newline='') as file:                         # Create new csv file
            writer = csv.writer(file)
            writer.writerow(['User', 'Message'])                                       # Write the first row
            async for message in general.history(limit = int(limit)):                  # For every message up until the limit
                writer.writerow([message.author.name, message.content])                # Write the contents of the history

        await message.author.send(file=discord.File(os.path.join('result.csv')))       # Send the csv file to the person who wrote the command
        os.remove('result.csv')                                                        # Remove the csv file for others to use
        

@Bot.command(name = 'news')
async def news(context):
""" Get newest 5 articles from the website PCGamer, can only be used one ready is printed """

    # -- Getting website -- #
    url = 'https://www.pcgamer.com/'
    page = requests.get(url)
    sorted = sorter(page.content, 'html.parser')

    # -- Getting articles -- #
    articles_li = sorted.find_all('span', class_='article-name')
    # -- Getting images -- #
    images = sorted.find_all('img')
    # -- Getting a tags -- #
    a_tags = sorted.find_all('a', class_='article-link')

    # -- links list for images -- #
    links = []
    # -- links list for links to the articles -- #
    links_sites = []

    # -- images -- #
    for img in images:
        picture = re.findall(r'https://[a-z]+[:.].*?(?=\s)', str(img))[-1]
        links.append(picture)

    del links[2:23]

    # -- links to articles -- #
    for link in a_tags:
        links_sites.append(link.get('href'))

    del links_sites[1:22]

    # -- getting text for description for embed -- #
    description = []
    for i in range(0, 5):
        page = requests.get(links_sites[i])
        sorted = sorter(page.content, 'html.parser')
        text = sorted.find_all('p')
        description.append(text[2].text)

    description.insert(0, '')
    links_sites.insert(0, '')
    
    print('ready')
    
    for i in range(1,6):
        embed = discord.Embed(title=str(articles_li[i].next))
        embed.add_field(name = 'Description', value=description[i], inline=False)
        embed.set_image(url = str(links[i]))
        embed.add_field(name = 'Link to site', value=links_sites[i])
        await context.channel.send(embed = embed)

        
@Bot.event
async def on_ready():
    general_channel = client.get_channel(815231056491839511)
    await general_channel.send("Hello world")


client.run('ODE1MjI2NzE2NTUyMjk4NTM2.YDpVCw.1F2Ipv-YAYBdnHvWA3dy17Jm1qg')
