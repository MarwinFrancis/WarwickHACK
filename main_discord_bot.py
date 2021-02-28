import discord
from PIL import Image, ImageDraw
import copy
import cv2 as cv
import numpy as np
import pandas as pd
from discord.ext import commands
from shopping import price_list
import requests
from bs4 import BeautifulSoup as sorter
import re
import csv
import os

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
    wrote the command """
    general = Bot.get_channel(815231056491839511)                                      # Getting the general channel with its ID

    if not isinstance(int(limit), int):                                                # Checking if the parameter is not a number
        await context.send('limit not a number')
    else:
        with open('result.csv', mode='w', newline='') as file:                         # Create new csv file
            writer = csv.writer(file)                                                 
            writer.writerow(['User', 'Message'])                                       # Write the first row
            async for message in general.history(limit=int(limit)):                    # For every message up until the limit
                writer.writerow([message.author.name, message.content])                # Write the contents of the history

        try:
            await context.author.send(file=discord.File(os.path.join('result.csv')))   # Send the csv file to the person who wrote the command
        except:
            pass
        os.remove('result.csv')                                                        # Remove the csv file for others to use

@Bot.command(name = 'news')
async def news(context):
    """ Get newest 5 articles from the website PCGamer, can only be used one ready is printed """

    url = 'https://www.pcgamer.com/'                                                    # Getting website 
    page = requests.get(url)
    sorted = sorter(page.content, 'html.parser')
    articles_li = sorted.find_all('span', class_='article-name')                        # List of articles
    images = sorted.find_all('img')                                                     # List of images
    a_tags = sorted.find_all('a', class_='article-link')                                # List of a tags 

    links = []                                                                          # Links list for images 
    links_sites = []                                                                    # Links list for links to the articles 

    for img in images:
        picture = re.findall(r'https://[a-z]+[:.].*?(?=\s)', str(img))[-1]              # Process images 
        links.append(picture)

    del links[2:23]

    for link in a_tags:
        links_sites.append(link.get('href'))                                            # Links to articles

    del links_sites[1:22]

    description = []                                                                    # Getting text for description for embed 
    for i in range(0, 5):
        page = requests.get(links_sites[i])
        sorted = sorter(page.content, 'html.parser')
        text = sorted.find_all('p')
        description.append(text[2].text)

    description.insert(0, '')
    links_sites.insert(0, '')
    
    print('ready')
    
    for i in range(1,6):                                                                 # Creating the embed to be sent to the user  
        embed = discord.Embed(title=str(articles_li[i].next))
        embed.add_field(name = 'Description', value=description[i], inline=False)
        embed.set_image(url = str(links[i]))
        embed.add_field(name = 'Link to site', value=links_sites[i])
        await context.channel.send(embed = embed)
 

img = Image.open("board.jpg")
width, height = img.size
img = img.convert('RGB')
pixels=img.load()
d=ImageDraw.Draw(img)
numbers = Image.open("N3.png")
numbers = numbers.convert('RGBA')
#numbers = numbers.resize((50,50))
img.paste(numbers,(0,80),numbers)
img.paste(numbers,(880,80),numbers)
letters = Image.open("L1.png")
letters = letters.convert('RGBA')
#numbers = numbers.resize((50,50))
img.paste(letters,(84,0),letters)
img.paste(letters,(84,870),letters)
black_Bishop = Image.open("pieces/blackBishop.png")
black_Bishop = black_Bishop.resize((100,100))
white_Bishop = Image.open("pieces/whiteBishop.png")
white_Bishop = white_Bishop.resize((100,100))
black_Pawn = Image.open("pieces/blackPawn.png")
black_Pawn = black_Pawn.resize((100,100))
white_Pawn = Image.open("pieces/whitePawn.png")
white_Pawn = white_Pawn.resize((100,100))
black_Horse = Image.open("pieces/blackHorse.png")
black_Horse = black_Horse.resize((100,100))
white_Horse = Image.open("pieces/whiteHorse.png")
white_Horse = white_Horse.resize((100,100))
black_Rook = Image.open("pieces/blackRook.png")
black_Rook = black_Rook.resize((100,100))
white_Rook = Image.open("pieces/whiteRook.png")
white_Rook = white_Rook.resize((100,100))
black_Queen = Image.open("pieces/blackQueen.png")
black_Queen = black_Queen.resize((100,100))
white_Queen = Image.open("pieces/whiteQueen.png")
white_Queen = white_Queen.resize((100,100))
black_King = Image.open("pieces/blackKing.png")
black_King = black_King.resize((100,100))
white_King = Image.open("pieces/whiteKing.png")
white_King = white_King.resize((100,100))


class Bishop:
    def __init__(self,colour,position):
        self.colour = colour
        self.position = position
    def check_if_this_move_is_legal(self,newPosition):
        if abs(self.position[0] - newPosition[0]) == abs(self.position[1] - newPosition[1]):
            if 0 <= newPosition[0] and newPosition[0] <= 7 and 0 <= newPosition[1] and newPosition[1] <= 7:
                orientation = 0
                if newPosition[0] > self.position[0] and newPosition[1] > self.position[1]:
                    orientation = 1
                if newPosition[0] < self.position[0] and newPosition[1] > self.position[1]:
                    orientation = 2
                if newPosition[0] < self.position[0] and newPosition[1] < self.position[1]:
                    orientation = 3
                i = self.position[0]
                j = self.position[1]
                if abs(self.position[0] - newPosition[0]) != 1:
                    if orientation == 0:
                        i = i + 1
                        j = j - 1
                        while board[i][j] == None and i != newPosition[0] and j != newPosition[1] and i>-1 and i<8 and j>-1 and j<8:
                            i = i + 1
                            j = j - 1
                        if i!=newPosition[0] and j!=newPosition[1]:
                            return "Move is illegal - the bishop cannot jump over other pieces."
                    if orientation == 1:
                        i = i + 1
                        j = j + 1
                        while board[i][j] == None and i != newPosition[0] and j != newPosition[1] and i>-1 and i<8 and j>-1 and j<8:
                            i = i + 1
                            j = j + 1
                        if i!=newPosition[0] and j!=newPosition[1]:
                            return "Move is illegal - the bishop cannot jump over other pieces."
                    if orientation == 2:
                        i = i - 1
                        j = j + 1
                        while board[i][j] == None and i != newPosition[0] and j != newPosition[1] and i>-1 and i<8 and j>-1 and j<8:
                            i = i - 1
                            j = j + 1
                        if i!=newPosition[0] and j!=newPosition[1]:
                            return "Move is illegal - the bishop cannot jump over other pieces."
                    if orientation == 3:
                        i = i - 1
                        j = j - 1
                        while board[i][j] == None and i != newPosition[0] and j != newPosition[1] and i>-1 and i<8 and j>-1 and j<8:
                            i = i - 1
                            j = j - 1
                        if i != newPosition[0] and j != newPosition[1]:
                            return "Move is illegal - the bishop cannot jump over other pieces."

                if board[newPosition[0]][newPosition[1]] != None and board[newPosition[0]][newPosition[1]].colour == self.colour:
                    return "Move is illegal - pieces of the same colour cannot be captured."
                else:
                    return "Yes"
            else:
                return "Move is illegal - pieces have to move within the borders of the board."
        else:
            return "Move is illegal - the bishop can only move diagonally."

class Pawn:
    def __init__(self,colour,position):
        self.colour = colour
        self.position = position
    def check_if_this_move_is_legal(self,newPosition):
        if newPosition[0] >-1 and newPosition[0]<8 and newPosition[1]>-1 and newPosition[1]<8:
            if self.colour == 'white':
                if newPosition[1] == self.position[1] - 1 and newPosition[0] == self.position[0]:
                    if board[newPosition[0]][newPosition[1]] != None:
                        return "Move is illegal - pawns cannot take what is exactly in front of them."
                    else:
                        return "Yes"
                elif newPosition[1] == self.position[1] - 1 and (newPosition[0] == self.position[0] - 1 or newPosition[0] == self.position[0] + 1):
                    if board[newPosition[0]][newPosition[1]] == None:
                        return "Move is illegal - pawns can move diagonally only when capturing."
                    else:
                        if board[newPosition[0]][newPosition[1]].colour != 'black':
                            return "Move is illegal - pieces of the same colour cannot be captured."
                        else:
                            return "Yes"
                elif newPosition[1] == self.position[1] - 2 and newPosition[0] == self.position[0]:
                    if board[self.position[0]][self.position[1] - 1] != None:
                        return "Move is illegal - the pawn cannot jump over other pieces."
                    elif board[self.position[0]][self.position[1] - 2] != None:
                        return "Move is illegal - the pawn cannot capture what is exactly in front of him."
                    else:
                        return "Yes"
                else:
                    return "Move is illegal - the pawn can only move one step ahead, one step ahead and one to the lift or one step ahead and one to the right."
            if self.colour == 'black':
                if newPosition[1] == self.position[1] + 1 and newPosition[0] == self.position[0]:
                    if board[newPosition[0]][newPosition[1]] != None:
                        return "Move is illegal - the pawn cannot capture what is exactly in front of him."
                    else:
                        return "Yes"
                elif newPosition[1] == self.position[1] + 1 and (newPosition[0] == self.position[0] - 1 or newPosition[0] == self.position[0] + 1):
                    if board[newPosition[0]][newPosition[1]] == None:
                        return "Move is illegal - the pawn can move diagonally only when capturing."
                    else:
                        return "Yes"
                elif newPosition[1] == self.position[1] + 2 and newPosition[0] == self.position[0]:
                    if board[self.position[0]][self.position[1] + 1] != None:
                        return "Move is illegal - the pawn cannot jump over other pieces."
                    elif board[self.position[0]][self.position[1] + 2] != None:
                        return "Move is illegal - the pawn cannot capture what is exactly in front of him."
                    else:
                        return "Yes"
                else:
                    return "Move is illegal - the pawn can only move one step ahead, one step ahead and one to the lift or one step ahead and one to the right."
        else:
            return "Move is illegal - pieces have to move within the borders of the board."

class Horse:
    def __init__(self,colour,position):
        self.colour = colour
        self.position = position
    def check_if_this_move_is_legal(self,newPosition):
        if newPosition[0] >-1 and newPosition[0]<8 and newPosition[1]>-1 and newPosition[1]<8:
            if (newPosition[0] == self.position[0] + 1 and newPosition[1] == self.position[1] - 2) or (newPosition[0] == self.position[0] + 2 and newPosition[1] == self.position[1] - 1) or (newPosition[0] == self.position[0] + 2 and newPosition[1] == self.position[1] + 1) or (newPosition[0] == self.position[0] + 1 and newPosition[1] == self.position[1] + 2) or (newPosition[0] == self.position[0] - 1 and newPosition[1] == self.position[1] + 2) or (newPosition[0] == self.position[0] - 2 and newPosition[1] == self.position[1] + 1) or (newPosition[0] == self.position[0] - 2 and newPosition[1] == self.position[1] - 1) or (newPosition[0] == self.position[0] - 1 and newPosition[1] == self.position[1] - 2):
                if board[newPosition[0]][newPosition[1]] != None:
                    if board[newPosition[0]][newPosition[1]].colour == self.colour:
                        "Move is illegal - pieces of the same colour cannot be captured."
                    else:
                        return 'Yes'
                else:
                    return 'Yes'
            return "Move is illegal - the horse can only move in an L-shaped path."
        else:
            return "Move is illegal - pieces have to move within the borders of the board."

class Rook:
    def __init__(self,colour,position):
        self.colour = colour
        self.position = position
    def check_if_this_move_is_legal(self,newPosition):
        if newPosition[0] >-1 and newPosition[0]<8 and newPosition[1]>-1 and newPosition[1]<8:
            if newPosition[0] == self.position[0] or newPosition[1] == self.position[1]:
                orientation = 0
                if newPosition[0] == self.position[0] and newPosition[1] > self.position[1]:
                    orientation = 1
                if newPosition[0] < self.position[0] and newPosition[1] == self.position[1]:
                    orientation = 2
                if newPosition[0] == self.position[0] and newPosition[1] < self.position[1]:
                    orientation = 3
                i = self.position[0]
                j = self.position[1]
                if orientation == 0:
                    i = i + 1
                    while board[i][j] == None and i != newPosition[0] and i > -1 and i < 8:
                        i = i + 1
                    if i != newPosition[0]:
                        return "Move is illegal - the rook cannot jump over other pieces."
                if orientation == 1:
                    j = j + 1
                    while board[i][j] == None and j != newPosition[1] and j > -1 and j < 8:
                        j = j + 1
                    if j != newPosition[1]:
                        return "Move is illegal - the rook cannot jump over other pieces."
                if orientation == 2:
                    i = i - 1
                    while board[i][j] == None and i != newPosition[0] and i > -1 and i < 8:
                            i = i - 1
                    if i != newPosition[0] and j != newPosition[1]:
                        return "Move is illegal - the rook cannot jump over other pieces."
                if orientation == 3:
                    j = j - 1
                    while board[i][j] == None and j != newPosition[1] and j > -1 and j < 8:
                        j = j - 1
                    if j != newPosition[1]:
                        return "Move is illegal - the rook cannot jump over other pieces."

                if board[newPosition[0]][newPosition[1]] != None:
                    if board[newPosition[0]][newPosition[1]].colour == self.colour:
                        return "Move is illegal - pieces of the same colour cannot be captured."
                    else:
                        return 'Yes'
                else:
                    return 'Yes'
            else:
                return "Move is illegal - the rook can only move in a linear path."
        else:
            return "Move is illegal - pieces have to move within the borders of the board."


class Queen:
    def __init__(self,colour,position):
        self.colour = colour
        self.position = position
    def check_if_this_move_is_legal(self,newPosition):
        if abs(self.position[0] - newPosition[0]) == abs(self.position[1] - newPosition[1]):
            if 0 <= newPosition[0] and newPosition[0] <= 7 and 0 <= newPosition[1] and newPosition[1] <= 7:
                orientation = 0
                if newPosition[0] > self.position[0] and newPosition[1] > self.position[1]:
                    orientation = 1
                if newPosition[0] < self.position[0] and newPosition[1] > self.position[1]:
                    orientation = 2
                if newPosition[0] < self.position[0] and newPosition[1] < self.position[1]:
                    orientation = 3
                i = self.position[0]
                j = self.position[1]
                if abs(self.position[0] - newPosition[0]) != 1:
                    if orientation == 0:
                        i = i + 1
                        j = j - 1
                        while board[i][j] == None and i != newPosition[0] and j != newPosition[1] and i>-1 and i<8 and j>-1 and j<8:
                            i = i + 1
                            j = j - 1
                        if i!=newPosition[0] and j!=newPosition[1]:
                            return "Move is illegal - the queen cannot jump over other pieces."
                    if orientation == 1:
                        i = i + 1
                        j = j + 1
                        while board[i][j] == None and i != newPosition[0] and j != newPosition[1] and i>-1 and i<8 and j>-1 and j<8:
                            i = i + 1
                            j = j + 1
                        if i != newPosition[0] and j != newPosition[1]:
                            return "Move is illegal - the queen cannot jump over other pieces."
                    if orientation == 2:
                        i = i - 1
                        j = j + 1
                        while board[i][j] == None and i != newPosition[0] and j != newPosition[1] and i>-1 and i<8 and j>-1 and j<8:
                            i = i - 1
                            j = j + 1
                        if i!=newPosition[0] and j!=newPosition[1]:
                            return "Move is illegal - the queen cannot jump over other pieces."
                    if orientation == 3:
                        i = i - 1
                        j = j - 1
                        while board[i][j] == None and i != newPosition[0] and j != newPosition[1] and i>-1 and i<8 and j>-1 and j<8:
                            i = i - 1
                            j = j - 1
                        if i!=newPosition[0] and j!=newPosition[1]:
                            return "Move is illegal - the queen cannot jump over other pieces."

                if board[newPosition[0]][newPosition[1]] != None and board[newPosition[0]][newPosition[1]].colour == self.colour:
                    return "Move is illegal - pieces of the same colour cannot be captured."
                else:
                    return "Yes"
            else:
                return "Move is illegal - pieces have to move within the borders of the board."
        elif newPosition[0] == self.position[0] or newPosition[1] == self.position[1]:
            orientation = 0
            if newPosition[0] == self.position[0] and newPosition[1] > self.position[1]:
                orientation = 1
            if newPosition[0] > self.position[0] and newPosition[1] == self.position[1]:
                orientation = 2
            if newPosition[0] == self.position[0] and newPosition[1] < self.position[1]:
                orientation = 3
            i = self.position[0]
            j = self.position[1]
            if orientation == 0:
                i = i + 1
                while board[i][j] == None and i != newPosition[0] and i > -1 and i < 8:
                    i = i + 1
                if i != newPosition[0]:
                    return "Move is illegal - the queen cannot jump over other pieces."
            if orientation == 1:
                j = j + 1
                while board[i][j] == None and j != newPosition[1] and j > -1 and j < 8:
                    j = j + 1
                if j != newPosition[1]:
                    return "Move is illegal - the queen cannot jump over other pieces."
            if orientation == 2:
                i = i - 1
                while board[i][j] == None and i != newPosition[0] and i > -1 and i < 8:
                    i = i - 1
                if i != newPosition[0] and j != newPosition[1]:
                    return "Move is illegal - the queen cannot jump over other pieces."
            if orientation == 3:
                j = j - 1
                while board[i][j] == None and j != newPosition[1] and j > -1 and j < 8:
                    j = j - 1
                if j != newPosition[1]:
                    return "Move is illegal - the queen cannot jump over other pieces."
            if board[newPosition[0]][newPosition[1]] != None:
                if board[newPosition[0]][newPosition[1]].colour == self.colour:
                    return "Move is illegal - pieces of the same colour cannot be captured."
                else:
                    return 'Yes'
        elif 0 > newPosition[0] or newPosition[0] > 7 or 0 > newPosition[1] or newPosition[1] > 7:
            return "Move is illegal - pieces have to move within the borders of the board."
        else:
            return "Move is illegal - the queen can only move diagonally or in a linear path."


class King:
    def __init__(self,colour,position):
        self.colour = colour
        self.position = position
    def check_if_this_move_is_legal(self,newPosition):
        if -1 < newPosition[0] and newPosition[0] < 8 and -1 < newPosition[1] and newPosition[1] < 8:
            if abs(newPosition[0] - self.position[0]) <=1 and abs(newPosition[1] - self.position[1]) <= 1:
                if board[newPosition[0]][newPosition[1]] != None:
                    if board[newPosition[0]][newPosition[1]].colour != self.colour:
                        return 'Yes'
                    else:
                        return "Move is illegal - pieces of the same colour cannot be captured."
                return 'Yes'
            else:
                return "Move is illegal - the king can only move one square in any direction - up, down, left, right or diagonally."
        else:
            return "Move is illegal - pieces have to move within the borders of the board."

    def in_check(self):
        for i in board:
            for j in i:
                if j != None and j.check_if_this_move_is_legal((self.position[0],self.position[1])) == 'Yes':
                    return 'Yes'
        return 'No'


def convert(x):
    code = [1,2,3,4]
    letters = ['a','b','c','d','e','f','g','h']
    if len(x) > 7:
        if x[0] in letters:
            for i in range(0, 8):
                if x[0] == letters[i]:
                    code[0] = i
        else:
            return None
        try:
            code[1] = 8 - int(x[1])
        except:
            return None
        if x[6] in letters:
            for i in range(0, 8):
                if x[6] == letters[i]:
                    code[2] = i
        else:
            return None
        try:
            code[3] = 8 - int(x[7])
        except:
            return None
    else:
        return None

    return code

print(convert("a2 to h5"))


@Bot.event
async def on_message(message):
    general_channel = Bot.get_channel(815231056491839511)
    global game
    stop = 0
    if message.content[0:5] == 'chess':
        if message.content[6:11] == 'start':
            if game == 'on':
                messageToSend = "There is another game going on right now. If you want to end it, please use 'chess end'."
                print(messageToSend)
                await general_channel.send(messageToSend)
                stop = 1
            else:
                game = 'on'
                messageToSend = "Game will now start. If you want to end it, please use 'chess end'."
                print(messageToSend)
                await general_channel.send(messageToSend)
                img = copy.deepcopy(empty_board)
                for i in board:
                    for j in i:
                        if str(type(j))[17:23] == 'Bishop':
                            if j.colour == 'black':
                                img.paste(black_Bishop, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          black_Bishop)
                            else:
                                img.paste(white_Bishop, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          white_Bishop)
                        elif str(type(j))[17:21] == 'Pawn':
                            if j.colour == 'black':
                                img.paste(black_Pawn, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          black_Pawn)
                            else:
                                img.paste(white_Pawn, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          white_Pawn)

                        elif str(type(j))[17:22] == 'Horse':
                            if j.colour == 'black':
                                img.paste(black_Horse, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          black_Horse)
                            else:
                                img.paste(white_Horse, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          white_Horse)
                        elif str(type(j))[17:21] == 'Rook':
                            if j.colour == 'black':
                                img.paste(black_Rook, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          black_Rook)
                            else:
                                img.paste(white_Rook, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          white_Rook)
                        elif str(type(j))[17:22] == 'Queen':
                            if j.colour == 'black':
                                img.paste(black_Queen, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          black_Queen)
                            else:
                                img.paste(white_Queen, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          white_Queen)
                        elif str(type(j))[17:21] == 'King':
                            if j.colour == 'black':
                                img.paste(black_King, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          black_King)
                            else:
                                img.paste(white_King, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          white_King)
                # img.show()
                img.save("image_to_show.jpg")
                await general_channel.send(file=discord.File('image_to_show.jpg'))


        elif stop == 0 and len(message.content) == 14:
            move = message.content[6:14]
            global turn
            check = None
            if str(message.author)[0:12] != 'JP_Chess_Bot':

                if convert(move) == None:
                    messageToSend = "Invalid command. Commands should be of the form 'chess [a-h][1-8] to [a-h][1-8]'."
                    print(messageToSend)
                    await general_channel.send(messageToSend)
                else:
                    y = convert(move)
                    print("y =",y)
                    if board[y[0]][y[1]] != None:
                        if board[y[0]][y[1]].colour == turn:
                            if board[y[0]][y[1]].check_if_this_move_is_legal((y[2],y[3])) == 'Yes':
                                if check == turn:

                                    piece = board[y[2]][y[3]]
                                    board[y[2]][y[3]] = board[y[0]][y[1]]
                                    board[y[2]][y[3]].position = (y[2],y[3])
                                    board[y[0]][y[1]] = None
                                    KingPosition = [0,0]
                                    for i in range(0,8):
                                        for j in range(0,8):
                                            if str(type(board[i][j]))[17:21] == 'King' and board[i][j].colour == turn:
                                                KingPosition[0] = board[i][j].position[0]
                                                KingPosition[1] = board[i][j].position[1]
                                    if board[KingPosition[0]][KingPosition[1]].in_check() == 'Yes':
                                        board[y[0]][y[1]] = board[y[2]][y[3]]
                                        board[y[0]][y[1]].position = (y[0],y[1])
                                        board[y[2]][y[3]] = piece
                                    else:
                                        check = None


                                else:
                                    board[y[2]][y[3]] = board[y[0]][y[1]]
                                    board[y[2]][y[3]].position = (y[2], y[3])
                                    board[y[0]][y[1]] = None

                                    if turn == 'white':
                                        turn = 'black'
                                    else:
                                        turn = 'white'

                                    KingPosition = [0, 0]
                                    for i in range(0,8):
                                        for j in range(0,8):
                                            if str(type(board[i][j]))[17:21] == 'King' and board[i][j].colour == turn:
                                                KingPosition[0] = board[i][j].position[0]
                                                KingPosition[1] = board[i][j].position[1]
                                    if board[KingPosition[0]][KingPosition[1]].in_check() == 'Yes':
                                        check = turn

                                    img = copy.deepcopy(empty_board)
                                    for i in board:
                                        for j in i:
                                            if str(type(j))[17:23] == 'Bishop':
                                                if j.colour == 'black':
                                                    img.paste(black_Bishop,(100*(1+j.position[0]),100*(1+j.position[1])), black_Bishop)
                                                else:
                                                    img.paste(white_Bishop, (100*(1+j.position[0]),100*(1+j.position[1])), white_Bishop)
                                            elif str(type(j))[17:21] == 'Pawn':
                                                if j.colour == 'black':
                                                    img.paste(black_Pawn, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])), black_Pawn)
                                                else:
                                                    img.paste(white_Pawn, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])), white_Pawn)

                                            elif str(type(j))[17:22] == 'Horse':
                                                if j.colour == 'black':
                                                    img.paste(black_Horse,(100*(1+j.position[0]),100*(1+j.position[1])), black_Horse)
                                                else:
                                                    img.paste(white_Horse, (100*(1+j.position[0]),100*(1+j.position[1])), white_Horse)
                                            elif str(type(j))[17:21] == 'Rook':
                                                if j.colour == 'black':
                                                    img.paste(black_Rook,(100*(1+j.position[0]),100*(1+j.position[1])), black_Rook)
                                                else:
                                                    img.paste(white_Rook, (100*(1+j.position[0]),100*(1+j.position[1])), white_Rook)
                                            elif str(type(j))[17:22] == 'Queen':
                                                if j.colour == 'black':
                                                    img.paste(black_Queen,(100*(1+j.position[0]),100*(1+j.position[1])), black_Queen)
                                                else:
                                                    img.paste(white_Queen, (100*(1+j.position[0]),100*(1+j.position[1])), white_Queen)
                                            elif str(type(j))[17:21] == 'King':
                                                if j.colour == 'black':
                                                    img.paste(black_King,(100*(1+j.position[0]),100*(1+j.position[1])), black_King)
                                                else:
                                                    img.paste(white_King, (100*(1+j.position[0]),100*(1+j.position[1])), white_King)
                                    #img.show()
                                    img.save("image_to_show.jpg")
                                    await general_channel.send(file=discord.File('image_to_show.jpg'))
                            else:
                                messageToSend = board[y[0]][y[1]].check_if_this_move_is_legal((y[2], y[3]))
                                print(messageToSend)
                                await general_channel.send(messageToSend)
                        else:
                            messageToSend = "It is " + str(turn) + "'s turn. Only " + turn + "pieces can be moved."
                            print(messageToSend)
                            await general_channel.send(messageToSend)
                    else:
                        messageToSend = "There is no piece at ("+str(y[0])+","+str(y[1])+")."
                        print(messageToSend)
                        await general_channel.send(messageToSend)



board = [[Rook("black",(0,0)),None,None,None,None,None,None,Rook("white",(0,7))],[Horse("black",(1,0)),None,None,None,None,None,None,Horse("white",(1,7))],[Bishop("black",(2,0)),None,None,None,None,None,None,Bishop("white",(2,7))],[Queen('black',(3,0)),None,None,None,None,None,None,Queen('white',(3,7))],[King('black',(4,0)),None,None,None,None,None,None,King('white',(4,7))],[Bishop("black",(5,0)),None,None,None,None,None,None,Bishop("white",(5,7))],[Horse("black",(6,0)),None,None,None,None,None,None,Horse("white",(6,7))],[Rook("black",(7,0)),None,None,None,None,None,None,Rook("white",(7,7))]]
for i in range(0,8):
    for j in range(0,8):
        if j == 1:
            board[i][j] = Pawn('black',(i,j))
        if j == 6:
            board[i][j] = Pawn('white',(i,j))
empty_board = copy.deepcopy(img)

turn = 'white'
game = 'over'

        
@Bot.event
async def on_ready():
    general_channel = Bot.get_channel(815231056491839511)
    await general_channel.send("Hello world")


Bot.run('ODE1MjI2NzE2NTUyMjk4NTM2.YDpVCw.1F2Ipv-YAYBdnHvWA3dy17Jm1qg')
