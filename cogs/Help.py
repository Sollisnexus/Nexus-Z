import discord
import time
import json
import os
import asyncio
import dbl
from discord.ext import commands

emoji = '\N{Heavy Check Mark}'

def get_prefix(client, message):
    with open('C:/Users/Administrator/Documents/prefixes.json', 'r') as f:
        prefixes = json.load(f)
        if message.guild == None:
            return "%"
        else:
            return prefixes[str(message.guild.id)]

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
            if message.channel.type is discord.ChannelType.private:
                embed = discord.Embed(title="Nexus-Z Commands", description="", color=0x2962FF)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/726589477295882283/727756911180644362/gmaxtrait.png")
                embed.add_field(name="Command:", value="`"+str(get_prefix(self, message))+"catch <Pokemon> (pokeball)`\n`"+str(get_prefix(self, message))+"catch (form) <Pokemon> (pokeball)`\n`"+str(get_prefix(self, message))+"pokedex <Pokemon>`\n`"+str(get_prefix(self, message))+"pokedex (form) <Pokemon>`\n`"+str(get_prefix(self, message))+"natures`\n`"+str(get_prefix(self, message))+"ball <name>`\n`"+str(get_prefix(self, message))+"den <den#>/<Pokemon>`\n\n\n**BETA! Pokemon Go Commands:**\n`"+str(get_prefix(self, message))+"godex (form) <pokemon>`\n`"+str(get_prefix(self, message))+"gopvp <Pokemon> <Level> <Atk IV> <Def IV> <HP IV>`\n`"+str(get_prefix(self, message))+"gorocket <type or leader>`\n`"+str(get_prefix(self, message))+"gohundo <Pokemon>`\n`"+str(get_prefix(self, message))+"gopure <Pokemon> <Atk IV> <Def IV> <HP IV>`\n\n**Other Commands:**\n`"+str(get_prefix(self, message))+"nexusz?`\n`"+str(get_prefix(self, message))+"addcommand`\n`"+str(get_prefix(self, message))+"freepokemon`\n`"+str(get_prefix(self, message))+"ping`\n`"+str(get_prefix(self, message))+"info`\n\n**Server Owner Only:**\n`"+str(get_prefix(self, message))+"changeprefix <prefix>`" , inline=True)
                embed.add_field(name="Description:", value="`Returns catch rates`\n`Forms inc: Alolan, Galarian, Gmax`\n`Returns Pokemon entry`\n`Forms include: Alolan, Galarian `\n`Shows a chart of Pokemon Natures`\n`Displays Poke-ball info`\n`Searches for den by Number/Pokemon`\n\n\n\n`Pokemon Go Data for Pokemon`\n`Compares your Pokemon to the Best of all the Leagues`\n`Go Rocket's Past & Current Pokemon.`\n`CP's of a Pokemon with 100% IV's`\n`Before and After example of purifying a shadow Pokemon`\n\n\n`Is that the real Nexus-Z?`\n`I wouldn't do this if I were you`\n`Free pokemon?`\n`Pong with latency check`\n`Statistics with link to voting`\n\n\n`Changes prefix for bot on this server`" , inline=True)
                embed.add_field(name= "Notes:", value="Pokemon with alternate forms can be found in their original\nentry (i.e: `"+str(get_prefix(self, message))+ "pokedex kyogre` will also include its Primal.)\n\nWhen searching for pokeball capture, spell out the entire name \nof the pokeball (i.e `heavyball`)\n\n ``() is optional` / ``<> is mandatory`", inline = False)
                await message.channel.send(embed=embed)
            else:
                page1 = discord.Embed(title="Nexus-Z Commands Page 1/3", description="", color=0x2962FF)
                page1.set_thumbnail(url="https://cdn.discordapp.com/attachments/726589477295882283/727756911180644362/gmaxtrait.png")
                page1.add_field(name="Sw/Sh Commands:", value="`"+str(get_prefix(self, message))+"catch <Pokemon> (pokeball)`\n`"+str(get_prefix(self, message))+"catch (form) <Pokemon> (pokeball)`\n`"+str(get_prefix(self, message))+"pokedex <Pokemon>`\n`"+str(get_prefix(self, message))+"pokedex (form) <Pokemon>`\n`"+str(get_prefix(self, message))+"natures`\n`"+str(get_prefix(self, message))+"ball <name>`\n`"+str(get_prefix(self, message))+"den <den#>/<Pokemon>`" , inline=True)
                page1.add_field(name="Description:", value="`Returns catch rates`\n`Forms inc: Alolan, Galarian, Gmax`\n`Returns Pokemon entry`\n`Forms include: Alolan, Galarian `\n`Shows a chart of Pokemon Natures`\n`Displays Poke-ball info`\n`Searches for den by Number/Pokemon`" , inline=True)
                page1.add_field(name= "Notes:", value="Pokemon with alternate forms can be found in their original\nentry (i.e: `"+str(get_prefix(self, message))+ "pokedex kyogre` will also include its Primal.)\n\nWhen searching for pokeball capture, spell out the entire name \nof the pokeball (i.e `heavyball`)\n\n () is optional / <> is mandatory", inline = False)
                page1.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")

                page2 = discord.Embed(title="Nexus-Z Commands Page 2/3", description="", color=0x2962FF)
                page2.set_thumbnail(url="https://cdn.discordapp.com/attachments/726589477295882283/727756911180644362/gmaxtrait.png")
                page2.add_field(name="|Beta!| Pokemon Go Commands:", value="`"+str(get_prefix(self, message))+"godex (form) <pokemon>`\n`"+str(get_prefix(self, message))+"gopvp <Pokemon> <Level> <Atk IV> <Def IV> <HP IV>`\n`"+str(get_prefix(self, message))+"gorocket <type or leader>`\n`"+str(get_prefix(self, message))+"gohundo <Pokemon>`\n`"+str(get_prefix(self, message))+"gopure <Pokemon> <Atk IV> <Def IV> <HP IV>`" , inline=True)
                page2.add_field(name="Description:", value="`Pokemon Go Data for Pokemon`\n`Compares your Pokemon to the Best of all the Leagues`\n`Go Rocket's Past & Current Pokemon`\n`CP's of a Pokemon with 100% IV's`\n`Before and After example of purifying a shadow Pokemon`" , inline=True)
                page2.add_field(name= "Notes:", value='() is optional / <> is mandatory', inline = False)
                page2.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")

                page3 = discord.Embed(title="Nexus-Z Commands Page 3/3", description="", color=0x2962FF)
                page3.set_thumbnail(url="https://cdn.discordapp.com/attachments/726589477295882283/727756911180644362/gmaxtrait.png")
                page3.add_field(name="Other Commands:", value="`"+str(get_prefix(self, message))+"nexusz?`\n`"+str(get_prefix(self, message))+"addcommand`\n`"+str(get_prefix(self, message))+"freepokemon`\n`"+str(get_prefix(self, message))+"ping`\n`"+str(get_prefix(self, message))+"info`\n\n**Server Owner Only:**\n`"+str(get_prefix(self, message))+"changeprefix <prefix>`" , inline=True)
                page3.add_field(name="Description:", value="`Is that the real Nexus-Z?`\n`I wouldn't do this if I were you`\n`Free pokemon?`\n`Pong with latency check`\n`Statistics with link to voting`\n\n\n`Changes prefix for bot on this server`" , inline=True)
                page3.add_field(name= "Notes:", value='``() is optional` / ``<> is mandatory`', inline = False)
                page3.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")

                contents = [ page1 , page2, page3]
                pages = 3
                cur_page = 1
                bool = 0
                await message.delete()
                message = await message.channel.send(embed = contents[cur_page-1])
                # getting the message object for editing and reacting

                await message.add_reaction("⏪")
                await message.add_reaction("◀️")
                await message.add_reaction("❌")
                await message.add_reaction("▶️")
                await message.add_reaction("⏩")

                def check(reaction, user):
                    return user == user and user != self.client.user and str(reaction.emoji) in ["⏪", "◀️","❌", "▶️","⏩"]
                    # This makes sure nobody except the command sender can interact with the "menu"

                while bool == 0:
                    try:
                        reaction, user = await self.client.wait_for("reaction_add", timeout=60, check=check)
                        # waiting for a reaction to be added - times out after x seconds, 60 in this
                        # example
                        if str(reaction.emoji) == "▶️" and cur_page != pages:
                            cur_page += 1
                            await message.edit(embed = contents[cur_page-1])
                            await message.remove_reaction(reaction, user)

                        elif str(reaction.emoji) == "◀️" and cur_page > 1:
                            cur_page -= 1
                            await message.edit(embed = contents[cur_page-1])
                            await message.remove_reaction(reaction, user)

                        elif str(reaction.emoji) == "⏩" and cur_page < 3:
                            cur_page = pages
                            await message.edit(embed = contents[cur_page - 1])
                            await message.remove_reaction(reaction, user)

                        elif str(reaction.emoji) == "⏪" and cur_page > 1:
                            cur_page = 1
                            await message.edit(embed = contents[cur_page - 1])
                            await message.remove_reaction(reaction, user)

                        elif str(reaction.emoji) == "❌":
                            await message.delete()
                            break
                        else:
                            await message.remove_reaction(reaction, user)
                            # removes reactions if the user tries to go forward on the last page or
                            # backwards on the first page
                    except asyncio.TimeoutError:
                        await message.delete()
                        break

                    # # ending the loop if user doesn't react after x seconds

                #embed = discord.Embed(title="Nexus-Z Commands", description="", color=0x2962FF)
                #embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/726589477295882283/727756911180644362/gmaxtrait.png")
                #embed.add_field(name="Command:", value=str(get_prefix(self, message))+"`catch <Pokemon> (pokeball)`\n"+str(get_prefix(self, message))+"`catch (form) <Pokemon> (pokeball)`\n"+str(get_prefix(self, message))+"`pokedex <Pokemon>`\n"+str(get_prefix(self, message))+"`pokedex (form) <Pokemon>`\n"+str(get_prefix(self, message))+"`natures`\n"+str(get_prefix(self, message))+"`ball <name>`\n"+str(get_prefix(self, message))+"`den <den#>/<Pokemon>`\n\n\n**BETA! Pokemon Go Commands:**\n"+str(get_prefix(self, message))+"`godex (form) <pokemon>`\n"+str(get_prefix(self, message))+"`gopvp <Pokemon> <Level> <Atk IV> <Def IV> <HP IV>`\n"+str(get_prefix(self, message))+"`gorocket <type or leader>`\n"+str(get_prefix(self, message))+"`gohundo <Pokemon>`\n"+str(get_prefix(self, message))+"`gopure <Pokemon> <Atk IV> <Def IV> <HP IV>`\n\n**Other Commands:**\n"+str(get_prefix(self, message))+"`nexusz?`\n"+str(get_prefix(self, message))+"`addcommand`\n\n**Server Owner Only:**\n"+str(get_prefix(self, message))+"`changeprefix <prefix>`" , inline=True)
                #embed.add_field(name="Description:", value="`Returns catch rates`\n`Forms inc: Alolan, Galarian, Gmax`\n`Returns Pokemon entry`\n`Forms include: Alolan, Galarian `\n`Shows a chart of Pokemon Natures`\n`Displays Poke-ball info`\n`Searches for den by Number/Pokemon`\n\n\n\n`Pokemon Go Data for Pokemon`\n`Compares your Pokemon to the Best of all the Leagues`\n`Go Rocket's Past & Current Pokemon.`\n`CP's of a Pokemon with 100% IV's`\n`Before and After example of purifying a shadow Pokemon`\n\n\n`Is that the real Nexus-Z?`\n`I wouldn't do this if I were you`\n\n\n`Changes prefix for bot on this server`" , inline=True)
                #embed.add_field(name= "Notes:", value='Pokemon with alternate forms can be found in their original\nentry (i.e: '+str(get_prefix(self, message))+'`pokedex kyogre` will also include its Primal.)\n\nWhen searching for pokeball capture, spell out the entire name \nof the pokeball (i.e `heavyball`)\n\n () is optional / <> is mandatory', inline = False)
                #await message.delete()
                #await message.channel.send(embed=embed)

    @commands.command()
    async def info(self, ctx):
        activeservers = self.client.guilds
        sum = 0
        for x in range (len(self.client.guilds)):
            sum += len(set(activeservers[x].members))
            print(activeservers[x])
        Info = discord.Embed(title="Nexus-Z Support Server Invite", url="https://discord.com/oauth2/authorize?client_id=674716932720558101&permissions=10240&scope=bot", color=0x2962FF )
        Info.set_author(name="Sollisnexus#1429", url="https://sollisnexus.github.io/NexusZ/",icon_url="https://cdn.discordapp.com/avatars/177200577430683648/a_0f28b72333cf75baea7eca74c09089ae.gif")
        Info.add_field(name="Serving:", value="**"+str(len(self.client.guilds))+ "** Guilds\n**"+ str(sum) + "** Members", inline=True)
        Info.add_field(name="Vote:", value="[Vote Here!](https://top.gg/bot/674716932720558101/vote)", inline=True)
        Info.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
        await ctx.message.delete()
        await ctx.channel.send(embed=Info)

    @commands.command()
    @commands.check_any(commands.is_owner(), is_guild_owner())
    async def leave(self, ctx):
        to_leave = self.client.get_guild(ctx.guild.id)
        await ctx.send("I must go, my people need me! _-flys away-_")
        await to_leave.leave()

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
