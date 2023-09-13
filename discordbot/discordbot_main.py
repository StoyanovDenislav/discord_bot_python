import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import sys

file_dir = os.path.dirname('./backend')
sys.path.append(file_dir)

from backend.osuapi.temp_get_token import getToken
import discordbot.beatmaps_discord as beatmaps_discord

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

access_token = getToken()

print(access_token)

@bot.command(name="getuserscore")
async def getUserScore(ctx, arg1, arg2, arg3=None, arg4=None):
    
    data = beatmaps_discord.getuserscore(access_token, arg1, arg2, arg3, arg4)
    
    await ctx.send(embed=data)


bot.run(bot_token)
