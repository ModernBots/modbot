import datetime

import disnake
from disnake.ext import commands
import humanfriendly

upsince = datetime.datetime.now()
version = "**ALPHA PRERELEASE**"


class InfoCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	class InfoButtons(disnake.ui.View):
		def __init__(self):
			super().__init__()
			self.add_item(disnake.ui.Button(
				style=disnake.ButtonStyle.link,
				label="GitHub",
				emoji="<:github:923861791409307659>",
				url="https://github.com/ThatOneCalculator/modernbot",
				row=0
			))
			self.add_item(disnake.ui.Button(
				style=disnake.ButtonStyle.link,
				label="Invite RankBot to another server",
				emoji="<:rankbot:924568569138802718>",
				url="https://discord.com/api/oauth2/authorize?client_id=924433694574391306&permissions=8&scope=bot%20applications.commands",
				row=0
			))
			self.add_item(disnake.ui.Button(
				style=disnake.ButtonStyle.link,
				label="ModernBots homepage",
				emoji="<:modernbots:924434750435897344>",
				url="https://github.com/modernbots",
				row=1
			))
			self.add_item(disnake.ui.Button(
				style=disnake.ButtonStyle.link,
				label="Check out DropBot",
				emoji="<:dropbot:924434751316697119>",
				url="https://github.com/modernbots/dropbot",
				row=1
			))
			self.add_item(disnake.ui.Button(
				style=disnake.ButtonStyle.link,
				label="Check out ContentBot",
				emoji="<:contentbot:924434750914068480>",
				url="https://github.com/modernbots/contentbot",
				row=1
			))
			self.add_item(disnake.ui.Button(
				style=disnake.ButtonStyle.link,
				label="Check out RankBot",
				emoji="<:rankbot:924568569138802718>",
				url="https://github.com/modernbots/rankbot",
				row=1
			))

	commands.slash_command(
		description="Gives some helpful information about the bot.")

	async def info(self, inter: disnake.ApplicationCommandInteraction):
		# botinfo = await self.bot.topggpy.get_bot_info()
		# votes = botinfo["monthly_points"]
		# allvotes = botinfo["points"]
		shardscounter = []
		for guild in self.bot.guilds:
			if guild.shard_id not in shardscounter:
				shardscounter.append(guild.shard_id)
		shards = []
		for i in shardscounter:
			shards.append(self.bot.get_shard(i))
		allmembers = 0
		for guild in self.bot.guilds:
			try:
				allmembers += guild.member_count
			except:
				pass
		uptime = datetime.datetime.now() - upsince
		embed = disnake.Embed(
			title="ModernBot Info",
			description="Made by ThatOneCalculator#0001",
			color=0x5865F2,
			#url="https://modernself.bot.t1c.dev/"
		)
		embed.set_thumbnail(
			url="https://cdn.discordapp.com/attachments/810799100940255260/924574844866138122/New_Project6.png")
		embed.add_field(
			name="🤔 How to use",
			value="""""",
			inline=False
		)
		embed.add_field(
			name="💁 About ModernBots",
			value="""ModernBots is a group of free and open source Discord bots made by ThatOneCalculator designed for Discord's new components.

There are currently 4 ModernBots: [DropBot](https://github.com/modernbots/dropbot), [ModBot](https://github.com/modernbots/modbot), [ContentBot](https://github.com/modernbots/contentbot), and [RankBot](https://github/.com/modernbots/rankbot).
DropBot makes dropdown role menus and polls, ModBot helps out with moderation, ContentBot makes content announcements (i.e. YouTube, Twitch), and RankBot handles server ranking/leveling.""",
			inline=False
		)
		embed.add_field(
			name="🏓 Ping",
			value=f"Bot latency is {str(round((self.bot.latency * 1000),2))} milliseconds.",
			inline=False
		)
		embed.add_field(
			name="☕ Uptime",
			value=f"I have been up for {humanfriendly.format_timespan(uptime)}.",
		)
		embed.add_field(
			name="🔮 Shards",
			value=f"This guild is on shard {inter.guild.shard_id}, with a total of {len(shards)} shards.",
		)
		embed.add_field(
			name="👪 Bot stats",
			value=f"I am in {len(self.bot.guilds):,} servers with a total of {allmembers:,} people.",
		)
		# embed.add_field(
		# 	name="📈 Votes",
		# 	value=f"I have {int(votes):,} mothly votes and {int(allvotes):,} all-time votes on top.gg.",
		# )
		embed.add_field(
			name="🧑‍💻 Version",
			value=f"I am on version {version}. This bot uses disnake, and is licensed under the A-GPLv3 code license. See the GitHub for more info.",
			inline=False
		)
		await inter.send(content=None, embed=embed, view=InfoCog.InfoButtons())


def setup(bot):
	bot.add_cog(InfoCog(bot))
