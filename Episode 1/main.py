**VERY OUTDATED**
**SOME PARTS MAY NOT WORK AS SHOWN**

#imports 
import os
import discord 

#from __
from discord.ext import commands



client = commands.Bot(command_prefix= '?')#bots prefix
#^^^
#If used bot then replace client with bot.



#once bot is ready print all infomtion below. 
@client.event
async def on_ready():
  print('Youtube Bot 1')
  print('Logged in as: '+client.user.name)
  print('Client User ID: '+str(client.user.id))

#print = displays in the console or discord. 

#Error Message
@client.event
async def on_command_error(ctx, error):
  if isinstance(error,commands.CommandNotFound):
    await ctx.send('Invalid Command Used :eyes:')#can customize error message.



#if not using replit. Just use client.run(your-bot-token)
#keep, Make bot online.
my_secret = os.environ['Bot Token']

client.run(my_secret)
