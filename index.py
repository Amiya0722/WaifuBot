import discord
from discord.ext import commands
import logging
import requests
from datetime import datetime


from dotenv import load_dotenv
import os
from pixiv_auth import mainFunct
load_dotenv() # Load environment variables from .env file

SECRET_KEY = os.getenv('TOKEN')


# Logging setup
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Intents setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Bot setup
bot = commands.Bot(command_prefix='@', intents=intents)

@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "shit" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} - don't use that word")
    await bot.process_commands(message)
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}")
@bot.command()
async def waifu(ctx,*,msg:str =''):
    print(msg)

# Define the API endpoint
    url = "https://api.waifu.im/search?included_tags=waifu"
    params = {
        'included_tags':['waifu']
    }
    if msg != '':
        params['included_tags'].extend(msg.split(' '))


# Send a GET request
    response = requests.get(url,params=params)


    if response.status_code == 200:

        data = response.json()
        print(data["images"][0]["url"])
        embed = discord.Embed(title = "here is your waifu",url = f"{data["images"][0]["source"]}",timestamp = datetime.now())
        embed.set_image(url = data["images"][0]["url"])
        embed.set_footer(text=f"Source: {data["images"][0]["source"]}")
        await ctx.send(embed = embed)

    else:
        print(f"Error: {response.status_code}")
@bot.command()
async def tag(ctx):
    url = "https://api.waifu.im/tags"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        valueVer = "" 
        valueNsfw = ""
        for i in data["versatile"]:
            valueVer = valueVer + f'- {i}\n'
        for i in data["nsfw"]:
            valueNsfw = valueNsfw + f'- {i}\n'
        embed = discord.Embed(title = "Tag")
        embed.add_field(name = "Versatile", value =valueVer)
        embed.add_field(name = "Nsfw", value =valueNsfw)
        await ctx.send(embed = embed)
@bot.command()
async def helpbot(ctx):
    value = "@hello: Greets the user who called the command. \n @waifu [tag1] [tag2] ...: Sends a random waifu image based on the specified tags.\n@tag: Displays a list of available tags for the waifu command.\n@helpbot: Displays a list of available commands.\n@pixiv [search_term]: Sends a random Pixiv illustration based on the specified search term."
    embed = discord.Embed(title = "Help")
    embed.add_field(name = "command", value = value)
    await ctx.send(embed = embed)
@bot.command()
async def pixiv(ctx,*,msg:str = 'Furina'):
    link = mainFunct(msg)
    if not link:
        await ctx.send("Không tìm thấy ảnh nào từ Pixiv.")
        return

    try:
        file = discord.File(link["file_path"], filename="pixiv.jpg")
        embed = discord.Embed(title=link["title"], timestamp=datetime.now())
        embed.add_field(name="Source", value=f'https://www.pixiv.net/en/artworks/{link["id"]}')
        embed.set_image(url="attachment://pixiv.jpg")
        await ctx.send(file=file, embed=embed)

    except Exception as e:
        await ctx.send(f"Lỗi khi gửi ảnh: {e}")
    if os.path.exists(link["file_path"]):
        os.remove(link["file_path"])


# Run bot
bot.run(SECRET_KEY, log_handler=handler, log_level=logging.DEBUG)
