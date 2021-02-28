# WarwickHACK 2021 - Discord Bot
A collection of features in a discord bot.

## Table of contents
* [Description](#description)
* [Technologies](#technologies)
* [Setup](#setup)

## Description of features
### Price check
A discord bot that can display the top 5 google shopping results. Using zenserp API and python to scrape the first 5 results of any product. After the cammand is entered, it will output the result as a discord embed message.
### Chat history
Command that takes an int parameter and stores that many past chat messages, it then creates a csv file with two columns, User and Message, then it private messages that file to the person who wrote the command and deletes it.
### List articles
Scans through the website PCGamer and lists the top 5 articles, their description and the link if the user feels like reading more about it

## Technologies
* Python 3.8.x or above
* Zenserp API

## Setup
- pip install requests
- pip install discord 

## Usage
###To check price a product:
'''
.check product GB
'''
- Note: for products with more than one word, for example: iPhone 12, use quotation marks:
'''
.check "iPhone 12" GB

### To see news:
'''
.news
'''

### To see history:
'''
.history 10
'''
where 10 is number of messages from before the command was issued. Other numbers can be used too.










