import discord
import os
import asyncio
import time
import random
from discord.ext import commands
from colorama import Fore as COL
from colorama import Style as STY

nigga = input(f'{COL.GREEN}{STY.BRIGHT}[?] {COL.RESET}Enter Prefix: ')
niggaa = input(f'{COL.GREEN}{STY.BRIGHT}[?] {COL.RESET}Enter Token: ')
niglet = input(f'{COL.GREEN}{STY.BRIGHT}[?] {COL.RESET}Enter Dank Memers Prefix In The Server You Are Farming: ')

dank = commands.Bot(command_prefix=nigga, self_bot=True, case_insensitive=True, intents=discord.Intents.all())
dank.remove_command('help')

@dank.event
async def on_ready():
  os.system('clear')
  print(rf"""{COL.GREEN}{STY.BRIGHT}                                                     
                             .-----.
                            /7  .  (
                           /   .-.  \
                          /   /   \  \
                         / `  )   (   )
                        / `   )   ).  \
                      .'  _.   \_/  . |
     .--.           .' _.' )`.        |
    (    `---...._.'   `---.'_)    ..  \
     \            `----....___    `. \  |
      `.           _ ----- _   `._  )/  |
        `.       /"  \   /"  \`.  `._   |
          `.    ((O)` ) ((O)` ) `.   `._\
            `-- '`---'   `---' )  `.    `-.
               /                  ` \      `-.
             .'                      `.       `.
            /                     `  ` `.       `-.
     .--.   \ ===._____.======. `    `   `. .___.--`     .''''.
    ' .` `-. `.                )`. `   ` ` \          .' . '  8)
   (8  .  ` `-.`.               ( .  ` `  .`\      .'  '    ' /
    \  `. `    `-.               ) ` .   ` ` \  .'   ' .  '  /
     \ ` `.  ` . \`.    .--.     |  ` ) `   .``/   '  // .  /
      `.  ``. .   \ \   .-- `.  (  ` /_   ` . / ' .  '/   .'
        `. ` \  `  \ \  '-.   `-'  .'  `-.  `   .  .'/  .'
          \ `.`.  ` \ \    ) /`._.`       `.  ` .  .'  /
           |  `.`. . \ \  (.'               `.   .'  .'
        __/  .. \ \ ` ) \                     \.' .. \__
 .-._.-'     '"  ) .-'   `.                   (  '"     `-._.--.
(_________.-====' / .' /\_)`--..__________..-- `====-. _________)
  {COL.RESET}
   {COL.RED}{STY.BRIGHT}[?] {COL.RESET}Dank Farmer Is Now Online - Run {dank.command_prefix}Help To Get Started!
{COL.MAGENTA} made by yum :)
""")

@dank.command(invoke_without_command=True)
async def help(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=0x2639eb)
  embed.set_author(name="𝘿𝘼𝙉𝙆 𝙁𝘼𝙍𝙈𝙀𝙍  | 𝙋𝙍𝙀𝙁𝙄𝙓: " + str(dank.command_prefix), icon_url=dank.user.avatar_url)
  embed.set_image(url="")
  embed.add_field(name=" :frog: Autobeg {On/Off}", value="Farm dank memer with `pls beg`", inline=True)
  embed.add_field(name=" :frog: Autodaily {On/Off}", value="Farm dank memer with `pls daily`", inline=True)
  embed.add_field(name=" :frog: Autoweek {On/Off}", value="Farm dank memer with `pls weekly`", inline=True)
  embed.add_field(name=" :frog: Automonth {On/Off}", value="Farm dank memer with `pls monthly`", inline=True)
  embed.add_field(name=" :frog: Automeme {On/Off}", value="Farm dank memer with `pls postmeme`", inline=True)
  embed.add_field(name=" :frog: Autolottery {On/Off}", value="Farm dank memer with `pls lottery`", inline=True)
  embed.add_field(name=" :frog: Autoslots {On/Off}", value="Farm dank memer with `pls slots`", inline=True)
  embed.add_field(name=" :frog: Autobet {On/Off}", value="Farm dank memer with `pls bet`", inline=True)
  embed.add_field(name=" :frog: Autogamble {On/Off}", value="Farm dank memer with `pls gamble`", inline=True)
  embed.add_field(name=" :frog: Autosnake {On/Off}", value="Farm dank memer with `pls snakeeyes`", inline=True)
  embed.add_field(name=" :frog: Autofish {On/Off}", value="Farm dank memer with `pls fish`", inline=True)
  embed.add_field(name=" :frog: Autohunt {On/Off}", value="Farm dank memer with `pls hunt`", inline=True)
  embed.add_field(name=" :frog: Autowash {On/Off}", value="Farm dank memer with `pls pet wash`", inline=True)
  embed.add_field(name=" :frog: Autofeed {On/Off}", value="Farm dank memer with `pls pet feed`", inline=True)
  embed.add_field(name=" :frog: Exit", value="Exits The Program", inline=True)
  embed.set_image(url="https://j.gifs.com/vgMnVL.gif")
  await ctx.send(embed=embed)

autobeg_enabled = False

@dank.command()
async def autobeg(ctx,choice):
    global autobeg_enabled
    await ctx.message.delete()
    if choice == 'on':
      await ctx.send(f"Autobeg is now enabled run `({dank.command_prefix}Autobeg off)` to disable Autobeg.")
      autobeg_enabled = True
      while True:
        try:
          await ctx.send(f'{niglet} beg')
          time.sleep(1)
          await ctx.send(f'{niglet} dep max')
          await asyncio.sleep(45)
        except:
          print("Couldn't Beg. Did the channel get nuked or deleted?")
     
    elif choice == 'off':
      await ctx.send("Autobeg is now disabled.")
      autobeg_enabled = False

autodaily_enabled = False

@dank.command()
async def autodaily(ctx,choice):
    global autodaily_enabled
    await ctx.message.delete()
    if choice == 'on':
      await ctx.send(f"Autodaily is now enabled run `({dank.command_prefix}Autodaily off)` to disable Autodaily.")
      autodaily_enabled = True
      while True:
        try:
          await ctx.send(f'{niglet} daily')
          time.sleep(1)
          await ctx.send(f'{niglet} dep max')
          await asyncio.sleep(86400)
        except:
          print("Couldn't Daily. Did the channel get nuked or deleted?")
     
    elif choice == 'off':
      await ctx.send("Autodaily is now disabled.")
      autodaily_enabled = False

autoweekly_enabled = False

@dank.command()
async def autoweekly(ctx,choice):
    global autoweekly_enabled
    await ctx.message.delete()
    if choice == 'on':
      await ctx.send(f"Autoweekly is now enabled run `({dank.command_prefix}Autoweekly off)` to disable Autoweekly.")
      autoweekly_enabled = True
      while True:
        try:
          await ctx.send(f'{niglet} weekly')
          time.sleep(1)
          await ctx.send(f'{niglet} dep max')
          await asyncio.sleep(604800)
        except:
          print("Couldn't Weekly. Did the channel get nuked or deleted?")
     
    elif choice == 'off':
      await ctx.send("Autoweekly is now disabled.")
      autoweekly_enabled = False

automonthly_enabled = False

@dank.command()
async def automonthly(ctx,choice):
    global automonthly_enabled
    await ctx.message.delete()
    if choice == 'on':
      await ctx.send(f"Automonthly is now enabled run `({dank.command_prefix}Automonthly off)` to disable Automonthly.")
      automonthly_enabled = True
      while True:
        try:
          await ctx.send(f'{niglet} monthly')
          time.sleep(1)
          await ctx.send(f'{niglet} dep max')
          await asyncio.sleep(2678400)
        except:
          print("Couldn't Monthly. Did the channel get nuked or deleted?")
     
    elif choice == 'off':
      await ctx.send("Automonthly is now disabled.")
      automonthly_enabled = False

automeme_enabled = False

@dank.command()
async def automeme(ctx,choice):
    frick = ['f', 'r', 'i', 'c', 'k']
    global automeme_enabled
    await ctx.message.delete()
    if choice == 'on':
      await ctx.send(f"Automeme is now enabled run `({dank.command_prefix}Automeme off)` to disable Automeme.")
      automeme_enabled = True
      while True:
        try:
          await ctx.send(f'{niglet} postmeme')
          time.sleep(1)
          await ctx.send(f'{random.choice(frick)}')
          time.sleep(1)
          await ctx.send(f'{niglet} dep max')
          await asyncio.sleep(60)
        except:
          print("Couldn't Post Meme. Did the channel get nuked or deleted?")
     
    elif choice == 'off':
      await ctx.send("Automeme is now disabled.")
      automeme_enabled = False

autolottery_enabled = False

@dank.command()
async def autolottery(ctx,choice):
    global autolottery_enabled
    await ctx.message.delete()
    if choice == 'on':
      await ctx.send(f"Autolottery is now enabled run `({dank.command_prefix}Autolottery off)` to disable Autolottery.")
      autolottery_enabled = True
      while True:
        try:
          await ctx.send(f'{niglet} lottery')
          time.sleep(1)
          await ctx.send('yes')
          await asyncio.sleep(3600)
        except:
          print("Couldn't Lottery. Did the channel get nuked or deleted?")
     
    elif choice == 'off':
      await ctx.send("Autolottery is now disabled.")
      autolottery_enabled = False

autoslots_enabled = False

@dank.command()
async def autoslots(ctx,choice):
    global autoslots_enabled
    await ctx.message.delete()
    if choice == 'on':
      await ctx.send(f"Autoslots is now enabled run `({dank.command_prefix}Autoslots off)` to disable Autoslots.")
      autoslots_enabled = True
      while True:
        try:
          await ctx.send(f'{niglet} with 100')
          time.sleep(1)
          await ctx.send(f'{niglet} slots 100')
          await asyncio.sleep(100)
        except:
          print("Couldn't Slot. Did the channel get nuked or deleted?")
     
    elif choice == 'off':
      await ctx.send("Autoslots is now disabled.")
      autoslots_enabled = False

autobet_enabled = False

@dank.command()
async def autobet(ctx,choice):
    global autobet_enabled
    await ctx.message.delete()
    if choice == 'on':
      await ctx.send(f"Autobet is now enabled run `({dank.command_prefix}Autobet off)` to disable Autobet.")
      autobet_enabled = True
      while True:
        try:
          await ctx.send(f'{niglet} with 100')
          time.sleep(1)
          await ctx.send(f'{niglet} bet 100')
          await asyncio.sleep(100)
        except:
          print("Couldn't Bet. Did the channel get nuked or deleted?")
     
    elif choice == 'off':
      await ctx.send("Autobet is now disabled.")
      autobet_enabled = False

autogamble_enabled = False

@dank.command()
async def autogamble(ctx,choice):
    global autogamble_enabled
    await ctx.message.delete()
    if choice == 'on':
      await ctx.send(f"Autogamble is now enabled run `({dank.command_prefix}Autogamble off)` to disable Autogamble.")
      autogamble_enabled = True
      while True:
        try:
          await ctx.send(f'{niglet} with 100')
          time.sleep(1)
          await ctx.send(f'{niglet} gamble 100')
          await asyncio.sleep(100)
        except:
          print("Couldn't Gamble. Did the channel get nuked or deleted?")
     
    elif choice == 'off':
      await ctx.send("Autogamble is now disabled.")
      autogamble_enabled = False

autofish_enabled = False

@dank.command()
async def autofish(ctx,choice):
    global autofish_enabled
    await ctx.message.delete()
    if choice == 'on':
      await ctx.send(f"Autofish is now enabled run `({dank.command_prefix}Autofish off)` to disable Autofish.")
      autofish_enabled = True
      while True:
        try:
          await ctx.send(f'{niglet} fish')
          await asyncio.sleep(60)
        except:
          print("Couldn't Fish. Did the channel get nuked or deleted?")
     
    elif choice == 'off':
      await ctx.send("Autofish is now disabled.")
      autofish_enabled = False

autohunt_enabled = False

@dank.command()
async def autohunt(ctx,choice):
    global autohunt_enabled
    await ctx.message.delete()
    if choice == 'on':
      await ctx.send(f"Autohunt is now enabled run `({dank.command_prefix}Autohunt off)` to disable Autohunt.")
      autohunt_enabled = True
      while True:
        try:
          await ctx.send(f'{niglet} hunt')
          await asyncio.sleep(60)
        except:
          print("Couldn't Fish. Did the channel get nuked or deleted?")
     
    elif choice == 'off':
      await ctx.send("Autohunt is now disabled.")
      autohunt_enabled = False

autowash_enabled = False

@dank.command()
async def autowash(ctx,choice):
    global autowash_enabled
    await ctx.message.delete()
    if choice == 'on':
      await ctx.send(f"Autowash is now enabled run `({dank.command_prefix}Autowash off)` to disable Autowash.")
      autowash_enabled = True
      while True:
        try:
          await ctx.send(f'{niglet} pet wash')
          await asyncio.sleep(3600)
        except:
          print("Couldn't Wash. Did the channel get nuked or deleted?")
     
    elif choice == 'off':
      await ctx.send("Autowash is now disabled.")
      autowash_enabled = False

autofeed_enabled = False

@dank.command()
async def autofeed(ctx,choice):
    global autofeed_enabled
    await ctx.message.delete()
    if choice == 'on':
      await ctx.send(f"Autofeed is now enabled run `({dank.command_prefix}Autofeed off)` to disable Autofeed.")
      autofeed_enabled = True
      while True:
        try:
          await ctx.send(f'{niglet} pet feed')
          await asyncio.sleep(3600)
        except:
          print("Couldn't Feed. Did the channel get nuked or deleted?")
     
    elif choice == 'off':
      await ctx.send("Autofeed is now disabled.")
      autofeed_enabled = False

autosnake_enabled = False

@dank.command()
async def autosnake(ctx,choice):
    global autosnake_enabled
    await ctx.message.delete()
    if choice == 'on':
      await ctx.send(f"Autosnake is now enabled run `({dank.command_prefix}Autosnake off)` to disable Autosnake.")
      autosnake_enabled = True
      while True:
        try:
          await ctx.send(f'{niglet} with 100')
          time.sleep(1)
          await ctx.send(f'{niglet} snakeeyes 100')
          await asyncio.sleep(100)
        except:
          print("Couldn't Snake. Did the channel get nuked or deleted?")
     
    elif choice == 'off':
      await ctx.send("Autosnake is now disabled.")
      autosnake_enabled = False

@dank.command()
async def credits(ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=0x2639eb, timestamp=ctx.message.created_at)
        embed.set_author(name="𝘾𝙍𝙀𝘿𝙄𝙏𝙎")
        embed.add_field(name="`YUM`", value="Creator")
        await ctx.send(embed=embed)

dank.run(niggaa, bot = False)
