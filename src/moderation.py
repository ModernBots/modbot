import datetime

import disnake
from bson.objectid import ObjectId
from disnake.ext import commands
from motor import motor_asyncio

mongoclient = motor_asyncio.AsyncIOMotorClient()
db = mongoclient.modernbot
guild_preferences = db.guild_preferences


class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    class Confirm(disnake.ui.View):
        def __init__(self):
            super().__init__()
            self.value = None

        @disnake.ui.button(label="Confirm", style=disnake.ButtonStyle.green, emoji="<:check_yes:925821993788526724>", row=0)
        async def confirm(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
            await inter.response.send_message("Confirming", ephemeral=True)
            self.value = True
            self.stop()

        @disnake.ui.button(label="Cancel", style=disnake.ButtonStyle.red, emoji="<:check_no:925822132976500787>", row=0)
        async def cancel(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
            await inter.response.send_message("Cancelling", ephemeral=True)
            self.value = False
            self.stop()

    @commands.slash_command()
    @commands.has_permissions(manage_messages=True)
    async def purge(
        self,
        inter: disnake.ApplicationCommandInteraction,
        amount: int=commands.Param(ge=1, le=100),
        person: disnake.Member=commands.Param(default=None)):
        """
        Purge the last X messages.

        Parameters
        ----------
        amount : int
            The amount of messages to purge.
        person : Member
            (Optional) the person to purge messages from.
        """

        def check_victim(m):
            if person != None:
                return m.author == person
            else:
                return True

        view = Confirm()
        await ctx.send("Do you want to continue?", view=view)
        await view.wait()
        if view.value is None:
            print("Timed out...")
        elif view.value:
            print("Confirmed...")
        else:
            print("Cancelled...")
        deleted = await inter.channel.purge(limit=amount, check=check_victim)
        await inter.send(content=f"I have purged {deleted} messages.", ephemeral=True)

    @commands.slash_command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason: str = None):
        """
        Ban a member.
        """
        await member.send("You've been banned.")
        await member.ban(reason=reason)

    @commands.slash_command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str = None):
        """
        Kick a member.
        """
        await member.send("You've been kicked.")
        await member.kick(reason=reason)

    @commands.slash_command()
    @commands.has_permissions(manage_roles=True)
    async def timeout(self, ctx, member: discord.Member, *, reason: str = None):
