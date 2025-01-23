import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
###sí

load_dotenv()
token = os.getenv("dt")

Intents = discord.Intents.default()
Intents.message_content = True

bot = commands.Bot(command_prefix= "==", intents = Intents)

@bot.event
async def on_ready():
    print(f"Bot iniciado:{bot.user}")

@bot.command(name= "SUP")
async def welcome(ctx):
    await ctx.send("Hello!!!!!!!1!!1!1") 

@bot.command(name= "file")
async def file(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Imagen guardada en ./{attachment.filename}")
    else: 
        await ctx.reply("Nigga dimension")
bot.run(token)