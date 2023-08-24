import discord
from discord.ext import commands
from Bot_logic import gen_pass
import random , os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(8))

@bot.command()
async def silly(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
        f.close()
    await ctx.send(file=picture)

@bot.command()
async def kitty(ctx):
    img_name = random.choice(os.listdir('Cats'))
    with open(f'Cats/{img_name}', 'rb') as f:
        picture = discord.File(f)
        f.close()
    await ctx.send(file=picture)

bot.run("")
