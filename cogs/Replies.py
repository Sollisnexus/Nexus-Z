import discord
import random
from discord.ext import commands

class Replies(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Reply online.')

    # Commands
    @commands.command()
    @commands.cooldown(rate=1, per=5.0)
    async def addcommand(self, ctx):
        embed = discord.Embed(title="", description="", color=0x2962FF)
        embed.set_image(url="https://thumbs.gfycat.com/DismalWarmArmadillo-size_restricted.gif")
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(rate=1, per=5.0)
    async def nexusz(self, ctx):
        embed = discord.Embed(title="", description="", color=0x2962FF)
        embed.set_image(url="https://thumbs.gfycat.com/RegularInnocentBug-size_restricted.gif")
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(rate=1, per=5.0)
    async def freepokemon(self, ctx):
        embed = discord.Embed(title="", description="", color=0x2962FF)
        embed.set_image(url="https://cdn.discordapp.com/attachments/676543990853795840/734577723804221503/SPOILER_YouFool.gif")
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(rate=1, per=5.0)
    async def echo(self, ctx, arg):
        await ctx.send(arg)


def setup(client):
    client.add_cog(Replies(client))
