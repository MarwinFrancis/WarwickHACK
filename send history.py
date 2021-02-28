import discord
from discord.ext import commands
import os
import csv

# Creating the Bot object
Bot = commands.Bot(command_prefix='.')


@Bot.command(name = 'history', pass_context = True)                                    # Overriding the Bot command with history
async def get_hist(context, limit):

    general = Bot.get_channel(810527278399488034)                                      # Getting the general channel with its ID

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


