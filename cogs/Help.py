import discord
import time
import json
import os
import asyncio
import asyncpg
import dbl
from discord.ext import commands

emoji = '\N{Heavy Check Mark}'

async def get_prefix(self, message):
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            try:
                search = await connection.fetchval("SELECT prefix FROM prefixes WHERE guildid = "+str(message.guild.id)+" ;")
            except:
                return '%'
            else:
                return search

async def get_delete(self, message):
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            try:
                search = await connection.fetchval("SELECT delete FROM deletion WHERE guildid = "+str(message.guild.id)+" ;")
            except:
                return 'False'
            else:
                return search

async def guildhostchannel(self, ctx):
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            channeltosend = await connection.fetchval("SELECT guildchannelid FROM guildhostchannel WHERE guildid = '"+str(ctx.guild.id)+"' ;")
            return channeltosend

def is_guild_owner():
    def predicate(ctx):
        return ctx.guild is not None and ctx.guild.owner_id == ctx.author.id
    return commands.check(predicate)

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Help online.')

    # Commands
    @commands.Cog.listener()#(name='help', help='Displays further explaination for commands')
    async def on_message(self, message):
    #async def help (self, ctx):
        if str(message.author) == self.client.user:
            return

        if message.author.bot:
            return

        if message.content.startswith("<>help"):
            prefix = await get_prefix(self, message)
            if message.channel.type is discord.ChannelType.private:
                responce = message.content
                content = responce.split()
                try:
                    content[1]
                except:
                    help = discord.Embed(title="Nexus-Z Commands", description="", color=0x2962FF) #name="", value="", inline=False
                    help.add_field(name="Use `<>help [command]` for more info on a command", value="\u200B", inline=False)
                    help.add_field(name="__**Pokemon SW/SH:**__", value="**catch\npokedex\nnatures\nball\nden\nsprite\nhost\nconfig**", inline=False)
                    help.add_field(name="__**Pokemon Go:**__", value="**godex\ngopvp\ngorocket\ngohundo\ngopure\ngotohome\ngosearchterms**", inline=False)
                    help.add_field(name="__**Other:**__", value="**fc\ninfo\nnexusz?\naddcommand\nfreepokemon\nping**", inline=False)
                    help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")

                    candelete = await get_delete(self, message)
                    if candelete == "True":
                        await message.delete()
                    await message.channel.send(embed = help)
                else:
                    if content[1].lower() == "catch":
                        help = discord.Embed(title="Catch Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"catch (form) [pokemon](*) (ball)`\n\n`()` is optional\n`[]` is needed\n`*` if you want a shiny image", inline=False)
                        help.add_field(name="Command Description:", value="Returns catch rates of the Pokemon", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"catch pikachu`\n`"+prefix+"catch piakchu*`\n`"+prefix+"catch alolan dugtrio`\n`"+prefix+"catch galarian meowth`\n`"+prefix+"catch gmax/gigantamax charizard`\n`"+prefix+"catch pikachu ultra/ultra ball`")
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "pokedex":
                        help = discord.Embed(title="Pokedex Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"pokedex (form) [pokemon](*)`\n\n`()` is optional\n`[]` is needed\n`*` if you want a shiny image", inline=False)
                        help.add_field(name="Command Description:", value="Returns Pokedex entry information about a Pokemon\nNotes: Pokemon with alternate forms can be found in their original entry (i.e: `"+prefix+ "pokedex kyogre` will also include its Primal.)", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"pokedex pikachu`\n`"+prefix+"pokedex pikachu*`\n`"+prefix+"pokedex alolan dugtrio`\n`"+prefix+"pokedex galarian meowth`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "natures":
                        help = discord.Embed(title="Natures Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"natures`", inline=False)
                        help.add_field(name="Command Description:", value="Returns a chart with all natures and their effects on Pokemon stats", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"natures`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "ball":
                        help = discord.Embed(title="Ball Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"ball [ball_type]`", inline=False)
                        help.add_field(name="Command Description:", value="Returns a Poke-ball's information", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"ball ultra`\n`"+prefix+"ball ultra ball`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "den":
                        help = discord.Embed(title="Den Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"den [den#/pokemon(*)]`\n\n`*` if you want a shiny image", inline=False)
                        help.add_field(name="Command Description:", value="Searches for den by number or Pokemon\n\nNote: Galarian forms are searched for by their regular form names", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"den 14`\n`"+prefix+"den meowth`\n`"+prefix+"den meowth*`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "sprite":
                        help = discord.Embed(title="Sprite Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"sprite [Pokemon](*)`\n\n`()` is optional\n`[]` is needed\n`*` if you want a shiny image", inline=False)
                        help.add_field(name="Command Description:", value="Returns a Home sprite of the named Pokemon", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"sprite zygarde`\n`"+prefix+"sprite ash greninja`\n`"+prefix+"sprite ash greninja*`\n`"+prefix+"sprite dawn wings necrozma`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "move":
                        help = discord.Embed(title="Move Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"move [move_name]`", inline=False)
                        help.add_field(name="Command Description:", value="Returns information about a Pokemon move (All moves available in Gen 8)", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"move protect`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "host":
                        help = discord.Embed(title="Host Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"host`", inline=False)
                        help.add_field(name="Command Description:", value="Allows to setup and embed/message host to be sent to a designated channel by the owner of the server. (if one is set)", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"host`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "config":
                        help = discord.Embed(title="Config Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"config`", inline=False)
                        help.add_field(name="Command Description:", value="Allows Owner to see the current settings of this bot.", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"config`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "godex":
                        help = discord.Embed(title="Godex Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"godex (form) [Pokemon](*)`\n\n`()` is optional\n`[]` is needed\n`*` if you want a shiny image", inline=False)
                        help.add_field(name="Command Description:", value="Returns Pokemon Go Pokedex information", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"godex charizard`\n`"+prefix+"godex charizard*`\n`"+prefix+"godex alolan dugtrio`\n`"+prefix+"godex galarian meowth`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "gopvp":
                        help = discord.Embed(title="Gopvp Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"gopvp (form) [Pokemon](*) [Level] [ATK_IV] [DEF_IV] [STA_IV]`\n\n`()` is optional\n`[]` is needed\n`*` if you want a shiny image", inline=False)
                        help.add_field(name="Command Description:", value="Returns PVP potential of your Pokemon compared to the best of each league", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"gopvp pikachu 30 14 6 12`\n`"+prefix+"gopvp piakchu* 30 14 16 12`\n`"+prefix+"gopvp alolan muk 50 15 15 14`\n`"+prefix+"gopvp galarian meowth 15 10 4 13`\n`"+prefix+"gopvp mega mewtwo y 50 15 15 15`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "gorocket":
                        help = discord.Embed(title="Gorocket Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"gorocket [type/leader]`\n\n`[]` is needed", inline=False)
                        help.add_field(name="Command Description:", value="Returns info on a Grunt /Leaders Pokemon setup", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"gorocket water`\n`"+prefix+"gorocket cliff`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "gohundo":
                        help = discord.Embed(title="Gohundo Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"gohundo [Pokemon](*)`\n\n`()` is optional\n`[]` is needed\n`*` if you want a shiny image", inline=False)
                        help.add_field(name="Command Description:", value="Returns 100% IV CP's of each level of a Pokemon in Go", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"gohundo venusaur`\n`"+prefix+"gohundo venusaur*`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "gopure":
                        help = discord.Embed(title="Gopure Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"gopure [Pokemon](*) [Atk_IV] [Def_IV] [Sta_IV]`\n\n`()` is optional\n`[]` is needed\n`*` if you want a shiny image", inline=False)
                        help.add_field(name="Command Description:", value="Returns comparison between shadow and purified forms of the Pokemon with the input information", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"gopure mudkip 13 6 3`\n`"+prefix+"gopure gardevoir* 15 14 12`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "gotohome":
                        help = discord.Embed(title="Gotohome Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"gotohome (form) [Pokemon](*) [Level] [ATK_IV] [DEF_IV] [STA_IV]`\n\n`()` is optional\n`[]` is needed\n`*` if you want a shiny image", inline=False)
                        help.add_field(name="Command Description:", value="Returns an estimation of a Pokemon's Stats whent transfered from Home to Sword and Sheild", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"gotohome pikachu 30 14 6 12`\n`"+prefix+"gotohome piakchu* 30 14 16 12`\n`"+prefix+"gotohome alolan muk 50 15 15 14`\n`"+prefix+"gotohome galarian meowth 15 10 4 13`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "gosearchterms":
                        help = discord.Embed(title="Gosearchterms Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"gosearchterms [Pokemon/Status/Type/Combination/Advanced]`", inline=False)
                        help.add_field(name="Command Description:", value="Returns useful info about search strings in Pokemon Go", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"gosearchterms pokemon`\n`"+prefix+"gosearchterms status`\n`"+prefix+"gosearchterms type`\n`"+prefix+"gosearchterms combination`\n`"+prefix+"gosearchterms advanced` ", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)

                    elif content[1].lower() == "fc":
                        try:
                            content[2]
                        except:
                            help = discord.Embed(title="FC (Friend Code) Help", description="", color=0x2962FF) #name="", value="", inline=False
                            help.add_field(name="Command Format:", value="`"+prefix+"fc (@user)`\n`() is optional`", inline=False)
                            help.add_field(name="Command Description:", value="Returns friend codes you have on the current server (@user will check if a the pinged user has friend codes)", inline=False)
                            help.add_field(name="Sub-commands:", value="set (aliases = add) `<>help fc set for more infomation`\ndelete `<>help fc delete for more infomation`", inline=False)
                            help.add_field(name="**Examples:**", value="`"+prefix+"fc`\n`"+prefix+"fc @Sollisnexus`", inline=False)
                            help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await message.channel.send(embed = help)
                        else:
                            if content[2] == "add" or content[2] == "set":
                                help = discord.Embed(title="FC Set/Add Help", description="", color=0x2962FF) #name="", value="", inline=False
                                help.add_field(name="Command Format:", value="`"+prefix+"fc add [system/game] [friendcode]`", inline=False)
                                help.add_field(name="Command Description:", value="Adds Friend code to a system/game to the first available slot in your friend code list", inline=False)
                                help.add_field(name="Systems and Games list", value="switch (8 slots!~)\npogo (4 slots!~)\nds (2 Slots!~)\nshuffle\nmaster\nhome\ncafemix", inline=False)
                                help.add_field(name="**Examples:**", value="`"+prefix+"fc set switch xxxx-xxxx-xxxx`\n`"+prefix+"fc add pogo xxxx-xxxx-xxxx`\n`"+prefix+"fc set ds xxxx-xxxx-xxxx`\n`"+prefix+"fc add shuffle xxxx-xxxx-xxxx`\n`"+prefix+"fc set master xxxx-xxxx-xxxx`\n`"+prefix+"fc add home xxxxxxxxxxxx`\n`"+prefix+"fc set cafemix xxxx-xxxx-xxxx`", inline=False)
                                help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                await message.channel.send(embed = help)
                            elif content[2] == "delete":
                                help = discord.Embed(title="FC Delete Help", description="", color=0x2962FF) #name="", value="", inline=False
                                help.add_field(name="Command Format:", value="`"+prefix+"fc delete [system][slot#]/[all]`\n\nslot# is only needed switch, pogo and ds", inline=False)
                                help.add_field(name="Command Description:", value="Deletes a/all friend code(s) from your fc list", inline=False)
                                help.add_field(name="**Examples:**", value="`"+prefix+"fc delete switch(1-8)`\n`"+prefix+"fc delete pogo(1-4)`\n`"+prefix+"fc delete ds(1-2)`\n`"+prefix+"fc delete shuffle`\n`"+prefix+"fc delete master`\n`"+prefix+"fc delete home`\n`"+prefix+"fc delete cafemix`\n`"+prefix+"fc delete all`", inline=False)
                                help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                await message.channel.send(embed = help)
                            else:
                                await message.channel.send("fc does not have a subcommand "+content[2]+"!")
                    elif content[1].lower() == "info":
                        help = discord.Embed(title="Info Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"info`", inline=False)
                        help.add_field(name="Command Description:", value="Statistics with link to voting and link to the support server", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"info`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "nexusz?":
                        help = discord.Embed(title="Nexusz? Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"nexusz?`", inline=False)
                        help.add_field(name="Command Description:", value="Is this the real Nexus-Z? (SFW)", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"nexusz?`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "invite":
                        help = discord.Embed(title="Invite Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"invite`", inline=False)
                        help.add_field(name="Command Description:", value="Provides invite link to invite to your server", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"invite`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "addcommand":
                        help = discord.Embed(title="Addcommand Help?", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"addcommand`", inline=False)
                        help.add_field(name="Command Description:", value="Adds a command? (SFW)", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"addcommand`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "freepokemon":
                        help = discord.Embed(title="Freepokemon Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"freepokemon`", inline=False)
                        help.add_field(name="Command Description:", value="Returns free pokemon? (SFW)", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"freepokemon`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "ping":
                        help = discord.Embed(title="Ping Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"ping`", inline=False)
                        help.add_field(name="Command Description:", value="Returns 'Pong!' and latecy check", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"ping`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    else:
                        await message.channel.send("No command named '"+str(content[1])+"' found")

                    candelete = await get_delete(self, message)
                    if candelete == "True":
                        await message.delete()
            else:
                responce = message.content
                content = responce.split()
                try:
                    content[1]
                except:
                    help = discord.Embed(title="Nexus-Z Commands", description="", color=0x2962FF) #name="", value="", inline=False
                    help.add_field(name="Use `<>help [command]` for more info on a command", value="\u200B", inline=False)
                    help.add_field(name="__**Pokemon SW/SH:**__", value="**catch\npokedex\nnatures\nball\nden\nsprite\nhost\nconfig**", inline=False)
                    help.add_field(name="__**Pokemon Go:**__", value="**godex\ngopvp\ngorocket\ngohundo\ngopure\ngotohome\ngosearchterms**", inline=False)
                    help.add_field(name="__**Other:**__", value="**fc\ninfo\nnexusz?\naddcommand\nfreepokemon\nping**", inline=False)
                    help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")

                    candelete = await get_delete(self, message)
                    if candelete == "True":
                        await message.delete()
                    await message.channel.send(embed = help)
                else:
                    if content[1].lower() == "catch":
                        help = discord.Embed(title="Catch Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"catch (form) [pokemon](*) (ball)`\n\n`()` is optional\n`[]` is needed\n`*` if you want a shiny image", inline=False)
                        help.add_field(name="Command Description:", value="Returns catch rates of the Pokemon", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"catch pikachu`\n`"+prefix+"catch piakchu*`\n`"+prefix+"catch alolan dugtrio`\n`"+prefix+"catch galarian meowth`\n`"+prefix+"catch gmax/gigantamax charizard`\n`"+prefix+"catch pikachu ultra/ultra ball`")
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "pokedex":
                        help = discord.Embed(title="Pokedex Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"pokedex (form) [pokemon](*)`\n\n`()` is optional\n`[]` is needed\n`*` if you want a shiny image", inline=False)
                        help.add_field(name="Command Description:", value="Returns Pokedex entry information about a Pokemon\nNotes: Pokemon with alternate forms can be found in their original entry (i.e: `"+prefix+ "pokedex kyogre` will also include its Primal.)", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"pokedex pikachu`\n`"+prefix+"pokedex pikachu*`\n`"+prefix+"pokedex alolan dugtrio`\n`"+prefix+"pokedex galarian meowth`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "natures":
                        help = discord.Embed(title="Natures Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"natures`", inline=False)
                        help.add_field(name="Command Description:", value="Returns a chart with all natures and their effects on Pokemon stats", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"natures`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "ball":
                        help = discord.Embed(title="Ball Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"ball [ball_type]`", inline=False)
                        help.add_field(name="Command Description:", value="Returns a Poke-ball's information", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"ball ultra`\n`"+prefix+"ball ultra ball`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "den":
                        help = discord.Embed(title="Den Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"den [den#/pokemon(*)]`\n\n`*` if you want a shiny image", inline=False)
                        help.add_field(name="Command Description:", value="Searches for den by number or Pokemon\n\nNote: Galarian forms are searched for by their regular form names", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"den 14`\n`"+prefix+"den meowth`\n`"+prefix+"den meowth*`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "sprite":
                        help = discord.Embed(title="Sprite Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"sprite [Pokemon](*)`\n\n`()` is optional\n`[]` is needed\n`*` if you want a shiny image", inline=False)
                        help.add_field(name="Command Description:", value="Returns a Home sprite of the named Pokemon", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"sprite zygarde`\n`"+prefix+"sprite ash greninja`\n`"+prefix+"sprite ash greninja*`\n`"+prefix+"sprite dawn wings necrozma`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "move":
                        help = discord.Embed(title="Move Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"move [move_name]`", inline=False)
                        help.add_field(name="Command Description:", value="Returns information about a Pokemon move (All moves available in Gen 8)", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"move protect`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "host":
                        help = discord.Embed(title="Host Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"host`", inline=False)
                        help.add_field(name="Command Description:", value="Allows to setup and embed/message host to be sent to a designated channel by the owner of the server. (if one is set)", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"host`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "config":
                        help = discord.Embed(title="Config Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"config`", inline=False)
                        help.add_field(name="Command Description:", value="Allows Owner to see the current settings of this bot.", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"config`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "godex":
                        help = discord.Embed(title="Godex Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"godex (form) [Pokemon](*)`\n\n`()` is optional\n`[]` is needed\n`*` if you want a shiny image", inline=False)
                        help.add_field(name="Command Description:", value="Returns Pokemon Go Pokedex information", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"godex charizard`\n`"+prefix+"godex charizard*`\n`"+prefix+"godex alolan dugtrio`\n`"+prefix+"godex galarian meowth`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "gopvp":
                        help = discord.Embed(title="Gopvp Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"gopvp (form) [Pokemon](*) [Level] [ATK_IV] [DEF_IV] [STA_IV]`\n\n`()` is optional\n`[]` is needed\n`*` if you want a shiny image", inline=False)
                        help.add_field(name="Command Description:", value="Returns PVP potential of your Pokemon compared to the best of each league", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"gopvp pikachu 30 14 6 12`\n`"+prefix+"gopvp piakchu* 30 14 16 12`\n`"+prefix+"gopvp alolan muk 50 15 15 14`\n`"+prefix+"gopvp galarian meowth 15 10 4 13`\n`"+prefix+"gopvp mega mewtwo y 50 15 15 15`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "gorocket":
                        help = discord.Embed(title="Gorocket Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"gorocket [type/leader]`\n\n`[]` is needed", inline=False)
                        help.add_field(name="Command Description:", value="Returns info on a Grunt /Leaders Pokemon setup", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"gorocket water`\n`"+prefix+"gorocket cliff`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "gohundo":
                        help = discord.Embed(title="Gohundo Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"gohundo [Pokemon](*)`\n\n`()` is optional\n`[]` is needed\n`*` if you want a shiny image", inline=False)
                        help.add_field(name="Command Description:", value="Returns 100% IV CP's of each level of a Pokemon in Go", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"gohundo venusaur`\n`"+prefix+"gohundo venusaur*`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "gopure":
                        help = discord.Embed(title="Gopure Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"gopure [Pokemon](*) [Atk_IV] [Def_IV] [Sta_IV]`\n\n`()` is optional\n`[]` is needed\n`*` if you want a shiny image", inline=False)
                        help.add_field(name="Command Description:", value="Returns comparison between shadow and purified forms of the Pokemon with the input information", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"gopure mudkip 13 6 3`\n`"+prefix+"gopure gardevoir* 15 14 12`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "gotohome":
                        help = discord.Embed(title="Gotohome Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"gotohome (form) [Pokemon](*) [Level] [ATK_IV] [DEF_IV] [STA_IV]`\n\n`()` is optional\n`[]` is needed\n`*` if you want a shiny image", inline=False)
                        help.add_field(name="Command Description:", value="Returns an estimation of a Pokemon's Stats whent transfered from Home to Sword and Sheild", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"gotohome pikachu 30 14 6 12`\n`"+prefix+"gotohome piakchu* 30 14 16 12`\n`"+prefix+"gotohome alolan muk 50 15 15 14`\n`"+prefix+"gotohome galarian meowth 15 10 4 13`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "gosearchterms":
                        help = discord.Embed(title="Gosearchterms Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"gosearchterms [Pokemon/Status/Type/Combination/Advanced]`", inline=False)
                        help.add_field(name="Command Description:", value="Returns useful info about search strings in Pokemon Go", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"gosearchterms pokemon`\n`"+prefix+"gosearchterms status`\n`"+prefix+"gosearchterms type`\n`"+prefix+"gosearchterms combination`\n`"+prefix+"gosearchterms advanced` ", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)

                    elif content[1].lower() == "fc":
                        try:
                            content[2]
                        except:
                            help = discord.Embed(title="FC (Friend Code) Help", description="", color=0x2962FF) #name="", value="", inline=False
                            help.add_field(name="Command Format:", value="`"+prefix+"fc (@user)`\n`() is optional`", inline=False)
                            help.add_field(name="Command Description:", value="Returns friend codes you have on the current server (@user will check if a the pinged user has friend codes)", inline=False)
                            help.add_field(name="Sub-commands:", value="set (aliases = add) `<>help fc set for more infomation`\ndelete `<>help fc delete for more infomation`", inline=False)
                            help.add_field(name="**Examples:**", value="`"+prefix+"fc`\n`"+prefix+"fc @Sollisnexus`", inline=False)
                            help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await message.channel.send(embed = help)
                        else:
                            if content[2] == "add" or content[2] == "set":
                                help = discord.Embed(title="FC Set/Add Help", description="", color=0x2962FF) #name="", value="", inline=False
                                help.add_field(name="Command Format:", value="`"+prefix+"fc add/set [system/game] [friendcode]`", inline=False)
                                help.add_field(name="Command Description:", value="Adds Friend code to a system/game to the first available slot in your friend code list", inline=False)
                                help.add_field(name="Systems and Games list", value="switch (8 slots!~)\npogo (4 slots!~)\nds (2 Slots!~)\nshuffle\nmaster\nhome\ncafemix", inline=False)
                                help.add_field(name="**Examples:**", value="`"+prefix+"fc set switch xxxx-xxxx-xxxx`\n`"+prefix+"fc add pogo xxxx-xxxx-xxxx`\n`"+prefix+"fc set ds xxxx-xxxx-xxxx`\n`"+prefix+"fc add shuffle xxxx-xxxx-xxxx`\n`"+prefix+"fc set master xxxx-xxxx-xxxx`\n`"+prefix+"fc add home xxxxxxxxxxxx`\n`"+prefix+"fc set cafemix xxxx-xxxx-xxxx`", inline=False)
                                help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                await message.channel.send(embed = help)
                            elif content[2] == "delete":
                                help = discord.Embed(title="FC Delete Help", description="", color=0x2962FF) #name="", value="", inline=False
                                help.add_field(name="Command Format:", value="`"+prefix+"fc delete [system][slot#]/[all]`\n\nslot# is only needed switch, pogo and ds", inline=False)
                                help.add_field(name="Command Description:", value="Deletes a/all friend code(s) from your fc list", inline=False)
                                help.add_field(name="**Examples:**", value="`"+prefix+"fc delete switch(1-8)`\n`"+prefix+"fc delete pogo(1-4)`\n`"+prefix+"fc delete ds(1-2)`\n`"+prefix+"fc delete shuffle`\n`"+prefix+"fc delete master`\n`"+prefix+"fc delete home`\n`"+prefix+"fc delete cafemix`\n`"+prefix+"fc delete all`", inline=False)
                                help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                await message.channel.send(embed = help)
                            else:
                                await message.channel.send("fc does not have a subcommand "+content[2]+"!")
                    elif content[1].lower() == "info":
                        help = discord.Embed(title="Info Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"info`", inline=False)
                        help.add_field(name="Command Description:", value="Statistics with link to voting and link to the support server", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"info`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "nexusz?":
                        help = discord.Embed(title="Nexusz? Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"nexusz?`", inline=False)
                        help.add_field(name="Command Description:", value="Is this the real Nexus-Z? (SFW)", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"nexusz?`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "addcommand":
                        help = discord.Embed(title="Addcommand Help?", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"addcommand`", inline=False)
                        help.add_field(name="Command Description:", value="Adds a command? (SFW)", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"addcommand`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "freepokemon":
                        help = discord.Embed(title="Freepokemon Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"freepokemon`", inline=False)
                        help.add_field(name="Command Description:", value="Returns free pokemon? (SFW)", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"freepokemon`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    elif content[1].lower() == "ping":
                        help = discord.Embed(title="Ping Help", description="", color=0x2962FF) #name="", value="", inline=False
                        help.add_field(name="Command Format:", value="`"+prefix+"ping`", inline=False)
                        help.add_field(name="Command Description:", value="Returns 'Pong!' and latecy check", inline=False)
                        help.add_field(name="**Examples:**", value="`"+prefix+"ping`", inline=False)
                        help.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await message.channel.send(embed = help)
                    else:
                        await message.channel.send("No command named '"+str(content[1])+"' found")

                    candelete = await get_delete(self, message)
                    if candelete == "True":
                        await message.delete()


    @commands.command()
    async def info(self, ctx):
        activeservers = self.client.guilds
        Info = discord.Embed(title="Nexus-Z Support Server Invite", url="https://discord.gg/At2zCHv", color=0x2962FF )
        Info.set_author(name="Sollisnexus#1429", url="https://sollisnexus.github.io/NexusZ/",icon_url="https://cdn.discordapp.com/avatars/177200577430683648/a_0f28b72333cf75baea7eca74c09089ae.gif")
        Info.add_field(name="Serving:", value="**"+str(len(self.client.guilds))+"** Servers", inline=True)
        Info.add_field(name="Server invite:", value="[Link](https://discord.com/oauth2/authorize?client_id=674716932720558101&permissions=26624&scope=bot) to invite\nNexus-Z to your\nown server!~", inline=True)
        Info.add_field(name="Top.GG Upvote:", value="[Vote Here!](https://top.gg/bot/674716932720558101/vote)\nand get a 🍪", inline=True)
        Info.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
        candelete = await get_delete(self, ctx.message)
        if candelete == "True":
            await message.delete()
        await ctx.channel.send(embed=Info)

    @commands.command()
    async def help(self, ctx):
        await ctx.channel.send("This command doesn't work for help, please use <>help for commands")

    @commands.command()
    @commands.check_any(commands.is_owner(), is_guild_owner())
    async def config(self, ctx):
        getprefix = await get_prefix(self, ctx)
        getdelete = await get_delete(self, ctx)
        gethostchannel = await guildhostchannel(self, ctx)


        embed = discord.Embed(title="Configuration for this server", description="", color=0x2962FF)
        embed.add_field(name="Prefix:", value=str(getprefix), inline=False)
        embed.add_field(name="Message Deletion:", value=str(getdelete), inline=False)
        embed.add_field(name="Hosting Channel (for Sw/Sh Dens):", value=str(gethostchannel), inline=False)
        embed.add_field(name="How to change settings:", value="Change prefix use `"+str(getprefix)+"changeprefix [prefix]`\nChange message deletion use `"+str(getprefix)+"changedelete (True/Yes/Y) or (False/No/N)`\nChange hosting channel use `"+str(getprefix)+"changehost [#channel]`", inline=False)
        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
        candelete = await get_delete(self, ctx)
        if candelete == "True":
            await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        Invite = discord.Embed(title="Nexus-Z Invite", url="https://discord.com/oauth2/authorize?client_id=674716932720558101&permissions=26624&scope=bot", color=0x2962FF)
        Invite.add_field(name="Server invite:", value="[Link](https://discord.com/oauth2/authorize?client_id=674716932720558101&permissions=26624&scope=bot) to invite\nNexus-Z to your\nown server!~", inline=True)
        candelete = await get_delete(self, ctx.message)
        if candelete == "True":
            await message.delete()
        await ctx.channel.send(embed=Invite)

    @commands.command()
    @commands.check_any(commands.is_owner(), is_guild_owner())
    async def leave(self, ctx):
        to_leave = self.client.get_guild(ctx.guild.id)
        await ctx.send("I must go, my people need me! _-flys away-_")
        await to_leave.leave()

    @leave.error
    async def leave_error(self, ctx, error):
        if isinstance(error, commands.CheckAnyFailure):
            candelete = await get_delete(self, message)
            if candelete == "True":
                await message.delete()
            await ctx.send("Only the owner of the server can remove this bot", delete_after=5)

    @commands.command()
    async def ping(self, ctx):
        """ Pong! (with Latency) """
        candelete = await get_delete(self, message)
        if candelete == "True":
            await message.delete()
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Pong!  `{int(ping)}ms`")
        await message.add_reaction(emoji)
        print(f'Ping {int(ping)}ms')

def setup(client):
    client.add_cog(Help(client))
