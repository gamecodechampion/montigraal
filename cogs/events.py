import discord
from discord.ext import commands

class event(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(738540358761316439)
        emb=discord.Embed(description = f'Welcome to the server {member.mention}!', color = discord.Colour.random())
        emb.set_thumbnail(url=member.avatar_url)
        await channel.send(embed=emb)
        await member.send("I hope you enjoy your time in this server! :slight_smile:")



def setup(bot):
    bot.add_cog(event(bot))
