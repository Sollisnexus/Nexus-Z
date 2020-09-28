import discord
import string
import math
import csv
import os
import itertools
import time
from discord.ext import commands

class Pokego(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Pokego online.')

    # Commands
    @commands.command()
    async def godex(self, ctx):
        responce = str(ctx.message.content)
        if responce.startswith(str(ctx.prefix)+"godex"):
            content = responce.split()
            Name = string.capwords(content[1])
            namea = "Alolan"
            namegl = "Galarian"
            if Name == namea:
                GaName = string.capwords(content[2])
                Listofalola = ["Rattata","Raticate","Raichu","Sandshrew","Sandslash","Vulpix","Ninetails","Diglett","Dugtrio","Meowth","Persian","Geodude","Graveler",
                               "Golem","Grimer","Muk","Exeggutor","Marowak"]
                if GaName in Listofalola:
                    AName = GaName
                    result = aloladex(str(AName))
                    embed = discord.Embed(title= result[0] + "   Alolan " + AName + "   " + result[2] , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Alolan/Shiny/"+AName+".png")
                    embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\n", inline=True)
                    embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 40, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                    embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.message.delete()
                    await ctx.send(embed=embed)
                else:
                    await ctx.send('This Alolan Pokémon does not exist!')
            elif Name == namegl:
                GlName = string.capwords(content[2])
                Listofgalar = ["Meowth","Farfetch'result[3]","Weezing","Zigzagoon","Linoone","Darumaka","Darmanitan","Stunfisk"]
                if GlName in Listofgalar:
                    result = galardex(str(GlName))
                    if GlName == "Farfetch'result[3]":
                        embed = discord.Embed(title= result[0] + "   Galarian " + GlName + "   " + result[2] , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/Shiny/Farfetchd.png")
                        embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\n", inline=True)
                        embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 40, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                        embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(title= result[0] + "   Galarian " + GlName + "   " + result[2] , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/Shiny/"+GlName+".png")
                        embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\n", inline=True)
                        embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 40, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                        embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.message.delete()
                        await ctx.send(embed=embed)
                else:
                    await ctx.send('This Galarian Pokémon does not exist!')
            else:
                if Name == "Mr":
                    if content[2] == "mime":
                        Name = "Mrmime"
                        result = dex(str(Name))
                        embed = discord.Embed(title= result[0] + "    Mr. Mime   " + result[2] , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                        embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\n", inline=True)
                        embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 40, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                        embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.message.delete()
                        await ctx.send('This Pokémon does not exist!')
                elif Name == "Mime":
                    Name = "Mimejr"
                    result = dex(str(Name))
                    embed = discord.Embed(title= result[0] + "    Mime Jr.   " + result[2] , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\n", inline=True)
                    embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 40, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                    embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.message.delete()
                    await ctx.send(embed=embed)
                elif Name.startswith("Nidoran\U00002640"):
                    Name = "Nidoranf"
                    result = dex(str(Name))
                    embed = discord.Embed(title= result[0] + "   Nidoran♀️   " + result[2] , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\n", inline=True)
                    embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 40, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                    embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.message.delete()
                    await ctx.send(embed=embed)
                elif Name.startswith("Nidoran\U00002642"):
                    Name = "Nidoranm"
                    result = dex(str(Name))
                    embed = discord.Embed(title= result[0] + "   Nidoran♂️   " + result[2] , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\n", inline=True)
                    embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 40, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                    embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.message.delete()
                    await ctx.send(embed=embed)
                elif Name == "Armored":
                    tname = content[2].capitalize()
                    if tname == "Mewtwo":
                        TrName = "Armoredmewtwo"
                        result = dex(str(TrName))
                        embed = discord.Embed(title= result[0] + "   Armored Mewtwo   " + result[2] , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://gamepress.gg/pokemongo/sites/pokemongo/files/2019-07/armored-mewtwo.png")
                        embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\n", inline=True)
                        embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 40, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                        embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.message.delete()
                        await ctx.send("Only Armored Mewtwo exists...     Ţ̸̧̖̘̒͐͌e̷̳͕͋a̸̗̫̓ḿ̷̡͙̱̊̚ ̵̘̖̼̪̦̟̏̂̀̓͌͘͝R̴̨̨͈̰̼̳̜̓̈̓o̷͙͠c̶͔̼̀̍̄̃̔͝ķ̸̦̜͚͂̅̀e̶̡̢̡̘̜̒̕t̷͎̼̙̀͌̊̂̕̚")
                elif Name == "Origin":
                    tname = content[2].capitalize()
                    if tname == "Giratina":
                        TrName = "Origingiratina"
                        result = dex(str(TrName))
                        embed = discord.Embed(title= result[0] + "   Origin Giratina   " + result[2] , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Ogiratina.png")
                        embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\n", inline=True)
                        embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 40, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                        embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.message.delete()
                        await ctx.send("Only Origin Giratina exists...")
                elif Name == "Wormadam":
                    StName = "Wormadams"
                    TrName = "Wormadamt"
                    result = dex(str(Name))
                    embed = discord.Embed(title= result[0] + "   " + Name + "   " + result[2] , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\n", inline=True)
                    embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 40, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                    embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.message.delete()
                    await ctx.send(embed=embed)

                    result = dex(str(StName))
                    embed = discord.Embed(title= result[0] + "   " + Name + "   " + result[2] , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+StName+".png")
                    embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\n", inline=True)
                    embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 40, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                    embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)

                    result = dex(str(TrName))
                    embed = discord.Embed(title= result[0] + "   " + Name + "   " + result[2] , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+TrName+".png")
                    embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\n", inline=True)
                    embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 40, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                    embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Deoxys":
                    AName = "Adeoxys"
                    DName = "Ddeoxys"
                    SName = "Sdeoxys"
                    result = dex(str(Name))
                    embed = discord.Embed(title= result[0] + "   " + Name + " Normal Forme   " + result[2] , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\n", inline=True)
                    embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 40, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                    embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.message.delete()
                    await ctx.send(embed=embed)

                    result = dex(str(AName))
                    embed = discord.Embed(title= result[0] + "   " + Name + " Attack Form   " + result[2] , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+AName+".png")
                    embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\n", inline=True)
                    embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 40, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                    embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)

                    result = dex(str(DName))
                    embed = discord.Embed(title= result[0] + "   " + Name + " Defense Form   " + result[2] , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+DName+".png")
                    embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\n", inline=True)
                    embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 40, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                    embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)

                    result = dex(str(SName))
                    embed = discord.Embed(title= result[0] + "   " + Name + " Speed Form   " + result[2] , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+SName+".png")
                    embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\n", inline=True)
                    embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 40, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                    embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Giratina":
                    OName = "Ogiratina"
                    result = dex(str(Name))
                    embed = discord.Embed(title= result[0] + "   " + Name + " Altered Forme   " + result[2] , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\n", inline=True)
                    embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 40, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                    embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)

                    result = dex(str(OName))
                    embed = discord.Embed(title= result[0] + "   " + Name + " Origin Forme   " + result[2] , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+OName+".png")
                    embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\n", inline=True)
                    embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 40, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                    embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.message.delete()
                    await ctx.send(embed=embed)
                else:
                    result = dex(str(Name))
                    if result == None:

                        await ctx.send('This Pokémon does not exist!')
                    elif result != None:
                        embed = discord.Embed(title= result[0] + "   " + Name + "   " + result[2] , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                        embed.add_field(name="Misc. info", value="**"+result[1]+"**\nHeight/Weight: \n**"+result[3]+"m** / **"+result[4]+"kg**\n", inline=True)
                        embed.add_field(name="Go Stats", value="Max CP: **"+ result[5] +"**\n(Lvl 40, 100% IV)\nAtk: **"+result[6]+"**\nDef: **"+result[7]+"**\nSta: **"+result[8]+"**\n", inline=True)
                        embed.add_field(name="Shiny",value="Shiny Available?: **"+result[9]+"**\nTimed Shiny?: **"+result[10]+"**\nRaid Shiny?: **"+result[11]+"**\nEgg Shiny?: **"+result[12]+"**\nResearch Shiny?: **"+result[13]+"**\n",inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.message.delete()
                        await ctx.send(embed=embed)

    @commands.command()
    async def gopvp(self, ctx):
        responce = str(ctx.message.content)
        if responce.startswith(str(ctx.prefix)+"gopvp"):
            content = responce.split()
            name = content[1]
            Cname = name.capitalize()
            if Cname == "Alolan":
                name = content[2]
                Cname = name.capitalize()
                ylvl = float(content[3])
                AIV = int(content[4])
                DIV = int(content[5])
                SIV = int(content[6])
                # msg = await ctx.send("Loading please wait...")
                before = time.monotonic()
                print("Time check")
                ping = (time.monotonic() - before) * 1000
                print(ping)
                results = AlolanMaintoGo(name,ylvl,AIV,DIV,SIV)
                if results == None:
                    await ctx.message.delete()
                    await ctx.send("This Pokemon does not exist")
                else:
                    ping2 = (time.monotonic() - before) * 1000
                    print("Result time")
                    print(ping2)
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
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Alolan/Shiny/"+Cname+".png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
                            await ctx.send(embed=embed)
                        else:
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= "Alolan " + Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Alolan/Shiny/"+Cname+".png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
                            await ctx.send(embed=embed)
                    else:
                        UP = round(((YPKM[2] / UPKM[2])*100),2)
                        if UP > 100.00:
                            UP = "~~"+str(UP)+"~~"
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= "Alolan " + Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Alolan/Shiny/"+Cname+".png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
                            await ctx.send(embed=embed)
                        else:
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= "Alolan " + Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Alolan/Shiny/"+Cname+".png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
                            await ctx.send(embed=embed)
            elif Cname == "Galarian":
                name = content[2]
                Cname = name.capitalize()
                ylvl = float(content[3])
                AIV = int(content[4])
                DIV = int(content[5])
                SIV = int(content[6])
                # msg = await ctx.send("Loading please wait...")
                before = time.monotonic()
                print("Time check")
                ping = (time.monotonic() - before) * 1000
                print(ping)
                results = GalarianMaintoGo(name,ylvl,AIV,DIV,SIV)
                if results == None:
                    await ctx.message.delete()
                    await ctx.send("This Pokemon does not exist")
                else:
                    ping2 = (time.monotonic() - before) * 1000
                    print("Result time")
                    print(ping2)
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
                            embed = discord.Embed(title= "Galarian " + Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/Shiny/"+Cname+".png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
                            await ctx.send(embed=embed)
                        else:
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= "Galarian " + Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/Shiny/"+Cname+".png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
                            await ctx.send(embed=embed)
                    else:
                        UP = round(((YPKM[2] / UPKM[2])*100),2)
                        if UP > 100.00:
                            UP = "~~"+str(UP)+"~~"
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= "Galarian " + Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/Shiny/"+Cname+".png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
                            await ctx.send(embed=embed)
                        else:
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= "Galarian " + Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/Shiny/"+Cname+".png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
                            await ctx.send(embed=embed)
            elif Cname == "Mega":
                name = content[2]
                Mname = name.capitalize()
                if Mname == "Charizard" or Mname == "Mewtwo":
                    if content[3] == "X":
                        if Mname == "Charizard":
                            Mname = "Xcharizard"
                            ylvl = float(content[4])
                            AIV = int(content[5])
                            DIV = int(content[6])
                            SIV = int(content[7])
                            before = time.monotonic()
                            print("Time check")
                            ping = (time.monotonic() - before) * 1000
                            print(ping)
                            results = MegaMaintoGo(Mname,ylvl,AIV,DIV,SIV)
                            if results == None:
                                await ctx.message.delete()
                                await ctx.send("This Pokemon does not exist")
                            else:
                                ping2 = (time.monotonic() - before) * 1000
                                print("Result time")
                                print(ping2)
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
                                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/Shiny/CharizardX.png")
                                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                        await ctx.message.delete()
                                        await ctx.send(embed=embed)
                                    else:
                                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                                        embed = discord.Embed(title= "Mega Charizard X's PvP Comparison"  , description="", color=0x2962FF)
                                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/Shiny/CharizardX.png")
                                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                        await ctx.message.delete()
                                        await ctx.send(embed=embed)
                                else:
                                    UP = round(((YPKM[2] / UPKM[2])*100),2)
                                    if UP > 100.00:
                                        UP = "~~"+str(UP)+"~~"
                                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                                        embed = discord.Embed(title= "Mega Charizard X's PvP Comparison"  , description="", color=0x2962FF)
                                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/Shiny/CharizardX.png")
                                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                        await ctx.message.delete()
                                        await ctx.send(embed=embed)
                                    else:
                                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                                        embed = discord.Embed(title= "Mega Charizard X's PvP Comparison"  , description="", color=0x2962FF)
                                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/Shiny/CharizardX.png")
                                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                        await ctx.message.delete()
                                        await ctx.send(embed=embed)
                        elif Mname == "Mewtwo":
                            Mname = "Xmewtwo"
                            ylvl = float(content[4])
                            AIV = int(content[5])
                            DIV = int(content[6])
                            SIV = int(content[7])
                            before = time.monotonic()
                            print("Time check")
                            ping = (time.monotonic() - before) * 1000
                            print(ping)
                            results = MegaMaintoGo(Mname,ylvl,AIV,DIV,SIV)
                            if results == None:
                                await ctx.message.delete()
                                await ctx.send("This Pokemon does not exist")
                            else:
                                ping2 = (time.monotonic() - before) * 1000
                                print("Result time")
                                print(ping2)
                                YPKM = results[0]
                                UPKM = results[2]
                                MPKM = results[3]
                                MP = round(((YPKM[2] / MPKM[2])*100),2)
                                UP = round(((YPKM[2] / UPKM[2])*100),2)

                                if UP > 100.00:
                                    UP = "~~"+str(UP)+"~~"
                                    embed = discord.Embed(title= "Mega Mewtwo X's PvP Comparison"  , description="", color=0x2962FF)
                                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/Shiny/MewtwoX.png")
                                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP%  U / M: **"+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                                    #embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                    await ctx.message.delete()
                                    await ctx.send(embed=embed)
                                else:
                                    embed = discord.Embed(title= "Mega Mewtwo X's PvP Comparison"  , description="", color=0x2962FF)
                                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/Shiny/MewtwoX.png")
                                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP%  U / M: **"+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                                    #embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                    await ctx.message.delete()
                                    await ctx.send(embed=embed)
                    elif content[3] == "Y":
                        if Mname == "Charizard":
                            Mname = "Ycharizard"
                            ylvl = float(content[4])
                            AIV = int(content[5])
                            DIV = int(content[6])
                            SIV = int(content[7])
                            before = time.monotonic()
                            print("Time check")
                            ping = (time.monotonic() - before) * 1000
                            print(ping)
                            results = MegaMaintoGo(Mname,ylvl,AIV,DIV,SIV)
                            if results == None:
                                await ctx.message.delete()
                                await ctx.send("This Pokemon does not exist")
                            else:
                                ping2 = (time.monotonic() - before) * 1000
                                print("Result time")
                                print(ping2)
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
                                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/Shiny/CharizardY.png")
                                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                        await ctx.message.delete()
                                        await ctx.send(embed=embed)
                                    else:
                                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                                        embed = discord.Embed(title= "Mega Charizard Y's PvP Comparison" , description="", color=0x2962FF)
                                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/Shiny/CharizardY.png")
                                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                        await ctx.message.delete()
                                        await ctx.send(embed=embed)
                                else:
                                    UP = round(((YPKM[2] / UPKM[2])*100),2)
                                    if UP > 100.00:
                                        UP = "~~"+str(UP)+"~~"
                                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                                        embed = discord.Embed(title= "Mega Charizard Y's PvP Comparison" , description="", color=0x2962FF)
                                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/Shiny/CharizardY.png")
                                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                        await ctx.message.delete()
                                        await ctx.send(embed=embed)
                                    else:
                                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                                        embed = discord.Embed(title= "Mega Charizard Y's PvP Comparison" , description="", color=0x2962FF)
                                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/Shiny/CharizardY.png")
                                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                        await ctx.message.delete()
                                        await ctx.send(embed=embed)
                        elif Mname == "Mewtwo":
                            Mname = "Ymewtwo"
                            ylvl = float(content[4])
                            AIV = int(content[5])
                            DIV = int(content[6])
                            SIV = int(content[7])
                            before = time.monotonic()
                            print("Time check")
                            ping = (time.monotonic() - before) * 1000
                            print(ping)
                            results = MegaMaintoGo(Mname,ylvl,AIV,DIV,SIV)
                            if results == None:
                                await ctx.message.delete()
                                await ctx.send("This Pokemon does not exist")
                            else:
                                ping2 = (time.monotonic() - before) * 1000
                                print("Result time")
                                print(ping2)
                                YPKM = results[0]
                                UPKM = results[2]
                                MPKM = results[3]
                                MP = round(((YPKM[2] / MPKM[2])*100),2)
                                UP = round(((YPKM[2] / UPKM[2])*100),2)
                                if UP > 100.00:
                                    UP = "~~"+str(UP)+"~~"
                                    embed = discord.Embed(title= "Mega Mewtwo Y's PvP Comparison"  , description="", color=0x2962FF)
                                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/Shiny/MewtwoY.png")
                                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP%  U / M: **"+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                                    #embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                    await ctx.message.delete()
                                    await ctx.send(embed=embed)
                                else:
                                    embed = discord.Embed(title= "Mega Mewtwo Y's PvP Comparison"  , description="", color=0x2962FF)
                                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/Shiny/MewtwoY.png")
                                    embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP%  U / M: **"+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                                    #embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                                    embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                                    embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                    await ctx.message.delete()
                                    await ctx.send(embed=embed)
                if Mname == "Gyarados" or Mname == "Heracross" or Mname == "Tyranitar" or Mname == "Salamence" or Mname == "Metagross" or Mname == "Latias" or Mname == "Latios" or Mname == "Rayquaza" or Mname == "Garchomp":
                    ylvl = float(content[3])
                    AIV = int(content[4])
                    DIV = int(content[5])
                    SIV = int(content[6])
                    before = time.monotonic()
                    print("Time check")
                    ping = (time.monotonic() - before) * 1000
                    print(ping)
                    results = MegaMaintoGo(Mname,ylvl,AIV,DIV,SIV)
                    if results == None:
                        await ctx.message.delete()
                        await ctx.send("This Pokemon does not exist")
                    else:
                        ping2 = (time.monotonic() - before) * 1000
                        print("Result time")
                        print(ping2)
                        YPKM = results[0]
                        UPKM = results[2]
                        MPKM = results[3]
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        UP = round(((YPKM[2] / UPKM[2])*100),2)

                        if UP > 100.00:
                            UP = "~~"+str(UP)+"~~"
                            embed = discord.Embed(title= "Mega "+ Mname +"'s PvP Comparison"  , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/Shiny/"+Mname+".png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP%  U / M: **"+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            #embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
                            await ctx.send(embed=embed)
                        else:
                            embed = discord.Embed(title= "Mega "+ Mname +"'s PvP Comparison"  , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/Shiny/"+Mname+".png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP%  U / M: **"+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            #embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
                            await ctx.send(embed=embed)
                elif Mname != "Charizard" and "Mewtwo":
                    ylvl = float(content[3])
                    AIV = int(content[4])
                    DIV = int(content[5])
                    SIV = int(content[6])
                    before = time.monotonic()
                    print("Time check")
                    ping = (time.monotonic() - before) * 1000
                    print(ping)
                    results = MegaMaintoGo(Mname,ylvl,AIV,DIV,SIV)
                    if results == 0:
                        await ctx.message.delete()
                        await ctx.send("This Pokemon does not exist")
                    else:
                        ping2 = (time.monotonic() - before) * 1000
                        print("Result time")
                        print(ping2)
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
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/Shiny/"+Mname+".png")
                                embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                                embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                                embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                                embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                await ctx.message.delete()
                                await ctx.send(embed=embed)
                            else:
                                MP = round(((YPKM[2] / MPKM[2])*100),2)
                                embed = discord.Embed(title= "Mega " + Mname + "'s PvP Comparison" , description="", color=0x2962FF)
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/Shiny/"+Mname+".png")
                                embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                                embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                                embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                                embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                await ctx.message.delete()
                                await ctx.send(embed=embed)
                        else:
                            UP = round(((YPKM[2] / UPKM[2])*100),2)
                            if UP > 100.00:
                                UP = "~~"+str(UP)+"~~"
                                MP = round(((YPKM[2] / MPKM[2])*100),2)
                                embed = discord.Embed(title= "Mega " + Mname + "'s PvP Comparison" , description="", color=0x2962FF)
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/Shiny/"+Mname+".png")
                                embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                                embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                                embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                                embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                await ctx.message.delete()
                                await ctx.send(embed=embed)
                            else:
                                MP = round(((YPKM[2] / MPKM[2])*100),2)
                                embed = discord.Embed(title= "Mega " + Mname + "'s PvP Comparison" , description="", color=0x2962FF)
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/Shiny/"+Mname+".png")
                                embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                                embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                                embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                                embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                await ctx.message.delete()
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
                    before = time.monotonic()
                    print("Time check")
                    ping = (time.monotonic() - before) * 1000
                    print(ping)
                    results = MaintoGo(Aname,ylvl,AIV,DIV,SIV)
                    ping2 = (time.monotonic() - before) * 1000
                    print("Result time")
                    print(ping2)
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
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Aname+".png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
                            await ctx.send(embed=embed)
                        else:
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= "Armored " + Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Aname+".png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
                            await ctx.send(embed=embed)
                    else:
                        UP = round(((YPKM[2] / UPKM[2])*100),2)
                        if UP > 100.00:
                            UP = "~~"+str(UP)+"~~"
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= "Armored " + Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Aname+".png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
                            await ctx.send(embed=embed)
                        else:
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= "Armored " + Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Aname+".png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
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
                    before = time.monotonic()
                    print("Time check")
                    ping = (time.monotonic() - before) * 1000
                    print(ping)
                    results = MaintoGo(Aname,ylvl,AIV,DIV,SIV)
                    ping2 = (time.monotonic() - before) * 1000
                    print("Result time")
                    print(ping2)
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
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Ogiratina.png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
                            await ctx.send(embed=embed)
                        else:
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= Cname + " Origin Forme's PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Ogiratina.png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
                            await ctx.send(embed=embed)
                    else:
                        UP = round(((YPKM[2] / UPKM[2])*100),2)
                        if UP > 100.00:
                            UP = "~~"+str(UP)+"~~"
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= Cname + " Origin Forme's PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Ogiratina.png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
                            await ctx.send(embed=embed)
                        else:
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= Cname + " Origin Forme's PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Ogiratina.png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
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
                before = time.monotonic()
                print("Time check")
                ping = (time.monotonic() - before) * 1000
                print(ping)
                results = MaintoGo(Aname,ylvl,AIV,DIV,SIV)
                ping2 = (time.monotonic() - before) * 1000
                print("Result time")
                print(ping2)
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
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Adeoxys.png")
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= Cname + " Attack Forme's PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Adeoxys.png")
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.message.delete()
                        await ctx.send(embed=embed)
                else:
                    UP = round(((YPKM[2] / UPKM[2])*100),2)
                    if UP > 100.00:
                        UP = "~~"+str(UP)+"~~"
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= Cname + " Attack Forme's PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Adeoxys.png")
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= Cname + " Attack Forme's PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Adeoxys.png")
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.message.delete()
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
                before = time.monotonic()
                print("Time check")
                ping = (time.monotonic() - before) * 1000
                print(ping)
                results = MaintoGo(Aname,ylvl,AIV,DIV,SIV)
                ping2 = (time.monotonic() - before) * 1000
                print("Result time")
                print(ping2)
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
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Ddeoxys.png")
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= Cname + " Defense Forme's PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Ddeoxys.png")
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.message.delete()
                        await ctx.send(embed=embed)
                else:
                    UP = round(((YPKM[2] / UPKM[2])*100),2)
                    if UP > 100.00:
                        UP = "~~"+str(UP)+"~~"
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= Cname + " Defense Forme's PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Ddeoxys.png")
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= Cname + " Defense Forme's PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Ddeoxys.png")
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.message.delete()
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
                before = time.monotonic()
                print("Time check")
                ping = (time.monotonic() - before) * 1000
                print(ping)
                results = MaintoGo(Aname,ylvl,AIV,DIV,SIV)
                ping2 = (time.monotonic() - before) * 1000
                print("Result time")
                print(ping2)
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
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Sdeoxys.png")
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= Cname + " Speed Forme's PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Sdeoxys.png")
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.message.delete()
                        await ctx.send(embed=embed)
                else:
                    UP = round(((YPKM[2] / UPKM[2])*100),2)
                    if UP > 100.00:
                        UP = "~~"+str(UP)+"~~"
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= Cname + " Speed Forme's PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Sdeoxys.png")
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        MP = round(((YPKM[2] / MPKM[2])*100),2)
                        embed = discord.Embed(title= Cname + " Speed Forme's PvP Comparison" , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Sdeoxys.png")
                        embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                        embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                        embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                        embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        await ctx.message.delete()
                        await ctx.send(embed=embed)
            elif Cname != "Galarian":
                name = content[1]
                Cname = content[1].capitalize()
                ylvl = float(content[2])
                AIV = int(content[3])
                DIV = int(content[4])
                SIV = int(content[5])
                # msg = await ctx.send("Loading please wait...")
                before = time.monotonic()
                print("Time check")
                ping = (time.monotonic() - before) * 1000
                print(ping)
                results = MaintoGo(name,ylvl,AIV,DIV,SIV)
                if results == None:
                    await ctx.send("This Pokemon does not exist")
                else:
                    ping2 = (time.monotonic() - before) * 1000
                    print("Result time")
                    print(ping2)
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
                            embed = discord.Embed(title= Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Cname+".png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
                            await ctx.send(embed=embed)
                        else:
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Cname+".png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
                            await ctx.send(embed=embed)
                    else:
                        UP = round(((YPKM[2] / UPKM[2])*100),2)
                        if UP > 100.00:
                            UP = "~~"+str(UP)+"~~"
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Cname+".png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
                            await ctx.send(embed=embed)
                        else:
                            MP = round(((YPKM[2] / MPKM[2])*100),2)
                            embed = discord.Embed(title= Cname + "'s PvP Comparison" , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Cname+".png")
                            embed.add_field(name="Your Pokemon:", value="CP: **"+str(YPKM[0])+ "**\nLevel: **" +str(YPKM[1])+ "**\nPVP% G / U / M: \n**"+str(GP)+"% / "+str(UP)+"% / "+str(MP)+"%**"+"\nAtk IV: **"+str(YPKM[3])+"**\nDef IV: **"+str(YPKM[4])+"**\nHP IV: **"+ str(YPKM[5]) + "**" , inline=False)
                            embed.add_field(name="Great League:", value="CP: **"+str(GPKM[0])+ "**\nLevel: **" +str(GPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(GPKM[3])+"**\nDef IV: **"+str(GPKM[4])+"**\nHP IV: **" +str(GPKM[5]) + "**", inline=False)
                            embed.add_field(name="Ultra League:",value="CP: **"+str(UPKM[0])+ "**\nLevel: **" +str(UPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(UPKM[3])+"**\nDef IV: **"+str(UPKM[4])+"**\nHP IV: **" +str(UPKM[5])+ "**", inline=False)
                            embed.add_field(name="Master League:",value="CP: **"+str(MPKM[0])+ "**\nLevel: **" +str(MPKM[1])+ "**\nPVP%: **100%** \nAtk IV: **"+str(MPKM[3])+"**\nDef IV: **"+str(MPKM[4])+"**\nHP IV: **" +str(MPKM[5])+ "**",inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.message.delete()
                            await ctx.send(embed=embed)

    @commands.command()
    async def gorocket(self, ctx):
        responce = str(ctx.message.content)
        if responce.startswith(str(ctx.prefix)+"gorocket"):
            content = responce.split()
            name = content[1].capitalize()
            if name == "Poison":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + " Grunt's Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://images.dexerto.com/uploads/2019/12/04121426/Pokemon-Go-Team-Rocket-Grunt-Types.jpg")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Normal":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + " Grunt's Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://images.dexerto.com/uploads/2019/12/04121426/Pokemon-Go-Team-Rocket-Grunt-Types.jpg")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Dragon":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + " Grunt's Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://images.dexerto.com/uploads/2019/12/04121426/Pokemon-Go-Team-Rocket-Grunt-Types.jpg")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Water":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + " Grunt's Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://images.dexerto.com/uploads/2019/12/04121426/Pokemon-Go-Team-Rocket-Grunt-Types.jpg")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Grass":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + " Grunt's Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://images.dexerto.com/uploads/2019/12/04121426/Pokemon-Go-Team-Rocket-Grunt-Types.jpg")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Flying":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + " Grunt's Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://images.dexerto.com/uploads/2019/12/04121426/Pokemon-Go-Team-Rocket-Grunt-Types.jpg")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Fire":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + " Grunt's Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://images.dexerto.com/uploads/2019/12/04121426/Pokemon-Go-Team-Rocket-Grunt-Types.jpg")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Bug":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + " Grunt's Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://images.dexerto.com/uploads/2019/12/04121426/Pokemon-Go-Team-Rocket-Grunt-Types.jpg")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Ground":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + " Grunt's Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://images.dexerto.com/uploads/2019/12/04121426/Pokemon-Go-Team-Rocket-Grunt-Types.jpg")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Rock":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + " Grunt's Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://images.dexerto.com/uploads/2019/12/04121426/Pokemon-Go-Team-Rocket-Grunt-Types.jpg")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Ghost":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + " Grunt's Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://images.dexerto.com/uploads/2019/12/04121426/Pokemon-Go-Team-Rocket-Grunt-Types.jpg")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Fighting":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + " Grunt's Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://images.dexerto.com/uploads/2019/12/04121426/Pokemon-Go-Team-Rocket-Grunt-Types.jpg")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Electric":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + " Grunt's Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://images.dexerto.com/uploads/2019/12/04121426/Pokemon-Go-Team-Rocket-Grunt-Types.jpg")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Psychic":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + " Grunt's Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://images.dexerto.com/uploads/2019/12/04121426/Pokemon-Go-Team-Rocket-Grunt-Types.jpg")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Dark":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + " Grunt's Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://images.dexerto.com/uploads/2019/12/04121426/Pokemon-Go-Team-Rocket-Grunt-Types.jpg")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Fairy":
                await ctx.message.delete()
                await ctx.send("Team Rocket does not have a Fairy type line-up that exists... Ţ̸̧̖̘̒͐͌e̷̳͕͋a̸̗̫̓ḿ̷̡͙̱̊̚ ̵̘̖̼̪̦̟̏̂̀̓͌͘͝R̴̨̨͈̰̼̳̜̓̈̓o̷͙͠c̶͔̼̀̍̄̃̔͝ķ̸̦̜͚͂̅̀e̶̡̢̡̘̜̒̕t̷͎̼̙̀͌̊̂̕̚")
            elif name == "Ice":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + " Grunt's Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://images.dexerto.com/uploads/2019/12/04121426/Pokemon-Go-Team-Rocket-Grunt-Types.jpg")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Steel":
                await ctx.message.delete()
                await ctx.send("Team Rocket does not have a Steel type line-up that exists... Ţ̸̧̖̘̒͐͌e̷̳͕͋a̸̗̫̓ḿ̷̡͙̱̊̚ ̵̘̖̼̪̦̟̏̂̀̓͌͘͝R̴̨̨͈̰̼̳̜̓̈̓o̷͙͠c̶͔̼̀̍̄̃̔͝ķ̸̦̜͚͂̅̀e̶̡̢̡̘̜̒̕t̷͎̼̙̀͌̊̂̕̚")
            elif name == "Ace":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + " Grunt's Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://images.dexerto.com/uploads/2019/12/04121426/Pokemon-Go-Team-Rocket-Grunt-Types.jpg")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Arlo":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + "'s Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://pokemongohub.net/wp-content/uploads/2019/10/EF4o-JEW4AAjqDy.jpg")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Cliff":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + "'s Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://pokemongohub.net/wp-content/uploads/2019/10/EF4oC68W4AAf-J9-696x348.jpg")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Sierra":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + "'s Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://pokemongohub.net/wp-content/uploads/2019/10/EF4p4lBWoA0MDdO-696x348.jpg")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Jessie":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + "'s Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://cdn.bulbagarden.net/upload/6/64/VSJessie_GO.png")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "James":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + "'s Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://cdn.bulbagarden.net/upload/2/22/VSJames_GO.png")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Decoy":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + "'s Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://images.dexerto.com/uploads/2019/12/04121426/Pokemon-Go-Team-Rocket-Grunt-Types.jpg")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif name == "Giovanni":
                Rocketdata = Rocketlookup(name)
                embed = discord.Embed(title= name + "'s Current and Past Shadow Pokemon" , description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://cdn.bulbagarden.net/upload/f/f3/VSGiovanni_GO.png")
                embed.add_field(name="First Pokemon:", value=str(Rocketdata[0]), inline=True)
                embed.add_field(name="Second Pokemon:", value=str(Rocketdata[1]), inline=True)
                embed.add_field(name="Third Pokemon:",value=str(Rocketdata[2]), inline=True)
                embed.add_field(name="Reward Pokemon:",value=str(Rocketdata[3]),inline=True)
                embed.add_field(name="Notes: ",value="**Bold** = Shiny Chance\n__*This*__ = Current Rotation\nThis Data is based on current and previous battle sets and rewards, may not represent the current rotation." ,inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=embed)

    @commands.command()
    async def gohundo(self, ctx):
        responce = str(ctx.message.content)
        if responce.startswith(str(ctx.prefix)+"gohundo"):
            content = responce.split()
            name = content[1]
            Cname = name.capitalize()
            if Cname == "Alolan":
                name = content[2]
                Cname = name.capitalize()
                result = PokemonHundoAlolan(name)
                Hundo = discord.Embed(title= "Alolan " + Cname + "'s Hundo Chart" , description="", color=0x2962FF)
                Hundo.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Alolan/Shiny/"+Cname+".png")
                Hundo.add_field(name="Level to 1-10:", value="Level 1:  **"+str(result[0])+"**\nLevel 2:  **"+str(result[1])+"**\nLevel 3:  **"+str(result[2])+"**\nLevel 4:  **"+str(result[3])+"**\nLevel 5:  **"+str(result[4])+"**\nLevel 6:  **"+str(result[5])+"**\nLevel 7:  **"+str(result[6])+"**\n Level 8:  **"+str(result[7])+"**\nLevel 9:  **"+str(result[8])+"**\nLevel 10:  **"+str(result[9])+"**", inline=True)
                Hundo.add_field(name="Level to 11-20:", value="Level 11:  **"+str(result[10])+"**\nLevel 12:  **"+str(result[11])+"**\nLevel 13:  **"+str(result[12])+"**\nLevel 14:  **"+str(result[13])+"**\nLevel 15:  **"+str(result[14])+"**\nLevel 16:  **"+str(result[15])+"**\nLevel 17:  **"+str(result[16])+"**\nLevel 18:  **"+str(result[17])+"**\nLevel 19:  **"+str(result[18])+"**\nLevel 20:  **"+str(result[19])+"**", inline=True)
                Hundo.add_field(name="\u200B", value="\u200B", inline=True)
                Hundo.add_field(name="Level to 21-30:", value="Level 21:  **"+str(result[20])+"**\nLevel 22:  **"+str(result[21])+"**\nLevel 23:  **"+str(result[22])+"**\nLevel 24:  **"+str(result[23])+"**\nLevel 25:  **"+str(result[24])+"**\nLevel 26:  **"+str(result[25])+"**\nLevel 27:  **"+str(result[26])+"**\nLevel 28:  **"+str(result[27])+"**\nLevel 29:  **"+str(result[28])+"**\nLevel 30:  **"+str(result[29])+"**", inline=True)
                Hundo.add_field(name="Level to 31-40:", value="Level 31:  **"+str(result[30])+"**\nLevel 32:  **"+str(result[31])+"**\nLevel 33:  **"+str(result[32])+"**\nLevel 34:  **"+str(result[33])+"**\nLevel 35:  **"+str(result[34])+"**\nLevel 36:  **"+str(result[35])+"**\nLevel 37:  **"+str(result[36])+"**\nLevel 38:  **"+str(result[37])+"**\nLevel 39:  **"+str(result[38])+"**\nLevel 40:  **"+str(result[39])+"**", inline=True)
                Hundo.add_field(name="\u200B", value="\u200B", inline=True)
                Hundo.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=Hundo)
            elif Cname == "Galarian":
                name = content[2]
                Cname = name.capitalize()
                result = PokemonHundoGalarian(name)
                Hundo = discord.Embed(title= "Galarian " + Cname + "'s Hundo Chart" , description="", color=0x2962FF)
                Hundo.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/Shiny/"+Cname+".png")
                Hundo.add_field(name="Level to 1-10:", value="Level 1:  **"+str(result[0])+"**\nLevel 2:  **"+str(result[1])+"**\nLevel 3:  **"+str(result[2])+"**\nLevel 4:  **"+str(result[3])+"**\nLevel 5:  **"+str(result[4])+"**\nLevel 6:  **"+str(result[5])+"**\nLevel 7:  **"+str(result[6])+"**\n Level 8:  **"+str(result[7])+"**\nLevel 9:  **"+str(result[8])+"**\nLevel 10:  **"+str(result[9])+"**", inline=True)
                Hundo.add_field(name="Level to 11-20:", value="Level 11:  **"+str(result[10])+"**\nLevel 12:  **"+str(result[11])+"**\nLevel 13:  **"+str(result[12])+"**\nLevel 14:  **"+str(result[13])+"**\nLevel 15:  **"+str(result[14])+"**\nLevel 16:  **"+str(result[15])+"**\nLevel 17:  **"+str(result[16])+"**\nLevel 18:  **"+str(result[17])+"**\nLevel 19:  **"+str(result[18])+"**\nLevel 20:  **"+str(result[19])+"**", inline=True)
                Hundo.add_field(name="\u200B", value="\u200B", inline=True)
                Hundo.add_field(name="Level to 21-30:", value="Level 21:  **"+str(result[20])+"**\nLevel 22:  **"+str(result[21])+"**\nLevel 23:  **"+str(result[22])+"**\nLevel 24:  **"+str(result[23])+"**\nLevel 25:  **"+str(result[24])+"**\nLevel 26:  **"+str(result[25])+"**\nLevel 27:  **"+str(result[26])+"**\nLevel 28:  **"+str(result[27])+"**\nLevel 29:  **"+str(result[28])+"**\nLevel 30:  **"+str(result[29])+"**", inline=True)
                Hundo.add_field(name="Level to 31-40:", value="Level 31:  **"+str(result[30])+"**\nLevel 32:  **"+str(result[31])+"**\nLevel 33:  **"+str(result[32])+"**\nLevel 34:  **"+str(result[33])+"**\nLevel 35:  **"+str(result[34])+"**\nLevel 36:  **"+str(result[35])+"**\nLevel 37:  **"+str(result[36])+"**\nLevel 38:  **"+str(result[37])+"**\nLevel 39:  **"+str(result[38])+"**\nLevel 40:  **"+str(result[39])+"**", inline=True)
                Hundo.add_field(name="\u200B", value="\u200B", inline=True)
                Hundo.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=Hundo)
            elif Cname == "Armored":
                if content[2] == "Mewtwo" or content[2] == "mewtwo":
                    Aname = "Armoredmewtwo"
                    name = content[2]
                    Cname = name.capitalize()
                    result = PokemonHundo(Aname)
                    Hundo = discord.Embed(title= "Armored " + Cname + "'s Hundo Chart" , description="", color=0x2962FF)
                    Hundo.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Aname+".png")
                    Hundo.add_field(name="Level to 1-10:", value="Level 1:  **"+str(result[0])+"**\nLevel 2:  **"+str(result[1])+"**\nLevel 3:  **"+str(result[2])+"**\nLevel 4:  **"+str(result[3])+"**\nLevel 5:  **"+str(result[4])+"**\nLevel 6:  **"+str(result[5])+"**\nLevel 7:  **"+str(result[6])+"**\n Level 8:  **"+str(result[7])+"**\nLevel 9:  **"+str(result[8])+"**\nLevel 10:  **"+str(result[9])+"**", inline=True)
                    Hundo.add_field(name="Level to 11-20:", value="Level 11:  **"+str(result[10])+"**\nLevel 12:  **"+str(result[11])+"**\nLevel 13:  **"+str(result[12])+"**\nLevel 14:  **"+str(result[13])+"**\nLevel 15:  **"+str(result[14])+"**\nLevel 16:  **"+str(result[15])+"**\nLevel 17:  **"+str(result[16])+"**\nLevel 18:  **"+str(result[17])+"**\nLevel 19:  **"+str(result[18])+"**\nLevel 20:  **"+str(result[19])+"**", inline=True)
                    Hundo.add_field(name="\u200B", value="\u200B", inline=True)
                    Hundo.add_field(name="Level to 21-30:", value="Level 21:  **"+str(result[20])+"**\nLevel 22:  **"+str(result[21])+"**\nLevel 23:  **"+str(result[22])+"**\nLevel 24:  **"+str(result[23])+"**\nLevel 25:  **"+str(result[24])+"**\nLevel 26:  **"+str(result[25])+"**\nLevel 27:  **"+str(result[26])+"**\nLevel 28:  **"+str(result[27])+"**\nLevel 29:  **"+str(result[28])+"**\nLevel 30:  **"+str(result[29])+"**", inline=True)
                    Hundo.add_field(name="Level to 31-40:", value="Level 31:  **"+str(result[30])+"**\nLevel 32:  **"+str(result[31])+"**\nLevel 33:  **"+str(result[32])+"**\nLevel 34:  **"+str(result[33])+"**\nLevel 35:  **"+str(result[34])+"**\nLevel 36:  **"+str(result[35])+"**\nLevel 37:  **"+str(result[36])+"**\nLevel 38:  **"+str(result[37])+"**\nLevel 39:  **"+str(result[38])+"**\nLevel 40:  **"+str(result[39])+"**", inline=True)
                    Hundo.add_field(name="\u200B", value="\u200B", inline=True)
                    Hundo.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.message.delete()
                    await ctx.send(embed=Hundo)
                else:
                    await ctx.message.delete()
                    await ctx.send("Only Armored Mewtwo exists...     Ţ̸̧̖̘̒͐͌e̷̳͕͋a̸̗̫̓ḿ̷̡͙̱̊̚ ̵̘̖̼̪̦̟̏̂̀̓͌͘͝R̴̨̨͈̰̼̳̜̓̈̓o̷͙͠c̶͔̼̀̍̄̃̔͝ķ̸̦̜͚͂̅̀e̶̡̢̡̘̜̒̕t̷͎̼̙̀͌̊̂̕̚")
            elif Cname == "Origin":
                if content[2] == "Giratina" or content[2] == "giratina":
                    Aname = "Origingiratina"
                    name = content[2]
                    Cname = name.capitalize()
                    result = PokemonHundo(Aname)
                    Hundo = discord.Embed(title= "Origin Forme " + Cname + "'s Hundo Chart" , description="", color=0x2962FF)
                    Hundo.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Cname+".png")
                    Hundo.add_field(name="Level to 1-10:", value="Level 1:  **"+str(result[0])+"**\nLevel 2:  **"+str(result[1])+"**\nLevel 3:  **"+str(result[2])+"**\nLevel 4:  **"+str(result[3])+"**\nLevel 5:  **"+str(result[4])+"**\nLevel 6:  **"+str(result[5])+"**\nLevel 7:  **"+str(result[6])+"**\n Level 8:  **"+str(result[7])+"**\nLevel 9:  **"+str(result[8])+"**\nLevel 10:  **"+str(result[9])+"**", inline=True)
                    Hundo.add_field(name="Level to 11-20:", value="Level 11:  **"+str(result[10])+"**\nLevel 12:  **"+str(result[11])+"**\nLevel 13:  **"+str(result[12])+"**\nLevel 14:  **"+str(result[13])+"**\nLevel 15:  **"+str(result[14])+"**\nLevel 16:  **"+str(result[15])+"**\nLevel 17:  **"+str(result[16])+"**\nLevel 18:  **"+str(result[17])+"**\nLevel 19:  **"+str(result[18])+"**\nLevel 20:  **"+str(result[19])+"**", inline=True)
                    Hundo.add_field(name="\u200B", value="\u200B", inline=True)
                    Hundo.add_field(name="Level to 21-30:", value="Level 21:  **"+str(result[20])+"**\nLevel 22:  **"+str(result[21])+"**\nLevel 23:  **"+str(result[22])+"**\nLevel 24:  **"+str(result[23])+"**\nLevel 25:  **"+str(result[24])+"**\nLevel 26:  **"+str(result[25])+"**\nLevel 27:  **"+str(result[26])+"**\nLevel 28:  **"+str(result[27])+"**\nLevel 29:  **"+str(result[28])+"**\nLevel 30:  **"+str(result[29])+"**", inline=True)
                    Hundo.add_field(name="Level to 31-40:", value="Level 31:  **"+str(result[30])+"**\nLevel 32:  **"+str(result[31])+"**\nLevel 33:  **"+str(result[32])+"**\nLevel 34:  **"+str(result[33])+"**\nLevel 35:  **"+str(result[34])+"**\nLevel 36:  **"+str(result[35])+"**\nLevel 37:  **"+str(result[36])+"**\nLevel 38:  **"+str(result[37])+"**\nLevel 39:  **"+str(result[38])+"**\nLevel 40:  **"+str(result[39])+"**", inline=True)
                    Hundo.add_field(name="\u200B", value="\u200B", inline=True)
                    Hundo.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.message.delete()
                    await ctx.send(embed=Hundo)
                else:
                    await ctx.message.delete()
                    await ctx.send("Only Origin Giratina exists...")
            elif Cname == "Attack":
                Aname = "Adeoxys"
                name = content[2]
                Cname = name.capitalize()
                result = PokemonHundo(Aname)
                Hundo = discord.Embed(title= "Attack Forme " + Cname + "'s Hundo Chart" , description="", color=0x2962FF)
                Hundo.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Adeoxys.png")
                Hundo.add_field(name="Level to 1-10:", value="Level 1:  **"+str(result[0])+"**\nLevel 2:  **"+str(result[1])+"**\nLevel 3:  **"+str(result[2])+"**\nLevel 4:  **"+str(result[3])+"**\nLevel 5:  **"+str(result[4])+"**\nLevel 6:  **"+str(result[5])+"**\nLevel 7:  **"+str(result[6])+"**\n Level 8:  **"+str(result[7])+"**\nLevel 9:  **"+str(result[8])+"**\nLevel 10:  **"+str(result[9])+"**", inline=True)
                Hundo.add_field(name="Level to 11-20:", value="Level 11:  **"+str(result[10])+"**\nLevel 12:  **"+str(result[11])+"**\nLevel 13:  **"+str(result[12])+"**\nLevel 14:  **"+str(result[13])+"**\nLevel 15:  **"+str(result[14])+"**\nLevel 16:  **"+str(result[15])+"**\nLevel 17:  **"+str(result[16])+"**\nLevel 18:  **"+str(result[17])+"**\nLevel 19:  **"+str(result[18])+"**\nLevel 20:  **"+str(result[19])+"**", inline=True)
                Hundo.add_field(name="\u200B", value="\u200B", inline=True)
                Hundo.add_field(name="Level to 21-30:", value="Level 21:  **"+str(result[20])+"**\nLevel 22:  **"+str(result[21])+"**\nLevel 23:  **"+str(result[22])+"**\nLevel 24:  **"+str(result[23])+"**\nLevel 25:  **"+str(result[24])+"**\nLevel 26:  **"+str(result[25])+"**\nLevel 27:  **"+str(result[26])+"**\nLevel 28:  **"+str(result[27])+"**\nLevel 29:  **"+str(result[28])+"**\nLevel 30:  **"+str(result[29])+"**", inline=True)
                Hundo.add_field(name="Level to 31-40:", value="Level 31:  **"+str(result[30])+"**\nLevel 32:  **"+str(result[31])+"**\nLevel 33:  **"+str(result[32])+"**\nLevel 34:  **"+str(result[33])+"**\nLevel 35:  **"+str(result[34])+"**\nLevel 36:  **"+str(result[35])+"**\nLevel 37:  **"+str(result[36])+"**\nLevel 38:  **"+str(result[37])+"**\nLevel 39:  **"+str(result[38])+"**\nLevel 40:  **"+str(result[39])+"**", inline=True)
                Hundo.add_field(name="\u200B", value="\u200B", inline=True)
                Hundo.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=Hundo)
            elif Cname == "Defense":
                Aname = "Ddeoxys"
                name = content[2]
                Cname = name.capitalize()
                result = PokemonHundo(Aname)
                Hundo = discord.Embed(title= "Defense Forme "+ Cname + "'s Hundo Chart" , description="", color=0x2962FF)
                Hundo.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Ddeoxys.png")
                Hundo.add_field(name="Level to 1-10:", value="Level 1:  **"+str(result[0])+"**\nLevel 2:  **"+str(result[1])+"**\nLevel 3:  **"+str(result[2])+"**\nLevel 4:  **"+str(result[3])+"**\nLevel 5:  **"+str(result[4])+"**\nLevel 6:  **"+str(result[5])+"**\nLevel 7:  **"+str(result[6])+"**\n Level 8:  **"+str(result[7])+"**\nLevel 9:  **"+str(result[8])+"**\nLevel 10:  **"+str(result[9])+"**", inline=True)
                Hundo.add_field(name="Level to 11-20:", value="Level 11:  **"+str(result[10])+"**\nLevel 12:  **"+str(result[11])+"**\nLevel 13:  **"+str(result[12])+"**\nLevel 14:  **"+str(result[13])+"**\nLevel 15:  **"+str(result[14])+"**\nLevel 16:  **"+str(result[15])+"**\nLevel 17:  **"+str(result[16])+"**\nLevel 18:  **"+str(result[17])+"**\nLevel 19:  **"+str(result[18])+"**\nLevel 20:  **"+str(result[19])+"**", inline=True)
                Hundo.add_field(name="\u200B", value="\u200B", inline=True)
                Hundo.add_field(name="Level to 21-30:", value="Level 21:  **"+str(result[20])+"**\nLevel 22:  **"+str(result[21])+"**\nLevel 23:  **"+str(result[22])+"**\nLevel 24:  **"+str(result[23])+"**\nLevel 25:  **"+str(result[24])+"**\nLevel 26:  **"+str(result[25])+"**\nLevel 27:  **"+str(result[26])+"**\nLevel 28:  **"+str(result[27])+"**\nLevel 29:  **"+str(result[28])+"**\nLevel 30:  **"+str(result[29])+"**", inline=True)
                Hundo.add_field(name="Level to 31-40:", value="Level 31:  **"+str(result[30])+"**\nLevel 32:  **"+str(result[31])+"**\nLevel 33:  **"+str(result[32])+"**\nLevel 34:  **"+str(result[33])+"**\nLevel 35:  **"+str(result[34])+"**\nLevel 36:  **"+str(result[35])+"**\nLevel 37:  **"+str(result[36])+"**\nLevel 38:  **"+str(result[37])+"**\nLevel 39:  **"+str(result[38])+"**\nLevel 40:  **"+str(result[39])+"**", inline=True)
                Hundo.add_field(name="\u200B", value="\u200B", inline=True)
                Hundo.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=Hundo)
            elif Cname == "Speed":
                Aname = "Sdeoxys"
                name = content[2]
                Cname = name.capitalize()
                result = PokemonHundo(name)
                Hundo = discord.Embed(title= "Speed Forme "+ Cname + "'s Hundo Chart" , description="", color=0x2962FF)
                Hundo.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Sdeoxys.png")
                Hundo.add_field(name="Level to 1-10:", value="Level 1:  **"+str(result[0])+"**\nLevel 2:  **"+str(result[1])+"**\nLevel 3:  **"+str(result[2])+"**\nLevel 4:  **"+str(result[3])+"**\nLevel 5:  **"+str(result[4])+"**\nLevel 6:  **"+str(result[5])+"**\nLevel 7:  **"+str(result[6])+"**\n Level 8:  **"+str(result[7])+"**\nLevel 9:  **"+str(result[8])+"**\nLevel 10:  **"+str(result[9])+"**", inline=True)
                Hundo.add_field(name="Level to 11-20:", value="Level 11:  **"+str(result[10])+"**\nLevel 12:  **"+str(result[11])+"**\nLevel 13:  **"+str(result[12])+"**\nLevel 14:  **"+str(result[13])+"**\nLevel 15:  **"+str(result[14])+"**\nLevel 16:  **"+str(result[15])+"**\nLevel 17:  **"+str(result[16])+"**\nLevel 18:  **"+str(result[17])+"**\nLevel 19:  **"+str(result[18])+"**\nLevel 20:  **"+str(result[19])+"**", inline=True)
                Hundo.add_field(name="\u200B", value="\u200B", inline=True)
                Hundo.add_field(name="Level to 21-30:", value="Level 21:  **"+str(result[20])+"**\nLevel 22:  **"+str(result[21])+"**\nLevel 23:  **"+str(result[22])+"**\nLevel 24:  **"+str(result[23])+"**\nLevel 25:  **"+str(result[24])+"**\nLevel 26:  **"+str(result[25])+"**\nLevel 27:  **"+str(result[26])+"**\nLevel 28:  **"+str(result[27])+"**\nLevel 29:  **"+str(result[28])+"**\nLevel 30:  **"+str(result[29])+"**", inline=True)
                Hundo.add_field(name="Level to 31-40:", value="Level 31:  **"+str(result[30])+"**\nLevel 32:  **"+str(result[31])+"**\nLevel 33:  **"+str(result[32])+"**\nLevel 34:  **"+str(result[33])+"**\nLevel 35:  **"+str(result[34])+"**\nLevel 36:  **"+str(result[35])+"**\nLevel 37:  **"+str(result[36])+"**\nLevel 38:  **"+str(result[37])+"**\nLevel 39:  **"+str(result[38])+"**\nLevel 40:  **"+str(result[39])+"**", inline=True)
                Hundo.add_field(name="\u200B", value="\u200B", inline=True)
                Hundo.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=Hundo)
            elif Cname != "Galarian":
                result = PokemonHundo(name)
                Hundo = discord.Embed(title= Cname + "'s Hundo Chart" , description="", color=0x2962FF)
                Hundo.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Cname+".png")
                Hundo.add_field(name="Level to 1-10:", value="Level 1:  **"+str(result[0])+"**\nLevel 2:  **"+str(result[1])+"**\nLevel 3:  **"+str(result[2])+"**\nLevel 4:  **"+str(result[3])+"**\nLevel 5:  **"+str(result[4])+"**\nLevel 6:  **"+str(result[5])+"**\nLevel 7:  **"+str(result[6])+"**\n Level 8:  **"+str(result[7])+"**\nLevel 9:  **"+str(result[8])+"**\nLevel 10:  **"+str(result[9])+"**", inline=True)
                Hundo.add_field(name="Level to 11-20:", value="Level 11:  **"+str(result[10])+"**\nLevel 12:  **"+str(result[11])+"**\nLevel 13:  **"+str(result[12])+"**\nLevel 14:  **"+str(result[13])+"**\nLevel 15:  **"+str(result[14])+"**\nLevel 16:  **"+str(result[15])+"**\nLevel 17:  **"+str(result[16])+"**\nLevel 18:  **"+str(result[17])+"**\nLevel 19:  **"+str(result[18])+"**\nLevel 20:  **"+str(result[19])+"**", inline=True)
                Hundo.add_field(name="\u200B", value="\u200B", inline=True)
                Hundo.add_field(name="Level to 21-30:", value="Level 21:  **"+str(result[20])+"**\nLevel 22:  **"+str(result[21])+"**\nLevel 23:  **"+str(result[22])+"**\nLevel 24:  **"+str(result[23])+"**\nLevel 25:  **"+str(result[24])+"**\nLevel 26:  **"+str(result[25])+"**\nLevel 27:  **"+str(result[26])+"**\nLevel 28:  **"+str(result[27])+"**\nLevel 29:  **"+str(result[28])+"**\nLevel 30:  **"+str(result[29])+"**", inline=True)
                Hundo.add_field(name="Level to 31-40:", value="Level 31:  **"+str(result[30])+"**\nLevel 32:  **"+str(result[31])+"**\nLevel 33:  **"+str(result[32])+"**\nLevel 34:  **"+str(result[33])+"**\nLevel 35:  **"+str(result[34])+"**\nLevel 36:  **"+str(result[35])+"**\nLevel 37:  **"+str(result[36])+"**\nLevel 38:  **"+str(result[37])+"**\nLevel 39:  **"+str(result[38])+"**\nLevel 40:  **"+str(result[39])+"**", inline=True)
                Hundo.add_field(name="\u200B", value="\u200B", inline=True)
                Hundo.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=Hundo)

    @commands.command()
    async def gopure(self, ctx):
        responce = str(ctx.message.content)
        if responce.startswith(str(ctx.prefix)+"gopure"):
            content = responce.split()
            name = content[1].capitalize()
            Cname = name.capitalize()
            Shadow = ("Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Weedle", "Kakuna", "Beedrill", "Rattata", "Raticate",
            "Sandshrew", "Sandslash", "Nidoran\U00002640", "Nidorina", "Nidoqueen", "Nidoran\U00002642", "Nidorino" ,"Nidoking", "Vulpix", "Ninetails", "Zubat", "Golbat", "Crobat", "Oddish",
            "Gloom", "Vileplume", "Bellossom", "Venonat", "Venomoth", "Meowth", "Persian", "Psyduck", "Golduck", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Politoed",
            "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Magnemite", "Magneton", "Magnezone", "Grimer", "Muk", "Drowzee", "Hypno",
            "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Koffing", "Weezing", "Scyther", "Scizor", "Electabuzz", "Electivire", "Magmar", "Magmortar", "Magikarp",
            "Gyarados", "Lapras", "Porygon", "Porygon2", "PorygonZ", "Omanyte", "Omastar", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mareep",
            "Flaaffy", "Ampharos", "Misdeavus", "Mismagius", "Wobuffett", "Pineco", "Forretress", "Gligar", "Gliscor", "Shuckle", "Sneasel", "Weavile", "Delibird", "Houndour", "Houndoom", "Stantler", "Raikou", "Entei",
            "Suicune", "Larvitar", "Pupitar", "Tyranitar", "Mudkip", "Marshtomp", "Swampert", "Seedot", "Nuzleaf", "Shiftry", "Ralts", "Kirlia", "Gardevoir", "Gallade", "Sableye", "Carvanha", "Sharpedo",
            "Trapinch", "Vibrava", "Flygon", "Cacnea", "Cacturne", "Shuppet", "Banette", "Duskull", "Dusclops", "Dusknoir", "Absol", "Bagon", "Shelgon", "Salamence", "Beldum", "Metang", "Metagross", "Turtwig",
            "Grotle", "Torterra", "Stunky", "Stuntank", "Snover", "Abomasnow")
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
                    await ctx.message.delete()
                    await ctx.send("The Value for the Attack IV isn't a valid number")
                try:
                    DIVB = int(content[3])
                except ValueError:
                    await ctx.message.delete()
                    await ctx.send("The Value for the Defense IV isn't a valid number")
                try:
                    SIVB = int(content[4])
                except ValueError:
                    await ctx.message.delete()
                    await ctx.send("The Value for the HP IV isn't a valid number")
                if AIVB > 15:
                    await ctx.send("That's not a valid Attack IV number, so I'll assume you meant 15", delete_after=10)
                if DIVB > 15:
                    await ctx.send("That's not a valid Defense IV number, so I'll assume you meant 15", delete_after=10)
                if SIVB > 15:
                    await ctx.send("That's not a valid HP IV number, so I'll assume you meant 15", delete_after=10)
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
                Pure.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Cname+".png")
                Pure.add_field(name="Attack IV Shadow:", value="**"+str(AIVB)+"**", inline=True)
                Pure.add_field(name="Defense IV Shadow:", value="**"+str(DIVB)+"**", inline=True)
                Pure.add_field(name="HP IV Shadow:", value="**"+str(SIVB)+"**", inline= True)
                Pure.add_field(name="Attack IV Purified:", value="**"+str(AIVA)+"**", inline=True)
                Pure.add_field(name="Defense IV Purified:", value="**"+str(DIVA)+"**", inline=True)
                Pure.add_field(name="HP IV Purified:", value="**"+str(SIVA)+"**", inline= True)
                Pure.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.message.delete()
                await ctx.send(embed=Pure)
            else:
                await ctx.send("This shadow pokemon doesn't exist... yet... Ţ̸̧̖̘̒͐͌e̷̳͕͋a̸̗̫̓ḿ̷̡͙̱̊̚ ̵̘̖̼̪̦̟̏̂̀̓͌͘͝R̴̨̨͈̰̼̳̜̓̈̓o̷͙͠c̶͔̼̀̍̄̃̔͝ķ̸̦̜͚͂̅̀e̶̡̢̡̘̜̒̕t̷͎̼̙̀͌̊̂̕̚", delete_after=10)

    # @commands.command()
    # async def gomovepvp(self, ctx):

    # @commands.command()
    # async def gomoveraid(self, ctx):

def dex(pokename):
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

    fileOpen = open('C:/Users/Administrator/Documents/pokegodex.csv', newline='')
    fileData = csv.reader(fileOpen)
    for row in fileData:
        for name in row:
            if name == pokename:
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
                    return (dexentry, generation, types, Height, Weight, Maxcp, pokeAtk, pokeDef, pokeSta, Shiny, Timed, RShiny, EggShiny, Research)
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
                    return (dexentry, generation, types, Height, Weight, Maxcp, pokeAtk, pokeDef, pokeSta, Shiny, Timed, RShiny, EggShiny, Research)

def aloladex(pokename):
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

    fileOpen = open('C:/Users/Administrator/Documents/alolangodex.csv', newline='')
    fileData = csv.reader(fileOpen)
    for row in fileData:
        for name in row:
            if name == pokename:
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
                    return (dexentry, generation, types, Height, Weight, Maxcp, pokeAtk, pokeDef, pokeSta, Shiny, Timed, RShiny, EggShiny, Research)
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
                    return (dexentry, generation, types, Height, Weight, Maxcp, pokeAtk, pokeDef, pokeSta, Shiny, Timed, RShiny, EggShiny, Research)

def galardex(pokename):
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

    fileOpen = open('C:/Users/Administrator/Documents/galargodex.csv', newline='')
    fileData = csv.reader(fileOpen)
    for row in fileData:
        for name in row:
            if name == pokename:
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
                    return (dexentry, generation, types, Height, Weight, Maxcp, pokeAtk, pokeDef, pokeSta, Shiny, Timed, RShiny, EggShiny, Research)
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
                    return (dexentry, generation, types, Height, Weight, Maxcp, pokeAtk, pokeDef, pokeSta, Shiny, Timed, RShiny, EggShiny, Research)

def MaintoGo(pokenamez, Lvl, IVA, IVD, IVS):
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

    fileOpen = open('C:/Users/Administrator/Documents/pokegodex.csv', newline='')
    fileData = csv.reader(fileOpen)
    for row in fileData:
        for Name in row:
            if Name == pokename:
                GoAtk = int(row[8])
                GoDef = int(row[9])
                GoStamina = int(row[10])
                RealAtk = GoAtk + IV1
                RealDef = GoDef + IV2
                RealStamina = GoStamina + IV3
                CPM = LeveltoCPM(Level)
                Statproduct = (((RealAtk*CPM)*(RealDef*CPM)*(RealStamina*CPM))/1000)
                CP = CPCalc(RealAtk, RealDef, RealStamina, CPM)
                YourPokemon = (CP, Level, Statproduct,IV1,IV2,IV3)
                BestofGreat= BestsearchGreat(GoAtk, GoDef, GoStamina, Great)
                BestofUltra= BestsearchUltra(GoAtk, GoDef, GoStamina, Ultra)
                BestofMaster= BestsearchMaster(GoAtk, GoDef, GoStamina, Master)
                return (YourPokemon,BestofGreat,BestofUltra,BestofMaster)

def AlolanMaintoGo(pokenamez, Lvl, IVA, IVD, IVS):
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

    fileOpen = open('C:/Users/Administrator/Documents/alolangodex.csv', newline='')
    fileData = csv.reader(fileOpen)
    for row in fileData:
        for Name in row:
            if Name == pokename:
                GoAtk = int(row[8])
                GoDef = int(row[9])
                GoStamina = int(row[10])
                RealAtk = GoAtk + IV1
                RealDef = GoDef + IV2
                RealStamina = GoStamina + IV3
                CPM = LeveltoCPM(Level)
                Statproduct = (((RealAtk*CPM)*(RealDef*CPM)*(RealStamina*CPM))/1000)
                CP = CPCalc(RealAtk, RealDef, RealStamina, CPM)
                YourPokemon = (CP, Level, Statproduct,IV1,IV2,IV3)
                BestofGreat= BestsearchGreat(GoAtk, GoDef, GoStamina, Great)
                BestofUltra= BestsearchUltra(GoAtk, GoDef, GoStamina, Ultra)
                BestofMaster= BestsearchMaster(GoAtk, GoDef, GoStamina, Master)
                return ((YourPokemon),(BestofGreat),(BestofUltra),(BestofMaster))

def GalarianMaintoGo(pokenamez, Lvl, IVA, IVD, IVS):
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

    fileOpen = open('C:/Users/Administrator/Documents/galargodex.csv', newline='')
    fileData = csv.reader(fileOpen)
    for row in fileData:
        for Name in row:
            if Name == pokename:
                GoAtk = int(row[8])
                GoDef = int(row[9])
                GoStamina = int(row[10])
                RealAtk = GoAtk + IV1
                RealDef = GoDef + IV2
                RealStamina = GoStamina + IV3
                CPM = LeveltoCPM(Level)
                Statproduct = (((RealAtk*CPM)*(RealDef*CPM)*(RealStamina*CPM))/1000)
                CP = CPCalc(RealAtk, RealDef, RealStamina, CPM)
                YourPokemon = (CP, Level, Statproduct,IV1,IV2,IV3)
                BestofGreat= BestsearchGreat(GoAtk, GoDef, GoStamina, Great)
                BestofUltra= BestsearchUltra(GoAtk, GoDef, GoStamina, Ultra)
                BestofMaster= BestsearchMaster(GoAtk, GoDef, GoStamina, Master)
                return (YourPokemon,BestofGreat,BestofUltra,BestofMaster)
            else:
                return 0

def MegaMaintoGo(pokenamez, Lvl, IVA, IVD, IVS):
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

    fileOpen = open('C:/Users/Administrator/Documents/megagodex.csv', newline='')
    fileData = csv.reader(fileOpen)
    for row in fileData:
        for Name in row:
            if Name == pokename:
                if pokename == "Xmewtwo" or pokename == "Ymewtwo":
                    GoAtk = int(row[8])
                    GoDef = int(row[9])
                    GoStamina = int(row[10])
                    RealAtk = GoAtk + IV1
                    RealDef = GoDef + IV2
                    RealStamina = GoStamina + IV3
                    CPM = LeveltoCPM(Level)
                    Statproduct = (((RealAtk*CPM)*(RealDef*CPM)*(RealStamina*CPM))/1000)
                    CP = CPCalc(RealAtk, RealDef, RealStamina, CPM)
                    YourPokemon = (CP, Level, Statproduct,IV1,IV2,IV3)
                    BestofGreat= int(0),float(0.0),float(0.0),int(0),int(0),int(0)
                    BestofUltra= BestsearchUltra(GoAtk, GoDef, GoStamina, Ultra)
                    BestofMaster= BestsearchMaster(GoAtk, GoDef, GoStamina, Master)
                    return (YourPokemon,BestofGreat,BestofUltra,BestofMaster)
                elif pokename == "Gyarados" or pokename == "Heracross" or pokename == "Tyranitar" or pokename == "Salamence" or pokename == "Metagross" or pokename == "Latias" or pokename == "Latios" or pokename == "Rayquaza" or pokename == "Garchomp":
                    GoAtk = int(row[8])
                    GoDef = int(row[9])
                    GoStamina = int(row[10])
                    RealAtk = GoAtk + IV1
                    RealDef = GoDef + IV2
                    RealStamina = GoStamina + IV3
                    CPM = LeveltoCPM(Level)
                    Statproduct = (((RealAtk*CPM)*(RealDef*CPM)*(RealStamina*CPM))/1000)
                    CP = CPCalc(RealAtk, RealDef, RealStamina, CPM)
                    YourPokemon = (CP, Level, Statproduct,IV1,IV2,IV3)
                    BestofGreat= int(0),float(0.0),float(0.0),int(0),int(0),int(0)
                    BestofUltra= BestsearchUltra(GoAtk, GoDef, GoStamina, Ultra)
                    BestofMaster= BestsearchMaster(GoAtk, GoDef, GoStamina, Master)
                    return (YourPokemon,BestofGreat,BestofUltra,BestofMaster)
                else:
                    GoAtk = int(row[8])
                    GoDef = int(row[9])
                    GoStamina = int(row[10])
                    RealAtk = GoAtk + IV1
                    RealDef = GoDef + IV2
                    RealStamina = GoStamina + IV3
                    CPM = LeveltoCPM(Level)
                    Statproduct = (((RealAtk*CPM)*(RealDef*CPM)*(RealStamina*CPM))/1000)
                    CP = CPCalc(RealAtk, RealDef, RealStamina, CPM)
                    YourPokemon = (CP, Level, Statproduct,IV1,IV2,IV3)
                    BestofGreat= BestsearchGreat(GoAtk, GoDef, GoStamina, Great)
                    BestofUltra= BestsearchUltra(GoAtk, GoDef, GoStamina, Ultra)
                    BestofMaster= BestsearchMaster(GoAtk, GoDef, GoStamina, Master)
                    return (YourPokemon,BestofGreat,BestofUltra,BestofMaster)
            elif Name in row == False:
                return 0

def BestsearchGreat(Atk, Def, Stamina, LCP):
    GoAtk = Atk
    GoDef = Def
    GoStamina = Stamina
    League = LCP
    Level = float(1.0)
    CPM = float(0.0)
    BestStatPro = float(0.0)
    IV = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]]
    y = int(0)

    if League == 1500.0:
        x = list(itertools.product(*IV))
        for y in range(4096):
            xy = x[y]
            SAIV = int(xy[0])
            SDIV = int(xy[1])
            StaIV = int(xy[2])
            Level = 12.5
            while Level < 40.5:
                #print("Level:" + str(Level) + " Atk IV: " +str(SAIV)+" Def IV: "+str(SDIV)+ " Sta IV: "+str(StaIV)+" ")
                CPM = LeveltoCPM(Level)
                #print(CPM)
                CP = (CPCalc((GoAtk+SAIV), (GoDef+SDIV), (GoStamina+StaIV), CPM))
                #print(CP)
                if CP <= League:
                    Atkproduct = ((GoAtk+SAIV)*CPM)
                    Defproduct = ((GoDef+SDIV)*CPM)
                    Stamproduct = ((GoStamina+StaIV)*CPM)
                    Statproduct = ((Atkproduct*Defproduct*Stamproduct)/1000)
                    #print(Statproduct)
                    if BestStatPro <= Statproduct:
                        GLA = SAIV
                        GLD = SDIV
                        GLS = StaIV
                        TestCP = CP
                        BSPL = Level
                        BestStatPro = Statproduct
                        #print(str(Level)+": "+str(BestStatPro)+" "+str(GLA)+str(GLD)+str(GLS))
                        Level += 0.5
                    else:
                        Level += 0.5
                else:
                    Level += 0.5
            y += 1
        return (TestCP,BSPL,BestStatPro,GLA,GLD,GLS)

def BestsearchUltra(Atk, Def, Stamina, LCP):
    GoAtk = Atk
    GoDef = Def
    GoStamina = Stamina
    League = LCP
    Level = float(1.0)
    CPM = float(0.0)
    BestStatPro = float(0.0)
    IV = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]]
    y = int(0)

    if League == 2500.0:
        x = list(itertools.product(*IV))
        for y in range(4096):
            xy = x[y]
            SAIV = int(xy[0])
            SDIV = int(xy[1])
            StaIV = int(xy[2])
            Level = 12.5
            while Level < 40.5:
                #print("Level:" + str(Level) + " Atk IV: " +str(SAIV)+" Def IV: "+str(SDIV)+ " Sta IV: "+str(StaIV)+" ")
                CPM = float(LeveltoCPM(Level))
                #print(CPM)
                CP = (CPCalc((GoAtk+SAIV), (GoDef+SDIV), (GoStamina+StaIV), CPM))
                #print(CP)
                if CP <= League:
                    Atkproduct = ((GoAtk+SAIV)*CPM)
                    Defproduct = ((GoDef+SDIV)*CPM)
                    Stamproduct = ((GoStamina+StaIV)*CPM)
                    Statproduct = ((Atkproduct*Defproduct*Stamproduct)/1000)
                    #print(Statproduct)
                    if BestStatPro <= Statproduct:
                        GLA = SAIV
                        GLD = SDIV
                        GLS = StaIV
                        TestCP = CP
                        BSPL = Level
                        BestStatPro = Statproduct
                        #print(str(Level)+": "+str(BestStatPro)+" "+str(GLA)+str(GLD)+str(GLS))
                        Level += 0.5
                    else:
                        Level += 0.5
                else:
                    Level += 0.5
            y += 1
        return (TestCP,BSPL,BestStatPro,GLA,GLD,GLS)

def BestsearchMaster(Atk, Def, Stamina, LCP):
    GoAtk = int(Atk)
    GoDef = int(Def)
    GoStamina = int(Stamina)
    League = LCP
    Level = float(1.0)
    CPM = float(0.0)
    BestStatPro = float(0.0)
    IV = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]]
    y = int(0)


    if League == 6000.0:
        Level = 40.0
        CPM = LeveltoCPM(float(Level))
        CP = CPCalc((GoAtk+15), (GoDef+15), (GoStamina+15), CPM)
        Atkproduct = float((GoAtk+15)*CPM)
        Defproduct = float((GoDef+15)*CPM)
        Stamproduct = float((GoStamina+15)*CPM)
        Statproduct = ((Atkproduct*Defproduct*Stamproduct)/1000)
        return (CP,Level,Statproduct,15,15,15)

def LeveltoCPM(Level):
    Lvl = Level
    LevelDict = {1:0.094,1.5:0.1351374318,2:0.16639787,2.5:0.192650919,3:0.21573247,3.5:0.2365726613,4:0.25572005,4.5:0.2735303812,5:0.29024988,5.5:0.3060573775,6:0.3210876,6.5:0.3354450362,7:0.34921268,7.5:0.3624577511,8:0.3752356,8.5:0.387592416,9:0.39956728,9.5:0.4111935514,10:0.4225,
                 10.5:0.4329264091,11:0.44310755,11.5:0.4530599591,12:0.4627984,12.5:0.472336093,13:0.48168495,13.5:0.4908558003,14:0.49985844,14.5:0.508701765,15:0.51739395,15.5:0.5259425113,16:0.5343543,16.5:0.5426357375,17:0.5507927,17.5:0.5588305862,18:0.5667545,18.5:0.5745691333,19:0.5822789,19.5:0.5898879072,20:0.5974,
                 20.5:0.6048236651,21:0.6121573,21.5:0.6194041216,22:0.6265671,22.5:0.6336491432,23:0.64065295,23.5:0.6475809666,24:0.65443563,24.5:0.6612192524,25:0.667934,25.5:0.6745818959,26:0.6811649,26.5:0.6876849038,27:0.69414365,27.5:0.70054287,28:0.7068842,28.5:0.7131691091,29:0.7193991,29.5:0.7255756136,30:0.7317,
                 30.5:0.7347410093,31:0.7377695,31.5:0.7407855938,32:0.74378943,32.5:0.7467812109,33:0.74976104,33.5:0.7527290867,34:0.7556855,34.5:0.7586303683,35:0.76156384,35.5:0.7644860647,36:0.76739717,36.5:0.7702972656,37:0.7731865,37.5:0.7760649616,38:0.77893275,38.5:0.7817900548,39:0.784637,39.5:0.7874736075,40:0.7903,
                 40.5:0.792800005, 41:0.79530001 }
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

def Rocketlookup(info):
    rocket = info

    fileOpen = open('C:/Users/Administrator/Documents/Teamgorocket.csv', newline='')
    fileData = csv.reader(fileOpen)
    for row in fileData:
        for Type in row:
            if Type == rocket:
                first = str(row[1])
                second = str(row[2])
                third = str(row[3])
                reward = str(row[4])
                return (first, second, third, reward)

def PokemonHundo(pokenamez):
    pokename = pokenamez.capitalize()
    Level = 1
    IV1 = 15
    IV2 = 15
    IV3 = 15
    GoAtk = 0
    GoDef = 0
    GoStamina = 0
    Data = []

    fileOpen = open('C:/Users/Administrator/Documents/pokegodex.csv', newline='')
    fileData = csv.reader(fileOpen)
    for row in fileData:
        for Name in row:
            if Name == pokename:
                GoAtk = int(row[8])
                GoDef = int(row[9])
                GoStamina = int(row[10])
                RealAtk = GoAtk + IV1
                RealDef = GoDef + IV2
                RealStamina = GoStamina + IV3
                while Level != 41:
                    CPM = LeveltoCPM(Level)
                    CP = CPCalc(RealAtk, RealDef, RealStamina, CPM)
                    Data.append(CP)
                    Level += 1
                return Data

def PokemonHundoAlolan(pokenamez):
    pokename = pokenamez.capitalize()
    Level = 1
    IV1 = 15
    IV2 = 15
    IV3 = 15
    GoAtk = 0
    GoDef = 0
    GoStamina = 0
    Data = []

    fileOpen = open('C:/Users/Administrator/Documents/alolangodex.csv', newline='')
    fileData = csv.reader(fileOpen)
    for row in fileData:
        for Name in row:
            if Name == pokename:
                GoAtk = int(row[8])
                GoDef = int(row[9])
                GoStamina = int(row[10])
                RealAtk = GoAtk + IV1
                RealDef = GoDef + IV2
                RealStamina = GoStamina + IV3
                while Level != 41:
                    CPM = LeveltoCPM(Level)
                    CP = CPCalc(RealAtk, RealDef, RealStamina, CPM)
                    Data.append(CP)
                    Level += 1
                return Data

def PokemonHundoGalarian(pokenamez):
    pokename = pokenamez.capitalize()
    Level = 1
    IV1 = 15
    IV2 = 15
    IV3 = 15
    GoAtk = 0
    GoDef = 0
    GoStamina = 0
    Data = []

    fileOpen = open('C:/Users/Administrator/Documents/galargodex.csv', newline='')
    fileData = csv.reader(fileOpen)
    for row in fileData:
        for Name in row:
            if Name == pokename:
                GoAtk = int(row[8])
                GoDef = int(row[9])
                GoStamina = int(row[10])
                RealAtk = GoAtk + IV1
                RealDef = GoDef + IV2
                RealStamina = GoStamina + IV3
                while Level != 41:
                    CPM = LeveltoCPM(Level)
                    CP = CPCalc(RealAtk, RealDef, RealStamina, CPM)
                    Data.append(CP)
                    Level += 1
                return Data

def setup(client):
    client.add_cog(Pokego(client))
