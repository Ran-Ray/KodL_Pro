import discord
from discord.ext import commands
import os, random
from sampah import sampah_anorganik, sampah_organik, link, perintah

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def  on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def organik(ctx):
    await ctx.send('salah satu contoh sampah organik adalah :')
    await ctx.send(sampah_organik())

@bot.command()
async def anorganik(ctx):
    await ctx.send('salah satu contoh sampah anorganik adalah :')
    await ctx.send(sampah_anorganik())

@bot.command()
async def joke(ctx):
    img_name = random.choice(os.listdir('E memes'))
    with open(f'E memes/{img_name}', 'rb') as f:
        picture = discord.File(f)
        f.close()
    await ctx.send(file=picture)

@bot.command()
async def usefull_link(ctx):
    await ctx.send('salah satu link yang dapat membantu anda mempelajari tentang enviromental :')
    await ctx.send(link())

@bot.command()
async def info(ctx):
    await ctx.send('command :')
    await ctx.send(perintah())
    await ctx.send('bot by : Ran')

bot.run("")
