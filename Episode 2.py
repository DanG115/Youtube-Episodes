#imports 
import os
import random
import discord 

#from
from discord.ext import commands



client = commands.Bot(command_prefix= '?') #bots prefix
#^^ Client or bot can be used but replace everything with bot e.g @bot.commands()


#rolling status 

LISTENING = ['Memes', 'Spotify', 'Spam', 'Dms']
PLAYING = ['Proteting your server!',
           'Helping Servers', 'Music', 'None your buisness.',
           'Moderating', 'Amoung Us', 'Fortnite', 'COD', 'Discord']
WATCHING = ['Paint dry', 'Music videos', 'Moderation', 'Youtube', 'Reddit', 'The Sky', 'Your Server']
ACTIVITYTYPE = {'LISTENING': discord.ActivityType.listening,
                'PLAYING': discord.ActivityType.playing,
                'WATCHING': discord.ActivityType.watching}
PRESENCELISTS = ['LISTENING', 'PLAYING', 'WATCHING']
PRESENCE = random.choice(PRESENCELISTS)


@client.event
async def on_ready():
  print('Youtube Bot 1')
  print('Logged in as: '+client.user.name)
  print('Client User ID: '+str(client.user.id))

  await client.change_presence(activity=discord.Activity(
    type=ACTIVITYTYPE[PRESENCE], name=(random.choice(globals()[PRESENCE])+' | ?help')))



  
#Error Message
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
      await ctx.send('Invalid Command Used :eyes:')#can customize error message.

 



# First command
@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(client.latency * 1000)}ms 🏓') #~ You can customize with any emoji!

  
  



#keep, Makes bot online.
my_secret = os.environ['Bot Token']

client.run(my_secret)
