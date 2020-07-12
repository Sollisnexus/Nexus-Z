import discord
import time
from discord.ext import commands

emoji = '\N{Heavy Check Mark}'

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Help cog is online.')
    
    # Commands
    @commands.command(name='help', help='Displays further explaination for commands')
    async def help (self, ctx):
        embed = discord.Embed(title="Nexus-Z Commands", description="", color=0x2962FF)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/726589477295882283/727756911180644362/gmaxtrait.png")
        embed.add_field(name="Command:", value="`%catch <Pokemon> (pokeball)`\n`%catch (form) <Pokemon> (pokeball)`\n`%pokedex <Pokemon>`\n`%pokedex (form) <Pokemon>`\n`%natures`\n`%ball <name>`\n `%den <den#>/<Pokemon>`\n\n\n`%nexusz?`\n`%addcommand`" , inline=True)
        embed.add_field(name="Description:", value="`Returns catch rates`\n`Forms inc: Alolan, Galarian, Gmax`\n`Returns Pokemon entry`\n`Forms include: Alolan, Galarian `\n`Shows a chart of Pokemon Natures`\n`Displays Poke-ball info`\n`Searches for den by Number/Pokemon`\n\n\n`Is that the real Nexus-Z?`\n`I wouldn't type this if I were you...`" , inline=True)
        embed.add_field(name= "Notes:", value='Pokemon with alternate forms can be found in their original\nentry (i.e: `%pokedex kyogre` will also include its Primal.)\n\nWhen searching for pokeball capture, spell out the entire name \nof the pokeball (i.e `heavyball`)\n\n () is optional / <> is mandatory', inline = False)
        await ctx.message.delete()
        await ctx.send(embed=embed)
        
    @commands.command(name='modulehelp', help='Displays modules and module commands' )
    @commands.has_role('Owner')
    async def modulehelp (self, ctx):
        embed = discord.Embed(title="Module Commands", description="", color=0x2962FF)
        embed.set_thumbnail(url='https://res.cloudinary.com/indepth-dev/image/fetch/w_1000,f_auto/https://admin.indepth.dev/content/images/2020/02/xmodules-375x300.png.pagespeed.ic.Vw-2crK2PI.png')
        embed.add_field(name="Module Commands:", value="%help\n%load <module name>\n%unload <module name>\n%reload <module name>", inline=True)
        embed.add_field(name="Descriptions:", value="shows loaded modules and commands.\nLoads the selected module.\nUnload the selected module.\nReloads the selected Module.", inline=True)
        embed.add_field(name="Available Modules:", value="Pokemon\nPing\nHelp\nReplies", inline=False)
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        """ Pong! (with Latency) """
        await ctx.message.delete()
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Pong!  `{int(ping)}ms`")
        await message.add_reaction(emoji)
        print(f'Ping {int(ping)}ms')
        
def setup(client):
    client.add_cog(Help(client))