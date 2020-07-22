import discord
import asyncio
import threading
from discord.ext import commands

class Replies(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Reply cog is online.')
    
    # Commands
    @commands.command(name='addcommand', help="You really shouldn't type this in if I were you")
    async def addcommand(self, ctx):
        embed = discord.Embed(title="", description="", color=0x2962FF)
        embed.set_image(url="https://thumbs.gfycat.com/DismalWarmArmadillo-size_restricted.gif")
        await ctx.send(embed=embed)
    
    @commands.command(name='nexusz?', help="Is this the real Nexus-Z?")
    async def nexusz(self, ctx):
        embed = discord.Embed(title="", description="", color=0x2962FF)
        embed.set_image(url="https://thumbs.gfycat.com/RegularInnocentBug-size_restricted.gif")
        await ctx.send(embed=embed)
    
    @commands.command(name='blaines')
    async def blaines(self, ctx):
        await ctx.author.message.delete()
        await ctx.send("Who?")
    
def setup(client):
    client.add_cog(Replies(client))