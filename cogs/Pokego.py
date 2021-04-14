import discord
import string
import math
import csv
import os
import itertools
import time
import json
import asyncio
import asyncpg
from discord.ext import commands

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

class Pokego(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Pokego online.')

    # Commands
    @commands.group(case_insensitive=True)
    async def godex(self, ctx):
        if ctx.invoked_subcommand is None:
            responce = str(ctx.message.content)
            content = responce.split()
            isshiny = "Normal"
            Name = string.capwords(content[1])
            if Name.endswith("*"):
                isshiny = "Shiny"
                Name = Name.replace("*", "")
            if Name == "Mr" or Name == "Mr.":
                if content[2].lower() == "mime" or content[2].lower() == "rime" or content[2].lower() == "mime*" or content[2].lower() == "rime*":
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].lower() == "mime":
                        Name = "Mrmime"
                        result = await dex(self, str(Name))
                        embed = discord.Embed(title= result[0] + "    Mr. Mime   " + result[2] , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                        embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\n", inline=True)
                        embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                        embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                        embed.add_field(name="Fast Moves",value=""+result[14], inline=True)
                        embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
                        embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                        await ctx.send(embed=embed)
                    elif content[2].lower() == "rime":
                        Name = "Mrrime"
                        result = await dex(self, str(Name))
                        embed = discord.Embed(title= result[0] + "    Mr. Rime   " + result[2] , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                        embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\n", inline=True)
                        embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                        embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                        embed.add_field(name="Fast Moves",value=""+result[14], inline=True)
                        embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
                        embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                        await ctx.send(embed=embed)
                    
                else:
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send('This Pokémon does not exist!')
            elif Name == "Mime":
                if content[2].endswith("*"):
                        isshiny = "Shiny"
                        Name = Name.replace("*", "")
                Name = "Mimejr"
                result = await dex(self, str(Name))
                embed = discord.Embed(title= result[0] + "    Mime Jr.   " + result[2] , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
                embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                embed.add_field(name="Fast Moves",value=""+result[14], inline=True)
                embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
                embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name.startswith("Nidoran\U00002640"):
                Name = "Nidoranf"
                result = await dex(self, str(Name))
                embed = discord.Embed(title= result[0] + "   Nidoran♀️   " + result[2] , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
                embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                embed.add_field(name="Fast Moves",value=""+result[14], inline=True)
                embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
                embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name.startswith("Nidoran\U00002642"):
                Name = "Nidoranm"
                result = await dex(self, str(Name))
                embed = discord.Embed(title= result[0] + "   Nidoran♂️   " + result[2] , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
                embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                embed.add_field(name="Fast Moves",value=""+result[14], inline=True)
                embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
                embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Armored":
                tname = content[2].capitalize()
                if content[2].endswith("*"):
                    isshiny = "Shiny"
                    tname = tname.replace("*", "")
                if tname == "Mewtwo":
                    TrName = "Armoredmewtwo"
                    result = await dex(self, str(TrName))
                    embed = discord.Embed(title= result[0] + "   Armored Mewtwo   " + result[2] , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://gamepress.gg/pokemongo/sites/pokemongo/files/2019-07/armored-mewtwo.png")
                    embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
                    embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                    embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                    embed.add_field(name="Fast Moves",value=""+result[14], inline=True)
                    embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
                    embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                else:
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send("Only Armored Mewtwo exists...     Ţ̸̧̖̘̒͐͌e̷̳͕͋a̸̗̫̓ḿ̷̡͙̱̊̚ ̵̘̖̼̪̦̟̏̂̀̓͌͘͝R̴̨̨͈̰̼̳̜̓̈̓o̷͙͠c̶͔̼̀̍̄̃̔͝ķ̸̦̜͚͂̅̀e̶̡̢̡̘̜̒̕t̷͎̼̙̀͌̊̂̕̚")
            elif Name == "Origin":
                tname = content[2].capitalize()
                if content[2].endswith("*"):
                        isshiny = "Shiny"
                        tname = tname.replace("*", "")
                if tname == "Giratina":
                    TrName = "Origingiratina"
                    result = await dex(self, str(TrName))
                    embed = discord.Embed(title= result[0] + "   Origin Giratina   " + result[2] , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Ogiratina.png")
                    embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
                    embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                    embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                    embed.add_field(name="Fast Moves",value=""+result[14], inline=True)
                    embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
                    embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                else:
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send("Only Origin Giratina exists...")
            elif Name == "Wormadam":
                StName = "Wormadams"
                TrName = "Wormadamt"
                result = await dex(self, str(Name))
                embed = discord.Embed(title= result[0] + "   " + Name + "   " + result[2] , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
                embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                embed.add_field(name="Fast Moves",value=""+result[14], inline=True)
                embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
                embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
                result = dex(str(StName))
                embed = discord.Embed(title= result[0] + "   " + Name + "   " + result[2] , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+StName+".png")
                embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
                embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                embed.add_field(name="Fast Moves",value=""+result[14], inline=True)
                embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
                embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.send(embed=embed)
                result = await dex(self, str(TrName))
                embed = discord.Embed(title= result[0] + "   " + Name + "   " + result[2] , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+TrName+".png")
                embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
                embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                embed.add_field(name="Fast Moves",value=""+result[14], inline=True)
                embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
                embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.send(embed=embed)
            elif Name == "Deoxys":
                AName = "Adeoxys"
                DName = "Ddeoxys"
                SName = "Sdeoxys"
                result = await dex(self, str(Name))
                embed = discord.Embed(title= result[0] + "   " + Name + " Normal Forme   " + result[2] , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
                embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                embed.add_field(name="Fast Moves",value=""+result[14], inline=True)
                embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
                embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
                result = dex(str(AName))
                embed = discord.Embed(title= result[0] + "   " + Name + " Attack Form   " + result[2] , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+AName+".png")
                embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
                embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                embed.add_field(name="Fast Moves",value=""+result[14], inline=True)
                embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
                embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.send(embed=embed)
                result = dex(str(DName))
                embed = discord.Embed(title= result[0] + "   " + Name + " Defense Form   " + result[2] , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+DName+".png")
                embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
                embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                embed.add_field(name="Fast Moves",value=""+result[14], inline=True)
                embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
                embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.send(embed=embed)
                result = dex(str(SName))
                embed = discord.Embed(title= result[0] + "   " + Name + " Speed Form   " + result[2] , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+SName+".png")
                embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
                embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                embed.add_field(name="Fast Moves",value=""+result[14], inline=True)
                embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
                embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.send(embed=embed)
            elif Name == "Giratina":
                OName = "Ogiratina"
                result = await dex(self, str(Name))
                embed = discord.Embed(title= result[0] + "   " + Name + " Altered Forme   " + result[2] , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
                embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                embed.add_field(name="Fast Moves",value=""+result[14], inline=True)
                embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
                embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.send(embed=embed)
                result = await dex(str(OName))
                embed = discord.Embed(title= result[0] + "   " + Name + " Origin Forme   " + result[2] , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+OName+".png")
                embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
                embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                embed.add_field(name="Fast Moves",value=""+result[14], inline=True)
                embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
                embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Therian":
                if content[2].capitalize() == "Thundurus":
                    Tname = "Tthundurus"
                    result = await dex(self, str(Tname))
                    embed = discord.Embed(title= result[0] + "   Therian " + content[2].capitalize() + "  " + result[2] , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Tname+".png")
                    embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
                    embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                    embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                    embed.add_field(name="Fast Moves",value=""+result[14], inline=True)
                    embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
                    embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                elif content[2].capitalize() == "Tornadus":
                    Tname = "Ttornadus"
                    result = await dex(self, str(Tname))
                    embed = discord.Embed(title= result[0] + "   Therian " + content[2].capitalize() + "  " + result[2] , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Tname+".png")
                    embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
                    embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                    embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                    embed.add_field(name="Fast Moves",value=""+result[14], inline=True)
                    embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
                    embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                elif content[2].capitalize() == "Landorus":
                    Tname = "Tlandorus"
                    result = await dex(self, str(Tname))
                    embed = discord.Embed(title= result[0] + "   Therian " + content[2].capitalize() + "  " + result[2] , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Tname+".png")
                    embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
                    embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                    embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                    embed.add_field(name="Fast Moves",value=""+result[14], inline=True)
                    embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
                    embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
            else:
                if Name == "Farfetch’d":
                    Name = "Farfetch'd"
                if Name == "Sirfetch’d":
                    Name = "Sirfetch'd"
                result = await dex(self, str(Name))
                if Name == "Porygon-z":
                    Name = "Porygon-Z"
                if result == None:
                    await ctx.send('This Pokémon does not exist!')
                elif result != None:
                    embed = discord.Embed(title= result[0] + "   " + Name + "   " + result[2] , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
                    embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                    embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                    embed.add_field(name="Fast Moves",value=result[14], inline=True)
                    embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
                    embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)

    @godex.command(aliases=["alola"])
    async def alolan(self, ctx):
        responce = str(ctx.message.content)
        content = responce.split()
        isshiny = "Normal"
        GaName = string.capwords(content[2])
        if content[2].endswith("*"):
            isshiny = "Shiny"
            GaName = GaName.replace("*", "")

        Listofalola = ["Rattata","Raticate","Raichu","Sandshrew","Sandslash","Vulpix","Ninetails","Diglett","Dugtrio","Meowth","Persian","Geodude","Graveler",
                       "Golem","Grimer","Muk","Exeggutor","Marowak"]
        if GaName in Listofalola:
            AName = GaName
            result = await aloladex(self, str(AName))
            embed = discord.Embed(title= result[0] + "   Alolan " + AName + "   " + result[2] , description="", color=0x2962FF)
            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Alolan/"+str(isshiny)+"/"+AName+".png")
            embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
            embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
            embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
            embed.add_field(name="Fast Moves",value=""+result[14], inline=True)
            embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
            embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send(embed=embed)
        else:
            await ctx.send('This Alolan Pokémon does not exist!')

    @godex.command(aliases=["galar"])
    async def galarian(self, ctx):
        responce = str(ctx.message.content)
        content = responce.split()
        isshiny = "Normal"
        GlName = string.capwords(content[2])
        if GlName.endswith("*"):
            isshiny = "Shiny"
            GlName = GlName.replace("*", "")

        Listofgalar = ["Meowth","Ponyta","Rapidash","Farfetch'd","Farfetch’d","Mr","Mr.","Weezing","Zigzagoon","Yamask","Linoone","Darumaka","Darmanitan","Stunfisk"]
        if GlName in Listofgalar:
            if GlName == "Farfetch’d":
                GlName = "Farfetch'd"
            if GlName == "Mr" or GlName == "Mr.":
                if content[3].lower() == "mime" or content[3].lower() == "mime*":
                    if content[3].endswith("*"):
                        isshiny = "Shiny"
                        content[3] = content[3].replace("*", "")
                    Name = "Mrmime"
                    result = await galardex(self, str(Name))
                    embed = discord.Embed(title= result[0] + "   Galarian Mr. Mime   " + result[2] , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
                    embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                    embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                    embed.add_field(name="Fast Moves",value=result[14], inline=True)
                    embed.add_field(name="Charged Moves",value=result[15], inline=True)
                    embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                else:
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send('This Pokémon does not exist!')
            if GlName == "Farfetch'd":
                result = await galardex(self, str("Farfetch''d"))
                embed = discord.Embed(title= result[0] + "   Galarian " + GlName + "   " + result[2] , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/Farfetchd.png")
                embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
                embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                embed.add_field(name="Fast Moves",value=""+result[14], inline=True)
                embed.add_field(name="Charged Moves",value=""+result[15], inline=True)
                embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            else:
                result = await galardex(self, str(GlName))
                embed = discord.Embed(title= result[0] + "   Galarian " + GlName + "   " + result[2] , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+GlName+".png")
                embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\nBuddy Dist: **"+result[18]+"**", inline=True)
                embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 50, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                embed.add_field(name="Fast Moves",value=result[14], inline=True)
                embed.add_field(name="Charged Moves",value=result[15], inline=True)
                embed.add_field(name="Vulnurable to:", value=result[17]+"\n**Resistant to:**\n"+result[16], inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
        else:
            await ctx.send('This Galarian Pokémon does not exist!')

    @commands.command()
    async def gorocket(self, ctx):
        responce = str(ctx.message.content)
        content = responce.split()
        name = content[1].capitalize()
        grunts = ["Fairy","Steel"]
        leaders = ["Arlo","Cliff","Sierra","Giovanni","Jessie","James"]
        if name not in grunts:
            Rocketdata = await Rocketlookup(self, name)
            if name not in leaders:
                name = name + " Grunt"
            embed = discord.Embed(title= name+"'s Current and Past Shadow Pokemon" , description="", color=0x2962FF)
            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Rocket/Grunt.png")
            if name in leaders:
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Rocket/"+name+".png")
            embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
            embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
            embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
            embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
            embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
            await ctx.send(embed=embed)
        elif name in grunts:
            await ctx.send("Team Rocket does not have a "+ name +" type line-up that exists... Ţ̸̧̖̘̒͐͌e̷̳͕͋a̸̗̫̓ḿ̷̡͙̱̊̚ ̵̘̖̼̪̦̟̏̂̀̓͌͘͝R̴̨̨͈̰̼̳̜̓̈̓o̷͙͠c̶͔̼̀̍̄̃̔͝ķ̸̦̜͚͂̅̀e̶̡̢̡̘̜̒̕t̷͎̼̙̀͌̊̂̕̚")

        candelete = await get_delete(self, ctx)
        if candelete == "True":
            await ctx.message.delete()

    @commands.command()
    async def gohundo(self, ctx):
        responce = str(ctx.message.content)
        content = responce.split()
        isshiny = "Normal"
        name = content[1]
        if name.endswith("*"):
            isshiny = "Shiny"
            name = name.replace("*", "")
        if name.lower() == "mr" or name.lower() =="mr.":
            name = "Mr"
        if name.capitalize() == "Farfetch’d":
                name = "farfetch'd"
        if name.capitalize() == "Sirfetch’d":
            name = "sirfetch'd"
        Cname = name.capitalize()
        if Cname == "Alolan":
            name = content[2]
            if name.endswith("*"):
                isshiny = "Shiny"
                name = name.replace("*", "")
            Cname = name.capitalize()
            result = await PokemonHundoAlolan(self, name)
            Hundo = discord.Embed(title= "Alolan " + Cname + "'s Hundo Chart" , description="", color=0x2962FF)
            Hundo.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Alolan/"+str(isshiny)+"/"+Cname+".png")
            Hundo.add_field(name="Level to 1-10:", value="Level 1:  **"+str(result[0])+"**\nLevel 2:  **"+str(result[1])+"**\nLevel 3:  **"+str(result[2])+"**\nLevel 4:  **"+str(result[3])+"**\nLevel 5:  **"+str(result[4])+"**\nLevel 6:  **"+str(result[5])+"**\nLevel 7:  **"+str(result[6])+"**\n Level 8:  **"+str(result[7])+"**\nLevel 9:  **"+str(result[8])+"**\nLevel 10:  **"+str(result[9])+"**", inline=True)
            Hundo.add_field(name="Level to 11-20:", value="Level 11:  **"+str(result[10])+"**\nLevel 12:  **"+str(result[11])+"**\nLevel 13:  **"+str(result[12])+"**\nLevel 14:  **"+str(result[13])+"**\nLevel 15:  **"+str(result[14])+"**\nLevel 16:  **"+str(result[15])+"**\nLevel 17:  **"+str(result[16])+"**\nLevel 18:  **"+str(result[17])+"**\nLevel 19:  **"+str(result[18])+"**\nLevel 20:  **"+str(result[19])+"**", inline=True)
            Hundo.add_field(name="Level to 21-30:", value="Level 21:  **"+str(result[20])+"**\nLevel 22:  **"+str(result[21])+"**\nLevel 23:  **"+str(result[22])+"**\nLevel 24:  **"+str(result[23])+"**\nLevel 25:  **"+str(result[24])+"**\nLevel 26:  **"+str(result[25])+"**\nLevel 27:  **"+str(result[26])+"**\nLevel 28:  **"+str(result[27])+"**\nLevel 29:  **"+str(result[28])+"**\nLevel 30:  **"+str(result[29])+"**", inline=True)
            Hundo.add_field(name="Level to 31-40:", value="Level 31:  **"+str(result[30])+"**\nLevel 32:  **"+str(result[31])+"**\nLevel 33:  **"+str(result[32])+"**\nLevel 34:  **"+str(result[33])+"**\nLevel 35:  **"+str(result[34])+"**\nLevel 36:  **"+str(result[35])+"**\nLevel 37:  **"+str(result[36])+"**\nLevel 38:  **"+str(result[37])+"**\nLevel 39:  **"+str(result[38])+"**\nLevel 40:  **"+str(result[39])+"**", inline=True)
            Hundo.add_field(name="Level to 41-50:", value="Level 41:  **"+str(result[40])+"**\nLevel 42:  **"+str(result[41])+"**\nLevel 43:  **"+str(result[42])+"**\nLevel 44:  **"+str(result[43])+"**\nLevel 45:  **"+str(result[44])+"**\nLevel 46:  **"+str(result[45])+"**\nLevel 47:  **"+str(result[46])+"**\nLevel 48:  **"+str(result[47])+"**\nLevel 49:  **"+str(result[48])+"**\nLevel 50:  **"+str(result[49])+"**", inline=True)
            Hundo.add_field(name="Level 51", value="Level 51: **"+str(result[50])+"**", inline=True)
            Hundo.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send(embed=Hundo)
        elif Cname == "Galarian":
            name = content[2]
            if name.endswith("*"):
                isshiny = "Shiny"
                name = name.replace("*", "")
            if name.capitalize() == "Farfetch’d":
                name = "farfetch'd"
            Cname = name.capitalize()
            result = await PokemonHundoGalarian(self, Cname)
            Hundo = discord.Embed(title= "Galarian " + Cname + "'s Hundo Chart" , description="", color=0x2962FF)
            if Cname =="Farfetch'd":
                Cname = "Farfetchd"
            Hundo.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+Cname+".png")
            Hundo.add_field(name="Level to 1-10:", value="Level 1:  **"+str(result[0])+"**\nLevel 2:  **"+str(result[1])+"**\nLevel 3:  **"+str(result[2])+"**\nLevel 4:  **"+str(result[3])+"**\nLevel 5:  **"+str(result[4])+"**\nLevel 6:  **"+str(result[5])+"**\nLevel 7:  **"+str(result[6])+"**\n Level 8:  **"+str(result[7])+"**\nLevel 9:  **"+str(result[8])+"**\nLevel 10:  **"+str(result[9])+"**", inline=True)
            Hundo.add_field(name="Level to 11-20:", value="Level 11:  **"+str(result[10])+"**\nLevel 12:  **"+str(result[11])+"**\nLevel 13:  **"+str(result[12])+"**\nLevel 14:  **"+str(result[13])+"**\nLevel 15:  **"+str(result[14])+"**\nLevel 16:  **"+str(result[15])+"**\nLevel 17:  **"+str(result[16])+"**\nLevel 18:  **"+str(result[17])+"**\nLevel 19:  **"+str(result[18])+"**\nLevel 20:  **"+str(result[19])+"**", inline=True)
            Hundo.add_field(name="Level to 21-30:", value="Level 21:  **"+str(result[20])+"**\nLevel 22:  **"+str(result[21])+"**\nLevel 23:  **"+str(result[22])+"**\nLevel 24:  **"+str(result[23])+"**\nLevel 25:  **"+str(result[24])+"**\nLevel 26:  **"+str(result[25])+"**\nLevel 27:  **"+str(result[26])+"**\nLevel 28:  **"+str(result[27])+"**\nLevel 29:  **"+str(result[28])+"**\nLevel 30:  **"+str(result[29])+"**", inline=True)
            Hundo.add_field(name="Level to 31-40:", value="Level 31:  **"+str(result[30])+"**\nLevel 32:  **"+str(result[31])+"**\nLevel 33:  **"+str(result[32])+"**\nLevel 34:  **"+str(result[33])+"**\nLevel 35:  **"+str(result[34])+"**\nLevel 36:  **"+str(result[35])+"**\nLevel 37:  **"+str(result[36])+"**\nLevel 38:  **"+str(result[37])+"**\nLevel 39:  **"+str(result[38])+"**\nLevel 40:  **"+str(result[39])+"**", inline=True)
            Hundo.add_field(name="Level to 41-50:", value="Level 41:  **"+str(result[40])+"**\nLevel 42:  **"+str(result[41])+"**\nLevel 43:  **"+str(result[42])+"**\nLevel 44:  **"+str(result[43])+"**\nLevel 45:  **"+str(result[44])+"**\nLevel 46:  **"+str(result[45])+"**\nLevel 47:  **"+str(result[46])+"**\nLevel 48:  **"+str(result[47])+"**\nLevel 49:  **"+str(result[48])+"**\nLevel 50:  **"+str(result[49])+"**", inline=True)
            Hundo.add_field(name="Level 51", value="Level 51: **"+str(result[50])+"**", inline=True)
            Hundo.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send(embed=Hundo)
        elif Cname == "Armored":
            if content[2].endswith("*"):
                isshiny = "Shiny"
                content[2] = content[2].replace("*", "")
            if content[2] == "Mewtwo" or content[2] == "mewtwo":
                Aname = "Armoredmewtwo"
                name = content[2]
                Cname = name.capitalize()
                result = await PokemonHundo(self, Aname)
                Hundo = discord.Embed(title= "Armored " + Cname + "'s Hundo Chart" , description="", color=0x2962FF)
                Hundo.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Aname+".png")
                Hundo.add_field(name="Level to 1-10:", value="Level 1:  **"+str(result[0])+"**\nLevel 2:  **"+str(result[1])+"**\nLevel 3:  **"+str(result[2])+"**\nLevel 4:  **"+str(result[3])+"**\nLevel 5:  **"+str(result[4])+"**\nLevel 6:  **"+str(result[5])+"**\nLevel 7:  **"+str(result[6])+"**\n Level 8:  **"+str(result[7])+"**\nLevel 9:  **"+str(result[8])+"**\nLevel 10:  **"+str(result[9])+"**", inline=True)
                Hundo.add_field(name="Level to 11-20:", value="Level 11:  **"+str(result[10])+"**\nLevel 12:  **"+str(result[11])+"**\nLevel 13:  **"+str(result[12])+"**\nLevel 14:  **"+str(result[13])+"**\nLevel 15:  **"+str(result[14])+"**\nLevel 16:  **"+str(result[15])+"**\nLevel 17:  **"+str(result[16])+"**\nLevel 18:  **"+str(result[17])+"**\nLevel 19:  **"+str(result[18])+"**\nLevel 20:  **"+str(result[19])+"**", inline=True)
                Hundo.add_field(name="Level to 21-30:", value="Level 21:  **"+str(result[20])+"**\nLevel 22:  **"+str(result[21])+"**\nLevel 23:  **"+str(result[22])+"**\nLevel 24:  **"+str(result[23])+"**\nLevel 25:  **"+str(result[24])+"**\nLevel 26:  **"+str(result[25])+"**\nLevel 27:  **"+str(result[26])+"**\nLevel 28:  **"+str(result[27])+"**\nLevel 29:  **"+str(result[28])+"**\nLevel 30:  **"+str(result[29])+"**", inline=True)
                Hundo.add_field(name="Level to 31-40:", value="Level 31:  **"+str(result[30])+"**\nLevel 32:  **"+str(result[31])+"**\nLevel 33:  **"+str(result[32])+"**\nLevel 34:  **"+str(result[33])+"**\nLevel 35:  **"+str(result[34])+"**\nLevel 36:  **"+str(result[35])+"**\nLevel 37:  **"+str(result[36])+"**\nLevel 38:  **"+str(result[37])+"**\nLevel 39:  **"+str(result[38])+"**\nLevel 40:  **"+str(result[39])+"**", inline=True)
                Hundo.add_field(name="Level to 41-50:", value="Level 41:  **"+str(result[40])+"**\nLevel 42:  **"+str(result[41])+"**\nLevel 43:  **"+str(result[42])+"**\nLevel 44:  **"+str(result[43])+"**\nLevel 45:  **"+str(result[44])+"**\nLevel 46:  **"+str(result[45])+"**\nLevel 47:  **"+str(result[46])+"**\nLevel 48:  **"+str(result[47])+"**\nLevel 49:  **"+str(result[48])+"**\nLevel 50:  **"+str(result[49])+"**", inline=True)
                Hundo.add_field(name="Level 51", value="Level 51: **"+str(result[50])+"**", inline=True)
                Hundo.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=Hundo)
            else:
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send("Only Armored Mewtwo exists...     Ţ̸̧̖̘̒͐͌e̷̳͕͋a̸̗̫̓ḿ̷̡͙̱̊̚ ̵̘̖̼̪̦̟̏̂̀̓͌͘͝R̴̨̨͈̰̼̳̜̓̈̓o̷͙͠c̶͔̼̀̍̄̃̔͝ķ̸̦̜͚͂̅̀e̶̡̢̡̘̜̒̕t̷͎̼̙̀͌̊̂̕̚")
        elif Cname == "Origin":
            if content[2].endswith("*"):
                isshiny = "Shiny"
                content[2] = content[2].replace("*", "")
            if content[2] == "Giratina" or content[2] == "giratina":
                Aname = "Origingiratina"
                name = content[2]
                Cname = name.capitalize()
                result = await PokemonHundo(self, Aname)
                Hundo = discord.Embed(title= "Origin Forme " + Cname + "'s Hundo Chart" , description="", color=0x2962FF)
                Hundo.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Cname+".png")
                Hundo.add_field(name="Level to 1-10:", value="Level 1:  **"+str(result[0])+"**\nLevel 2:  **"+str(result[1])+"**\nLevel 3:  **"+str(result[2])+"**\nLevel 4:  **"+str(result[3])+"**\nLevel 5:  **"+str(result[4])+"**\nLevel 6:  **"+str(result[5])+"**\nLevel 7:  **"+str(result[6])+"**\n Level 8:  **"+str(result[7])+"**\nLevel 9:  **"+str(result[8])+"**\nLevel 10:  **"+str(result[9])+"**", inline=True)
                Hundo.add_field(name="Level to 11-20:", value="Level 11:  **"+str(result[10])+"**\nLevel 12:  **"+str(result[11])+"**\nLevel 13:  **"+str(result[12])+"**\nLevel 14:  **"+str(result[13])+"**\nLevel 15:  **"+str(result[14])+"**\nLevel 16:  **"+str(result[15])+"**\nLevel 17:  **"+str(result[16])+"**\nLevel 18:  **"+str(result[17])+"**\nLevel 19:  **"+str(result[18])+"**\nLevel 20:  **"+str(result[19])+"**", inline=True)
                Hundo.add_field(name="Level to 21-30:", value="Level 21:  **"+str(result[20])+"**\nLevel 22:  **"+str(result[21])+"**\nLevel 23:  **"+str(result[22])+"**\nLevel 24:  **"+str(result[23])+"**\nLevel 25:  **"+str(result[24])+"**\nLevel 26:  **"+str(result[25])+"**\nLevel 27:  **"+str(result[26])+"**\nLevel 28:  **"+str(result[27])+"**\nLevel 29:  **"+str(result[28])+"**\nLevel 30:  **"+str(result[29])+"**", inline=True)
                Hundo.add_field(name="Level to 31-40:", value="Level 31:  **"+str(result[30])+"**\nLevel 32:  **"+str(result[31])+"**\nLevel 33:  **"+str(result[32])+"**\nLevel 34:  **"+str(result[33])+"**\nLevel 35:  **"+str(result[34])+"**\nLevel 36:  **"+str(result[35])+"**\nLevel 37:  **"+str(result[36])+"**\nLevel 38:  **"+str(result[37])+"**\nLevel 39:  **"+str(result[38])+"**\nLevel 40:  **"+str(result[39])+"**", inline=True)
                Hundo.add_field(name="Level to 41-50:", value="Level 41:  **"+str(result[40])+"**\nLevel 42:  **"+str(result[41])+"**\nLevel 43:  **"+str(result[42])+"**\nLevel 44:  **"+str(result[43])+"**\nLevel 45:  **"+str(result[44])+"**\nLevel 46:  **"+str(result[45])+"**\nLevel 47:  **"+str(result[46])+"**\nLevel 48:  **"+str(result[47])+"**\nLevel 49:  **"+str(result[48])+"**\nLevel 50:  **"+str(result[49])+"**", inline=True)
                Hundo.add_field(name="Level 51", value="Level 51: **"+str(result[50])+"**", inline=True)
                Hundo.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=Hundo)
            else:
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send("Only Origin Giratina exists...")
        elif Cname == "Attack":
            Aname = "Adeoxys"
            name = content[2]
            if name.endswith("*"):
                isshiny = "Shiny"
                name = name.replace("*", "")
            Cname = name.capitalize()
            result = await PokemonHundo(self, Aname)
            Hundo = discord.Embed(title= "Attack Forme " + Cname + "'s Hundo Chart" , description="", color=0x2962FF)
            Hundo.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Adeoxys.png")
            Hundo.add_field(name="Level to 1-10:", value="Level 1:  **"+str(result[0])+"**\nLevel 2:  **"+str(result[1])+"**\nLevel 3:  **"+str(result[2])+"**\nLevel 4:  **"+str(result[3])+"**\nLevel 5:  **"+str(result[4])+"**\nLevel 6:  **"+str(result[5])+"**\nLevel 7:  **"+str(result[6])+"**\n Level 8:  **"+str(result[7])+"**\nLevel 9:  **"+str(result[8])+"**\nLevel 10:  **"+str(result[9])+"**", inline=True)
            Hundo.add_field(name="Level to 11-20:", value="Level 11:  **"+str(result[10])+"**\nLevel 12:  **"+str(result[11])+"**\nLevel 13:  **"+str(result[12])+"**\nLevel 14:  **"+str(result[13])+"**\nLevel 15:  **"+str(result[14])+"**\nLevel 16:  **"+str(result[15])+"**\nLevel 17:  **"+str(result[16])+"**\nLevel 18:  **"+str(result[17])+"**\nLevel 19:  **"+str(result[18])+"**\nLevel 20:  **"+str(result[19])+"**", inline=True)
            Hundo.add_field(name="Level to 21-30:", value="Level 21:  **"+str(result[20])+"**\nLevel 22:  **"+str(result[21])+"**\nLevel 23:  **"+str(result[22])+"**\nLevel 24:  **"+str(result[23])+"**\nLevel 25:  **"+str(result[24])+"**\nLevel 26:  **"+str(result[25])+"**\nLevel 27:  **"+str(result[26])+"**\nLevel 28:  **"+str(result[27])+"**\nLevel 29:  **"+str(result[28])+"**\nLevel 30:  **"+str(result[29])+"**", inline=True)
            Hundo.add_field(name="Level to 31-40:", value="Level 31:  **"+str(result[30])+"**\nLevel 32:  **"+str(result[31])+"**\nLevel 33:  **"+str(result[32])+"**\nLevel 34:  **"+str(result[33])+"**\nLevel 35:  **"+str(result[34])+"**\nLevel 36:  **"+str(result[35])+"**\nLevel 37:  **"+str(result[36])+"**\nLevel 38:  **"+str(result[37])+"**\nLevel 39:  **"+str(result[38])+"**\nLevel 40:  **"+str(result[39])+"**", inline=True)
            Hundo.add_field(name="Level to 41-50:", value="Level 41:  **"+str(result[40])+"**\nLevel 42:  **"+str(result[41])+"**\nLevel 43:  **"+str(result[42])+"**\nLevel 44:  **"+str(result[43])+"**\nLevel 45:  **"+str(result[44])+"**\nLevel 46:  **"+str(result[45])+"**\nLevel 47:  **"+str(result[46])+"**\nLevel 48:  **"+str(result[47])+"**\nLevel 49:  **"+str(result[48])+"**\nLevel 50:  **"+str(result[49])+"**", inline=True)
            Hundo.add_field(name="Level 51", value="Level 51: **"+str(result[50])+"**", inline=True)
            Hundo.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send(embed=Hundo)
        elif Cname == "Defense":
            Aname = "Ddeoxys"
            name = content[2]
            if name.endswith("*"):
                isshiny = "Shiny"
                name = name.replace("*", "")
            Cname = name.capitalize()
            result = await PokemonHundo(self, Aname)
            Hundo = discord.Embed(title= "Defense Forme "+ Cname + "'s Hundo Chart" , description="", color=0x2962FF)
            Hundo.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Ddeoxys.png")
            Hundo.add_field(name="Level to 1-10:", value="Level 1:  **"+str(result[0])+"**\nLevel 2:  **"+str(result[1])+"**\nLevel 3:  **"+str(result[2])+"**\nLevel 4:  **"+str(result[3])+"**\nLevel 5:  **"+str(result[4])+"**\nLevel 6:  **"+str(result[5])+"**\nLevel 7:  **"+str(result[6])+"**\n Level 8:  **"+str(result[7])+"**\nLevel 9:  **"+str(result[8])+"**\nLevel 10:  **"+str(result[9])+"**", inline=True)
            Hundo.add_field(name="Level to 11-20:", value="Level 11:  **"+str(result[10])+"**\nLevel 12:  **"+str(result[11])+"**\nLevel 13:  **"+str(result[12])+"**\nLevel 14:  **"+str(result[13])+"**\nLevel 15:  **"+str(result[14])+"**\nLevel 16:  **"+str(result[15])+"**\nLevel 17:  **"+str(result[16])+"**\nLevel 18:  **"+str(result[17])+"**\nLevel 19:  **"+str(result[18])+"**\nLevel 20:  **"+str(result[19])+"**", inline=True)
            Hundo.add_field(name="Level to 21-30:", value="Level 21:  **"+str(result[20])+"**\nLevel 22:  **"+str(result[21])+"**\nLevel 23:  **"+str(result[22])+"**\nLevel 24:  **"+str(result[23])+"**\nLevel 25:  **"+str(result[24])+"**\nLevel 26:  **"+str(result[25])+"**\nLevel 27:  **"+str(result[26])+"**\nLevel 28:  **"+str(result[27])+"**\nLevel 29:  **"+str(result[28])+"**\nLevel 30:  **"+str(result[29])+"**", inline=True)
            Hundo.add_field(name="Level to 31-40:", value="Level 31:  **"+str(result[30])+"**\nLevel 32:  **"+str(result[31])+"**\nLevel 33:  **"+str(result[32])+"**\nLevel 34:  **"+str(result[33])+"**\nLevel 35:  **"+str(result[34])+"**\nLevel 36:  **"+str(result[35])+"**\nLevel 37:  **"+str(result[36])+"**\nLevel 38:  **"+str(result[37])+"**\nLevel 39:  **"+str(result[38])+"**\nLevel 40:  **"+str(result[39])+"**", inline=True)
            Hundo.add_field(name="Level to 41-50:", value="Level 41:  **"+str(result[40])+"**\nLevel 42:  **"+str(result[41])+"**\nLevel 43:  **"+str(result[42])+"**\nLevel 44:  **"+str(result[43])+"**\nLevel 45:  **"+str(result[44])+"**\nLevel 46:  **"+str(result[45])+"**\nLevel 47:  **"+str(result[46])+"**\nLevel 48:  **"+str(result[47])+"**\nLevel 49:  **"+str(result[48])+"**\nLevel 50:  **"+str(result[49])+"**", inline=True)
            Hundo.add_field(name="Level 51", value="Level 51: **"+str(result[50])+"**", inline=True)
            Hundo.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send(embed=Hundo)
        elif Cname == "Speed":
            Aname = "Sdeoxys"
            name = content[2]
            if name.endswith("*"):
                isshiny = "Shiny"
                name = name.replace("*", "")
            Cname = name.capitalize()
            result = await PokemonHundo(self, name)
            Hundo = discord.Embed(title= "Speed Forme "+ Cname + "'s Hundo Chart" , description="", color=0x2962FF)
            Hundo.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Sdeoxys.png")
            Hundo.add_field(name="Level to 1-10:", value="Level 1:  **"+str(result[0])+"**\nLevel 2:  **"+str(result[1])+"**\nLevel 3:  **"+str(result[2])+"**\nLevel 4:  **"+str(result[3])+"**\nLevel 5:  **"+str(result[4])+"**\nLevel 6:  **"+str(result[5])+"**\nLevel 7:  **"+str(result[6])+"**\n Level 8:  **"+str(result[7])+"**\nLevel 9:  **"+str(result[8])+"**\nLevel 10:  **"+str(result[9])+"**", inline=True)
            Hundo.add_field(name="Level to 11-20:", value="Level 11:  **"+str(result[10])+"**\nLevel 12:  **"+str(result[11])+"**\nLevel 13:  **"+str(result[12])+"**\nLevel 14:  **"+str(result[13])+"**\nLevel 15:  **"+str(result[14])+"**\nLevel 16:  **"+str(result[15])+"**\nLevel 17:  **"+str(result[16])+"**\nLevel 18:  **"+str(result[17])+"**\nLevel 19:  **"+str(result[18])+"**\nLevel 20:  **"+str(result[19])+"**", inline=True)
            Hundo.add_field(name="Level to 21-30:", value="Level 21:  **"+str(result[20])+"**\nLevel 22:  **"+str(result[21])+"**\nLevel 23:  **"+str(result[22])+"**\nLevel 24:  **"+str(result[23])+"**\nLevel 25:  **"+str(result[24])+"**\nLevel 26:  **"+str(result[25])+"**\nLevel 27:  **"+str(result[26])+"**\nLevel 28:  **"+str(result[27])+"**\nLevel 29:  **"+str(result[28])+"**\nLevel 30:  **"+str(result[29])+"**", inline=True)
            Hundo.add_field(name="Level to 31-40:", value="Level 31:  **"+str(result[30])+"**\nLevel 32:  **"+str(result[31])+"**\nLevel 33:  **"+str(result[32])+"**\nLevel 34:  **"+str(result[33])+"**\nLevel 35:  **"+str(result[34])+"**\nLevel 36:  **"+str(result[35])+"**\nLevel 37:  **"+str(result[36])+"**\nLevel 38:  **"+str(result[37])+"**\nLevel 39:  **"+str(result[38])+"**\nLevel 40:  **"+str(result[39])+"**", inline=True)
            Hundo.add_field(name="Level to 41-50:", value="Level 41:  **"+str(result[40])+"**\nLevel 42:  **"+str(result[41])+"**\nLevel 43:  **"+str(result[42])+"**\nLevel 44:  **"+str(result[43])+"**\nLevel 45:  **"+str(result[44])+"**\nLevel 46:  **"+str(result[45])+"**\nLevel 47:  **"+str(result[46])+"**\nLevel 48:  **"+str(result[47])+"**\nLevel 49:  **"+str(result[48])+"**\nLevel 50:  **"+str(result[49])+"**", inline=True)
            Hundo.add_field(name="Level 51", value="Level 51: **"+str(result[50])+"**", inline=True)
            Hundo.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send(embed=Hundo)
        elif Cname == "Therian":
            if content[2].capitalize() == "Tornadus":
                name = content[2]
                if name.endswith("*"):
                    isshiny = "Shiny"
                    name = name.replace("*", "")
                Cname = name.capitalize()
                result = await PokemonHundo(self, "Ttornadus")
                Hundo = discord.Embed(title= "Therian "+ Cname + "'s Hundo Chart" , description="", color=0x2962FF)
                Hundo.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Ttornadus.png")
                Hundo.add_field(name="Level to 1-10:", value="Level 1:  **"+str(result[0])+"**\nLevel 2:  **"+str(result[1])+"**\nLevel 3:  **"+str(result[2])+"**\nLevel 4:  **"+str(result[3])+"**\nLevel 5:  **"+str(result[4])+"**\nLevel 6:  **"+str(result[5])+"**\nLevel 7:  **"+str(result[6])+"**\n Level 8:  **"+str(result[7])+"**\nLevel 9:  **"+str(result[8])+"**\nLevel 10:  **"+str(result[9])+"**", inline=True)
                Hundo.add_field(name="Level to 11-20:", value="Level 11:  **"+str(result[10])+"**\nLevel 12:  **"+str(result[11])+"**\nLevel 13:  **"+str(result[12])+"**\nLevel 14:  **"+str(result[13])+"**\nLevel 15:  **"+str(result[14])+"**\nLevel 16:  **"+str(result[15])+"**\nLevel 17:  **"+str(result[16])+"**\nLevel 18:  **"+str(result[17])+"**\nLevel 19:  **"+str(result[18])+"**\nLevel 20:  **"+str(result[19])+"**", inline=True)
                Hundo.add_field(name="Level to 21-30:", value="Level 21:  **"+str(result[20])+"**\nLevel 22:  **"+str(result[21])+"**\nLevel 23:  **"+str(result[22])+"**\nLevel 24:  **"+str(result[23])+"**\nLevel 25:  **"+str(result[24])+"**\nLevel 26:  **"+str(result[25])+"**\nLevel 27:  **"+str(result[26])+"**\nLevel 28:  **"+str(result[27])+"**\nLevel 29:  **"+str(result[28])+"**\nLevel 30:  **"+str(result[29])+"**", inline=True)
                Hundo.add_field(name="Level to 31-40:", value="Level 31:  **"+str(result[30])+"**\nLevel 32:  **"+str(result[31])+"**\nLevel 33:  **"+str(result[32])+"**\nLevel 34:  **"+str(result[33])+"**\nLevel 35:  **"+str(result[34])+"**\nLevel 36:  **"+str(result[35])+"**\nLevel 37:  **"+str(result[36])+"**\nLevel 38:  **"+str(result[37])+"**\nLevel 39:  **"+str(result[38])+"**\nLevel 40:  **"+str(result[39])+"**", inline=True)
                Hundo.add_field(name="Level to 41-50:", value="Level 41:  **"+str(result[40])+"**\nLevel 42:  **"+str(result[41])+"**\nLevel 43:  **"+str(result[42])+"**\nLevel 44:  **"+str(result[43])+"**\nLevel 45:  **"+str(result[44])+"**\nLevel 46:  **"+str(result[45])+"**\nLevel 47:  **"+str(result[46])+"**\nLevel 48:  **"+str(result[47])+"**\nLevel 49:  **"+str(result[48])+"**\nLevel 50:  **"+str(result[49])+"**", inline=True)
                Hundo.add_field(name="Level 51", value="Level 51: **"+str(result[50])+"**", inline=True)
                Hundo.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=Hundo)
            elif content[2].capitalize() == "Thundurus":
                name = content[2]
                if name.endswith("*"):
                    isshiny = "Shiny"
                    name = name.replace("*", "")
                Cname = name.capitalize()
                result = await PokemonHundo(self, "Tthundurus")
                Hundo = discord.Embed(title= "Therian "+ Cname + "'s Hundo Chart" , description="", color=0x2962FF)
                Hundo.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Tthundurus.png")
                Hundo.add_field(name="Level to 1-10:", value="Level 1:  **"+str(result[0])+"**\nLevel 2:  **"+str(result[1])+"**\nLevel 3:  **"+str(result[2])+"**\nLevel 4:  **"+str(result[3])+"**\nLevel 5:  **"+str(result[4])+"**\nLevel 6:  **"+str(result[5])+"**\nLevel 7:  **"+str(result[6])+"**\n Level 8:  **"+str(result[7])+"**\nLevel 9:  **"+str(result[8])+"**\nLevel 10:  **"+str(result[9])+"**", inline=True)
                Hundo.add_field(name="Level to 11-20:", value="Level 11:  **"+str(result[10])+"**\nLevel 12:  **"+str(result[11])+"**\nLevel 13:  **"+str(result[12])+"**\nLevel 14:  **"+str(result[13])+"**\nLevel 15:  **"+str(result[14])+"**\nLevel 16:  **"+str(result[15])+"**\nLevel 17:  **"+str(result[16])+"**\nLevel 18:  **"+str(result[17])+"**\nLevel 19:  **"+str(result[18])+"**\nLevel 20:  **"+str(result[19])+"**", inline=True)
                Hundo.add_field(name="Level to 21-30:", value="Level 21:  **"+str(result[20])+"**\nLevel 22:  **"+str(result[21])+"**\nLevel 23:  **"+str(result[22])+"**\nLevel 24:  **"+str(result[23])+"**\nLevel 25:  **"+str(result[24])+"**\nLevel 26:  **"+str(result[25])+"**\nLevel 27:  **"+str(result[26])+"**\nLevel 28:  **"+str(result[27])+"**\nLevel 29:  **"+str(result[28])+"**\nLevel 30:  **"+str(result[29])+"**", inline=True)
                Hundo.add_field(name="Level to 31-40:", value="Level 31:  **"+str(result[30])+"**\nLevel 32:  **"+str(result[31])+"**\nLevel 33:  **"+str(result[32])+"**\nLevel 34:  **"+str(result[33])+"**\nLevel 35:  **"+str(result[34])+"**\nLevel 36:  **"+str(result[35])+"**\nLevel 37:  **"+str(result[36])+"**\nLevel 38:  **"+str(result[37])+"**\nLevel 39:  **"+str(result[38])+"**\nLevel 40:  **"+str(result[39])+"**", inline=True)
                Hundo.add_field(name="Level to 41-50:", value="Level 41:  **"+str(result[40])+"**\nLevel 42:  **"+str(result[41])+"**\nLevel 43:  **"+str(result[42])+"**\nLevel 44:  **"+str(result[43])+"**\nLevel 45:  **"+str(result[44])+"**\nLevel 46:  **"+str(result[45])+"**\nLevel 47:  **"+str(result[46])+"**\nLevel 48:  **"+str(result[47])+"**\nLevel 49:  **"+str(result[48])+"**\nLevel 50:  **"+str(result[49])+"**", inline=True)
                Hundo.add_field(name="Level 51", value="Level 51: **"+str(result[50])+"**", inline=True)
                Hundo.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=Hundo)            
            elif content[2].capitalize() == "Landorus":
                name = content[2]
                if name.endswith("*"):
                    isshiny = "Shiny"
                    name = name.replace("*", "")
                Cname = name.capitalize()
                result = await PokemonHundo(self, "Tlandorus")
                Hundo = discord.Embed(title= "Therian "+ Cname + "'s Hundo Chart" , description="", color=0x2962FF)
                Hundo.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Tlandorus.png")
                Hundo.add_field(name="Level to 1-10:", value="Level 1:  **"+str(result[0])+"**\nLevel 2:  **"+str(result[1])+"**\nLevel 3:  **"+str(result[2])+"**\nLevel 4:  **"+str(result[3])+"**\nLevel 5:  **"+str(result[4])+"**\nLevel 6:  **"+str(result[5])+"**\nLevel 7:  **"+str(result[6])+"**\n Level 8:  **"+str(result[7])+"**\nLevel 9:  **"+str(result[8])+"**\nLevel 10:  **"+str(result[9])+"**", inline=True)
                Hundo.add_field(name="Level to 11-20:", value="Level 11:  **"+str(result[10])+"**\nLevel 12:  **"+str(result[11])+"**\nLevel 13:  **"+str(result[12])+"**\nLevel 14:  **"+str(result[13])+"**\nLevel 15:  **"+str(result[14])+"**\nLevel 16:  **"+str(result[15])+"**\nLevel 17:  **"+str(result[16])+"**\nLevel 18:  **"+str(result[17])+"**\nLevel 19:  **"+str(result[18])+"**\nLevel 20:  **"+str(result[19])+"**", inline=True)
                Hundo.add_field(name="Level to 21-30:", value="Level 21:  **"+str(result[20])+"**\nLevel 22:  **"+str(result[21])+"**\nLevel 23:  **"+str(result[22])+"**\nLevel 24:  **"+str(result[23])+"**\nLevel 25:  **"+str(result[24])+"**\nLevel 26:  **"+str(result[25])+"**\nLevel 27:  **"+str(result[26])+"**\nLevel 28:  **"+str(result[27])+"**\nLevel 29:  **"+str(result[28])+"**\nLevel 30:  **"+str(result[29])+"**", inline=True)
                Hundo.add_field(name="Level to 31-40:", value="Level 31:  **"+str(result[30])+"**\nLevel 32:  **"+str(result[31])+"**\nLevel 33:  **"+str(result[32])+"**\nLevel 34:  **"+str(result[33])+"**\nLevel 35:  **"+str(result[34])+"**\nLevel 36:  **"+str(result[35])+"**\nLevel 37:  **"+str(result[36])+"**\nLevel 38:  **"+str(result[37])+"**\nLevel 39:  **"+str(result[38])+"**\nLevel 40:  **"+str(result[39])+"**", inline=True)
                Hundo.add_field(name="Level to 41-50:", value="Level 41:  **"+str(result[40])+"**\nLevel 42:  **"+str(result[41])+"**\nLevel 43:  **"+str(result[42])+"**\nLevel 44:  **"+str(result[43])+"**\nLevel 45:  **"+str(result[44])+"**\nLevel 46:  **"+str(result[45])+"**\nLevel 47:  **"+str(result[46])+"**\nLevel 48:  **"+str(result[47])+"**\nLevel 49:  **"+str(result[48])+"**\nLevel 50:  **"+str(result[49])+"**", inline=True)
                Hundo.add_field(name="Level 51", value="Level 51: **"+str(result[50])+"**", inline=True)
                Hundo.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=Hundo)
        elif Cname != "Galarian":
            if name == "Mr":
                if content[2].endswith("*"):
                    isshiny = "Shiny"
                    name = name.replace("*", "")
                name = "Mrmime"
                Cname = "Mr. Mime"
                result = await PokemonHundo(self, name)
                Hundo = discord.Embed(title= Cname + "'s Hundo Chart" , description="", color=0x2962FF)
                Hundo.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Mrmime.png")
                Hundo.add_field(name="Level to 1-10:", value="Level 1:  **"+str(result[0])+"**\nLevel 2:  **"+str(result[1])+"**\nLevel 3:  **"+str(result[2])+"**\nLevel 4:  **"+str(result[3])+"**\nLevel 5:  **"+str(result[4])+"**\nLevel 6:  **"+str(result[5])+"**\nLevel 7:  **"+str(result[6])+"**\n Level 8:  **"+str(result[7])+"**\nLevel 9:  **"+str(result[8])+"**\nLevel 10:  **"+str(result[9])+"**", inline=True)
                Hundo.add_field(name="Level to 11-20:", value="Level 11:  **"+str(result[10])+"**\nLevel 12:  **"+str(result[11])+"**\nLevel 13:  **"+str(result[12])+"**\nLevel 14:  **"+str(result[13])+"**\nLevel 15:  **"+str(result[14])+"**\nLevel 16:  **"+str(result[15])+"**\nLevel 17:  **"+str(result[16])+"**\nLevel 18:  **"+str(result[17])+"**\nLevel 19:  **"+str(result[18])+"**\nLevel 20:  **"+str(result[19])+"**", inline=True)
                Hundo.add_field(name="Level to 21-30:", value="Level 21:  **"+str(result[20])+"**\nLevel 22:  **"+str(result[21])+"**\nLevel 23:  **"+str(result[22])+"**\nLevel 24:  **"+str(result[23])+"**\nLevel 25:  **"+str(result[24])+"**\nLevel 26:  **"+str(result[25])+"**\nLevel 27:  **"+str(result[26])+"**\nLevel 28:  **"+str(result[27])+"**\nLevel 29:  **"+str(result[28])+"**\nLevel 30:  **"+str(result[29])+"**", inline=True)
                Hundo.add_field(name="Level to 31-40:", value="Level 31:  **"+str(result[30])+"**\nLevel 32:  **"+str(result[31])+"**\nLevel 33:  **"+str(result[32])+"**\nLevel 34:  **"+str(result[33])+"**\nLevel 35:  **"+str(result[34])+"**\nLevel 36:  **"+str(result[35])+"**\nLevel 37:  **"+str(result[36])+"**\nLevel 38:  **"+str(result[37])+"**\nLevel 39:  **"+str(result[38])+"**\nLevel 40:  **"+str(result[39])+"**", inline=True)
                Hundo.add_field(name="Level to 41-50:", value="Level 41:  **"+str(result[40])+"**\nLevel 42:  **"+str(result[41])+"**\nLevel 43:  **"+str(result[42])+"**\nLevel 44:  **"+str(result[43])+"**\nLevel 45:  **"+str(result[44])+"**\nLevel 46:  **"+str(result[45])+"**\nLevel 47:  **"+str(result[46])+"**\nLevel 48:  **"+str(result[47])+"**\nLevel 49:  **"+str(result[48])+"**\nLevel 50:  **"+str(result[49])+"**", inline=True)
                Hundo.add_field(name="Level 51", value="Level 51: **"+str(result[50])+"**", inline=True)
                Hundo.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=Hundo)
            else:
                result = await PokemonHundo(self, name)
                Hundo = discord.Embed(title= Cname + "'s Hundo Chart" , description="", color=0x2962FF)
                Hundo.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Cname+".png")
                Hundo.add_field(name="Level to 1-10:", value="Level 1:  **"+str(result[0])+"**\nLevel 2:  **"+str(result[1])+"**\nLevel 3:  **"+str(result[2])+"**\nLevel 4:  **"+str(result[3])+"**\nLevel 5:  **"+str(result[4])+"**\nLevel 6:  **"+str(result[5])+"**\nLevel 7:  **"+str(result[6])+"**\n Level 8:  **"+str(result[7])+"**\nLevel 9:  **"+str(result[8])+"**\nLevel 10:  **"+str(result[9])+"**", inline=True)
                Hundo.add_field(name="Level to 11-20:", value="Level 11:  **"+str(result[10])+"**\nLevel 12:  **"+str(result[11])+"**\nLevel 13:  **"+str(result[12])+"**\nLevel 14:  **"+str(result[13])+"**\nLevel 15:  **"+str(result[14])+"**\nLevel 16:  **"+str(result[15])+"**\nLevel 17:  **"+str(result[16])+"**\nLevel 18:  **"+str(result[17])+"**\nLevel 19:  **"+str(result[18])+"**\nLevel 20:  **"+str(result[19])+"**", inline=True)
                Hundo.add_field(name="Level to 21-30:", value="Level 21:  **"+str(result[20])+"**\nLevel 22:  **"+str(result[21])+"**\nLevel 23:  **"+str(result[22])+"**\nLevel 24:  **"+str(result[23])+"**\nLevel 25:  **"+str(result[24])+"**\nLevel 26:  **"+str(result[25])+"**\nLevel 27:  **"+str(result[26])+"**\nLevel 28:  **"+str(result[27])+"**\nLevel 29:  **"+str(result[28])+"**\nLevel 30:  **"+str(result[29])+"**", inline=True)
                Hundo.add_field(name="Level to 31-40:", value="Level 31:  **"+str(result[30])+"**\nLevel 32:  **"+str(result[31])+"**\nLevel 33:  **"+str(result[32])+"**\nLevel 34:  **"+str(result[33])+"**\nLevel 35:  **"+str(result[34])+"**\nLevel 36:  **"+str(result[35])+"**\nLevel 37:  **"+str(result[36])+"**\nLevel 38:  **"+str(result[37])+"**\nLevel 39:  **"+str(result[38])+"**\nLevel 40:  **"+str(result[39])+"**", inline=True)
                Hundo.add_field(name="Level to 41-50:", value="Level 41:  **"+str(result[40])+"**\nLevel 42:  **"+str(result[41])+"**\nLevel 43:  **"+str(result[42])+"**\nLevel 44:  **"+str(result[43])+"**\nLevel 45:  **"+str(result[44])+"**\nLevel 46:  **"+str(result[45])+"**\nLevel 47:  **"+str(result[46])+"**\nLevel 48:  **"+str(result[47])+"**\nLevel 49:  **"+str(result[48])+"**\nLevel 50:  **"+str(result[49])+"**", inline=True)
                Hundo.add_field(name="Level 51", value="Level 51: **"+str(result[50])+"**", inline=True)
                Hundo.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=Hundo)

    @commands.command()
    async def gopure(self, ctx):
        responce = str(ctx.message.content)
        content = responce.split()
        isshiny = "Normal"
        name = content[1].capitalize()
        if name.endswith("*"):
            isshiny = "Shiny"
            name = name.replace("*", "")
        Cname = name.capitalize()
        if Cname.endswith("*"):
            Cname = Cname.replace("*", "")
        Shadow = ("Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Weedle", "Kakuna", "Beedrill", "Rattata", "Raticate",
        "Sandshrew", "Sandslash", "Nidoran\U00002640", "Nidorina", "Nidoqueen", "Nidoran\U00002642", "Nidorino" ,"Nidoking", "Vulpix", "Ninetails", "Zubat", "Golbat", "Crobat", "Oddish",
        "Gloom", "Vileplume", "Bellossom", "Venonat", "Venomoth", "Meowth", "Persian", "Psyduck", "Golduck", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Politoed",
        "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Magnemite", "Magneton", "Magnezone", "Grimer", "Muk", "Drowzee", "Hypno",
        "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Koffing", "Weezing", "Scyther", "Scizor", "Electabuzz", "Electivire", "Magmar", "Magmortar", "Magikarp",
        "Gyarados", "Lapras", "Porygon", "Porygon2", "PorygonZ", "Omanyte", "Omastar", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mareep",
        "Flaaffy", "Ampharos", "Hoppip", "Skiploom", "Jumpluff", "Wooper", "Quagsire", "Misdeavus", "Mismagius", "Wobuffett", "Pineco", "Forretress", "Gligar", "Gliscor", "Shuckle", "Sneasel",
        "Weavile", "Swinub", "Piloswine", "Mamoswine", "Teddiursa", "Ursaring", "Delibird", "Skarmory", "Houndour", "Houndoom", "Stantler", "Raikou", "Entei", "Suicune", "Larvitar", "Pupitar", "Tyranitar", "Mudkip", "Marshtomp",
        "Swampert", "Seedot", "Nuzleaf", "Shiftry", "Ralts", "Kirlia", "Gardevoir", "Gallade", "Nosepass", "Probopass", "Sableye", "Mawile", "Aron", "Lairon", "Aggron", "Carvanha", "Sharpedo", "Trapinch", "Vibrava", "Flygon", "Cacnea", "Cacturne", "Lileep", "Cradily", "Anorith", "Armaldo"
        "Shuppet", "Banette", "Duskull", "Dusclops", "Dusknoir", "Absol", "Spheal", "Sealeo", "Walrein", "Bagon", "Shelgon", "Salamence", "Beldum", "Metang", "Metagross", "Turtwig", "Grotle", "Torterra", "Stunky", "Stuntank", "Snover", "Abomasnow")
        if Cname.startswith("Nidoran\U00002640"):
            Cname = "Nidoranf"
            name = "Nidoran\U00002640"
        elif Cname.startswith("Nidoran\U00002642"):
            Cname = "Nidoranm"
            name = "Nidoran\U00002640"
        if name in Shadow:
            try:
                AIVB = int(content[2])
            except ValueError:
                # if candelete == "True":await ctx.message.delete()
                await ctx.send("The Value for the Attack IV isn't a valid number",delete_after=10)
            try:
                DIVB = int(content[3])
            except ValueError:
                # if candelete == "True":await ctx.message.delete()
                await ctx.send("The Value for the Defense IV isn't a valid number",delete_after=10)
            try:
                SIVB = int(content[4])
            except ValueError:
                # if candelete == "True":await ctx.message.delete()
                await ctx.send("The Value for the HP IV isn't a valid number",delete_after=10)
            if AIVB > 15:
                await ctx.send("That's not a valid Attack IV number, so I'll assume you meant 15", delete_after=5)
            if DIVB > 15:
                await ctx.send("That's not a valid Defense IV number, so I'll assume you meant 15", delete_after=5)
            if SIVB > 15:
                await ctx.send("That's not a valid HP IV number, so I'll assume you meant 15", delete_after=5)
            AIVA = AIVB + 2
            DIVA = DIVB + 2
            SIVA = SIVB + 2
            if AIVB >= 15:
                AIVB = 15
            if DIVB >= 15:
                DIVB = 15
            if SIVB >= 15:
                SIVB = 15
            if AIVA >= 15:
                AIVA = 15
            if DIVA >= 15:
                DIVA = 15
            if SIVA >= 15:
                SIVA = 15
            Pure = discord.Embed(title= name + "'s Purified Stats" , description="", color=0x2962FF)
            Pure.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Cname+".png")
            Pure.add_field(name="Attack IV Shadow:", value="**"+str(AIVB)+"**", inline=True)
            Pure.add_field(name="Defense IV Shadow:", value="**"+str(DIVB)+"**", inline=True)
            Pure.add_field(name="HP IV Shadow:", value="**"+str(SIVB)+"**", inline= True)
            Pure.add_field(name="Attack IV Purified:", value="**"+str(AIVA)+"**", inline=True)
            Pure.add_field(name="Defense IV Purified:", value="**"+str(DIVA)+"**", inline=True)
            Pure.add_field(name="HP IV Purified:", value="**"+str(SIVA)+"**", inline= True)
            Pure.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send(embed=Pure)
        else:
            await ctx.send("This shadow pokemon doesn't exist... yet... Ţ̸̧̖̘̒͐͌e̷̳͕͋a̸̗̫̓ḿ̷̡͙̱̊̚ ̵̘̖̼̪̦̟̏̂̀̓͌͘͝R̴̨̨͈̰̼̳̜̓̈̓o̷͙͠c̶͔̼̀̍̄̃̔͝ķ̸̦̜͚͂̅̀e̶̡̢̡̘̜̒̕t̷͎̼̙̀͌̊̂̕̚", delete_after=5)

    @commands.command()
    async def gopvp(self, ctx):
        responce = str(ctx.message.content)
        content = responce.split()
        isshiny = "Normal"
        name = content[1]
        if name.endswith("*"):
            isshiny = "Shiny"
            name = name.replace("*", "")
        if name == "Farfetch’d" or name == "farfetch’d":
                name = "farfetch'd"
        Cname = name.capitalize()
        if Cname == "Alolan":
            name = content[2]
            Cname = name.capitalize()
            if Cname.endswith("*"):
                isshiny = "Shiny"
                Cname = Cname.replace("*", "")
                name = name.replace("*", "")
            ylvl = float(content[3])
            AIV = int(content[4])
            DIV = int(content[5])
            SIV = int(content[6])
            # msg = await ctx.send("Loading please wait...")
            results = await AlolanMaintoGo(self,name,ylvl,AIV,DIV,SIV)
            if results == None:
                await ctx.send("This Pokemon does not exist")
            else:
                # await msg.edit(content="Calculation complete please wait...")
                # await msg.delete()
                YPKM = results[0]
                GPKM = results[1]
                UPKM = results[2]
                MPKM = results[3]
                GP = round(((YPKM[2] / GPKM[2])*100),2)
                if GP > 100.00:
                    GP = "~~"+str(GP)+"~~"
                    UP = round(((YPKM[2] / UPKM[2])*100),2)
                    if UP > 100.00:
                        UP = "~~"+str(UP)+"~~"
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= "Alolan " + Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Alolan/"+str(isshiny)+"/"+Cname+".png")
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.send(embed=embed)
                    else:
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= "Alolan " + Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Alolan/"+str(isshiny)+"/"+Cname+".png")
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.send(embed=embed)
                else:
                    UP = round(((YPKM[2] / UPKM[2])*100),2)
                    if UP > 100.00:
                        UP = "~~"+str(UP)+"~~"
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= "Alolan " + Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Alolan/"+str(isshiny)+"/"+Cname+".png")
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.send(embed=embed)
                    else:
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= "Alolan " + Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Alolan/"+str(isshiny)+"/"+Cname+".png")
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.send(embed=embed)
        elif Cname == "Galarian":
            name = content[2]
            if name.endswith("*"):
                isshiny = "Shiny"
                name = Cname.replace("*", "")
            if name.lower().startswith("mr"):
                if content[3].endswith("*"):
                    isshiny = "Shiny"
                    content[3] = content[3].replace("*", "")
                name = "mrmime"
            if name == "Farfetch’d" or name == "farfetch’d":
                name = "farfetch'd"
            Cname = name.capitalize()
            if Cname == "Mrmime":
                ylvl = float(content[4])
                AIV = int(content[5])
                DIV = int(content[6])
                SIV = int(content[7])
            if Cname != "Mrmime":
                ylvl = float(content[3])
                AIV = int(content[4])
                DIV = int(content[5])
                SIV = int(content[6])
            # msg = await ctx.send("Loading please wait...")
            results = await GalarianMaintoGo(self,name,ylvl,AIV,DIV,SIV)
            if results == None:
                await ctx.send("This Pokemon does not exist")
            else:
                # await msg.edit(content="Calculation complete please wait...")
                # await msg.delete()
                YPKM = results[0]
                GPKM = results[1]
                UPKM = results[2]
                MPKM = results[3]
                if name == "Mrmime":
                    name = "Mr. Mime"
                if Cname == "Farfetch'd":
                    Cname = "Farfetchd"
                GP = round(((YPKM[2] / GPKM[2])*100),2)
                if GP > 100.00:
                    GP = "~~"+str(GP)+"~~"
                    UP = round(((YPKM[2] / UPKM[2])*100),2)
                    if UP > 100.00:
                        UP = "~~"+str(UP)+"~~"
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= "Galarian " + name.capitalize() + "'s PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+Cname+".png")
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.send(embed=embed)
                    else:
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= "Galarian " + name.capitalize() + "'s PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+Cname+".png")
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.send(embed=embed)
                else:
                    UP = round(((YPKM[2] / UPKM[2])*100),2)
                    if UP > 100.00:
                        UP = "~~"+str(UP)+"~~"
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= "Galarian " + name.capitalize() + "'s PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+Cname+".png")
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.send(embed=embed)
                    else:
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= "Galarian " + name.capitalize() + "'s PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+Cname+".png")
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.send(embed=embed)
        elif Cname == "Mega":
            name = content[2]
            Mname = name.capitalize()
            if Mname.endswith("*"):
                isshiny = "Shiny"
                Mname = Cname.replace("*", "")
            if Mname == "Charizard" or Mname == "Mewtwo":
                if content[3].capitalize() == "X":
                    if content[3].endswith("*"):
                        isshiny = "Shiny"
                        content[3] = content[3].replace("*", "")
                    if Mname == "Charizard":
                        Mname = "Xcharizard"
                        ylvl = float(content[4])
                        AIV = int(content[5])
                        DIV = int(content[6])
                        SIV = int(content[7])
                        results = await MegaMaintoGo(self,Mname,ylvl,AIV,DIV,SIV)
                        if results == None:
                            await ctx.send("This Pokemon does not exist")
                        else:
                            YPKM = results[0]
                            GPKM = results[1]
                            UPKM = results[2]
                            MPKM = results[3]
                            GP = round(((YPKM[2] / GPKM[2])*100),2)
                            if GP > 100.00:
                                GP = "~~"+str(GP)+"~~"
                                UP = round(((YPKM[2] / UPKM[2])*100),2)
                                if UP > 100.00:
                                    UP = "~~"+str(UP)+"~~"
                                    MP = round(((YPKM[2] / MPKM[2])*100),2)
                                    embed = discord.Embed(title= "Mega Charizard X's PvP Comparison" , description="", color=0x2962FF)
                                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/Xcharizard.png")
                                    embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                    await ctx.send(embed=embed)
                                else:
                                    MP = round(((YPKM[2] / MPKM[2])*100),2)
                                    embed = discord.Embed(title= "Mega Charizard X's PvP Comparison"  , description="", color=0x2962FF)
                                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/Xcharizard.png")
                                    embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                    await ctx.send(embed=embed)
                            else:
                                UP = round(((YPKM[2] / UPKM[2])*100),2)
                                if UP > 100.00:
                                    UP = "~~"+str(UP)+"~~"
                                    MP = round(((YPKM[2] / MPKM[2])*100),2)
                                    embed = discord.Embed(title= "Mega Charizard X's PvP Comparison"  , description="", color=0x2962FF)
                                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/Xcharizard.png")
                                    embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                    await ctx.send(embed=embed)
                                else:
                                    MP = round(((YPKM[2] / MPKM[2])*100),2)
                                    embed = discord.Embed(title= "Mega Charizard X's PvP Comparison"  , description="", color=0x2962FF)
                                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/Xcharizard.png")
                                    embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                    await ctx.send(embed=embed)
                    elif Mname == "Mewtwo":
                        Mname = "Xmewtwo"
                        ylvl = float(content[4])
                        AIV = int(content[5])
                        DIV = int(content[6])
                        SIV = int(content[7])
                        results = await MegaMaintoGo(self,Mname,ylvl,AIV,DIV,SIV)
                        if results == None:
                            await ctx.send("This Pokemon does not exist")
                        else:
                            YPKM = results[0]
                            UPKM = results[2]
                            MPKM = results[3]
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            UP = round(((YPKM[2] / UPKM[2])*100),2)
                            if UP > 100.00:
                                UP = "~~"+str(UP)+"~~"
                                embed = discord.Embed(title= "Mega Mewtwo X's PvP Comparison"  , description="", color=0x2962FF)
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(ishiny)+"/Xmewtwo.png")
                                embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                                embed.add_field(name="\u200B", value="\u200B", inline=True)
                                embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                                embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                await ctx.send(embed=embed)
                            else:
                                embed = discord.Embed(title= "Mega Mewtwo X's PvP Comparison"  , description="", color=0x2962FF)
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/Xmewtwo.png")
                                embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                                embed.add_field(name="\u200B", value="\u200B", inline=True)
                                embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                                embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                await ctx.send(embed=embed)
                elif content[3].capitalize() == "Y":
                    if content[3].endswith("*"):
                        isshiny = "Shiny"
                        content[3] = content[3].replace("*", "")
                    if Mname == "Charizard":
                        Mname = "Ycharizard"
                        ylvl = float(content[4])
                        AIV = int(content[5])
                        DIV = int(content[6])
                        SIV = int(content[7])
                        results = await MegaMaintoGo(self,Mname,ylvl,AIV,DIV,SIV)
                        if results == None:
                            await ctx.send("This Pokemon does not exist")
                        else:
                            YPKM = results[0]
                            GPKM = results[1]
                            UPKM = results[2]
                            MPKM = results[3]
                            GP = round(((YPKM[2] / GPKM[2])*100),2)
                            if GP > 100.00:
                                GP = "~~"+str(GP)+"~~"
                                UP = round(((YPKM[2] / UPKM[2])*100),2)
                                if UP > 100.00:
                                    UP = "~~"+str(UP)+"~~"
                                    MP = round(((YPKM[2] / MPKM[2])*100),2)
                                    embed = discord.Embed(title= "Mega Charizard Y's PvP Comparison" , description="", color=0x2962FF)
                                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/Ycharizard.png")
                                    embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                    await ctx.send(embed=embed)
                                else:
                                    MP = round(((YPKM[2] / MPKM[2])*100),2)
                                    embed = discord.Embed(title= "Mega Charizard Y's PvP Comparison" , description="", color=0x2962FF)
                                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/Ycharizard.png")
                                    embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                    await ctx.send(embed=embed)
                            else:
                                UP = round(((YPKM[2] / UPKM[2])*100),2)
                                if UP > 100.00:
                                    UP = "~~"+str(UP)+"~~"
                                    MP = round(((YPKM[2] / MPKM[2])*100),2)
                                    embed = discord.Embed(title= "Mega Charizard Y's PvP Comparison" , description="", color=0x2962FF)
                                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/CharizardY.png")

                                    embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                    await ctx.send(embed=embed)
                                else:
                                    MP = round(((YPKM[2] / MPKM[2])*100),2)
                                    embed = discord.Embed(title= "Mega Charizard Y's PvP Comparison" , description="", color=0x2962FF)
                                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/CharizardY.png")
                                    embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                    await ctx.send(embed=embed)
                    elif Mname == "Mewtwo":
                        Mname = "Ymewtwo"
                        ylvl = float(content[4])
                        AIV = int(content[5])
                        DIV = int(content[6])
                        SIV = int(content[7])
                        results = await MegaMaintoGo(self,Mname,ylvl,AIV,DIV,SIV)
                        if results == None:
                            await ctx.send("This Pokemon does not exist")
                        else:
                            YPKM = results[0]
                            UPKM = results[2]
                            MPKM = results[3]
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            UP = round(((YPKM[2] / UPKM[2])*100),2)
                            if UP > 100.00:
                                UP = "~~"+str(UP)+"~~"
                                embed = discord.Embed(title= "Mega Mewtwo Y's PvP Comparison"  , description="", color=0x2962FF)
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/Ymewtwo.png")
                                embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                                embed.add_field(name="\u200B", value="\u200B", inline=True)
                                embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                                embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                await ctx.send(embed=embed)
                            else:
                                embed = discord.Embed(title= "Mega Mewtwo Y's PvP Comparison"  , description="", color=0x2962FF)
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/Ymewtwo.png")
                                embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                                embed.add_field(name="\u200B", value="\u200B", inline=True)
                                embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                                embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                await ctx.send(embed=embed)
            if Mname == "Gyarados" or Mname == "Heracross" or Mname == "Tyranitar" or Mname == "Salamence" or Mname == "Metagross" or Mname == "Latias" or Mname == "Latios" or Mname == "Rayquaza" or Mname == "Garchomp":
                ylvl = float(content[3])
                AIV = int(content[4])
                DIV = int(content[5])
                SIV = int(content[6])
                results = await MegaMaintoGo(self,Mname,ylvl,AIV,DIV,SIV)
                if results == None:
                    await ctx.send("This Pokemon does not exist")
                else:
                    YPKM = results[0]
                    UPKM = results[2]
                    MPKM = results[3]
                    MP = round(((YPKM[2] / MPKM[2])*100),2)
                    UP = round(((YPKM[2] / UPKM[2])*100),2)
                    if UP > 100.00:
                        UP = "~~"+str(UP)+"~~"
                        embed = discord.Embed(title= "Mega "+ Mname +"'s PvP Comparison"  , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/"+Mname+".png")
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                        embed.add_field(name="\u200B", value="\u200B", inline=True)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(title= "Mega "+ Mname +"'s PvP Comparison"  , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/"+Mname+".png")
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                        embed.add_field(name="\u200B", value="\u200B", inline=True)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.send(embed=embed)
            elif Mname != "Charizard" and Mname != "Mewtwo" and content[3] != "x" and content[3] != "y":
                ylvl = float(content[3])
                AIV = int(content[4])
                DIV = int(content[5])
                SIV = int(content[6])
                results = await MegaMaintoGo(self,Mname,ylvl,AIV,DIV,SIV)
                if results == 0:
                    await ctx.send("This Pokemon does not exist")
                else:
                    YPKM = results[0]
                    GPKM = results[1]
                    UPKM = results[2]
                    MPKM = results[3]
                    GP = round(((YPKM[2] / GPKM[2])*100),2)
                    if GP > 100.00:
                        GP = "~~"+str(GP)+"~~"
                        UP = round(((YPKM[2] / UPKM[2])*100),2)
                        if UP > 100.00:
                            UP = "~~"+str(UP)+"~~"
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= "Mega " + Mname + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/"+Mname+".png")
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.send(embed=embed)
                        else:
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= "Mega " + Mname + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/"+Mname+".png")
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.send(embed=embed)
                    else:
                        UP = round(((YPKM[2] / UPKM[2])*100),2)
                        if UP > 100.00:
                            UP = "~~"+str(UP)+"~~"
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= "Mega " + Mname + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/"+Mname+".png")
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.send(embed=embed)
                        else:
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= "Mega " + Mname + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/"+Mname+".png")
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.send(embed=embed)
        elif Cname == "Armored":
            if content[2] == "Mewtwo" or content[2] == "mewtwo":
                Aname = "Armoredmewtwo"
                name = content[2]
                Cname = name.capitalize()
                ylvl = float(content[3])
                AIV = int(content[4])
                DIV = int(content[5])
                SIV = int(content[6])
                # msg = await ctx.send("Loading please wait...")
                results = await MaintoGo(self,Aname,ylvl,AIV,DIV,SIV)
                # await msg.edit(content="Calculation complete please wait...")
                # await msg.delete()
                YPKM = results[0]
                GPKM = results[1]
                UPKM = results[2]
                MPKM = results[3]
                GP = round(((YPKM[2] / GPKM[2])*100),2)
                if GP > 100.00:
                    GP = "~~"+str(GP)+"~~"
                    UP = round(((YPKM[2] / UPKM[2])*100),2)
                    if UP > 100.00:
                        UP = "~~"+str(UP)+"~~"
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= "Armored " + Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Aname+".png")
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.send(embed=embed)
                    else:
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= "Armored " + Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Aname+".png")
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.send(embed=embed)
                else:
                    UP = round(((YPKM[2] / UPKM[2])*100),2)
                    if UP > 100.00:
                        UP = "~~"+str(UP)+"~~"
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= "Armored " + Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Aname+".png")
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.send(embed=embed)
                    else:
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= "Armored " + Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Aname+".png")
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.send(embed=embed)
            else:
                await ctx.send("Only Armored Mewtwo exists...     Ţ̸̧̖̘̒͐͌e̷̳͕͋a̸̗̫̓ḿ̷̡͙̱̊̚ ̵̘̖̼̪̦̟̏̂̀̓͌͘͝R̴̨̨͈̰̼̳̜̓̈̓o̷͙͠c̶͔̼̀̍̄̃̔͝ķ̸̦̜͚͂̅̀e̶̡̢̡̘̜̒̕t̷͎̼̙̀͌̊̂̕̚")
        elif Cname == "Origin":
            if content[2] == "Giratina" or content[2] == "giratina":
                Aname = "Origingiratina"
                name = content[2]
                Cname = name.capitalize()
                ylvl = float(content[3])
                AIV = int(content[4])
                DIV = int(content[5])
                SIV = int(content[6])
                # msg = await ctx.send("Loading please wait...")
                results = await MaintoGo(self,Aname,ylvl,AIV,DIV,SIV)
                # await msg.edit(content="Calculation complete please wait...")
                # await msg.delete()
                YPKM = results[0]
                GPKM = results[1]
                UPKM = results[2]
                MPKM = results[3]
                GP = round(((YPKM[2] / GPKM[2])*100),2)
                if GP > 100.00:
                    GP = "~~"+str(GP)+"~~"
                    UP = round(((YPKM[2] / UPKM[2])*100),2)
                    if UP > 100.00:
                        UP = "~~"+str(UP)+"~~"
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= Cname + " Origin Forme's PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Ogiratina.png")

                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.send(embed=embed)
                    else:
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= Cname + " Origin Forme's PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Ogiratina.png")

                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.send(embed=embed)
                else:
                    UP = round(((YPKM[2] / UPKM[2])*100),2)
                    if UP > 100.00:
                        UP = "~~"+str(UP)+"~~"
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= Cname + " Origin Forme's PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Ogiratina.png")

                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.send(embed=embed)
                    else:
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= Cname + " Origin Forme's PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Ogiratina.png")

                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.send(embed=embed)
            else:
                await ctx.send("Only Origin Giratina exists...")
        elif Cname == "Attack":
            Aname = "Adeoxys"
            name = content[2]
            Cname = name.capitalize()
            ylvl = float(content[3])
            AIV = int(content[4])
            DIV = int(content[5])
            SIV = int(content[6])
            # msg = await ctx.send("Loading please wait...")
            results = await MaintoGo(self,Aname,ylvl,AIV,DIV,SIV)
            # await msg.edit(content="Calculation complete please wait...")
            # await msg.delete()
            YPKM = results[0]
            GPKM = results[1]
            UPKM = results[2]
            MPKM = results[3]
            GP = round(((YPKM[2] / GPKM[2])*100),2)
            if GP > 100.00:
                GP = "~~"+str(GP)+"~~"
                UP = round(((YPKM[2] / UPKM[2])*100),2)
                if UP > 100.00:
                    UP = "~~"+str(UP)+"~~"
                    MP = round(((YPKM[2] / MPKM[2])*100),2)
                    embed = discord.Embed(title= Cname + " Attack Forme's PvP Comparison" , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Adeoxys.png")

                    embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                else:
                    MP = round(((YPKM[2] / MPKM[2])*100),2)
                    embed = discord.Embed(title= Cname + " Attack Forme's PvP Comparison" , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Adeoxys.png")

                    embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
            else:
                UP = round(((YPKM[2] / UPKM[2])*100),2)
                if UP > 100.00:
                    UP = "~~"+str(UP)+"~~"
                    MP = round(((YPKM[2] / MPKM[2])*100),2)
                    embed = discord.Embed(title= Cname + " Attack Forme's PvP Comparison" , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Adeoxys.png")

                    embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                else:
                    MP = round(((YPKM[2] / MPKM[2])*100),2)
                    embed = discord.Embed(title= Cname + " Attack Forme's PvP Comparison" , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Adeoxys.png")

                    embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
        elif Cname == "Defense":
            Aname = "Ddeoxys"
            name = content[2]
            Cname = name.capitalize()
            ylvl = float(content[3])
            AIV = int(content[4])
            DIV = int(content[5])
            SIV = int(content[6])
            # msg = await ctx.send("Loading please wait...")
            results = await MaintoGo(self,Aname,ylvl,AIV,DIV,SIV)
            # await msg.edit(content="Calculation complete please wait...")
            # await msg.delete()
            YPKM = results[0]
            GPKM = results[1]
            UPKM = results[2]
            MPKM = results[3]
            GP = round(((YPKM[2] / GPKM[2])*100),2)
            if GP > 100.00:
                GP = "~~"+str(GP)+"~~"
                UP = round(((YPKM[2] / UPKM[2])*100),2)
                if UP > 100.00:
                    UP = "~~"+str(UP)+"~~"
                    MP = round(((YPKM[2] / MPKM[2])*100),2)
                    embed = discord.Embed(title= Cname + " Defense Forme's PvP Comparison" , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Ddeoxys.png")

                    embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                else:
                    MP = round(((YPKM[2] / MPKM[2])*100),2)
                    embed = discord.Embed(title= Cname + " Defense Forme's PvP Comparison" , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Ddeoxys.png")

                    embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
            else:
                UP = round(((YPKM[2] / UPKM[2])*100),2)
                if UP > 100.00:
                    UP = "~~"+str(UP)+"~~"
                    MP = round(((YPKM[2] / MPKM[2])*100),2)
                    embed = discord.Embed(title= Cname + " Defense Forme's PvP Comparison" , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Ddeoxys.png")

                    embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                else:
                    MP = round(((YPKM[2] / MPKM[2])*100),2)
                    embed = discord.Embed(title= Cname + " Defense Forme's PvP Comparison" , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Ddeoxys.png")

                    embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
        elif Cname == "Speed":
            Aname = "Sdeoxys"
            name = content[2]
            Cname = name.capitalize()
            ylvl = float(content[3])
            AIV = int(content[4])
            DIV = int(content[5])
            SIV = int(content[6])
            # msg = await ctx.send("Loading please wait...")
            results = await MaintoGo(self,Aname,ylvl,AIV,DIV,SIV)
            # await msg.edit(content="Calculation complete please wait...")
            # await msg.delete()
            YPKM = results[0]
            GPKM = results[1]
            UPKM = results[2]
            MPKM = results[3]
            GP = round(((YPKM[2] / GPKM[2])*100),2)
            if GP > 100.00:
                GP = "~~"+str(GP)+"~~"
                UP = round(((YPKM[2] / UPKM[2])*100),2)
                if UP > 100.00:
                    UP = "~~"+str(UP)+"~~"
                    MP = round(((YPKM[2] / MPKM[2])*100),2)
                    embed = discord.Embed(title= Cname + " Speed Forme's PvP Comparison" , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Sdeoxys.png")

                    embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                else:
                    MP = round(((YPKM[2] / MPKM[2])*100),2)
                    embed = discord.Embed(title= Cname + " Speed Forme's PvP Comparison" , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Sdeoxys.png")

                    embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
            else:
                UP = round(((YPKM[2] / UPKM[2])*100),2)
                if UP > 100.00:
                    UP = "~~"+str(UP)+"~~"
                    MP = round(((YPKM[2] / MPKM[2])*100),2)
                    embed = discord.Embed(title= Cname + " Speed Forme's PvP Comparison" , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Sdeoxys.png")

                    embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                else:
                    MP = round(((YPKM[2] / MPKM[2])*100),2)
                    embed = discord.Embed(title= Cname + " Speed Forme's PvP Comparison" , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Sdeoxys.png")

                    embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
        elif Cname != "Galarian":
            name = content[1]
            if name.endswith("*"):
                isshiny = "Shiny"
                name = name.replace("*", "")
            if name == "Farfetch’d" or name == "farfetch’d":
                name = "farfetch'd"
            if name == "Mr" or name == "mr" or name == "Mr." or name == "mr.":
                if content[2].endswith("*"):
                    isshiny = "Shiny"
                    content[2] = content[2].replace("*", "")
                if content[2].lower() == "mime":
                    name = "mrmime"
                if content[2].lower() == "rime":
                    name = "mrrime"
                
                Cname = name.capitalize()
                if Cname =="Mr" or Cname =="Mr.":
                    if content[2].lower() == "mime":
                        Cname = "Mrmime"
                    elif content[2] == "rime":
                        Cname = "Mrrime"
                Cname = name.capitalize()
                ylvl = float(content[3])
                AIV = int(content[4])
                DIV = int(content[5])
                SIV = int(content[6])
                results = await MaintoGo(self,name,ylvl,AIV,DIV,SIV)
                if name == "mrmime":
                    name = "Mr. Mime"
                if name == "mrrime":
                    name = "Mr. Rime"
                if results == None:
                    await ctx.send("This Pokemon does not exist")
                else:
                    YPKM = results[0]
                    GPKM = results[1]
                    UPKM = results[2]
                    MPKM = results[3]
                    GP = round(((YPKM[2] / GPKM[2])*100),2)
                    if GP > 100.00:
                        GP = "~~"+str(GP)+"~~"
                        UP = round(((YPKM[2] / UPKM[2])*100),2)
                        if UP > 100.00:
                            UP = "~~"+str(UP)+"~~"
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= name + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Cname+".png")

                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.send(embed=embed)
                        else:
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= name + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Cname+".png")

                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.send(embed=embed)
                    else:
                        UP = round(((YPKM[2] / UPKM[2])*100),2)
                        if UP > 100.00:
                            UP = "~~"+str(UP)+"~~"
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= name + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Cname+".png")

                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.send(embed=embed)
                        else:
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= name + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Cname+".png")

                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.send(embed=embed)
            else:
                Cname = name.capitalize()
                ylvl = float(content[2])
                AIV = int(content[3])
                DIV = int(content[4])
                SIV = int(content[5])
                results = await MaintoGo(self,name,ylvl,AIV,DIV,SIV)
                if results == None:
                    await ctx.send("This Pokemon does not exist")
                else:
                    YPKM = results[0]
                    GPKM = results[1]
                    UPKM = results[2]
                    MPKM = results[3]
                    GP = round(((YPKM[2] / GPKM[2])*100),2)
                    if GP > 100.00:
                        GP = "~~"+str(GP)+"~~"
                        UP = round(((YPKM[2] / UPKM[2])*100),2)
                        if UP > 100.00:
                            UP = "~~"+str(UP)+"~~"
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= name.capitalize() + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Cname+".png")
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.send(embed=embed)
                        else:
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= name.capitalize() + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Cname+".png")
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.send(embed=embed)
                    else:
                        UP = round(((YPKM[2] / UPKM[2])*100),2)
                        if UP > 100.00:
                            UP = "~~"+str(UP)+"~~"
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= name.capitalize() + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Cname+".png")
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.send(embed=embed)
                        else:
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= name.capitalize() + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Cname+".png")
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=True)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=True)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=True)
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% Great League: **"+str(GP)+"%**\nPVP% Ultra League: **"+str(UP)+"%**\n PVP% Master League: **"+str(MP)+"%**\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=True)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.send(embed=embed)

    @commands.command()
    async def gotohome(self, ctx):
        responce = str(ctx.message.content)
        content = responce.split()
        isshiny = "Normal"
        Name = string.capwords(content[1])
        if Name.endswith("*"):
            isshiny = "Shiny"
            Name = Name.replace("*", "")
        namea = "Alolan"
        namegl = "Galarian"
        if Name == namea:
            GaName = string.capwords(content[2])
            if GaName.endswith("*"):
                isshiny = "Shiny"
                GaName = GaName.replace("*", "")
            Listofalola = ["Rattata","Raticate","Raichu","Sandshrew","Sandslash","Vulpix","Ninetails","Diglett","Dugtrio","Meowth","Persian","Geodude","Graveler",
                           "Golem","Grimer","Muk","Exeggutor","Marowak"]
            if GaName in Listofalola:
                result = await gotohomeAlolan(self, str(GaName))
                Level = int(float(content[3]))
                if Level > 50:
                        await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 50",delete_after=10)
                        Level = 50
                GOATK = int(content[4])
                GODEF = int(content[5])
                GOHP  = int(content[6])
                TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                embed = discord.Embed(title= "Alolan "+str(GaName)+"'s Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Alolan/"+str(isshiny)+"/"+GaName+".png")
                embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            else:
                await ctx.send('This Alolan Pokémon does not exist')
        elif Name == namegl:
            if content[2].endswith("*"):
                isshiny = "Shiny"
                content[2] = content[2].replace("*", "")
            GlName = string.capwords(content[2])
            GlmName = string.capwords(content[2]) + " Mime"
            Listofgalar = ["Meowth","Ponyta","Rapidash","Slowpoke","Slowbro","Farfetch'd","Farfetch’d","Weezing","Mr Mime","Mr. Mime","Articuno","Zapdos","Moltres","Slowking","Corsola","Zigzagoon","Linoone","Darumaka",
                           "Darmanitan","Yamask","Stunfisk"]
            if GlName in Listofgalar or GlmName in Listofgalar:
                    if GlName== "Darmanitan":
                        result = await GotohomeGalar(self, str(GlName))
                        Level = int(float(content[3]))
                        if Level > 50:
                            await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 50",delete_after=10)
                            Level = 50
                        GOATK = int(content[4])
                        GODEF = int(content[5])
                        GOHP  = int(content[6])
                        TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                        TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                        TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                        TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                        TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                        TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                        TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                        TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                        TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                        TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                        TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                        TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                        TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                        TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                        TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                        TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                        TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                        embed = discord.Embed(title= "Galarian "+str(GlName)+"'s Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+GlName+".png")
                        embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                        embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                        embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                        embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                        await ctx.send(embed=embed)
                    if GlName == "Mr" or GlName == "Mr.":
                        if content[3].endswith("*"):
                            isshiny = "Shiny"
                            content[3] = content[3].replace("*", "")
                        if content[3].lower() == "mime":
                            GlName = "Mr. Mime"
                            GlmName = "Mrmime"
                        result = await GotohomeGalar(self, str(GlmName))
                        Level = int(float(content[4]))
                        if Level > 50:
                            await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 40",delete_after=10)
                            Level = 50
                        GOATK = int(content[5])
                        GODEF = int(content[6])
                        GOHP  = int(content[7])
                        TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                        TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                        TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                        TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                        TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                        TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                        TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                        TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                        TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                        TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                        TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                        TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                        TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                        TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                        TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                        TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                        TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                        embed = discord.Embed(title= "Galarian "+str(GlName)+"'s Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+GlmName+".png")
                        embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                        embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                        embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                        embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                        await ctx.send(embed=embed)
                        
                    if GlName != "Mr Mime" and GlName != "Mr. Mime":
                        result = await GotohomeGalar(self, str(GlName))
                        if GlName == "Farfetch'd" or GlName == "Farfetch’d":
                            w = "Farfetchd"
                            Level = int(float(content[3]))
                            if Level > 50:
                                await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 50",delete_after=10)
                                Level = 50
                            GOATK = int(content[4])
                            GODEF = int(content[5])
                            GOHP  = int(content[6])
                            TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                            TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                            TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                            TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                            TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                            TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                            TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                            TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                            TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                            TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                            TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                            TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                            TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                            TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                            TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                            TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                            TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                            embed = discord.Embed(title= "Galarian "+str(GlName)+"'s Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+str(w)+".png")
                            embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                            embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                            embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                            embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            candelete = await get_delete(self, ctx)
                            if candelete == "True":
                                await ctx.message.delete()
                            await ctx.send(embed=embed)
                        else:
                            Level = int(float(content[3]))
                            if Level > 50:
                                await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 50",delete_after=10)
                                Level = 50
                            GOATK = int(content[4])
                            GODEF = int(content[5])
                            GOHP  = int(content[6])
                            TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                            TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                            TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                            TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                            TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                            TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                            TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                            TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                            TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                            TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                            TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                            TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                            TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                            TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                            TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                            TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                            TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                            embed = discord.Embed(title= "Galarian "+str(GlName)+"'s Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+GlName+".png")
                            embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                            embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                            embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                            embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            candelete = await get_delete(self, ctx)
                            if candelete == "True":
                                await ctx.message.delete()
                            await ctx.send(embed=embed)
            else:
                await ctx.send('This Galarian Pokémon does not exist!')
        elif Name != namegl:
            if Name == "Mr" or Name == "Mr.":
                if content[2].endswith("*"):
                    isshiny = "Shiny"
                    content[2] = content[2].replace("*", "")
                if content[2] == "mime" or content[2] =="Mime":
                    RName = "Mrmime"
                    result = gotohome(str(RName))
                    Level = int(float(content[3]))
                    if Level > 40:
                        await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 40",delete_after=10)
                        Level = 40
                    GOATK = int(content[4])
                    GODEF = int(content[5])
                    GOHP  = int(content[6])
                    TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                    TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                    TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                    TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                    TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                    TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                    TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                    TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                    TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                    TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                    TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                    TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                    TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                    TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                    TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                    TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                    TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                    embed = discord.Embed(title= "Mr. Mime's Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+RName+".png")
                    embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                    embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                    embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                    embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                #elif content[2] == 'rime':
                #    RRName = "Mrrime"
                #    result = pokedex(str(RRName))
            elif Name == "Mime":
                if content[2].endswith("*"):
                    isshiny = "Shiny"
                    content[2] = content[2].replace("*", "")
                RName = "Mimejr"
                result = gotohome(str(RName))
                Level = int(float(content[3]))
                if Level > 50:
                    await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 50",delete_after=10)
                    Level = 50
                GOATK = int(content[4])
                GODEF = int(content[5])
                GOHP  = int(content[6])
                TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                embed = discord.Embed(title=  "Mime Jr's Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+RName+".png")
                embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name.startswith("Nidoran\U00002640"):
                Name = "Nidoranf"
                result = await gotohome(self, str(Name))
                Level = int(float(content[2]))
                if Level > 50:
                    await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 50",delete_after=10)
                    Level = 50
                GOATK = int(content[3])
                GODEF = int(content[4])
                GOHP  = int(content[5])
                TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                embed = discord.Embed(title=  "Nidoran\U00002640's Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name.startswith("Nidoran\U00002642"):
                Name = "Nidoranm"
                result = await gotohome(self, str(Name))
                Level = int(float(content[2]))
                if Level > 50:
                    await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 50",delete_after=10)
                    Level = 50
                GOATK = int(content[3])
                GODEF = int(content[4])
                GOHP  = int(content[5])
                TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                embed = discord.Embed(title=  "Nidoran\U00002642's Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name== "Darmanitan":
                result = await gotohome(self, str(Name))
                Level = int(float(content[2]))
                if Level > 50:
                        await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 50",delete_after=10)
                        Level = 50
                GOATK = int(content[3])
                GODEF = int(content[4])
                GOHP  = int(content[5])
                TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                embed = discord.Embed(title=  Name + "'s Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Wormadam":
                result = await gotohome(self, str(Name))
                Level = int(float(content[2]))
                if Level > 50:
                        await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 50",delete_after=10)
                        Level = 50
                GOATK = int(content[3])
                GODEF = int(content[4])
                GOHP  = int(content[5])
                TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                embed = discord.Embed(title=  Name + "'s Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Kyogre":
                result = await gotohome(self, str(Name))
                Level = int(float(content[2]))
                if Level > 50:
                        await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 50",delete_after=10)
                        Level = 50
                GOATK = int(content[3])
                GODEF = int(content[4])
                GOHP  = int(content[5])
                TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                embed = discord.Embed(title=  Name + "'s Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Groudon":
                result = await gotohome(self, str(Name))
                Level = int(float(content[2]))
                if Level > 50:
                        await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 50",delete_after=10)
                        Level = 50
                GOATK = int(content[3])
                GODEF = int(content[4])
                GOHP  = int(content[5])
                TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                embed = discord.Embed(title=  Name + "'s Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Deoxys":
                result = await gotohome(self, str(Name))
                Level = int(float(content[2]))
                if Level > 50:
                        await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 50",delete_after=10)
                        Level = 50
                GOATK = int(content[3])
                GODEF = int(content[4])
                GOHP  = int(content[5])
                TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                embed = discord.Embed(title=  Name + "'s Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Attack":
                if content[2].endswith("*"):
                    isshiny = "Shiny"
                    content[2] = content[2].replace("*", "")
                GzzName = "Adeoxys"
                result = gotohome(str(GzzName))
                Level = int(float(content[3]))
                if Level > 50:
                        await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 50",delete_after=10)
                        Level = 50
                GOATK = int(content[4])
                GODEF = int(content[5])
                GOHP  = int(content[6])
                TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                embed = discord.Embed(title=  Name + " Deoxys's Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Defense":
                if content[2].endswith("*"):
                    isshiny = "Shiny"
                    content[2] = content[2].replace("*", "")
                GzzzName = "Ddeoxys"
                result = gotohome(str(GzzzName))
                Level = int(float(content[3]))
                if Level > 50:
                        await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 50",delete_after=10)
                        Level = 50
                GOATK = int(content[4])
                GODEF = int(content[5])
                GOHP  = int(content[6])
                TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                embed = discord.Embed(title=  Name + " Deoxys's Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Speed":
                if content[2].endswith("*"):
                    isshiny = "Shiny"
                    content[2] = content[2].replace("*", "")
                GzzzzName = "Sdeoxys"
                result = gotohome(str(GzzzzName))
                Level = int(float(content[3]))
                if Level > 50:
                        await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 50",delete_after=10)
                        Level = 50
                GOATK = int(content[4])
                GODEF = int(content[5])
                GOHP  = int(content[6])
                TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                embed = discord.Embed(title=  Name + " Deoxys's Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Rotom":
                result = pokedex(str(Name))
            elif Name == "Heat":
                GzzName = "Hrotom"
                result = pokedex(str(GzzName))
            elif Name == "Wash":
                GzzzName = "Wrotom"
                result = pokedex(str(GzzzName))
            elif Name == "Frost":
                GzzzzName = "Frotom"
                result = pokedex(str(GzzzzName))
            elif Name == "Fan":
                GzzzzzName = "Fanrotom"
                result = pokedex(str(GzzzzzName))
            elif Name == "Motor":
                GzzzzzzName = "Mrotom"
                result = pokedex(str(GzzzzzzName))
            elif Name == "Giratina":
                result = await gotohome(self, str(Name))
                Level = int(float(content[2]))
                if Level > 50:
                        await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 50",delete_after=10)
                        Level = 50
                GOATK = int(content[3])
                GODEF = int(content[4])
                GOHP  = int(content[5])
                TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                embed = discord.Embed(title=  Name + "'s Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Origin":
                if content[2].endswith("*"):
                    isshiny = "Shiny"
                    content[2] = content[2].replace("*", "")
                GzzName = "Ogiratina"
                result = gotohome(str(GzzName))
                Level = int(float(content[3]))
                if Level > 50:
                    await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 40",delete_after=10)
                    Level = 50
                GOATK = int(content[4])
                GODEF = int(content[5])
                GOHP  = int(content[6])
                TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                embed = discord.Embed(title=  Name + " Giratina's Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Tornadus":
                result = await gotohome(self, str(Name))
                Level = int(float(content[2]))
                if Level > 50:
                        await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 50",delete_after=10)
                        Level = 50
                GOATK = int(content[3])
                GODEF = int(content[4])
                GOHP  = int(content[5])
                TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                embed = discord.Embed(title=  Name + "'s Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
                #GzzName = "Ttornadus"
                #result = pokedex(str(GzzName))
            elif Name == "Thundurus":
                result = await gotohome(self, str(Name))
                Level = int(float(content[2]))
                if Level > 50:
                        await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 50",delete_after=10)
                        Level = 50
                GOATK = int(content[3])
                GODEF = int(content[4])
                GOHP  = int(content[5])
                TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                embed = discord.Embed(title=  Name + "'s Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
                #GzzName = "Tthundurus"
                #result = pokedex(str(GzzName))
            elif Name == "Landorus":
                result = await gotohome(self, str(Name))
                Level = int(float(content[2]))
                if Level > 50:
                        await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 50",delete_after=10)
                        Level = 50
                GOATK = int(content[3])
                GODEF = int(content[4])
                GOHP  = int(content[5])
                TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                embed = discord.Embed(title=  Name + "'s Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
                #GzzName = "Tlandorus"
                #result = pokedex(str(GzzName))
            elif Name == "Kyurem":
                result = await gotohome(self, str(Name))
                Level = int(float(content[2]))
                if Level > 50:
                        await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 50",delete_after=10)
                        Level = 50
                GOATK = int(content[3])
                GODEF = int(content[4])
                GOHP  = int(content[5])
                TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                embed = discord.Embed(title=  Name + "'s Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
                #GzzName = "Blackkyurem"
                #result = pokedex(str(GzzName))
                #GzzzName = "Whitekyurem"
                #result = pokedex(str(GzzzName))
            else:
                if Name == "Sirfetch’d":
                    Name = "Sirfetch'd"
                if Name == "Farfetch’d":
                    Name = "Farfetch'd"
                result = await gotohome(self, str(Name))
                if result == None:
                    await ctx.send('This Pokémon does not exist!')
                elif result != None:
                    Level = int(float(content[2]))
                    if Level > 50:
                        await ctx.send("I don't think Pokemon in Go... um go that high...I'll assume you meant Level 50",delete_after=10)
                        Level = 50
                    GOATK = int(content[3])
                    GODEF = int(content[4])
                    GOHP  = int(content[5])
                    TrueHP = HPGotoHome(GOHP,int(result[0]),Level)
                    TrueATKLow = ATKGotohomeLow(GOATK,int(result[1]),Level)
                    TrueATK = ATKGotohome(GOATK,int(result[1]),Level)
                    TrueATKHigh = ATKGotohomeHigh(GOATK,int(result[1]),Level)
                    TrueDEFLow = DEFGotohomeLow(GODEF,int(result[2]),Level)
                    TrueDEF = DEFGotohome(GODEF,int(result[2]),Level)
                    TrueDEFHigh = DEFGotohomeHigh(GODEF,int(result[2]),Level)
                    TrueSPALow = SPAGotohomeLow(GOATK,int(result[3]),Level)
                    TrueSPA = SPAGotohome(GOATK,int(result[3]),Level)
                    TrueSPAHigh = SPAGotohomeHigh(GOATK,int(result[3]),Level)
                    TrueSPDLow = SPDGotohomeLow(GODEF,int(result[4]),Level)
                    TrueSPD = SPDGotohome(GODEF,int(result[4]),Level)
                    TrueSPDHigh = SPDGotohomeHigh(GODEF,int(result[4]),Level)
                    TrueSpeedNLow = SpeedGotohomeNLow(int(0),int(result[5]),Level)
                    TrueSpeedLow = SpeedGotohomeLow(int(0),int(result[5]),Level)
                    TrueSpeedHigh = SpeedGotohomeHigh(int(15),int(result[5]),Level)
                    TrueSpeedNHigh = SpeedGotohomeNHigh(int(15),int(result[5]),Level)
                    embed = discord.Embed(title=  Name + "'s Pokemon Go to Home Stat Conversion", description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="'-' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKLow)+"**\nDef: \n**"+str(TrueDEFLow)+"**\nSPA: \n**"+str(TrueSPALow)+"**\nSPD: \n**"+str(TrueSPDLow)+"**\nSpeed: \n**"+str(TrueSpeedNLow)+"-"+str(TrueSpeedLow)+"**",inline=True)
                    embed.add_field(name="Neutral Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATK)+"**\nDef: \n**"+str(TrueDEF)+"**\nSPA: \n**"+str(TrueSPA)+"**\nSPD: \n**"+str(TrueSPD)+"**\nSpeed: \n**"+str(TrueSpeedLow)+"-"+str(TrueSpeedHigh)+"**", inline=True)
                    embed.add_field(name="'+' Nature", value="HP: \n**"+str(TrueHP)+"**\nATK: \n**"+str(TrueATKHigh)+"**\nDef: \n**"+str(TrueDEFHigh)+"**\nSPA: \n**"+str(TrueSPAHigh)+"**\nSPD: \n**"+str(TrueSPDHigh)+"**\nSpeed: \n**"+str(TrueSpeedHigh)+"-"+str(TrueSpeedNHigh)+"**", inline=True)
                    embed.add_field(name="Go Stats Given", value="Level: **"+str(Level)+"**  ATK: **"+str(GOATK)+"**  DEF: **"+str(GODEF)+"**  HP: **"+str(GOHP)+"**", inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)

    @commands.group(case_insensitive=True)
    async def gosearchterms(self, ctx):
        if ctx.invoked_subcommand is None:
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send("Please enter the type of search function (`pokemon`, `status`, `type` or `combination`) you want to lookup when executing the command!~", delete_after=10)

    @gosearchterms.command()
    async def pokemon(self, ctx):
        embed = discord.Embed(title="Find Specific Pokemon" , description="**Notes**:\n1. Search terms can be lower case where applicable\n2. Searches by number can be ranged where applicable", color=0x2962FF)
        embed.set_thumbnail(url="https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/decrypted_assets/png/Badge_46_3_01.png")
        embed.add_field(name="Terms:", value="`CP#: Pokemon by CP`\t=>\t`CP300`\n`Distance#: By km distance`\t=>\t`Distance 1000`\n`+: Evolution line`\t=>\t`+Pikachu`\n`HP#: Pokemon by HP`\t=>\t`HP150`\n`evolvemega: Can Mega Evolve`\t=>\t`evolvemega`\n`@movename: By Named Move`\t=>\t`@scratch`\n`@movetype: By Move Type`\t=>\t`@grass`\n`@special: By Special Move)`\t=>\t`@special`\n`@#type: By Fast/Charged Move Type`\t=>\t`@3ghost`", inline=True)
        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
        candelete = await get_delete(self, ctx)
        if candelete == "True":
            await ctx.message.delete()
        await ctx.send(embed=embed)

    @gosearchterms.command()
    async def status(self, ctx):
        embed = discord.Embed(title="Find Specific Status" , description="Notes: Search terms can be lower case where applicable\nSearches by number can be ranged where applicable", color=0x2962FF)
        embed.set_thumbnail(url="https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/decrypted_assets/png/Badge_46_3_01.png")
        embed.add_field(name="Terms:", value="`age#: By Days Old` => `age0`\n`buddy#: By Buddy Level` => `buddy2`\n`evolve: Evolvable Pokemon` => `evolve`\n`defender: Defending Gym` => `defender`\n`item: Evolve By Item` => `item`\n`evolvenew: New Entry By Evolution` => `evolvenew`\n`tradeevolve: Evolvable By Trade` => `tradevolve`\n`@weather: By Boosted Attacks` => `@weather`\n`year #: By Year Caught` => `year 2016`", inline=True)
        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
        candelete = await get_delete(self, ctx)
        if candelete == "True":
            await ctx.message.delete()
        await ctx.send(embed=embed)

    @gosearchterms.command()
    async def type(self, ctx):
        embed = discord.Embed(title="Find Specifc Type" , description="Notes: Search terms can be lower case where applicable\nSearches by number can be ranged where applicable", color=0x2962FF)
        embed.set_thumbnail(url="https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/decrypted_assets/png/Badge_46_3_01.png")
        embed.add_field(name="Terms:", value="`alolan: Alolan form pokemon` => `alolan`\n`0-4* : By Star Rating` => `0*`\n`eggslonly: Egg Only Pokemon` => `eggsonly`\n`hatched: Hatched Pokemon` => `hatched`\n`lucky: Lucky Pokemon` => `lucky`\n`legendary: Legendary Pokemon` => `legendary`\n`mythical: Mythical Pokemon` => `mythical`\n`purified: Purified Pokemon` => `purified`\n`shadow: Shadow Pokemon` => `shadow`\n`shiny: Shiny Pokemon` => `shiny`\n`costume: Costumed Pokemon` => `costume`\n`traded: Traded Pokemon` => `traded`", inline=True)
        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
        candelete = await get_delete(self, ctx)
        if candelete == "True":
            await ctx.message.delete()
        await ctx.send(embed=embed)

    @gosearchterms.command()
    async def combination(self, ctx):
        embed = discord.Embed(title="Useful Search Functions" , description="", color=0x2962FF)
        embed.set_thumbnail(url="https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/decrypted_assets/png/Badge_46_3_01.png")
        embed.add_field(name="Terms:", value="``& or | : Acts as an AND` => `3*&shiny` or `3*|shiny`\n`!: Acts as a NOT` => `!evolve`\n`-: Minimum function` => `CP500-`\n`,` : Acts as an OR` => `hatched,shiny`", inline=True)
        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
        candelete = await get_delete(self, ctx)
        if candelete == "True":
            await ctx.message.delete()
        await ctx.send(embed=embed)

    @gosearchterms.command()
    async def advanced(self, ctx):
        embed = discord.Embed(title="Advanced Searches" , description="", color=0x2962FF)
        embed.set_thumbnail(url="https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/decrypted_assets/png/Badge_46_3_01.png")
        embed.add_field(name="Examples:", value="`hatched&!fire&!normal`\nTranslates to\n`Searches for a Hatched Pokemon that isn't Fire or Normal type`\n\n\n`@weather&!fighting&@3fairy`\nTranslates to\n`Searches for a Weather Boosted Non Fighting Pokemon with a 2nd Charged Fairy Move`", inline=True)
        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
        candelete = await get_delete(self, ctx)
        if candelete == "True":
            await ctx.message.delete()
        await ctx.send(embed=embed)

    @gotohome.error
    async def gotohome_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send("Please insert the Form (optional), Name, Level, and all three IV's of the pokemon\n\n Do '<>help gotohome' for examples if confused", delete_after=5)

    @gopvp.error
    async def gopvp_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            print(error)
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send("Please insert the Form (optional), Name, Level, and all three IV's of the pokemon\n\n Do '<>help gopvp' for examples if confused", delete_after=5)

    @godex.error
    async def godex_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            print(error)
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send("Please insert the name of the Pokemon (With/Without Form or Regional Varient)\n\n Do '<>help godex' for examples if confused", delete_after=5)

    @gorocket.error
    async def gorocket_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send("Please insert the grunt type or leader name into the search\n\n Do '<>help gorocket' for examples if confused", delete_after=5)

    @gohundo.error
    async def gohundo_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send("Please insert the name of the Pokemon (With/Without Form or Regional Varient)\n\n Do '<>help gohundo' for examples if confused", delete_after=5)

    @gopure.error
    async def gopure_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send("Please insert the Name, and all three IV's of the pokemon\n\n Do '<>help gopure' for examples if confused", delete_after=5)

async def dex(self, pokename):
    pokename = pokename.capitalize()
    dexentry = ''
    generation = ''
    types = ''
    Height = 0
    Weight = 0
    Maxcp = 0
    pokeAtk = 0
    pokeDef = 0
    pokeSta = 0
    Shiny = ''
    Timed = ''
    RShiny = ''
    EggShiny = ''
    Research = ''
    Fastmove = ''
    Chargemove = ''
    Resistant = ''
    Weak = ''
    Distancecandy = ''
    #fileOpen = open('E:/pokegodex.csv', newline='')
    #fileData = csv.reader(fileOpen)
    #for row in fileData:
    #    for name in row:
    #        if name == pokename:

    if pokename == "Farfetch'd":
        pokename = "Farfetch''d"
    if pokename == "Sirfetch'd":
        pokename = "Sirfetch''d"

    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM gopokedex WHERE name = '"+str(pokename)+"';"))
            row = list(prerow.values())
            dexentry = row[0]
            generation = row[2]
            types = row[3]
            if row[4] != "Unknown":
                types = row[3] + " / " + row[4]
                Height = row[5]
                Weight = row[6]
                Maxcp =  row[7]
                pokeAtk = row[8]
                pokeDef = row[9]
                pokeSta = row[10]
                Shiny = row[11]
                Timed = row[12]
                RShiny = row[13]
                EggShiny = row[14]
                Research = row[15]
                Fastmove = row[16]
                Chargemove = row[17]
                Resistant = row[18]
                Weak = row[19]
                Distancecandy = row[20]
                return (dexentry, generation, types, Height, Weight, Maxcp, pokeAtk, pokeDef, pokeSta, Shiny, Timed, RShiny, EggShiny, Research, Fastmove, Chargemove, Resistant, Weak, Distancecandy)
            elif row[4] == "Unknown":
                types = row[3]
                Height = row[5]
                Weight = row[6]
                Maxcp = row[7]
                pokeAtk = row[8]
                pokeDef = row[9]
                pokeSta = row[10]
                Shiny = row[11]
                Timed = row[12]
                RShiny = row[13]
                EggShiny= row[14]
                Research = row[15]
                Fastmove = row[16]
                Chargemove = row[17]
                Resistant = row[18]
                Weak = row[19]
                Distancecandy = row[20]
                return (dexentry, generation, types, Height, Weight, Maxcp, pokeAtk, pokeDef, pokeSta, Shiny, Timed, RShiny, EggShiny, Research, Fastmove, Chargemove, Resistant, Weak, Distancecandy)

async def aloladex(self, pokename):
    pokename = pokename.capitalize()
    dexentry = ''
    generation = ''
    types = ''
    Height = 0
    Weight = 0
    Maxcp = 0
    pokeAtk = 0
    pokeDef = 0
    pokeSta = 0
    Shiny = ''
    Timed = ''
    RShiny = ''
    EggShiny = ''
    Research = ''
    Fastmove = ''
    Chargemove = ''
    Resistant = ''
    Weak = ''
    Distancecandy = ''

    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM goaloladex WHERE name = '"+str(pokename)+"';"))
            row = list(prerow.values())
            dexentry = row[0]
            generation = row[2]
            types = row[3]
            if row[4] != "Unknown":
                types = row[3] + " / " + row[4]
                Height = row[5]
                Weight = row[6]
                Maxcp =  row[7]
                pokeAtk = row[8]
                pokeDef = row[9]
                pokeSta = row[10]
                Shiny = row[11]
                Timed = row[12]
                RShiny = row[13]
                EggShiny = row[14]
                Research = row[15]
                Fastmove = row[16]
                Chargemove = row[17]
                Resistant = row[18]
                Weak = row[19]
                Distancecandy = row[20]
                return (dexentry, generation, types, Height, Weight, Maxcp, pokeAtk, pokeDef, pokeSta, Shiny, Timed, RShiny, EggShiny, Research, Fastmove, Chargemove, Resistant, Weak, Distancecandy)
            elif row[4] == "Unknown":
                types = row[3]
                Height = row[5]
                Weight = row[6]
                Maxcp =  row[7]
                pokeAtk = row[8]
                pokeDef = row[9]
                pokeSta = row[10]
                Shiny = row[11]
                Timed = row[12]
                RShiny = row[13]
                EggShiny= row[14]
                Research = row[15]
                Fastmove = row[16]
                Chargemove = row[17]
                Resistant = row[18]
                Weak = row[19]
                Distancecandy = row[20]
                return (dexentry, generation, types, Height, Weight, Maxcp, pokeAtk, pokeDef, pokeSta, Shiny, Timed, RShiny, EggShiny, Research, Fastmove, Chargemove, Resistant, Weak, Distancecandy)

async def galardex(self, pokename):
    pokename = pokename.capitalize()
    dexentry = ''
    generation = ''
    types = ''
    Height = 0
    Weight = 0
    Maxcp = 0
    pokeAtk = 0
    pokeDef = 0
    pokeSta = 0
    Shiny = ''
    Timed = ''
    RShiny = ''
    EggShiny = ''
    Research = ''
    Fastmove = ''
    Chargemove = ''
    Resistant = ''
    Weak = ''
    Distancecandy = ''

    if pokename == "Farfetch'd":
        pokename = "Farfetch''d"

    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM gogalardex WHERE name = '"+str(pokename)+"';"))
            row = list(prerow.values())
            dexentry = row[0]
            generation = row[2]
            types = row[3]
            if row[4] != "Unknown":
                types = row[3] + " / " + row[4]
                Height = row[5]
                Weight = row[6]
                Maxcp =  row[7]
                pokeAtk = row[8]
                pokeDef = row[9]
                pokeSta = row[10]
                Shiny = row[11]
                Timed = row[12]
                RShiny = row[13]
                EggShiny = row[14]
                Research = row[15]
                Fastmove = row[16]
                Chargemove = row[17]
                Resistant = row[18]
                Weak = row[19]
                Distancecandy = row[20]
                return (dexentry, generation, types, Height, Weight, Maxcp, pokeAtk, pokeDef, pokeSta, Shiny, Timed, RShiny, EggShiny, Research, Fastmove, Chargemove, Resistant, Weak, Distancecandy)
            elif row[4] == "Unknown":
                types = row[3]
                Height = row[5]
                Weight = row[6]
                Maxcp =  row[7]
                pokeAtk = row[8]
                pokeDef = row[9]
                pokeSta = row[10]
                Shiny = row[11]
                Timed = row[12]
                RShiny = row[13]
                EggShiny= row[14]
                Research = row[15]
                Fastmove = row[16]
                Chargemove = row[17]
                Resistant = row[18]
                Weak = row[19]
                Distancecandy = row[20]
                return (dexentry, generation, types, Height, Weight, Maxcp, pokeAtk, pokeDef, pokeSta, Shiny, Timed, RShiny, EggShiny, Research, Fastmove, Chargemove, Resistant, Weak, Distancecandy)

async def Rocketlookup(self, info):
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM teamgorocket WHERE type = '"+str(info)+"';"))
            row = list(prerow.values())
            firstmon = row[1]
            secondmon = row[2]
            thirdmon = row[3]
            reward = row[4]
            return (firstmon, secondmon, thirdmon, reward)

async def PokemonHundo(self, pokenamez):
    pokename = pokenamez.capitalize()
    Level = 1
    IV1 = 15
    IV2 = 15
    IV3 = 15
    GoAtk = 0
    GoDef = 0
    GoStamina = 0
    Data = []
    
    if pokename == "Farfetch'd":
        pokename = "Farfetch''d"
    if pokename == "Sirfetch'd":
        pokename = "Sirfetch''d"
        
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM gopokedex WHERE name = '"+str(pokename)+"';"))
            row = list(prerow.values())
            GoAtk = int(row[8])
            GoDef = int(row[9])
            GoStamina = int(row[10])
            RealAtk = GoAtk + IV1
            RealDef = GoDef + IV2
            RealStamina = GoStamina + IV3
            while Level != 52:
                CPM = LeveltoCPM(Level)
                CP = CPCalc(RealAtk, RealDef, RealStamina, CPM)
                Data.append(CP)
                Level += 1
            return Data

async def PokemonHundoAlolan(self, pokenamez):
    pokename = pokenamez.capitalize()
    Level = 1
    IV1 = 15
    IV2 = 15
    IV3 = 15
    GoAtk = 0
    GoDef = 0
    GoStamina = 0
    Data = []
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM goaloladex WHERE name = '"+str(pokename)+"';"))
            row = list(prerow.values())
            RealAtk = int(row[8]) + IV1
            RealDef = int(row[9]) + IV2
            RealStamina = int(row[10]) + IV3
            while Level != 52:
                CPM = LeveltoCPM(Level)
                CP = CPCalc(RealAtk, RealDef, RealStamina, CPM)
                Data.append(CP)
                Level += 1
            return Data

async def PokemonHundoGalarian(self, pokenamez):
    pokename = pokenamez.capitalize()
    Level = 1
    IV1 = 15
    IV2 = 15
    IV3 = 15
    GoAtk = 0
    GoDef = 0
    GoStamina = 0
    Data = []
    
    if pokename == "Farfetch'd":
        pokename = "Farfetch''d"
    
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM gogalardex WHERE name = '"+str(pokename)+"';"))
            row = list(prerow.values())
            RealAtk = int(row[8]) + IV1
            RealDef = int(row[9]) + IV2
            RealStamina = int(row[10]) + IV3
            while Level != 52:
                CPM = LeveltoCPM(Level)
                CP = CPCalc(RealAtk, RealDef, RealStamina, CPM)
                Data.append(CP)
                Level += 1
            return Data

async def MaintoGo(self, pokenamez, Lvl, IVA, IVD, IVS):
    pokename = pokenamez.capitalize()
    Level = float(Lvl)
    IV1 = int(IVA)
    IV2 = int(IVD)
    IV3 = int(IVS)
    GoAtk = 0
    GoDef = 0
    GoStamina = 0
    RealAtk = 0
    RealDef = 0
    RealStamina = 0
    CP = 0
    Great = 1500.0
    Ultra = 2500.0
    Master = 6000.0
    Statproduct = 0.0
    
    if pokename == "Farfetch'd":
        pokename = "Farfetch''d"
    if pokename == "Sirfetch'd":
        pokename = "Sirfetch''d"
    
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM gopokedex WHERE name = '"+str(pokename)+"';"))
            row = list(prerow.values())
            RealAtk = int(row[8]) + IV1
            RealDef = int(row[9]) + IV2
            RealStamina = int(row[10]) + IV3
            CPM = LeveltoCPM(Level)
            Statproduct = (((RealAtk*CPM)*(RealDef*CPM)*math.floor((RealStamina*CPM)))/1000)
            CP = CPCalc(RealAtk, RealDef, RealStamina, CPM)
            YourPokemon = (CP, Level, Statproduct,IV1,IV2,IV3)
            BestofGreat = await BestsearchGreat(self, pokename)
            BestofUltra = await BestsearchUltra(self, pokename)
            BestofMaster= BestsearchMaster((RealAtk - IV1), (RealDef - IV2), (RealStamina - IV3), Master)
            return (YourPokemon,BestofGreat,BestofUltra,BestofMaster)

async def AlolanMaintoGo(self, pokenamez, Lvl, IVA, IVD, IVS):
    pokename = pokenamez.capitalize()
    Level = float(Lvl)
    IV1 = int(IVA)
    IV2 = int(IVD)
    IV3 = int(IVS)
    GoAtk = 0
    GoDef = 0
    GoStamina = 0
    RealAtk = 0
    RealDef = 0
    RealStamina = 0
    CP = 0
    Great = 1500.0
    Ultra = 2500.0
    Master = 6000.0
    Statproduct = 0.0
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM goaloladex WHERE name = '"+str(pokename)+"';"))
            row = list(prerow.values())
            RealAtk = int(row[8]) + IV1
            RealDef = int(row[9]) + IV2
            RealStamina = int(row[10]) + IV3
            CPM = LeveltoCPM(Level)
            Statproduct = (((RealAtk*CPM)*(RealDef*CPM)*math.floor(RealStamina*CPM))/1000)
            CP = CPCalc(RealAtk, RealDef, RealStamina, CPM)
            YourPokemon = (CP, Level, Statproduct,IV1,IV2,IV3)
            BestofGreat= await BestalolasearchGreat(self, pokename)
            BestofUltra= await BestalolasearchUltra(self, pokename)
            BestofMaster= BestsearchMaster((RealAtk - IV1), (RealDef - IV2), (RealStamina - IV3), Master)
            return (YourPokemon,BestofGreat,BestofUltra,BestofMaster)

async def GalarianMaintoGo(self, pokenamez, Lvl, IVA, IVD, IVS):
    pokename = pokenamez.capitalize()
    Level = Lvl
    IV1 = IVA
    IV2 = IVD
    IV3 = IVS
    GoAtk = 0
    GoDef = 0
    GoStamina = 0
    RealAtk = 0
    RealDef = 0
    RealStamina = 0
    CP = 0
    Great = 1500.0
    Ultra = 2500.0
    Master = 6000.0
    Statproduct = 0.0
    
    if pokename == "Farfetch'd":
        pokename = "Farfetch''d"
    
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM gogalardex WHERE name = '"+str(pokename)+"';"))
            row = list(prerow.values())
            RealAtk = int(row[8]) + IV1
            RealDef = int(row[9]) + IV2
            RealStamina = int(row[10]) + IV3
            CPM = LeveltoCPM(Level)
            Statproduct = (((RealAtk*CPM)*(RealDef*CPM)*math.floor(RealStamina*CPM))/1000)
            CP = CPCalc(RealAtk, RealDef, RealStamina, CPM)
            YourPokemon = (CP, Level, Statproduct,IV1,IV2,IV3)
            BestofGreat= await BestgalarsearchGreat(self, pokename)
            BestofUltra= await BestgalarsearchUltra(self, pokename)
            BestofMaster= BestsearchMaster((RealAtk - IV1), (RealDef - IV2), (RealStamina - IV3), Master)
            return (YourPokemon,BestofGreat,BestofUltra,BestofMaster)

async def MegaMaintoGo(self, pokenamez, Lvl, IVA, IVD, IVS):
    pokename = pokenamez.capitalize()
    Level = Lvl
    IV1 = IVA
    IV2 = IVD
    IV3 = IVS
    GoAtk = 0
    GoDef = 0
    GoStamina = 0
    RealAtk = 0
    RealDef = 0
    RealStamina = 0
    CP = 0
    Great = 1500.0
    Ultra = 2500.0
    Master = 6000.0
    Statproduct = 0.0
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM gomegadex WHERE name = '"+str(pokename)+"';"))
            row = list(prerow.values())
            if pokename == "Xmewtwo" or pokename == "Ymewtwo":
                RealAtk = int(row[8]) + IV1
                RealDef = int(row[9]) + IV2
                RealStamina = int(row[10]) + IV3
                CPM = LeveltoCPM(Level)
                Statproduct = (((RealAtk*CPM)*(RealDef*CPM)*math.floor(RealStamina*CPM))/1000)
                CP = CPCalc(RealAtk, RealDef, RealStamina, CPM)
                YourPokemon = (CP, Level, Statproduct,IV1,IV2,IV3)
                BestofGreat= int(0),float(0.0),float(0.0),int(0),int(0),int(0)
                BestofUltra= await BestmegasearchUltra(self, pokename)
                BestofMaster= BestsearchMaster((RealAtk - IV1), (RealDef - IV2), (RealStamina - IV3), Master)
                return (YourPokemon,BestofGreat,BestofUltra,BestofMaster)
            elif pokename == "Gyarados" or pokename == "Heracross" or pokename == "Tyranitar" or pokename == "Salamence" or pokename == "Metagross" or pokename == "Latias" or pokename == "Latios" or pokename == "Rayquaza" or pokename == "Garchomp":
                RealAtk = int(row[8]) + IV1
                RealDef = int(row[9]) + IV2
                RealStamina = int(row[10]) + IV3
                CPM = LeveltoCPM(Level)
                Statproduct = (((RealAtk*CPM)*(RealDef*CPM)*math.floor(RealStamina*CPM))/1000)
                CP = CPCalc(RealAtk, RealDef, RealStamina, CPM)
                YourPokemon = (CP, Level, Statproduct,IV1,IV2,IV3)
                BestofGreat= int(0),float(0.0),float(0.0),int(0),int(0),int(0)
                BestofUltra= await BestmegasearchUltra(self, pokename)
                BestofMaster= BestsearchMaster((RealAtk - IV1), (RealDef - IV2), (RealStamina - IV3), Master)
                return (YourPokemon,BestofGreat,BestofUltra,BestofMaster)
            else:
                RealAtk = int(row[8]) + IV1
                RealDef = int(row[9]) + IV2
                RealStamina = int(row[10]) + IV3
                CPM = LeveltoCPM(Level)
                Statproduct = (((RealAtk*CPM)*(RealDef*CPM)*math.floor(RealStamina*CPM))/1000)
                CP = CPCalc(RealAtk, RealDef, RealStamina, CPM)
                YourPokemon = (CP, Level, Statproduct,IV1,IV2,IV3)
                BestofGreat= await BestmegasearchGreat(self, pokename)
                BestofUltra= await BestmegasearchUltra(self, pokename)
                BestofMaster= BestsearchMaster((RealAtk - IV1), (RealDef - IV2), (RealStamina - IV3), Master)
                return (YourPokemon,BestofGreat,BestofUltra,BestofMaster)

async def BestsearchGreat(self, pokenamez):
    pokename = pokenamez   
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM glsearch WHERE name = '"+str(pokenamez)+"';"))
            row = list(prerow.values())
            CP = int(row[1])
            Level = float(row[2])
            BestStatPro = float(row[3])
            GLA = int(row[4])
            GLD = int(row[5])
            GLS = int(row[6])
            return (CP,Level,BestStatPro,GLA,GLD,GLS)

async def BestsearchUltra(self, pokenamez):
    pokename = pokenamez
    
    if pokename == "Farfetch'd":
        pokename = "Farfetch''d"
    if pokename == "Sirfetch'd":
        pokename = "Sirfetch''d"
    
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM ulsearch WHERE name = '"+str(pokename)+"';"))
            row = list(prerow.values())
            CP = int(row[1])
            Level = float(row[2])
            BestStatPro = float(row[3])
            GLA = int(row[4])
            GLD = int(row[5])
            GLS = int(row[6])
            return (CP,Level,BestStatPro,GLA,GLD,GLS)

async def BestalolasearchGreat(self, pokenamez):
    pokename = pokenamez
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM alolaglsearch WHERE name = '"+str(pokename)+"';"))
            row = list(prerow.values())
            CP = int(row[1])
            Level = float(row[2])
            BestStatPro = float(row[3])
            GLA = int(row[4])
            GLD = int(row[5])
            GLS = int(row[6])
            return (CP,Level,BestStatPro,GLA,GLD,GLS)

async def BestalolasearchUltra(self, pokenamez):
        pokename = pokenamez
        # retrieve an individual connection from our pool, defined later
        async with self.client.pool.acquire() as connection:
            # create a transaction for that connection
            async with connection.transaction():
                prerow = dict(await connection.fetchrow("SELECT * FROM alolaulsearch WHERE name = '"+str(pokename)+"';"))
                row = list(prerow.values())
                CP = int(row[1])
                Level = float(row[2])
                BestStatPro = float(row[3])
                GLA = int(row[4])
                GLD = int(row[5])
                GLS = int(row[6])
                return (CP,Level,BestStatPro,GLA,GLD,GLS)

async def BestgalarsearchGreat(self, pokenamez):
    pokename = pokenamez
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM galarglsearch WHERE name = '"+str(pokename)+"';"))
            row = list(prerow.values())
            CP = int(row[1])
            Level = float(row[2])
            BestStatPro = float(row[3])
            GLA = int(row[4])
            GLD = int(row[5])
            GLS = int(row[6])
            return (CP,Level,BestStatPro,GLA,GLD,GLS)

async def BestgalarsearchUltra(self, pokenamez):
        pokename = pokenamez
        # retrieve an individual connection from our pool, defined later
        async with self.client.pool.acquire() as connection:
            # create a transaction for that connection
            async with connection.transaction():
                prerow = dict(await connection.fetchrow("SELECT * FROM galarulsearch WHERE name = '"+str(pokename)+"';"))
                row = list(prerow.values())
                CP = int(row[1])
                Level = float(row[2])
                BestStatPro = float(row[3])
                GLA = int(row[4])
                GLD = int(row[5])
                GLS = int(row[6])
                return (CP,Level,BestStatPro,GLA,GLD,GLS)

async def BestmegasearchGreat(self, pokenamez):
        pokename = pokenamez
        # retrieve an individual connection from our pool, defined later
        async with self.client.pool.acquire() as connection:
            # create a transaction for that connection
            async with connection.transaction():
                prerow = dict(await connection.fetchrow("SELECT * FROM megaglsearch WHERE name = '"+str(pokename)+"';"))
                row = list(prerow.values())
                CP = int(row[1])
                Level = float(row[2])
                BestStatPro = float(row[3])
                GLA = int(row[4])
                GLD = int(row[5])
                GLS = int(row[6])
                return (CP,Level,BestStatPro,GLA,GLD,GLS)

async def BestmegasearchUltra(self, pokenamez):
        pokename = pokenamez
        # retrieve an individual connection from our pool, defined later
        async with self.client.pool.acquire() as connection:
            # create a transaction for that connection
            async with connection.transaction():
                prerow = dict(await connection.fetchrow("SELECT * FROM megaulsearch WHERE name = '"+str(pokename)+"';"))
                row = list(prerow.values())
                CP = int(row[1])
                Level = float(row[2])
                BestStatPro = float(row[3])
                GLA = int(row[4])
                GLD = int(row[5])
                GLS = int(row[6])
                return (CP,Level,BestStatPro,GLA,GLD,GLS)

def BestsearchMaster(Atk, Def, Stamina, LCP):
    League = LCP
    Level = float(1.0)
    CPM = float(0.0)
    CP = 0
    GoAtk = Atk
    GoDef = Def
    GoStamina = Stamina
    if League == 6000.0:
        Level = 50.0
        CPM = 0.840300023555755
        CP = CPCalc((GoAtk+15), (GoDef+15), (GoStamina+15), CPM)
        Atkproduct = float((GoAtk+15)*CPM)
        Defproduct = float((GoDef+15)*CPM)
        Stamproduct = float(math.floor((GoStamina+15)*CPM))
        Statproduct = ((Atkproduct*Defproduct*Stamproduct)/1000)
        return (CP,Level,Statproduct,15,15,15) ###

def LeveltoCPM(Level):
    Lvl = Level
    LevelDict = {1:0.09399999678,1.5:0.1351374321,2:0.1663978696,2.5:0.1926509132,3:0.2157324702,3.5:0.2365726514,4:0.2557200491,4.5:0.2735303721,5:0.2902498841,5.5:0.3060573814,6:0.3210875988,6.5:0.335445032,7:0.3492126763,7.5:0.3624577366,8:0.3752355874,8.5:0.3875924077,9:0.3995672762,9.5:0.4111935532,10:0.4225000143,10.5:0.4329264205,11:0.4431075454,11.5:0.4530599482,12:0.4627983868,12.5:0.4723360853,13:0.481684953,13.5:0.4908558072,14:0.499858439,14.5:0.508701749,15:0.5173939466,15.5:0.5259425161,16:0.5343543291,16.5:0.5426357538,17:0.5507926941,17.5:0.5588305845,18:0.5667545199,18.5:0.5745691281,19:0.5822789073,19.5:0.5898879079,20:0.5974000096,20.5:0.6048236487,21:0.6121572852,21.5:0.619404108,22:0.6265671253,22.5:0.6336491787,23:0.6406529546,23.5:0.6475809714,24:0.6544356346,24.5:0.6612192658,25:0.6679340005,25.5:0.6745818856,26:0.6811649203,26.5:0.6876849013,27:0.6941436529,27.5:0.700542901,28:0.7068842053,28.5:0.7131690749,29:0.7193990946,29.5:0.7255755869,30:0.7317000031,30.5:0.7347410386,31:0.7377694845,31.5:0.7407855797,32:0.7437894344,32.5:0.7467811972,33:0.749761045,33.5:0.7527290997,34:0.7556855083,34.5:0.7586303702,35:0.7615638375,35.5:0.7644860496,36:0.7673971653,36.5:0.7702972937,37:0.7731865048,37.5:0.7760649471,38:0.7789327502,38.5:0.7817900508,39:0.7846369743,39.5:0.7874736085,40:0.7903000116,40.5:0.792803968023538,41:0.795300006866455,41.5:0.797803898371622,42:0.800300002098083,42.5:0.802803871877596,43:0.805299997329711,43.5:0.807803850847053,44:0.81029999256134,44.5:0.812803835179168,45:0.815299987792968,45.5:0.817803806620319,46:0.820299983024597,46.5:0.822803778631297,47:0.825299978256225,47.5:0.827803750922782,48:0.830299973487854,48.5:0.832803753381377,49:0.835300028324127,49.5:0.837803755931569,50:0.840300023555755,50.5:0.842803729,51:0.8453000188}
    return LevelDict[Lvl]

def CPCalc(Atk, Def, Stamina, CPM):
    CAtk = Atk
    CDef = Def
    CStamina = Stamina
    DCPM = CPM
    H = DCPM ** 2
    J = CStamina ** 0.5
    K = CDef ** 0.5
    resultCP = int(max(10,(CAtk*H*J*K/10)))
    return resultCP

def HPGotoHome(RHPIV, base, level):
    HPIV = (RHPIV * 2) + 1
    BaseHP = base
    level = level
    Base2 = (2 * BaseHP)
    HPcalculated = int((((Base2 + HPIV)*level)/100) + (level + 10) )
    return HPcalculated

def ATKGotohomeLow(RATKIV, base, level):
    ATKIV = (RATKIV * 2) + 1
    BaseATK = base
    level = level
    Base2 = (2 * BaseATK)
    G = ((Base2 + ATKIV)*level)
    Atkcalculated = int(((G/100)+5)* 0.9)
    return Atkcalculated

def ATKGotohome(RATKIV, base, level):
    ATKIV = (RATKIV * 2) + 1
    BaseATK = base
    level = level
    Base2 = (2 * BaseATK)
    G = ((Base2 + ATKIV)*level)
    Atkcalculated = int(((G/100)+5))
    return Atkcalculated

def ATKGotohomeHigh(RATKIV, base, level):
    ATKIV = (RATKIV * 2) + 1
    BaseATK = base
    level = level
    Base2 = (2 * BaseATK)
    G = ((Base2 + ATKIV)*level)
    Atkcalculated = int(((G/100)+5)* 1.1)
    return Atkcalculated

def DEFGotohomeLow(RDEFIV, base, level):
    DEFIV = (RDEFIV * 2) + 1
    BaseDEF = base
    level = level
    Base2 = (2 * BaseDEF)
    G = ((Base2 + DEFIV)*level)
    DEFcalculated = int(((G/100)+5)* 0.9)
    return DEFcalculated

def DEFGotohome(RDEFIV, base, level):
    DEFIV = (RDEFIV * 2) + 1
    BaseDEF = base
    level = level
    Base2 = (2 * BaseDEF)
    G = ((Base2 + DEFIV)*level)
    DEFcalculated = int(((G/100)+5))
    return DEFcalculated

def DEFGotohomeHigh(RDEFIV, base, level):
    DEFIV = (RDEFIV * 2) + 1
    BaseDEF = base
    level = level
    Base2 = (2 * BaseDEF)
    G = ((Base2 + DEFIV)*level)
    DEFcalculated = int(((G/100)+5)* 1.1)
    return DEFcalculated

def SPAGotohomeLow(RSPAIV, base, level):
    SPAIV = (RSPAIV * 2) + 1
    BaseSPA = base
    level = level
    Base2 = (2 * BaseSPA)
    G = ((Base2 + SPAIV)*level)
    SPAcalculated = int(((G/100)+5)* 0.9)
    return SPAcalculated

def SPAGotohome(RSPAIV, base, level):
    SPAIV = (RSPAIV * 2) + 1
    BaseSPA = base
    level = level
    Base2 = (2 * BaseSPA)
    G = ((Base2 + SPAIV)*level)
    SPAcalculated = int(((G/100)+5))
    return SPAcalculated

def SPAGotohomeHigh(RSPAIV, base, level):
    SPAIV = (RSPAIV * 2) + 1
    BaseSPA = base
    level = level
    Base2 = (2 * BaseSPA)
    G = ((Base2 + SPAIV)*level)
    SPAcalculated = int(((G/100)+5)* 1.1)
    return SPAcalculated

def SPDGotohomeLow(RSPDIV, base, level):
    SPDIV = (RSPDIV * 2) + 1
    BaseSPD = base
    level = level
    Base2 = (2 * BaseSPD)
    G = ((Base2 + SPDIV)*level)
    SPDcalculated = int(((G/100)+5)* 0.9)
    return SPDcalculated

def SPDGotohome(RSPDIV, base, level):
    SPDIV = (RSPDIV * 2) + 1
    BaseSPD = base
    level = level
    Base2 = (2 * BaseSPD)
    G = ((Base2 + SPDIV)*level)
    SPDcalculated = int(((G/100)+5))
    return SPDcalculated

def SPDGotohomeHigh(RSPDIV, base, level):
    SPDIV = (RSPDIV * 2) + 1
    BaseSPD = base
    level = level
    Base2 = (2 * BaseSPD)
    G = ((Base2 + SPDIV)*level)
    SPDcalculated = int(((G/100)+5)* 1.1)
    return SPDcalculated

def SpeedGotohomeNHigh(SpeedIVa, base, level):
    SpeedIV = (SpeedIVa * 2) + 1
    BaseSpeed = base
    level = level
    Base2 = (2 * BaseSpeed)
    G = ((Base2 + SpeedIV)*level)
    Speedcalculated = int(((G/100)+5)* 1.1)
    return Speedcalculated

def SpeedGotohomeHigh(SpeedIVa, base, level):
    SpeedIV = (SpeedIVa * 2) + 1
    BaseSpeed = base
    level = level
    Base2 = (2 * BaseSpeed)
    G = ((Base2 + SpeedIV)*level)
    Speedcalculated = int(((G/100)+5))
    return Speedcalculated

def SpeedGotohomeLow(SpeedIVa, base, level):
    SpeedIV = (SpeedIVa * 2) + 1
    BaseSpeed = base
    level = level
    Base2 = (2 * BaseSpeed)
    G = ((Base2 + SpeedIV)*level)
    Speedcalculated = int(((G/100)+5))
    return Speedcalculated

def SpeedGotohomeNLow(SpeedIVa, base, level):
    SpeedIV = (SpeedIVa * 2) + 1
    BaseSpeed = base
    level = level
    Base2 = (2 * BaseSpeed)
    G = ((Base2 + SpeedIV)*level)
    Speedcalculated = int(((G/100)+5)* 0.9)
    return Speedcalculated

async def gotohome(self, pokenamez):
    pokename = pokenamez
    
    if pokename == "Farfetch'd":
        pokename = "Farfetch''d"
    if pokename == "Sirfetch'd":
        pokename = "Sirfetch''d"
    
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            if pokename == "Farfetch'd":
                prerow = dict(await connection.fetchrow("SELECT * FROM pokedex WHERE name = 'Farfetch''d';"))
                row = list(prerow.values())
                pokeHp = int(row[5])
                pokeAtk = int(row[6])
                pokeDef = int(row[7])
                pokeSpA = int(row[8])
                pokeSPD = int(row[9])
                pokeSpeed = int(row[10])
                return (pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed)
            else:
                prerow = dict(await connection.fetchrow("SELECT * FROM pokedex WHERE name = '"+str(pokename)+"';"))
                row = list(prerow.values())
                pokeHp = int(row[5])
                pokeAtk = int(row[6])
                pokeDef = int(row[7])
                pokeSpA = int(row[8])
                pokeSPD = int(row[9])
                pokeSpeed = int(row[10])
                return (pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed)

async def gotohomeAlolan(self, pokenamez):
    pokename = pokenamez
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM alolapokedex WHERE name = '"+str(pokename)+"';"))
            row = list(prerow.values())
            pokeHp = int(row[5])
            pokeAtk = int(row[6])
            pokeDef = int(row[7])
            pokeSpA = int(row[8])
            pokeSPD = int(row[9])
            pokeSpeed = int(row[10])
            return (pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed)

async def GotohomeGalar(self, pokenamez):
    pokename = pokenamez
    
    if pokename == "Farfetch'd":
        pokename = "Farfetch''d"
    
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            if pokename == "Farfetch'd":
                prerow = dict(await connection.fetchrow("SELECT * FROM galarpokedex WHERE name = 'Farfetch''d';"))
                row = list(prerow.values())
                pokeHp = int(row[5])
                pokeAtk = int(row[6])
                pokeDef = int(row[7])
                pokeSpA = int(row[8])
                pokeSPD = int(row[9])
                pokeSpeed = int(row[10])
                return (pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed)
            else:
                prerow = dict(await connection.fetchrow("SELECT * FROM galarpokedex WHERE name = '"+str(pokename)+"';"))
                row = list(prerow.values())
                pokeHp = int(row[5])
                pokeAtk = int(row[6])
                pokeDef = int(row[7])
                pokeSpA = int(row[8])
                pokeSPD = int(row[9])
                pokeSpeed = int(row[10])
                return (pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed)

def setup(client):
    client.add_cog(Pokego(client))
