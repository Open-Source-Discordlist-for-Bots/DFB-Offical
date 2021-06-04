import datetime
from datetime import datetime
from datetime import timedelta
import discord
import platform
import time
from discord.ext import commands
import psutil
import sys
import os
import messages
from messages import *
import youtube_dl
from discord import voice_client
from googleapiclient.discovery import build
from discord.ext.commands import command
import asyncio

bot = commands.Bot(command_prefix = 'dfb?', intents=discord.Intents.all())
bot.remove_command('help')

# -- Discord Bot Configurations --

# Bot Variables
startTime = time.time()
botVersion = '1.2-stable'


# Discord Colors
dfbColor = 0x5865F2
procColor = 0xE4B400
nprocColor = 0x277ECD
certColor = 0x00FF00
approveColor = 0x00FF00


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Discordlist for Bots'))

    print('-- Discordlist for Bots --')
    print('**************************')
    print(f'Python Version: {platform.python_version()}')
    print('Bot started!')
    print('DFB is now ready to use.')
    print(f'Bot Version: {botVersion}')
    print('')
    print('-- System Monitor --')
    print('**************************')
    print(f'CPU Usage: {psutil.cpu_percent()}%')
    print(f'OS: {platform.platform()}')
    print(f'System Memory Usage: {psutil.virtual_memory()[2]}%')
    print("**************************")
    print('-- Bot Log --')
    print('')
    onStarted()


@bot.event
async def on_command_error(ctx, error):
    errorEmbed = discord.Embed(title='An Error occurred', description=f'=> {error}', color=discord.Color.red())
    await ctx.send(embed=errorEmbed)
    onError(error)


@bot.event
async def on_member_join(member):
    rank = discord.utils.get(member.guild.roles, id=768940141498204181)
    await member.add_roles(rank)
    onMemberJoined(member)


@bot.event
async def on_member_remove(member):
    onMemberLeft(member)

@bot.event
async def on_message_delete(message):
    onMessageDeleted(message)

@bot.event
async def on_member_update(after, before):
    if not before.bot:
        return

    if str(before.status) == "offline":
        if str(after.status) == "online":
            botOnOffline(after, before)

@bot.command()
async def help(ctx):
    if ctx.author.id == 703944517048598568 or ctx.author.id == 775017772358434817 or ctx.author.id == 705557092802625576:
        em = discord.Embed(
            title="Commands for DFB", color=dfbColor,
            description="**:gear: Moderation**\n"
                        "- `dfb?<emptyCommand>`\n"
                        "`<emptyDescription>`\n\n"
                        "**:hammer_pick: Utilities**\n"
                        "- `dfb?about`\n"
                        "Lets look some useful information about the bot\n\n"
                        "- `dfb?ping`\n"
                        "Shows you the bot ping\n\n"
                        "- `dfb?info`\n"
                        "Lets look info about the concept of DFB\n\n"
                        "**:musical_note: Music**\n"
                        "- `dfb?join`\n"
                        "DFB will join the voice channel where you are inside\n\n"
                        "- `dfb?leave`\n"
                        "DFB leaves the voice channel\n\n"
                        "- `dfb?localplay`\n"
                        "Plays a local soundfile (mp3)\n\n"
                        "**💻 For Developer**\n"
                        "- `dfb?approve <bot> <owner>`\n"
                        "Approves the mentioned bot\n\n"
                        "- `dfb?decline <bot> <owner> <reason>`\n"
                        "Declines the mentioned bot\n\n"
                        "- `dfb?nproc <bot> <owner>`\n"
                        "The mentioned bot won't be certified 'cause some mistakes!\n\n"
                        "- `dfb?certified <owner> <bot>`\n"
                        "Certifies the mentioned bot\n\n"
                        "- `dfb?slink`\n"
                        "Backup-Link for this Server\n\n"
                        "- `dfb?say <msg>`\n"
                        "Botsay Command\n\n"
                        "- `dfb?embedsay <msg>`\n"
                        "Embedbotsay Command\n\n"
                        "- `dfb?shutdown`\n"
                        "Shutdowns the Bot. (Buggy and does not work 100%)\n\n"
                        f"**Offical DFB Server » [Invite](https://discord.gg/9Hq7wqsmJy)**",
        )
        em.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
        await ctx.send(embed=em)

    else:
        em = discord.Embed(
            title="Commands for DFB", color=dfbColor,
            description="**:gear: Moderation**\n"
                        "- `dfb?<emptyCommand>`\n"
                        "`<emptyDescription>`\n\n"
                        "**:hammer_pick: Utilities**\n"
                        "- `dfb?about`\n"
                        "Lets look some useful information about the bot\n\n"
                        "- `dfb?ping`\n"
                        "Shows you the bot ping\n\n"
                        "- `dfb?info`\n"
                        "Lets look info about the concept of DFB\n\n"
                        "**:musical_note: Music**\n"
                        "- `dfb?join`\n"
                        "DFB will join the voice channel where you are inside\n\n"
                        "- `dfb?leave`\n"
                        "DFB leaves the voice channel\n\n"
                        "- `dfb?localplay`\n"
                        "Plays a local soundfile (mp3)\n\n"
                        f"**Offical DFB Server » [Invite](https://discord.gg/9Hq7wqsmJy)**",
        )
        em.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
        await ctx.send(embed=em)

# -- Help Command --


@bot.command()
@commands.has_permissions(administrator = True)
async def approve(ctx, bot, owner):
    em = discord.Embed(title='Bot approved', description=f'The Bot {bot} by {owner} was approved by <@{ctx.author.id}>! \n Your Bot is now available on the DFB website!', color=approveColor)
    await ctx.send(embed=em)
    await ctx.message.delete()


@bot.command()
@commands.has_permissions(administrator=True)
async def decline(ctx, arg1, arg2, *, arg3):
    em = discord.Embed(title='Bot declined', description=f'The Bot {arg1} by {arg2} was declined by <@{ctx.author.id}> \n \n**Reason** \n{arg3}', color=discord.Color.red())
    await ctx.send(embed=em)
    await ctx.message.delete()


@bot.command()
@commands.has_permissions(administrator=True)
async def proc(ctx, bot, owner):
    em = discord.Embed(title='Bot is in certification process', description=f'The Bot {bot} by {owner} is in cerfification process \n \n', color=procColor)
    await ctx.send(embed=em)
    await ctx.message.delete()


@bot.command()
@commands.has_permissions(administrator=True)
async def nproc(ctx, bot, owner):
    em = discord.Embed(title="Bot won't be certified!", description=f"The Bot {bot} by {owner} won't be certified \n \nSorry {owner} but we found a lot of mistakes. So the bot CANNOT be certified!", color=nprocColor)
    await ctx.send(embed=em)
    await ctx.message.delete()


@bot.command()
@commands.has_permissions(administrator=True)
async def certified(ctx, owner, bot):
    em = discord.Embed(title='Bot has been certified!', description=f'Hey {owner}! We have something big to say you! Your bot, {bot} was cerified by <@{ctx.author.id}>! \nYou are now a certified bot developer and your bot is one of the featured bots!', color=certColor)
    await ctx.send(embed=em)
    await ctx.message.delete()


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong 🏓 {round(bot.latency * 1000)}ms")


@bot.command()
@commands.has_role(768938229259960370)
async def slink(ctx):
    await ctx.send(f"> **__Serverbackup__**: https://discord.new/9rPgS6CncCFA")


@bot.command()
async def about(ctx):
    async with ctx.typing():
        em = discord.Embed(title="About the offical DFB!", color=dfbColor)
        em.add_field(name="CPU Usage", value=f"{psutil.cpu_percent(4)} %", inline=False)
        em.add_field(name="System Memory Usage", value=f"{psutil.virtual_memory()[2]} %", inline=True)
        em.add_field(name="Python Version", value=f"{platform.python_version()}", inline=True)
        em.add_field(name="Python Compiler", value=f"{platform.python_compiler()}", inline=False)
        em.add_field(name="Bot Version", value=f"{botVersion}")
        em.add_field(name="Uptime", value=f'{str(timedelta(seconds=int(round(time.time()-startTime))))}', inline=True)
        em.add_field(name="Other Informations", value=f'OS: {platform.system()} ' f' {platform.release()} \n')
        em.add_field(name="Github Repository", value=f'Main: https://github.com/Discordlist-for-Bots/ \nDFB by Julius: https://github.com/Discordlist-for-Bots/old-dfb-in-py/ \nImages: https://github.com/Discordlist-for-Bots/images', inline=False)
    await ctx.send(embed=em)


@bot.command()
async def info(ctx):
    em = discord.Embed(title="Discord list for Bots - Your Botlist", description="<Hier werden Informationen über Discordlist for Bots stehen>", color=discord.Color.blue())
    await ctx.send(embed=em)


@bot.command()
@commands.has_role(768938229259960370)
async def say(ctx, * , args):
    await ctx.send(args)
    await ctx.message.delete()


@bot.command()
@commands.has_role(768938229259960370)
async def embedsay(ctx, * , args):
    em = discord.Embed(description=args)
    await ctx.send(embed=em)
    await ctx.message.delete()


@bot.command()
@commands.has_role(768938229259960370)
async def shutdown(ctx):
    em = discord.Embed(title="Shutting down...", description="The bot will be shutting down...", color=discord.Color.red())
    await ctx.send(embed=em)


@bot.command()
async def join(ctx):
    em = discord.Embed(title="Joined Voicechannel", description="I've joined the Voicechannel", color=discord.Color.blue())
    channel = ctx.author.voice.channel
    await ctx.send(embed=em)
    await channel.connect()


@bot.command()
async def leave(ctx):
    em = discord.Embed(title="Left Voicechannel", description="I've left the Voicechannel", color=discord.Color.red())
    await ctx.send(embed=em)
    await ctx.voice_client.disconnect()


@bot.command()
async def localplay(self, ctx, *, query):
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)


# -- Token --
bot.run('Insert your Bot.Token here')
