import asyncio
import datetime

import disnake
import humanfriendly
import pymongo
# import topgg
from async_timeout import timeout
from disnake.ext import commands, tasks
from dotenv import dotenv_values
# from statcord import StatcordClient

token = dotenv_values(".env")["DISCORD"]
upsince = datetime.datetime.now()
version = "**ALPHA PRERELEASE**"
intents = disnake.Intents.default()
bot = commands.AutoShardedBot(
	command_prefix=commands.when_mentioned_or(";;"),
	intents=intents,
	chunk_guilds_at_startup=False,
)

# topggtoken = dotenv_values(".env")["TOPGG"]
# statcordkey = dotenv_values(".env")["STATCORD"]
# bot.topggpy = topgg.DBLClient(
# 	bot, topggtoken, autopost=True, post_shard_count=True)
# bot.statcord_client = StatcordClient(bot, statcordkey)

mongoclient = pymongo.MongoClient()
db = mongoclient.contentbot
guild_preferences = db.guild_preferences
announcements = db.announcements
