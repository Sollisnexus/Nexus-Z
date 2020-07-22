import discord
import string
import math
import csv
import os
import asyncio
import threading
from discord.ext import commands

class Pokemon(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Pokemon module is online.')
    
    # Commands
    @commands.command(name ='catch', help='Shows the catch rate of Pokemon')
    async def catch(self, ctx):
        responce = str(ctx.message.content)
        if responce.startswith('%catch'):
            content = responce.split()
    
            try:
                content[2].endswith('ball') or content[3].endswith('ball') or content[4].endswith('ball')
            except:            
                Name = string.capwords(content[1])
                namea = "Alolan"
                namegl = "Galarian"
                nameg = "Gmax"
                if Name == namea:
                    GaName = string.capwords(content[2])
                    Listofalola = ["Rattata","Raticate","Raichu","Sandshrew","Sandslash","Vulpix","Ninetails","Diglett","Dugtrio","Meowth","Persian","Geodude","Graveler",
                                   "Golem","Grimer","Muk","Exeggutor","Marowak"]
                    if GaName in Listofalola:
                            msg = alolanmain(str(GaName), str("pokeball"))
                            msg1= alolanmain(str(GaName), str("greatball"))
                            msg2= alolanmain(str(GaName), str("ultraball"))
                            msg3= alolanmain(str(GaName), str("duskball"))
                            msg4= alolanmain(str(GaName), str("repeatball"))
                            msg5= alolanmain(str(GaName), str("netball"))
                            msg6= alolanmain(str(GaName), str("Apriball"))
                            msg7= alolanmain(str(GaName), str("beastball"))                        
                            List2 = [(msg),(msg1),(msg2),(msg3),(msg4),(msg5),(msg6),(msg7)]
                            List = sorted(List2, key=getNKey)
                            Test = sorted(List, key=getKey, reverse=True)
                            msg = Test[0]
                            msga = str(msg[0])
                            msgb = str(msg[1])
                            msgc = str(msg[2])
                            msg1 = Test[1]
                            msg1a = str(msg1[0])
                            msg1b = str(msg1[1])
                            msg1c = str(msg1[2])                       
                            msg2 = Test[2]
                            msg2a = str(msg2[0])
                            msg2b = str(msg2[1])
                            msg2c = str(msg2[2])                        
                            msg3 = Test[3]
                            msg3a = str(msg3[0])
                            msg3b = str(msg3[1])
                            msg3c = str(msg3[2])
                            msg4 = Test[4]
                            msg4a = str(msg4[0])
                            msg4b = str(msg4[1])
                            msg4c = str(msg4[2])
                            msg5 = Test[5]
                            msg5a = str(msg5[0])
                            msg5b = str(msg5[1])
                            msg5c = str(msg5[2])
                            msg6 = Test[6]
                            msg6a = str(msg6[0])
                            msg6b = str(msg6[1])
                            msg6c = str(msg6[2])
                            msg7 = Test[7]
                            msg7a = str(msg7[0])
                            msg7b = str(msg7[1])
                            msg7c = str(msg7[2])
                            embed = discord.Embed(title= "Alolan " + GaName + "'s Capture Odds", description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Alolan/Shiny/"+GaName+".png")
                            embed.add_field(name= "Ball Type", value=msga+"\n"+msg1a+"\n"+msg2a+"\n"+msg3a+"\n"+msg4a+"\n"+msg5a+"\n"+msg6a+"\n"+msg7a+"\n", inline=True)
                            embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n" + msg1b+"% - "+msg1c+"%\n" + msg2b+"% - "+msg2c+"%\n" + msg3b+"% - "+msg3c+"%\n" + msg4b+"% - "+msg4c+"%\n" + msg5b+"% - "+msg5c+"%\n" + msg6b+"% - "+msg6c+"%\n" + msg7b+"% - "+msg7c+"%\n", inline=True)
                            await ctx.author.message.delete()
                            await ctx.send(embed=embed)
                    else:
                        await ctx.send('This Alolan Pokémon does not exist!')       
                elif Name == namegl:
                    GlName = string.capwords(content[2])
                    GlmName = string.capwords(content[2]) + " Mime"
                    Listofgalar = ["Meowth","Ponyta","Rapidash","Slowpoke","Slowbro","Farfetch'd","Weezing","Mr Mime","Corsola","Zigzagoon","Linoone","Darumaka",
                                   "Darmanitan","Yamask","Stunfisk"]
                    if GlName in Listofgalar or GlmName in Listofgalar:
                        if GlName == "Mr":
                            RGName = "Mrmime"
                            msg = galarianmain(str(RGName), str("pokeball"))
                            msg1= galarianmain(str(RGName), str("greatball"))
                            msg2= galarianmain(str(RGName), str("ultraball"))
                            msg3= galarianmain(str(RGName), str("duskball"))
                            msg4= galarianmain(str(RGName), str("repeatball"))
                            msg5= galarianmain(str(RGName), str("netball"))
                            msg6= galarianmain(str(RGName), str("Apriball"))
                            msg7= galarianmain(str(RGName), str("beastball"))
                            List2 = [(msg),(msg1),(msg2),(msg3),(msg4),(msg5),(msg6),(msg7)]
                            List = sorted(List2, key=getNKey)
                            Test = sorted(List, key=getKey, reverse=True)
                            msg = Test[0]
                            msga = str(msg[0])
                            msgb = str(msg[1])
                            msgc = str(msg[2])
                            msg1 = Test[1]
                            msg1a = str(msg1[0])
                            msg1b = str(msg1[1])
                            msg1c = str(msg1[2])                       
                            msg2 = Test[2]
                            msg2a = str(msg2[0])
                            msg2b = str(msg2[1])
                            msg2c = str(msg2[2])                        
                            msg3 = Test[3]
                            msg3a = str(msg3[0])
                            msg3b = str(msg3[1])
                            msg3c = str(msg3[2])
                            msg4 = Test[4]
                            msg4a = str(msg4[0])
                            msg4b = str(msg4[1])
                            msg4c = str(msg4[2])
                            msg5 = Test[5]
                            msg5a = str(msg5[0])
                            msg5b = str(msg5[1])
                            msg5c = str(msg5[2])
                            msg6 = Test[6]
                            msg6a = str(msg6[0])
                            msg6b = str(msg6[1])
                            msg6c = str(msg6[2])
                            msg7 = Test[7]
                            msg7a = str(msg7[0])
                            msg7b = str(msg7[1])
                            msg7c = str(msg7[2])
                            embed = discord.Embed(title= "Galarian Mr. Mime's Capture Odds", description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/Shiny/Mrmime.png")
                            embed.add_field(name= "Ball Type", value=msga+"\n"+msg1a+"\n"+msg2a+"\n"+msg3a+"\n"+msg4a+"\n"+msg5a+"\n"+msg6a+"\n"+msg7a+"\n", inline=True)
                            embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n" + msg1b+"% - "+msg1c+"%\n" + msg2b+"% - "+msg2c+"%\n" + msg3b+"% - "+msg3c+"%\n" + msg4b+"% - "+msg4c+"%\n" + msg5b+"% - "+msg5c+"%\n" + msg6b+"% - "+msg6c+"%\n" + msg7b+"% - "+msg7c+"%\n", inline=True)
                            await ctx.author.message.delete()
                            await ctx.send(embed=embed)
                        elif GlName != "Mr":
                            msg = galarianmain(str(GlName), str("pokeball"))
                            msg1= galarianmain(str(GlName), str("greatball"))
                            msg2= galarianmain(str(GlName), str("ultraball"))
                            msg3= galarianmain(str(GlName), str("duskball"))
                            msg4= galarianmain(str(GlName), str("repeatball"))
                            msg5= galarianmain(str(GlName), str("netball"))
                            msg6= galarianmain(str(GlName), str("apriball"))
                            msg7= galarianmain(str(GlName), str("beastball"))
                            List2 = [(msg),(msg1),(msg2),(msg3),(msg4),(msg5),(msg6),(msg7)]
                            List = sorted(List2, key=getNKey)
                            Test = sorted(List, key=getKey, reverse=True)
                            msg = Test[0]
                            msga = str(msg[0])
                            msgb = str(msg[1])
                            msgc = str(msg[2])
                            msg1 = Test[1]
                            msg1a = str(msg1[0])
                            msg1b = str(msg1[1])
                            msg1c = str(msg1[2])                       
                            msg2 = Test[2]
                            msg2a = str(msg2[0])
                            msg2b = str(msg2[1])
                            msg2c = str(msg2[2])                        
                            msg3 = Test[3]
                            msg3a = str(msg3[0])
                            msg3b = str(msg3[1])
                            msg3c = str(msg3[2])
                            msg4 = Test[4]
                            msg4a = str(msg4[0])
                            msg4b = str(msg4[1])
                            msg4c = str(msg4[2])
                            msg5 = Test[5]
                            msg5a = str(msg5[0])
                            msg5b = str(msg5[1])
                            msg5c = str(msg5[2])
                            msg6 = Test[6]
                            msg6a = str(msg6[0])
                            msg6b = str(msg6[1])
                            msg6c = str(msg6[2])
                            msg7 = Test[7]
                            msg7a = str(msg7[0])
                            msg7b = str(msg7[1])
                            msg7c = str(msg7[2])
                            if GlName == "Farfetch'd":
                                GlfName = "Farfetchd"
                                embed = discord.Embed(title= "Galarian " + GlName + "'s Capture Odds", description="", color=0x2962FF)
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/Shiny/"+GlfName+".png")
                                embed.add_field(name= "Ball Type", value=msga+"\n"+msg1a+"\n"+msg2a+"\n"+msg3a+"\n"+msg4a+"\n"+msg5a+"\n"+msg6a+"\n"+msg7a+"\n", inline=True)
                                embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n" + msg1b+"% - "+msg1c+"%\n" + msg2b+"% - "+msg2c+"%\n" + msg3b+"% - "+msg3c+"%\n" + msg4b+"% - "+msg4c+"%\n" + msg5b+"% - "+msg5c+"%\n" + msg6b+"% - "+msg6c+"%\n" + msg7b+"% - "+msg7c+"%\n", inline=True)
                                await ctx.author.message.delete()
                                await ctx.send(embed=embed)
                            else:
                                embed = discord.Embed(title= "Galarian " + GlName + "'s Capture Odds", description="", color=0x2962FF)
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/Shiny/"+GlName+".png")
                                embed.add_field(name= "Ball Type", value=msga+"\n"+msg1a+"\n"+msg2a+"\n"+msg3a+"\n"+msg4a+"\n"+msg5a+"\n"+msg6a+"\n"+msg7a+"\n", inline=True)
                                embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n" + msg1b+"% - "+msg1c+"%\n" + msg2b+"% - "+msg2c+"%\n" + msg3b+"% - "+msg3c+"%\n" + msg4b+"% - "+msg4c+"%\n" + msg5b+"% - "+msg5c+"%\n" + msg6b+"% - "+msg6c+"%\n" + msg7b+"% - "+msg7c+"%\n", inline=True)
                                await ctx.author.message.delete()
                                await ctx.send(embed=embed)
                    else:
                        await ctx.send('This Galarian Pokémon does not exist!')       
                elif Name == nameg:
                    GName = string.capwords(content[2])
                    Listofgmax = ["Venusaur","Charizard","Blastoise","Butterfree","Pikachu","Meowth","Machamp","Gengar","Kingler","Lapras","Eevee","Snorlax","Garbodor",
                                  "Melmetal","Rillaboom","Cinderace","Inteleon","Corviknight","Orbeetle","Drednaw","Coalossal","Flapple","Appletun","Sandaconda","Toxtricity",
                                  "Centiskorch", "Hatterene","Grimmsnarl","Alcremie","Copperajah","Duraludon","Urshifu"]
                    if GName in Listofgmax:
                        msg = gmaxmain(str(GName), str("pokeball"))
                        msg1= gmaxmain(str(GName), str("greatball"))
                        msg2= gmaxmain(str(GName), str("ultraball"))
                        msg3= gmaxmain(str(GName), str("duskball"))
                        msg4= gmaxmain(str(GName), str("repeatball"))
                        msg5= gmaxmain(str(GName), str("netball"))
                        msg6= gmaxmain(str(GName), str("apriball"))
                        msg7= gmaxmain(str(GName), str("beastball"))                    
                        List2 = [(msg),(msg1),(msg2),(msg3),(msg4),(msg5),(msg6),(msg7)]
                        List = sorted(List2, key=getNKey)
                        Test = sorted(List, key=getKey, reverse=True)
                        msg = Test[0]
                        msga = str(msg[0])
                        msgb = str(msg[1])
                        msgc = str(msg[2])
                        msg1 = Test[1]
                        msg1a = str(msg1[0])
                        msg1b = str(msg1[1])
                        msg1c = str(msg1[2])                       
                        msg2 = Test[2]
                        msg2a = str(msg2[0])
                        msg2b = str(msg2[1])
                        msg2c = str(msg2[2])                        
                        msg3 = Test[3]
                        msg3a = str(msg3[0])
                        msg3b = str(msg3[1])
                        msg3c = str(msg3[2])
                        msg4 = Test[4]
                        msg4a = str(msg4[0])
                        msg4b = str(msg4[1])
                        msg4c = str(msg4[2])
                        msg5 = Test[5]
                        msg5a = str(msg5[0])
                        msg5b = str(msg5[1])
                        msg5c = str(msg5[2])
                        msg6 = Test[6]
                        msg6a = str(msg6[0])
                        msg6b = str(msg6[1])
                        msg6c = str(msg6[2])
                        msg7 = Test[7]
                        msg7a = str(msg7[0])
                        msg7b = str(msg7[1])
                        msg7c = str(msg7[2])
                        embed = discord.Embed(title= "Gmax " + GName + "'s Capture Odds", description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Gmax/Shiny/"+GName+".png")
                        embed.add_field(name= "Ball Type", value=msga+"\n"+msg1a+"\n"+msg2a+"\n"+msg3a+"\n"+msg4a+"\n"+msg5a+"\n"+msg6a+"\n"+msg7a+"\n", inline=True)
                        embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n" + msg1b+"% - "+msg1c+"%\n" + msg2b+"% - "+msg2c+"%\n" + msg3b+"% - "+msg3c+"%\n" + msg4b+"% - "+msg4c+"%\n" + msg5b+"% - "+msg5c+"%\n" + msg6b+"% - "+msg6c+"%\n" + msg7b+"% - "+msg7c+"%\n", inline=True)
                        await ctx.author.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send('This Gmax Pokémon does not exist!')
                elif Name != nameg:
                    if Name == "Mr":
                        FLCap = string.capwords(content[1])
                        FLLCap = string.capwords(content[2])
                        RName = content[1] + content[2]
                        RealN= FLCap+". "+FLLCap
                        LowN = content[1].lower()
                        LowM = content[2].lower()
                        msg = main(str(RName), str("pokeball"))
                        msg1= main(str(RName), str("greatball"))
                        msg2= main(str(RName), str("ultraball"))
                        msg3= main(str(RName), str("duskball"))
                        msg4= main(str(RName), str("repeatball"))
                        msg5= main(str(RName), str("netball"))
                        msg6= main(str(RName), str("Apriball"))
                        msg7= main(str(RName), str("beastball"))
                        List2 = [(msg),(msg1),(msg2),(msg3),(msg4),(msg5),(msg6),(msg7)]
                        List = sorted(List2, key=getNKey)
                        Test = sorted(List, key=getKey, reverse=True)
                        msg = Test[0]
                        msga = str(msg[0])
                        msgb = str(msg[1])
                        msgc = str(msg[2])
                        msg1 = Test[1]
                        msg1a = str(msg1[0])
                        msg1b = str(msg1[1])
                        msg1c = str(msg1[2])                       
                        msg2 = Test[2]
                        msg2a = str(msg2[0])
                        msg2b = str(msg2[1])
                        msg2c = str(msg2[2])                        
                        msg3 = Test[3]
                        msg3a = str(msg3[0])
                        msg3b = str(msg3[1])
                        msg3c = str(msg3[2])
                        msg4 = Test[4]
                        msg4a = str(msg4[0])
                        msg4b = str(msg4[1])
                        msg4c = str(msg4[2])
                        msg5 = Test[5]
                        msg5a = str(msg5[0])
                        msg5b = str(msg5[1])
                        msg5c = str(msg5[2])
                        msg6 = Test[6]
                        msg6a = str(msg6[0])
                        msg6b = str(msg6[1])
                        msg6c = str(msg6[2])
                        msg7 = Test[7]
                        msg7a = str(msg7[0])
                        msg7b = str(msg7[1])
                        msg7c = str(msg7[2])
                        embed = discord.Embed(title= RealN + "'s Capture Odds", description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Mrmime.png")
                        embed.add_field(name= "Ball Type", value=msga+"\n"+msg1a+"\n"+msg2a+"\n"+msg3a+"\n"+msg4a+"\n"+msg5a+"\n"+msg6a+"\n"+msg7a+"\n", inline=True)
                        embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n" + msg1b+"% - "+msg1c+"%\n" + msg2b+"% - "+msg2c+"%\n" + msg3b+"% - "+msg3c+"%\n" + msg4b+"% - "+msg4c+"%\n" + msg5b+"% - "+msg5c+"%\n" + msg6b+"% - "+msg6c+"%\n" + msg7b+"% - "+msg7c+"%\n", inline=True)
                        await ctx.author.message.delete()
                        await ctx.send(embed=embed)
                    elif Name == "Mime":
                        RName = "Mimejr"
                        msg = main(str(RName), str("pokeball"))
                        msg1= main(str(RName), str("greatball"))
                        msg2= main(str(RName), str("ultraball"))
                        msg3= main(str(RName), str("duskball"))
                        msg4= main(str(RName), str("repeatball"))
                        msg5= main(str(RName), str("netball"))
                        msg6= main(str(RName), str("Apriball"))
                        msg7= main(str(RName), str("beastball"))
                        List2 = [(msg),(msg1),(msg2),(msg3),(msg4),(msg5),(msg6),(msg7)]
                        List = sorted(List2, key=getNKey)
                        Test = sorted(List, key=getKey, reverse=True)
                        msg = Test[0]
                        msga = str(msg[0])
                        msgb = str(msg[1])
                        msgc = str(msg[2])
                        msg1 = Test[1]
                        msg1a = str(msg1[0])
                        msg1b = str(msg1[1])
                        msg1c = str(msg1[2])                       
                        msg2 = Test[2]
                        msg2a = str(msg2[0])
                        msg2b = str(msg2[1])
                        msg2c = str(msg2[2])                        
                        msg3 = Test[3]
                        msg3a = str(msg3[0])
                        msg3b = str(msg3[1])
                        msg3c = str(msg3[2])
                        msg4 = Test[4]
                        msg4a = str(msg4[0])
                        msg4b = str(msg4[1])
                        msg4c = str(msg4[2])
                        msg5 = Test[5]
                        msg5a = str(msg5[0])
                        msg5b = str(msg5[1])
                        msg5c = str(msg5[2])
                        msg6 = Test[6]
                        msg6a = str(msg6[0])
                        msg6b = str(msg6[1])
                        msg6c = str(msg6[2])
                        msg7 = Test[7]
                        msg7a = str(msg7[0])
                        msg7b = str(msg7[1])
                        msg7c = str(msg7[2])
                        embed = discord.Embed(title= "Mime Jr.'s Capture Odds", description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Mimejr.png")
                        embed.add_field(name= "Ball Type", value=msga+"\n"+msg1a+"\n"+msg2a+"\n"+msg3a+"\n"+msg4a+"\n"+msg5a+"\n"+msg6a+"\n"+msg7a+"\n", inline=True)
                        embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n" + msg1b+"% - "+msg1c+"%\n" + msg2b+"% - "+msg2c+"%\n" + msg3b+"% - "+msg3c+"%\n" + msg4b+"% - "+msg4c+"%\n" + msg5b+"% - "+msg5c+"%\n" + msg6b+"% - "+msg6c+"%\n" + msg7b+"% - "+msg7c+"%\n", inline=True)
                        await ctx.author.message.delete()
                        await ctx.send(embed=embed)
                    elif Name == "Type:":
                        TName = "Type-null"
                        msg = main(str(TName), str("pokeball"))
                        msg1= main(str(TName), str("greatball"))
                        msg2= main(str(TName), str("ultraball"))
                        msg3= main(str(TName), str("duskball"))
                        msg4= main(str(TName), str("repeatball"))
                        msg5= main(str(TName), str("netball"))
                        msg6= main(str(TName), str("Apriball"))
                        msg7= main(str(TName), str("beastball"))
                        List2 = [(msg),(msg1),(msg2),(msg3),(msg4),(msg5),(msg6),(msg7)]
                        List = sorted(List2, key=getNKey)
                        Test = sorted(List, key=getKey, reverse=True)
                        msg = Test[0]
                        msga = str(msg[0])
                        msgb = str(msg[1])
                        msgc = str(msg[2])
                        msg1 = Test[1]
                        msg1a = str(msg1[0])
                        msg1b = str(msg1[1])
                        msg1c = str(msg1[2])                       
                        msg2 = Test[2]
                        msg2a = str(msg2[0])
                        msg2b = str(msg2[1])
                        msg2c = str(msg2[2])                        
                        msg3 = Test[3]
                        msg3a = str(msg3[0])
                        msg3b = str(msg3[1])
                        msg3c = str(msg3[2])
                        msg4 = Test[4]
                        msg4a = str(msg4[0])
                        msg4b = str(msg4[1])
                        msg4c = str(msg4[2])
                        msg5 = Test[5]
                        msg5a = str(msg5[0])
                        msg5b = str(msg5[1])
                        msg5c = str(msg5[2])
                        msg6 = Test[6]
                        msg6a = str(msg6[0])
                        msg6b = str(msg6[1])
                        msg6c = str(msg6[2])
                        msg7 = Test[7]
                        msg7a = str(msg7[0])
                        msg7b = str(msg7[1])
                        msg7c = str(msg7[2])
                        embed = discord.Embed(title= "Type: Null's Capture Odds", description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+TName+".png")
                        embed.add_field(name= "Ball Type", value=msga+"\n"+msg1a+"\n"+msg2a+"\n"+msg3a+"\n"+msg4a+"\n"+msg5a+"\n"+msg6a+"\n"+msg7a+"\n", inline=True)
                        embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n" + msg1b+"% - "+msg1c+"%\n" + msg2b+"% - "+msg2c+"%\n" + msg3b+"% - "+msg3c+"%\n" + msg4b+"% - "+msg4c+"%\n" + msg5b+"% - "+msg5c+"%\n" + msg6b+"% - "+msg6c+"%\n" + msg7b+"% - "+msg7c+"%\n", inline=True)
                        await ctx.author.message.delete()
                        await ctx.send(embed=embed)
                    elif Name == "Nidoranf":
                        msg = main(str(Name), str("pokeball"))
                        msg1= main(str(Name), str("greatball"))
                        msg2= main(str(Name), str("ultraball"))
                        msg3= main(str(Name), str("duskball"))
                        msg4= main(str(Name), str("repeatball"))
                        msg5= main(str(Name), str("netball"))
                        msg6= main(str(Name), str("Apriball"))
                        msg7= main(str(Name), str("beastball"))
                        List2 = [(msg),(msg1),(msg2),(msg3),(msg4),(msg5),(msg6),(msg7)]
                        List = sorted(List2, key=getNKey)
                        Test = sorted(List, key=getKey, reverse=True)
                        msg = Test[0]
                        msga = str(msg[0])
                        msgb = str(msg[1])
                        msgc = str(msg[2])
                        msg1 = Test[1]
                        msg1a = str(msg1[0])
                        msg1b = str(msg1[1])
                        msg1c = str(msg1[2])                       
                        msg2 = Test[2]
                        msg2a = str(msg2[0])
                        msg2b = str(msg2[1])
                        msg2c = str(msg2[2])                        
                        msg3 = Test[3]
                        msg3a = str(msg3[0])
                        msg3b = str(msg3[1])
                        msg3c = str(msg3[2])
                        msg4 = Test[4]
                        msg4a = str(msg4[0])
                        msg4b = str(msg4[1])
                        msg4c = str(msg4[2])
                        msg5 = Test[5]
                        msg5a = str(msg5[0])
                        msg5b = str(msg5[1])
                        msg5c = str(msg5[2])
                        msg6 = Test[6]
                        msg6a = str(msg6[0])
                        msg6b = str(msg6[1])
                        msg6c = str(msg6[2])
                        msg7 = Test[7]
                        msg7a = str(msg7[0])
                        msg7b = str(msg7[1])
                        msg7c = str(msg7[2])
                        embed = discord.Embed(title= "Nidoran♀️", description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                        embed.add_field(name= "Ball Type", value=msga+"\n"+msg1a+"\n"+msg2a+"\n"+msg3a+"\n"+msg4a+"\n"+msg5a+"\n"+msg6a+"\n"+msg7a+"\n", inline=True)
                        embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n" + msg1b+"% - "+msg1c+"%\n" + msg2b+"% - "+msg2c+"%\n" + msg3b+"% - "+msg3c+"%\n" + msg4b+"% - "+msg4c+"%\n" + msg5b+"% - "+msg5c+"%\n" + msg6b+"% - "+msg6c+"%\n" + msg7b+"% - "+msg7c+"%\n", inline=True)
                        await ctx.author.message.delete()
                        await ctx.send(embed=embed)
                    elif Name == "Nidoranm":
                        msg = main(str(Name), str("pokeball"))
                        msg1= main(str(Name), str("greatball"))
                        msg2= main(str(Name), str("ultraball"))
                        msg3= main(str(Name), str("duskball"))
                        msg4= main(str(Name), str("repeatball"))
                        msg5= main(str(Name), str("netball"))
                        msg6= main(str(Name), str("Apriball"))
                        msg7= main(str(Name), str("beastball"))
                        List2 = [(msg),(msg1),(msg2),(msg3),(msg4),(msg5),(msg6),(msg7)]
                        List = sorted(List2, key=getNKey)
                        Test = sorted(List, key=getKey, reverse=True)
                        msg = Test[0]
                        msga = str(msg[0])
                        msgb = str(msg[1])
                        msgc = str(msg[2])
                        msg1 = Test[1]
                        msg1a = str(msg1[0])
                        msg1b = str(msg1[1])
                        msg1c = str(msg1[2])                       
                        msg2 = Test[2]
                        msg2a = str(msg2[0])
                        msg2b = str(msg2[1])
                        msg2c = str(msg2[2])                        
                        msg3 = Test[3]
                        msg3a = str(msg3[0])
                        msg3b = str(msg3[1])
                        msg3c = str(msg3[2])
                        msg4 = Test[4]
                        msg4a = str(msg4[0])
                        msg4b = str(msg4[1])
                        msg4c = str(msg4[2])
                        msg5 = Test[5]
                        msg5a = str(msg5[0])
                        msg5b = str(msg5[1])
                        msg5c = str(msg5[2])
                        msg6 = Test[6]
                        msg6a = str(msg6[0])
                        msg6b = str(msg6[1])
                        msg6c = str(msg6[2])
                        msg7 = Test[7]
                        msg7a = str(msg7[0])
                        msg7b = str(msg7[1])
                        msg7c = str(msg7[2])
                        embed = discord.Embed(title= "Nidoran♂️", description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                        embed.add_field(name= "Ball Type", value=msga+"\n"+msg1a+"\n"+msg2a+"\n"+msg3a+"\n"+msg4a+"\n"+msg5a+"\n"+msg6a+"\n"+msg7a+"\n", inline=True)
                        embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n" + msg1b+"% - "+msg1c+"%\n" + msg2b+"% - "+msg2c+"%\n" + msg3b+"% - "+msg3c+"%\n" + msg4b+"% - "+msg4c+"%\n" + msg5b+"% - "+msg5c+"%\n" + msg6b+"% - "+msg6c+"%\n" + msg7b+"% - "+msg7c+"%\n", inline=True)
                        await ctx.author.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        msg = main(str(Name), str("pokeball")) 
                        if msg[1] == 0.0:
                            await ctx.send("This Pokemon does not exist")
                        else:
                            msg1= main(str(Name), str("greatball"))
                            msg2= main(str(Name), str("ultraball"))
                            msg3= main(str(Name), str("duskball"))
                            msg4= main(str(Name), str("repeatball"))
                            msg5= main(str(Name), str("netball"))
                            msg6= main(str(Name), str("Apriball"))
                            msg7= main(str(Name), str("beastball"))
                            List2 = [(msg),(msg1),(msg2),(msg3),(msg4),(msg5),(msg6),(msg7)]
                            List = sorted(List2, key=getNKey)
                            Test = sorted(List, key=getKey, reverse=True)
                            msg = Test[0]
                            msga = str(msg[0])
                            msgb = str(msg[1])
                            msgc = str(msg[2])
                            msg1 = Test[1]
                            msg1a = str(msg1[0])
                            msg1b = str(msg1[1])
                            msg1c = str(msg1[2])                       
                            msg2 = Test[2]
                            msg2a = str(msg2[0])
                            msg2b = str(msg2[1])
                            msg2c = str(msg2[2])                        
                            msg3 = Test[3]
                            msg3a = str(msg3[0])
                            msg3b = str(msg3[1])
                            msg3c = str(msg3[2])
                            msg4 = Test[4]
                            msg4a = str(msg4[0])
                            msg4b = str(msg4[1])
                            msg4c = str(msg4[2])
                            msg5 = Test[5]
                            msg5a = str(msg5[0])
                            msg5b = str(msg5[1])
                            msg5c = str(msg5[2])
                            msg6 = Test[6]
                            msg6a = str(msg6[0])
                            msg6b = str(msg6[1])
                            msg6c = str(msg6[2])
                            msg7 = Test[7]
                            msg7a = str(msg7[0])
                            msg7b = str(msg7[1])
                            msg7c = str(msg7[2])
                            if Name == "Farfetch'd":
                                Nfame = "Farfetchd"
                                embed = discord.Embed(title= Name + "'s Capture Odds", description="", color=0x2962FF)
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Mfame+".png")
                                embed.add_field(name= "Ball Type", value=msga+"\n"+msg1a+"\n"+msg2a+"\n"+msg3a+"\n"+msg4a+"\n"+msg5a+"\n"+msg6a+"\n"+msg7a+"\n", inline=True)
                                embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n" + msg1b+"% - "+msg1c+"%\n" + msg2b+"% - "+msg2c+"%\n" + msg3b+"% - "+msg3c+"%\n" + msg4b+"% - "+msg4c+"%\n" + msg5b+"% - "+msg5c+"%\n" + msg6b+"% - "+msg6c+"%\n" + msg7b+"% - "+msg7c+"%\n", inline=True)
                                await ctx.author.message.delete()
                                await ctx.send(embed=embed)
                            else:
                                embed = discord.Embed(title= Name + "'s Capture Odds", description="", color=0x2962FF)
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                                embed.add_field(name= "Ball Type", value=msga+"\n"+msg1a+"\n"+msg2a+"\n"+msg3a+"\n"+msg4a+"\n"+msg5a+"\n"+msg6a+"\n"+msg7a+"\n", inline=True)
                                embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n" + msg1b+"% - "+msg1c+"%\n" + msg2b+"% - "+msg2c+"%\n" + msg3b+"% - "+msg3c+"%\n" + msg4b+"% - "+msg4c+"%\n" + msg5b+"% - "+msg5c+"%\n" + msg6b+"% - "+msg6c+"%\n" + msg7b+"% - "+msg7c+"%\n", inline=True)
                                await ctx.author.message.delete()
                                await ctx.send(embed=embed)
            else:
                Ballist = ["Pokeball","Greatball","Ultraball","Masterball","Safariball","Fastball","Levelball","Lureball","Heavyball","Loveball","Friendball","Moonball",
                           "Sportsball","Netball","Nestball","Repeatball","Timerball","Luxuryball","Premierball","Diveball","Duskball","Healball","Quickball", "Dreamball", "Beastball"]
                    
                Name = string.capwords(content[1])
                Ball = string.capwords(content[2])
                namea = "Alolan"
                namegl = "Galarian"
                nameg = "Gmax"
                if Name == namea:
                    GaName = string.capwords(content[2])
                    Listofalola = ["Rattata","Raticate","Raichu","Sandshrew","Sandslash","Vulpix","Ninetails","Diglett","Dugtrio","Meowth","Persian","Geodude","Graveler",
                                   "Golem","Grimer","Muk","Exeggutor","Marowak"]
                    if GaName in Listofalola:
                            Ball = string.capwords(content[3])
                            if Ball in Ballist:
                                msg = alolanmain(str(GaName), str(Ball))       
                                msga = str(msg[0])
                                msgb = str(msg[1])
                                msgc = str(msg[2])
                                embed = discord.Embed(title= "Alolan " + GaName + "'s Capture Odds", description="", color=0x2962FF)
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Alolan/Shiny/"+GaName+".png")
                                embed.add_field(name= "Ball Type", value=msga, inline=True)
                                embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n", inline=True)
                                await ctx.author.message.delete()
                                await ctx.send(embed=embed)
                            elif Ball not in Ballist:
                                await ctx.send("This Pokeball doesn't exist")
                    else:
                        await ctx.send('This Alolan Pokémon does not exist!')       
                elif Name == namegl:
                    GlName = string.capwords(content[2])
                    GlmName = string.capwords(content[2]) + " Mime"
                    Listofgalar = ["Meowth","Ponyta","Rapidash","Slowpoke","Slowbro","Farfetch'd","Weezing","Mr Mime","Corsola","Zigzagoon","Linoone","Darumaka",
                                   "Darmanitan","Yamask","Stunfisk"]
                    if GlName in Listofgalar or GlmName in Listofgalar:
                        if GlName == "Mr":
                            RGName = "Mrmime"
                            Ball = string.capwords(content[4])
                            if Ball in Ballist:
                                msg = galarianmain(str(RGName), str(Ball))
                                msga = str(msg[0])
                                msgb = str(msg[1])
                                msgc = str(msg[2])
                                embed = discord.Embed(title= "Galarian Mr. Mime's Capture Odds", description="", color=0x2962FF)
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/Shiny/Mrmime.png")
                                embed.add_field(name= "Ball Type", value=msga, inline=True)
                                embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n", inline=True)
                                await ctx.author.message.delete()
                                await ctx.send(embed=embed)
                            elif Ball not in Ballist:
                                await ctx.send("This Pokeball doesn't exist")
                        elif GlName != "Mr":
                            
                            Ball = string.capwords(content[3])
                            if Ball in Ballist:
                                msg = galarianmain(str(GlName), str(Ball))
                                msga = str(msg[0])
                                msgb = str(msg[1])
                                msgc = str(msg[2])
                                if GlName == "Farfetch'd":
                                    GlfName = "Farfetchd"
                                    embed = discord.Embed(title= "Galarian " + GlName + "'s Capture Odds", description="", color=0x2962FF)
                                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/Shiny/"+GlfName+".png")
                                    embed.add_field(name= "Ball Type", value=msga, inline=True)
                                    embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n", inline=True)
                                    await ctx.author.message.delete()
                                    await ctx.send(embed=embed)
                                else:
                                    embed = discord.Embed(title= "Galarian " + GlName + "'s Capture Odds", description="", color=0x2962FF)
                                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/Shiny/"+GlName+".png")
                                    embed.add_field(name= "Ball Type", value=msga, inline=True)
                                    embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n", inline=True)
                                    await ctx.author.message.delete()
                                    await ctx.send(embed=embed)
                            elif Ball not in Ballist:
                                ctx.send("This Pokeball doesn't exist")
                    else:
                        await ctx.send('This Galarian Pokémon does not exist!')       
                elif Name == nameg:
                    GName = string.capwords(content[2])
                    Listofgmax = ["Venusaur","Charizard","Blastoise","Butterfree","Pikachu","Meowth","Machamp","Gengar","Kingler","Lapras","Eevee","Snorlax","Garbodor",
                                  "Melmetal","Rillaboom","Cinderace","Inteleon","Corviknight","Orbeetle","Drednaw","Coalossal","Flapple","Appletun","Sandaconda","Toxtricity",
                                  "Centiskorch", "Hatterene","Grimmsnarl","Alcremie","Copperajah","Duraludon","Urshifu"]
                    if GName in Listofgmax:
                        Ball = string.capwords(content[3])
                        if Ball in Ballist:                       
                            if Ball == "Heavyball":
                                msg = gmaxmain(str(GName), str("Pokeball"))
                                msga = "Heavyball"
                                msgb = str(msg[1])
                                msgc = str(msg[2])
                                embed = discord.Embed(title= "Gmax " + GName + "'s Capture Odds", description="", color=0x2962FF)
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Gmax/Shiny/"+GName+".png")
                                embed.add_field(name= "Ball Type", value=msga, inline=True)
                                embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n", inline=True)
                                await ctx.author.message.delete()
                                await ctx.send(embed=embed)
                            else:
                                msg = gmaxmain(str(GName), str(Ball))
                                msga = str(msg[0])
                                msgb = str(msg[1])
                                msgc = str(msg[2])
                                embed = discord.Embed(title= "Gmax " + GName + "'s Capture Odds", description="", color=0x2962FF)
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Gmax/Shiny/"+GName+".png")
                                embed.add_field(name= "Ball Type", value=msga, inline=True)
                                embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n", inline=True)
                                await ctx.author.message.delete()
                                await ctx.send(embed=embed)
                        elif Ball not in Ballist:
                            await ctx.send("This Pokeball Doesn't exist")
                    else:
                        await ctx.send('This Gmax Pokémon does not exist!')
                elif Name != nameg:
                    if Name == "Mr":
                        FLCap = string.capwords(content[1])
                        FLLCap = string.capwords(content[2])
                        RName = FLCap + content[2]
                        RealN= FLCap+". "+FLLCap
                        LowN = content[1].lower()
                        LowM = content[2].lower()
                        Ball = string.capwords(content[3])
                        if Ball in Ballist:
                            msg = main(str(RName), str(Ball))
                            msga = str(msg[0])
                            msgb = str(msg[1])
                            msgc = str(msg[2])
                            embed = discord.Embed(title= RealN + "'s Capture Odds", description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+RName+".png")
                            embed.add_field(name= "Ball Type", value=msga, inline=True)
                            embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n", inline=True)
                            await ctx.author.message.delete()
                            await ctx.send(embed=embed)
                        elif Ball not in Ballist:
                            await ctx.send("This Pokeball Doesn't exist")
                    elif Name == "Mime":
                        RName = "Mimejr"
                        Ball = string.capwords(content[3])
                        if Ball in Ballist:
                            msg = main(str(RName), str(Ball))
                            msga = str(msg[0])
                            msgb = str(msg[1])
                            msgc = str(msg[2])
                            embed = discord.Embed(title= "Mime Jr.'s Capture Odds", description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Mimejr.png")
                            embed.add_field(name= "Ball Type", value=msga, inline=True)
                            embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n", inline=True)
                            await ctx.author.message.delete()
                            await ctx.send(embed=embed)
                        elif Ball not in Ballist:
                            await ctx.send("This Pokeball Doesn't exist")
                    elif Name == "Type:":
                        TName = "Type-null"
                        Ball = string.capwords(content[3])
                        if Ball in Ballist:
                            msg = main(str(TName), str(Ball))
                            msga = str(msg[0])
                            msgb = str(msg[1])
                            msgc = str(msg[2])
                            embed = discord.Embed(title= "Type: Null's Capture Odds", description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+TName+".png")
                            embed.add_field(name= "Ball Type", value=msga, inline=True)
                            embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n", inline=True)
                            await ctx.author.message.delete()
                            await ctx.send(embed=embed)
                        elif Ball not in Ballist:
                            await ctx.send("This Pokeball Doesn't exist")
                    elif Name == "Nidoranf":
                        if Ball not in Ballist:
                            msg = main(str(Name), str(Ball))
                            msga = str(msg[0])
                            msgb = str(msg[1])
                            msgc = str(msg[2])
                            embed = discord.Embed(title= "Nidoran♀️", description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                            embed.add_field(name= "Ball Type", value=msga, inline=True)
                            embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n", inline=True)
                            await ctx.author.message.delete()
                            await ctx.send(embed=embed)
                        elif Ball not in Ballist:
                            await ctx.send("This Pokeball Doesn't exist")
                    elif Name == "Nidoranm":
                        if Ball in Ballist:
                            msg = main(str(Name), str(Ball))
                            msga = str(msg[0])
                            msgb = str(msg[1])
                            msgc = str(msg[2])
                            embed = discord.Embed(title= "Nidoran♂️", description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                            embed.add_field(name= "Ball Type", value=msga, inline=True)
                            embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n", inline=True)
                            await ctx.author.message.delete()
                            await ctx.send(embed=embed)
                        elif Ball not in Ballist:
                            await ctx.send("This Pokeball Doesn't exist")
                    else:
                        if Ball in Ballist:
                            msg = main(str(Name), str(Ball)) 
                            if msg[1] == 0.0:
                                await ctx.send("This Pokemon does not exist")
                            else:
                                msga = str(msg[0])
                                msgb = str(msg[1])
                                msgc = str(msg[2])
                                if Name == "Farfetch'd":
                                    Nfame = "Farfetchd"
                                    embed = discord.Embed(title= Name + "'s Capture Odds", description="", color=0x2962FF)
                                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Mfame+".png")
                                    embed.add_field(name= "Ball Type", value=msga, inline=True)
                                    embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n", inline=True)
                                    await ctx.author.message.delete()
                                    await ctx.send(embed=embed)
                                else:
                                    embed = discord.Embed(title= Name + "'s Capture Odds", description="", color=0x2962FF)
                                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                                    embed.add_field(name= "Ball Type", value=msga, inline=True)
                                    embed.add_field(name="Odds", value=msgb+"% - "+msgc+"%\n", inline=True)
                                    await ctx.author.message.delete()
                                    await ctx.send(embed=embed)
                        elif Ball not in Ballist:
                            await ctx.send("This Pokeball Doesn't exist")
   
    @commands.command(name ='pokedex', help='Looks up information on Pokemon')                   
    async def pokedex(self, ctx):
        responce = str(ctx.message.content)
        if responce.startswith('%pokedex'):
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
                    result = alolanpokedex(str(AName))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    w = AName
                    embed = discord.Embed(title= a + " " + Name + " " + AName + "   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Alolan/Shiny/"+w+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                else:
                    await ctx.send('This Alolan Pokémon does not exist')          
            elif Name == namegl:
                GlName = string.capwords(content[2])
                GlmName = string.capwords(content[2]) + " Mime"
                Listofgalar = ["Meowth","Ponyta","Rapidash","Slowpoke","Slowbro","Farfetch'd","Weezing","Mr Mime","Articuno","Zapdos","Moltres","Slowking","Corsola","Zigzagoon","Linoone","Darumaka",
                               "Darmanitan","Yamask","Stunfisk"]
                if GlName in Listofgalar or GlmName in Listofgalar:
                    if GlName == "Mr":
                        RGName = "Mrmime"
                        result = galarianpokedex(str(RGName))
                        a = str(result[0])
                        b = str(result[1])
                        c = str(result[2])                 
                        d = str(result[3])
                        e = str(result[4])
                        f = str(result[5])
                        g = str(result[6])
                        h = str(result[7])
                        i = str(result[8])
                        j = str(result[9])
                        k = str(result[10])
                        l = str(result[11])
                        m = str(result[12])
                        n = str(result[13])
                        o = str(result[14])
                        p = str(result[15])
                        q = str(result[16])
                        r = str(result[17])
                        s = str(result[18])
                        t = str(result[19])
                        u = str(result[20])
                        v = str(result[21])
                        w = Name.lower()
                        embed = discord.Embed(title= a + "   " + Name + " " + GlmName + "   " + c , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/Shiny/"+RGName+".png")
                        embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                        embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                        embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                        embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                        await ctx.author.message.delete()
                        await ctx.send(embed=embed)
                    elif GlName != "Mr":                       
                        if GlName== "Darmanitan":  
                                    result = galarianpokedex(str(GlName))
                                    a = str(result[0])
                                    b = str(result[1])
                                    c = str(result[2])
                                    d = str(result[3])
                                    e = str(result[4])
                                    f = str(result[5])
                                    g = str(result[6])
                                    h = str(result[7])
                                    i = str(result[8])
                                    j = str(result[9])
                                    k = str(result[10])
                                    l = str(result[11])
                                    m = str(result[12])
                                    n = str(result[13])
                                    o = str(result[14])
                                    p = str(result[15])
                                    q = str(result[16])
                                    r = str(result[17])
                                    s = str(result[18])
                                    t = str(result[19])
                                    u = str(result[20])
                                    v = str(result[21])
                                    w = GlName
                                    embed = discord.Embed(title= a + "   " + Name + " " + GlName + "   " + c , description="", color=0x2962FF)
                                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/Shiny/"+GlName+".png")
                                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                                    await ctx.author.message.delete()
                                    await ctx.send(embed=embed)

                                    GzzName = "Darmanitanzen"
                                    result = galarianpokedex(str(GzzName))
                                    a1 = str(result[0])
                                    b1 = str(result[1])
                                    c1 = str(result[2])
                                    d1 = str(result[3])
                                    e1 = str(result[4])
                                    f1 = str(result[5])
                                    g1 = str(result[6])
                                    h1 = str(result[7])
                                    i1 = str(result[8])
                                    j1 = str(result[9])
                                    k1 = str(result[10])
                                    l1 = str(result[11])
                                    m1 = str(result[12])
                                    n1 = str(result[13])
                                    o1 = str(result[14])
                                    p1 = str(result[15])
                                    q1 = str(result[16])
                                    r1 = str(result[17])
                                    s1 = str(result[18])
                                    t1 = str(result[19])
                                    u1 = str(result[20])
                                    v1 = str(result[21])
                                    embed = discord.Embed(title= a1 + "   " + Name + " Darmanitan Zen Mode   " + c1 , description="", color=0x2962FF)
                                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/Shiny/"+GzzName+".png")
                                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                                    await ctx.send(embed=embed)              
                        else:
                            result = galarianpokedex(str(GlName))
                            a = str(result[0])
                            b = str(result[1])
                            c = str(result[2])
                            d = str(result[3])
                            e = str(result[4])
                            f = str(result[5])
                            g = str(result[6])
                            h = str(result[7])
                            i = str(result[8])
                            j = str(result[9])
                            k = str(result[10])
                            l = str(result[11])
                            m = str(result[12])
                            n = str(result[13])
                            o = str(result[14])
                            p = str(result[15])
                            q = str(result[16])
                            r = str(result[17])
                            s = str(result[18])
                            t = str(result[19])
                            u = str(result[20])
                            v = str(result[21])
                            w = GlName
                            if GlName == "Farfetch'd":
                                w = "Farfetchd"
                                embed = discord.Embed(title= a + "   " + Name + " " + GlName + "   " + c , description="", color=0x2962FF)
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/Shiny/"+w+".png")
                                embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                                embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                                embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                                embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                                await ctx.author.message.delete()
                                await ctx.send(embed=embed)
                            else:
                                embed = discord.Embed(title= a + "   " + Name + " " + GlName + "   " + c , description="", color=0x2962FF)
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/Shiny/"+w+".png")
                                embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                                embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                                embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                                embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                                await ctx.author.message.delete()
                                await ctx.send(embed=embed)

                    else:
                        await ctx.send('This Galarian Pokémon does not exist!')                   
            elif Name != namegl:
                if Name == "Mr":
                    if content[2] == "mime":
                        RName = "Mrmime"
                        result = pokedex(str(RName))
                        a = str(result[0])
                        b = str(result[1])
                        c = str(result[2])
                        d = str(result[3])
                        e = str(result[4])
                        f = str(result[5])
                        g = str(result[6])
                        h = str(result[7])
                        i = str(result[8])
                        j = str(result[9])
                        k = str(result[10])
                        l = str(result[11])
                        m = str(result[12])
                        n = str(result[13])
                        o = str(result[14])
                        p = str(result[15])
                        q = str(result[16])
                        r = str(result[17])
                        s = str(result[18])
                        t = str(result[19])
                        u = str(result[20])
                        v = str(result[21])
                        embed = discord.Embed(title= a + "   Mr. Mime️   " + c , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+RName+".png")
                        embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                        embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                        embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                        embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                        await ctx.author.message.delete()
                        await ctx.send(embed=embed)
                    elif content[2] == 'rime':
                        RRName = "Mrrime"
                        result = pokedex(str(RRName))
                        a = str(result[0])
                        b = str(result[1])
                        c = str(result[2])
                        d = str(result[3])
                        e = str(result[4])
                        f = str(result[5])
                        g = str(result[6])
                        h = str(result[7])
                        i = str(result[8])
                        j = str(result[9])
                        k = str(result[10])
                        l = str(result[11])
                        m = str(result[12])
                        n = str(result[13])
                        o = str(result[14])
                        p = str(result[15])
                        q = str(result[16])
                        r = str(result[17])
                        s = str(result[18])
                        t = str(result[19])
                        u = str(result[20])
                        v = str(result[21])
                        embed = discord.Embed(title= a + "   Mr. Rime️   " + c , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+RRName+".png")
                        embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                        embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                        embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                        embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                        await ctx.author.message.delete()
                        await ctx.send(embed=embed)
                if Name == "Mime":
                    RName = "Mimejr"
                    result = pokedex(str(RName))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    w = Name.lower()
                    embed = discord.Embed(title= a + "    " + Name + "   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+RName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                elif Name == "Type:":
                    TName = "Type-null"
                    result = pokedex(str(TName))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    w = Name.lower()
                    embed = discord.Embed(title= a + " Type: Null   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)   
                elif Name == "Nidoranf":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    w = Name.lower()
                    embed = discord.Embed(title= a + "   Nidoran♀️   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                elif Name == "Nidoranm":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])                   
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    w = Name.lower()
                    embed = discord.Embed(title= a + "   Nidoran♂️   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                elif Name== "Darmanitan":  
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   " + Name + "   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Darmanitanzen"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Darmanitan Zen Mode   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Wormadam":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   " + Name + " Plant Cloak   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Wormadams"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   " + Name + " Sandy Cloak  " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                    
                    GzzzName = "Wormadamt"
                    result = pokedex(str(GzzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   " + Name + " Trash Cloak  " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Kyogre":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   " + Name + "   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Kyogreprimal"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Primal " + Name + "  " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Groudon":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   " + Name + "   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Groudonprimal"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Primal " + Name + "   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Deoxys":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   " + Name + " Normal Form   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                    
                    GzzName = "Adeoxys"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   " + Name + " Attack Form  " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                    
                    GzzzName = "Ddeoxys"
                    result = pokedex(str(GzzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   " + Name + " Defense Form  " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                    
                    GzzzzName = "Sdeoxys"
                    result = pokedex(str(GzzzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   " + Name + " Speed Form  " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Rotom":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   " + Name + "   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Hrotom"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Heat " + Name + "   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)

                    GzzzName = "Wrotom"
                    result = pokedex(str(GzzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Wash " + Name + "   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)

                    GzzzzName = "Frotom"
                    result = pokedex(str(GzzzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Frost " + Name + "   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                    
                    GzzzzzName = "Fanrotom"
                    result = pokedex(str(GzzzzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Fan " + Name + "   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                    
                    GzzzzzzName = "Mrotom"
                    result = pokedex(str(GzzzzzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Mow " + Name + "   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzzzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Giratina":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   " + Name + " Altered Form   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Ogiratina"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   " + Name + " Origin Form  " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Shaymin":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   " + Name + " Land Forme   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Sshaymin"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   " + Name + " Sky Forme " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Tornadus":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   " + Name + " Incarnate Forme   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Ttornadus"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   " + Name + " Therian Forme   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Thundurus":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   " + Name + " Incanate Forme   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Tthundurus"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   " + Name + " Therian Forme   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Landorus":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   " + Name + " Incarnate Forme   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Tlandorus"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   " + Name + " Therian Forme   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Kyurem":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   " + Name + "   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Blackkyurem"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Black " + Name + "  " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                    
                    GzzzName = "Whitekyurem"
                    result = pokedex(str(GzzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   White " + Name + "  " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Meloetta":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   " + Name + " Aria Forme   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Pmeloetta"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   " + Name + " Pirouette Forme   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Greninja":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   " + Name + "   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Ashgreninja"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Ash-" + Name + "  " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Aegislash":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   " + Name + " Shield Forme   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Baegislash"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   " + Name + " Blade Forme   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)                
                elif Name == "Pumpkaboo":                    
                    GzzaName = "Tpumpkaboo"
                    result = pokedex(str(GzzaName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Small Size " + Name + "   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzaName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()                    
                    await ctx.send(embed=embed)                    
                    
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   Average Size " + Name + "   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)

                    GzzzName = "Lpumpkaboo"
                    result = pokedex(str(GzzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Large Size " + Name + "  " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)

                    GzzzzName = "Spumpkaboo"
                    result = pokedex(str(GzzzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Super Size " + Name + "  " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Gourgeist":
                    GzzvName = "Smgourgeist"
                    result = pokedex(str(GzzvName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Small Size " + Name + "   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzvName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   Average Size " + Name + "   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)

                    GzzName = "Lgourgeist"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Large Size " + Name + "  " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                    
                    GzzzName = "Sgourgeist"
                    result = pokedex(str(GzzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Super Size " + Name + "  " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)                    
                elif Name == "Zygarde":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   50% Forme " + Name + "   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Tzygarde"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   10% Forme " + Name + "   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                    
                    GzzzName = "Czygarde"
                    result = pokedex(str(GzzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Complete Forme " + Name + "   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Hoopa":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   " + Name + " Confined   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Uhoopa"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   " + Name + " Unbound   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Lycanroc":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   Midday Form " + Name + "   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Mlycanroc"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Midnight Form " + Name + "   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                    
                    GzzzName = "Dlycanroc"
                    result = pokedex(str(GzzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Dusk Forme " + Name + "  " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Wishiwashi":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   Solo Form " + Name + "   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Swishiwashi"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   School Form" + Name + "   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Necrozma":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   " + Name + "   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Dmnecrozma"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Dusk Mane " + Name + "   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed) 

                    GzzzName = "Dwnecrozma"
                    result = pokedex(str(GzzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Dawn Wing " + Name + "   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed) 

                    GzzzzName = "Unecrozma"
                    result = pokedex(str(GzzzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Ultra " + Name + "   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)                     
                elif Name == "Eiscue":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   Ice Face " + Name + "   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Neiscue"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Noice Face " + Name + "   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Zacian":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   " + Name + ": Hero of Many Battles   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Czacian"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Crowned " + Name + "   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Zamazenta":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   " + Name + ": Hero of Many Battles   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Czamazenta"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   Crowned " + Name + "   " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                elif Name == "Urshifu":
                    result = pokedex(str(Name))
                    a = str(result[0])
                    b = str(result[1])
                    c = str(result[2])
                    d = str(result[3])
                    e = str(result[4])
                    f = str(result[5])
                    g = str(result[6])
                    h = str(result[7])
                    i = str(result[8])
                    j = str(result[9])
                    k = str(result[10])
                    l = str(result[11])
                    m = str(result[12])
                    n = str(result[13])
                    o = str(result[14])
                    p = str(result[15])
                    q = str(result[16])
                    r = str(result[17])
                    s = str(result[18])
                    t = str(result[19])
                    u = str(result[20])
                    v = str(result[21])
                    embed = discord.Embed(title= a + "   " + Name + " 'Single Strike Style'   " + c , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

                    GzzName = "Rurshifu"
                    result = pokedex(str(GzzName))
                    a1 = str(result[0])
                    b1 = str(result[1])
                    c1 = str(result[2])
                    d1 = str(result[3])
                    e1 = str(result[4])
                    f1 = str(result[5])
                    g1 = str(result[6])
                    h1 = str(result[7])
                    i1 = str(result[8])
                    j1 = str(result[9])
                    k1 = str(result[10])
                    l1 = str(result[11])
                    m1 = str(result[12])
                    n1 = str(result[13])
                    o1 = str(result[14])
                    p1 = str(result[15])
                    q1 = str(result[16])
                    r1 = str(result[17])
                    s1 = str(result[18])
                    t1 = str(result[19])
                    u1 = str(result[20])
                    v1 = str(result[21])
                    embed = discord.Embed(title= a1 + "   " + Name + " 'Rapid Strike Style'  " + c1 , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o1+"% M** / **"+p1+"% F**\nHeight/Weight: \n**"+q1+"m** / **"+r1+"kg**\nCatch Rate: **"+k1+"**\n**"+b1+"**\nEgg Groups: **"+s1+"** , **"+t1+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+d1+"**\nAtk: **"+e1+"**\nDef: **"+f1+"**\nSpA: **"+g1+"**\nSpD: **"+h1+"**\nSpe: **"+i1+"**\nTotal: **"+ j1 +"**", inline=True)
                    embed.add_field(name="Abilites", value="Ability 1: \n**" +l1+"**\nAbility 2: \n**"+m1+"**\nHidden Ability: \n**" + n1 +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ u1 +"\nShield: " + v1, inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.send(embed=embed)
                else: 
                    result = pokedex(str(Name))
                    if result == None:
                        await ctx.author.message.delete()
                        await ctx.send('This Pokémon does not exist!')
                    elif result != None: 
                        a = str(result[0])
                        b = str(result[1])
                        c = str(result[2])
                        d = str(result[3])
                        e = str(result[4])
                        f = str(result[5])
                        g = str(result[6])
                        h = str(result[7])
                        i = str(result[8])
                        j = str(result[9])
                        k = str(result[10])
                        l = str(result[11])
                        m = str(result[12])
                        n = str(result[13])
                        o = str(result[14])
                        p = str(result[15])
                        q = str(result[16])
                        r = str(result[17])
                        s = str(result[18])
                        t = str(result[19])
                        u = str(result[20])
                        v = str(result[21])
                        w = Name.lower()
                        embed = discord.Embed(title= a + "   " + Name + "   " + c , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Name+".png")
                        embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+o+"% M** / **"+p+"% F**\nHeight/Weight: \n**"+q+"m** / **"+r+"kg**\nCatch Rate: **"+k+"**\n**"+b+"**\nEgg Groups: **"+s+"** , **"+t+"**" , inline=True)
                        embed.add_field(name="Base Stats", value="HP: **"+d+"**\nAtk: **"+e+"**\nDef: **"+f+"**\nSpA: **"+g+"**\nSpD: **"+h+"**\nSpe: **"+i+"**\nTotal: **"+ j +"**", inline=True)
                        embed.add_field(name="Abilites", value="Ability 1: \n**" +l+"**\nAbility 2: \n**"+m+"**\nHidden Ability: \n**" + n +"**", inline=True)
                        embed.add_field(name="Dens", value="Sword: "+ u +"\nShield: " + v, inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                        await ctx.author.message.delete()
                        await ctx.send(embed=embed)

    @commands.command(name ='natures', help='Shows a chart of Pokemon natures')
    async def natures(self, ctx):
        responce = str(ctx.message.content)
        if responce.startswith("%natures"):
            embed = discord.Embed(title="", description="", color=0x2962FF)
            embed.set_image(url="https://static2.thegamerimages.com/wordpress/wp-content/uploads/2019/04/Nature-Charrt-via-Bulbapedia.jpg?")
            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
            await ctx.author.message.delete()
            await ctx.send(embed=embed)

    @commands.command(name ='ball', help='Looks up information on Pokeballs')                   
    async def ball(self, ctx):
        responce = str(ctx.message.content)
        if responce.startswith('%ball'):
            content = responce.split()
            BName = string.capwords(content[1])
            if BName.startswith("Cherish") or BName.startswith("Premier"):
                baln = BName[0:7]    
                ballresult = ball(str(baln))
                b1 = ballresult[0]
                b2 = ballresult[1]
                b3 = ballresult[2]
                lbname = baln.lower()
                link = "https://serebii.net/itemdex/"+lbname+"ball.shtml"
                
                embed = discord.Embed(title= "**"+ baln + " Ball**", url=link, color=0x2962FF)
                embed.set_thumbnail(url= "https://img.pokemondb.net/sprites/items/"+lbname+"-ball.png")
                embed.add_field(name= "**Info:**", value="**Ball Modifier**: `"+b1+"`\n**Ball Conditions**: `"+b2+"`\n**Ball Effects**: `"+b3+"`", inline=True)
                
                if baln == "Cherish":
                    embed.set_image(url="https://media2.giphy.com/media/jnEBXaTewyLpqIttNi/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                    
                elif baln == "Premier":
                    embed.set_image(url="https://media0.giphy.com/media/RISohRZRfEQ4sJFZvw/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)

            elif BName.startswith("Friend") or BName.startswith("Luxury") or BName.startswith("Master") or BName.startswith("Repeat") or BName.startswith("Safari") or BName.startswith("Sports"):
                baln = BName[0:6]    
                ballresult = ball(str(baln))
                b1 = ballresult[0]
                b2 = ballresult[1]
                b3 = ballresult[2]
                lbname = baln.lower()
                link = "https://serebii.net/itemdex/"+lbname+"ball.shtml"
                
                embed = discord.Embed(title= "**"+ baln + " Ball**", url=link, color=0x2962FF)
                embed.set_thumbnail(url= "https://img.pokemondb.net/sprites/items/"+lbname+"-ball.png")
                embed.add_field(name= "**Info:**", value="**Ball Modifier**: `"+b1+"`\n**Ball Conditions**: `"+b2+"`\n**Ball Effects**: `"+b3+"`", inline=True)
                
                if baln == "Friend":
                    embed.set_image(url="https://media0.giphy.com/media/f7Yl1vFzJqAudkJLTZ/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                    
                elif baln == "Luxury":
                    embed.set_image(url="https://media0.giphy.com/media/l29PJ0F8w8tvqPOZsn/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                
                elif baln == "Master":
                    embed.set_image(url="https://media0.giphy.com/media/ggKzsZLL9d3xv6gsaQ/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                    
                elif baln == "Repeat":
                    embed.set_image(url="https://media2.giphy.com/media/lrzfd4lZI8BdWdJVHw/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                
                elif baln == "Safari":
                    embed.set_image(url="https://media2.giphy.com/media/ihYy3vbNBdSZ12oPFv/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                
                elif baln == "Sports":
                    embed.set_image(url="https://media1.giphy.com/media/ihSCEcioiNza0EkPJ8/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                    
            elif BName.startswith("Beast") or BName.startswith("Dream") or BName.startswith("Great") or BName.startswith("Heavy") or BName.startswith("Level") or BName.startswith("Quick") or BName.startswith("Timer") or BName.startswith("Ultra"):
                baln = BName[0:5]    
                ballresult = ball(str(baln))
                b1 = ballresult[0]
                b2 = ballresult[1]
                b3 = ballresult[2]
                lbname = baln.lower()
                link = "https://serebii.net/itemdex/"+lbname+"ball.shtml"
                
                embed = discord.Embed(title= "**"+ baln + " Ball**", url=link, color=0x2962FF)
                embed.set_thumbnail(url= "https://img.pokemondb.net/sprites/items/"+lbname+"-ball.png")
                embed.add_field(name= "**Info:**", value="**Ball Modifier**: `"+b1+"`\n**Ball Conditions**: `"+b2+"`\n**Ball Effects**: `"+b3+"`", inline=True)
                
                if baln == "Beast":
                    embed.set_image(url="https://media0.giphy.com/media/Q8UsFRwVcAxBnXNo8q/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                    
                if baln == "Dream":
                    embed.set_image(url="https://media3.giphy.com/media/cMbaN5Pxe6ZX1RZmhV/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)                
                
                if baln == "Great":
                    embed.set_image(url="https://media0.giphy.com/media/J4h1EfSfBSDqQYqGs5/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)                
                
                if baln == "Heavy":
                    embed.set_image(url="https://media2.giphy.com/media/kDYfi0nctLKmrTjAVQ/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)                
                
                if baln == "Level":
                    embed.set_image(url="https://media0.giphy.com/media/MESCIFEPTDOHtiDAN9/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)                
                
                if baln == "Quick":
                    embed.set_image(url="https://media3.giphy.com/media/Sw0njjABoq2RwdZ021/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)                
                
                if baln == "Timer":
                    embed.set_image(url="https://media2.giphy.com/media/YonSDJD7IqH5ZR6Rty/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                               
                if baln == "Ultra":
                    embed.set_image(url="https://media2.giphy.com/media/kcUFH2HoOL2sVqAc0u/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                                               
            elif BName.startswith("Dive") or BName.startswith("Dusk") or BName.startswith("Fast") or BName.startswith("Heal") or BName.startswith("Love") or BName.startswith("Lure") or BName.startswith("Moon") or BName.startswith("Nest") or BName.startswith("Poke"):
                baln = BName[0:4]    
                ballresult = ball(str(baln))
                b1 = ballresult[0]
                b2 = ballresult[1]
                b3 = ballresult[2]
                lbname = baln.lower()
                link = "https://serebii.net/itemdex/"+lbname+"ball.shtml"
                
                embed = discord.Embed(title= "**"+ baln + " Ball**", url=link, color=0x2962FF)
                embed.set_thumbnail(url= "https://img.pokemondb.net/sprites/items/"+lbname+"-ball.png")
                embed.add_field(name= "**Info:**", value="**Ball Modifier**: `"+b1+"`\n**Ball Conditions**: `"+b2+"`\n**Ball Effects**: `"+b3+"`", inline=True)
                
                if baln == "Dive":
                    embed.set_image(url="https://media1.giphy.com/media/Q5M0qlYbqWlhvK34H4/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                
                elif baln == "Dusk":
                    embed.set_image(url="https://media2.giphy.com/media/dUT8l6lgavNTVdAk9V/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                
                elif baln == "Fast":
                    embed.set_image(url="https://media2.giphy.com/media/VdKewUvAPbzGrsIpC3/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                
                elif baln == "Heal":
                    embed.set_image(url="https://media2.giphy.com/media/gj5rnzcbdiKaugdDJ1/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                
                elif baln == "Love":
                    embed.set_image(url="https://media0.giphy.com/media/WrTdRwsteoMFjtyak5/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                
                elif baln == "Lure":
                    embed.set_image(url="https://media2.giphy.com/media/eJGGUpd33e4FAQFetJ/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                
                elif baln == "Moon":
                    embed.set_image(url="https://media0.giphy.com/media/Pns9GA5WRrMKBib3Ns/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                
                elif baln == "Nest":
                    embed.set_image(url="https://media0.giphy.com/media/VJwZtnk8eBBwddOBpJ/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
                
                elif baln == "Poke":
                    embed.set_image(url="https://media3.giphy.com/media/YMSzuD6AtcUWC7Ejvv/giphy.gif")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
            
            elif BName.startswith("Net"):
                baln = BName[0:3]    
                ballresult = ball(str(baln))
                b1 = ballresult[0]
                b2 = ballresult[1]
                b3 = ballresult[2]
                lbname = baln.lower()
                link = "https://serebii.net/itemdex/"+lbname+"ball.shtml"
                
                embed = discord.Embed(title= "**"+ baln + " Ball**", url=link, color=0x2962FF)
                embed.set_thumbnail(url= "https://img.pokemondb.net/sprites/items/"+lbname+"-ball.png")
                embed.add_field(name= "**Info:**", value="**Ball Modifier**: `"+b1+"`\n**Ball Conditions**: `"+b2+"`\n**Ball Effects**: `"+b3+"`", inline=True)
                embed.set_image(url="https://media3.giphy.com/media/iJhvFRLVMXNk7tJzVC/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                await ctx.author.message.delete()
                await ctx.send(embed=embed) 
 
            else:
                await ctx.send("The Poké-Ball requested was not found or doesn't exist.")

    @commands.command(name="den", help="?")
    async def den(self, ctx):
        responce = str(ctx.message.content)
        if responce.startswith('%den'):
            content = responce.split()
            res = content[1].isdigit()
            Den = string.capwords(content[1])
            if res == True:

                result = dennumber(str(Den))
                if result == None:
                    await ctx.send("This den does not exist")
                else:
                    sword = result[0]
                    shield = result[1]
                    MainD = result[2]
                    IoAD = result[3]
                    TCTD = result[4]
                    link = "https://www.serebii.net/swordshield/maxraidbattles/den"+Den+".shtml"
                    embed = discord.Embed(title= "Den "+ Den + ":", url=link, color=0x2962FF)
                    embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/Dens/den"+Den+".png")
                    embed.add_field(name="Sword HA:", value=sword, inline=True)
                    embed.add_field(name="Shield HA:", value=shield, inline=True)
                    embed.add_field(name="Wild Area Location:", value="Wild Area: "+ MainD +"\nIsle of Armor: "+ IoAD +"\nThe Crown Tundra: " + TCTD + " ", inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                    await ctx.author.message.delete()
                    await ctx.send(embed=embed)
            elif res != True:
                Gnm = Den
                if Den == "Farfetch'd" or Gnm == "Mr":
                    if Den =="Farfetch'd":
                        g = "Farfetchd"
                        result = denname(str(g))
                        SwNHA = result[0]
                        ShNHA = result[1]
                        SwHA = result[2]
                        ShHA = result[3]
                        embed = discord.Embed(title= "Galarian "+ Den + " is in the following dens:", color=0x2962FF)
                        embed.set_thumbnail(url="https://img.pokemondb.net/sprites/home/shiny/farfetchd-galarian.png")
                        embed.add_field(name="Sword:", value="Non-HA: "+SwNHA+"\nHA: "+ SwHA, inline=False)
                        embed.add_field(name="Shield:", value="Non-HA: " + ShNHA + "\nHA: "+ ShHA, inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                        await ctx.author.message.delete()
                        await ctx.send(embed=embed)
                    elif Gnm == "Mr":
                        Gnm = Gnm + " " + content[2]
                        if Gnm == "Mr mime":
                            g = "Mrmime"
                            result = denname(str(g))
                            SwNHA = result[0]
                            ShNHA = result[1]
                            SwHA = result[2]
                            ShHA = result[3]
                            embed = discord.Embed(title= "Galarian "+ Den + " is in the following dens:", color=0x2962FF)
                            embed.set_thumbnail(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/Shiny/Mrmime.png")
                            embed.add_field(name="Sword:", value="Non-HA: "+SwNHA+"\nHA: "+ SwHA, inline=False)
                            embed.add_field(name="Shield:", value="Non-HA: " + ShNHA + "\nHA: "+ ShHA, inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                            await ctx.author.message.delete()
                            await ctx.send(embed=embed)
                        elif Gnm == "Mr rime":
                            g = "Mrrime"
                            result = denname(str(g))
                            SwNHA = result[0]
                            ShNHA = result[1]
                            SwHA = result[2]
                            ShHA = result[3]
                            embed = discord.Embed(title= Den + " is in the following dens:", color=0x2962FF)
                            embed.set_thumbnail(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Mrrime.png")
                            embed.add_field(name="Sword:", value="Non-HA: "+SwNHA+"\nHA: "+ SwHA, inline=False)
                            embed.add_field(name="Shield:", value="Non-HA: " + ShNHA + "\nHA: "+ ShHA, inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                            await ctx.author.message.delete()
                            await ctx.send(embed=embed)
                else:
                    if Den == "Mime":
                        g = "Mimejr"
                        result = denname(str(g))
                        SwNHA = result[0]
                        ShNHA = result[1]
                        SwHA = result[2]
                        ShHA = result[3]
                        embed = discord.Embed(title= "Mime Jr. is in the following dens:", color=0x2962FF)
                        embed.set_thumbnail(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/Mimejr.png")
                        embed.add_field(name="Sword:", value="Non-HA: "+SwNHA+"\nHA: "+ SwHA, inline=False)
                        embed.add_field(name="Shield:", value="Non-HA: " + ShNHA + "\nHA: "+ ShHA, inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                        await ctx.author.message.delete()
                        await ctx.send(embed=embed)
                        
                    else:
                        result = denname(str(Den))
                        if result == None:
                           await ctx.send("This Pokemon cannot be found in a Den")
                        else:
                          SwNHA = result[0]
                          ShNHA = result[1]
                          SwHA = result[2]
                          ShHA = result[3]
                          Glr = ["Meowth", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Weezing", "Corsola",
                                 "Zigzagoon", "Linoone", "Darumaka", "Darmanitan", "Yamask", "Stunfisk"]
            
                        if Den in Glr:
                          nenl = Den
                          embed = discord.Embed(title= "Galarian "+ Den + " is in the following dens:", color=0x2962FF)
                          embed.set_thumbnail(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/Shiny/"+nenl+".png")
                          embed.add_field(name="Sword:", value="Non-HA: "+SwNHA+"\nHA: "+ SwHA, inline=False)
                          embed.add_field(name="Shield:", value="Non-HA: " + ShNHA + "\nHA: "+ ShHA, inline=False)
                          embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                          await ctx.author.message.delete()
                          await ctx.send(embed=embed)
                        elif Den not in Glr:
                          Den1 = Den
                          embed = discord.Embed(title= Den + " is in the following dens:", color=0x2962FF)
                          embed.set_thumbnail(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Shiny/"+Den1+".png")
                          embed.add_field(name="Sword:", value="Non-HA: "+SwNHA+"\nHA: "+ SwHA, inline=False)
                          embed.add_field(name="Shield:", value="Non-HA: " + ShNHA + "\nHA: "+ ShHA, inline=False)
                          embed.set_footer(text="Provided by Nexus-Z", icon_url="https://www.serebii.net/Shiny/SWSH/474.png")
                          await ctx.author.message.delete()
                          await ctx.send(embed=embed)
                    
def main(pokename, ballType):
    ballType = ballType.capitalize()
    pokename = pokename.capitalize()
    pokeHP = 0
    BasepokeHp = 0
    catchRate = 0
    realcatchRate = 0
    weight = 0
    basespd = 0
    Mostone = 0
    types = ''
    
    fileOpen = open('E:/bulbapedia_data.csv', newline='')
    fileData = csv.reader(fileOpen)
    for row in fileData:
        for name in row:
            if name == pokename:
                types = [row[3]]
                if row[4] != "Unknown":
                    types.append(row[4])
                pokeHP = int(row[5])
                basespd = int(row[10])
                catchRate = int(row[12])
                weight = float(row[19])
                Mostone = int(row[24])
        if name not in row:
                types = "Fire"
                pokeHP = 5
                catchRate = 0

    BasepokeHp = pokeHP
    if ballType == "Heavyball":
        if weight >= 99.9:
            if weight >= 199.9:
                if weight >= 299.9:
                    if weight > 300.0:
                        realcatchRate = catchRate + 30
                        catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
                        catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
                        if catch_value >= 255 or catch_value2 >= 255:
                            finalRate = 0.1
                        else:
                            minRate = getCatchRate(catch_value)
                            maxRate = getCatchRate(catch_value2)

                            finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                            finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

                        try:
                            finalRate2 * 2
                        except:
                            return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
                        else:
                            return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
                else:
                    realcatchRate = catchRate + 20
                    catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
                    catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
                    if catch_value >= 255 or catch_value2 >= 255:
                        finalRate = 0.1
                    else:
                        minRate = getCatchRate(catch_value)
                        maxRate = getCatchRate(catch_value2)

                        finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                        finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

                    try:
                        finalRate2 * 2
                    except:
                        return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
                    else:
                        return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
            else:
                realcatchRate = catchRate
                catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
                catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
                if catch_value >= 255 or catch_value2 >= 255:
                    finalRate = 0.1
                else:
                    minRate = getCatchRate(catch_value)
                    maxRate = getCatchRate(catch_value2)

                    finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                    finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

                try:
                    finalRate2 * 2
                except:
                    return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
                else:
                    return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
        else:
            realcatchRate = catchRate - 20
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
            else:
                return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))                
    elif ballType == "Fastball":
        if basespd >= 100:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
            else:
                return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
        else:
                realcatchRate = catchRate
                catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, "Pokeball", types)
                catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, "Pokeball", types)
                if catch_value >= 255 or catch_value2 >= 255:
                    finalRate = 0.1
                else:
                    minRate = getCatchRate(catch_value)
                    maxRate = getCatchRate(catch_value2)

                    finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                    finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

                try:
                    finalRate2 * 2
                except:
                    return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
                else:
                    return "Fastball", (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))  
    elif ballType == "Moonball":
        if Mostone == 1:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
            else:
                return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
        else:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, "Pokeball", types)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, "Pokeball", types)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
            else:
                return "Moonball", (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
    else:
        realcatchRate = catchRate
        catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
        catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
        if catch_value >= 255 or catch_value2 >= 255:
            finalRate = 0.1
        else:
            minRate = getCatchRate(catch_value)
            maxRate = getCatchRate(catch_value2)

            finalRate = ((minRate + 1) / (2 ** 16)) ** 4
            finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

        try:
            finalRate2 * 2
        except:
            return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
        else:
            return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
       
def alolanmain(pokename, ballType):
    ballType = ballType.capitalize()
    pokename = pokename.capitalize()
    pokeHP = 0
    BasepokeHp = 0
    catchRate = 0
    realcatchRate = 0
    weight = 0
    basespd = 0
    Mostone = 0
    types = ''
    
    fileOpen = open('E:/Alolan.csv', newline='')
    fileData = csv.reader(fileOpen)
    for row in fileData:
        for name in row:
            if name == pokename:
                types = [row[3]]
                if row[4] != "Unknown":
                    types.append(row[4])
                pokeHP = int(row[5])
                basespd = int(row[10])
                catchRate = int(row[12])
                weight = float(row[19])
                Mostone = int(row[24])
        if name not in row:
                types = "Fire"
                pokeHP = 5
                catchRate = 0

    BasepokeHp = pokeHP
    if ballType == "Heavyball":
        if weight >= 99.9:
            if weight >= 199.9:
                if weight >= 299.9:
                    if weight > 300.0:
                        realcatchRate = catchRate + 30
                        catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
                        catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
                        if catch_value >= 255 or catch_value2 >= 255:
                            finalRate = 0.1
                        else:
                            minRate = getCatchRate(catch_value)
                            maxRate = getCatchRate(catch_value2)

                            finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                            finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

                        try:
                            finalRate2 * 2
                        except:
                            return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
                        else:
                            return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
                else:
                    realcatchRate = catchRate + 20
                    catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
                    catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
                    if catch_value >= 255 or catch_value2 >= 255:
                        finalRate = 0.1
                    else:
                        minRate = getCatchRate(catch_value)
                        maxRate = getCatchRate(catch_value2)

                        finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                        finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

                    try:
                        finalRate2 * 2
                    except:
                        return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
                    else:
                        return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
            else:
                realcatchRate = catchRate
                catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
                catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
                if catch_value >= 255 or catch_value2 >= 255:
                    finalRate = 0.1
                else:
                    minRate = getCatchRate(catch_value)
                    maxRate = getCatchRate(catch_value2)

                    finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                    finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

                try:
                    finalRate2 * 2
                except:
                    return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
                else:
                    return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
        else:
            realcatchRate = catchRate - 20
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
            else:
                return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))                
    elif ballType == "Fastball":
        if basespd >= 100:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
            else:
                return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
        else:
                realcatchRate = catchRate
                catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, "Pokeball", types)
                catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, "Pokeball", types)
                if catch_value >= 255 or catch_value2 >= 255:
                    finalRate = 0.1
                else:
                    minRate = getCatchRate(catch_value)
                    maxRate = getCatchRate(catch_value2)

                    finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                    finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

                try:
                    finalRate2 * 2
                except:
                    return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
                else:
                    return "Fastball", (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))  
    elif ballType == "Moonball":
        if Mostone == 1:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
            else:
                return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
        else:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, "Pokeball", types)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, "Pokeball", types)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
            else:
                return "Moonball", (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
    else:
        realcatchRate = catchRate
        catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
        catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
        if catch_value >= 255 or catch_value2 >= 255:
            finalRate = 0.1
        else:
            minRate = getCatchRate(catch_value)
            maxRate = getCatchRate(catch_value2)

            finalRate = ((minRate + 1) / (2 ** 16)) ** 4
            finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

        try:
            finalRate2 * 2
        except:
            return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
        else:
            return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))

def galarianmain(pokename, ballType):
    ballType = ballType.capitalize()
    pokename = pokename.capitalize()
    pokeHP = 0
    BasepokeHp = 0
    catchRate = 0
    realcatchRate = 0
    weight = 0
    basespd = 0
    Mostone = 0
    types = ''
    
    fileOpen = open('E:/galariandata.csv', newline='')
    fileData = csv.reader(fileOpen)
    for row in fileData:
        for name in row:
            if name == pokename:
                types = [row[3]]
                if row[4] != "Unknown":
                    types.append(row[4])
                pokeHP = int(row[5])
                basespd = int(row[10])
                catchRate = int(row[12])
                weight = float(row[19])
                Mostone = int(row[24])
        if name not in row:
                types = "Fire"
                pokeHP = 5
                catchRate = 0

    BasepokeHp = pokeHP
    if ballType == "Heavyball":
        if weight >= 99.9:
            if weight >= 199.9:
                if weight >= 299.9:
                    if weight > 300.0:
                        realcatchRate = catchRate + 30
                        catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
                        catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
                        if catch_value >= 255 or catch_value2 >= 255:
                            finalRate = 0.1
                        else:
                            minRate = getCatchRate(catch_value)
                            maxRate = getCatchRate(catch_value2)

                            finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                            finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

                        try:
                            finalRate2 * 2
                        except:
                            return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
                        else:
                            return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
                else:
                    realcatchRate = catchRate + 20
                    catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
                    catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
                    if catch_value >= 255 or catch_value2 >= 255:
                        finalRate = 0.1
                    else:
                        minRate = getCatchRate(catch_value)
                        maxRate = getCatchRate(catch_value2)

                        finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                        finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

                    try:
                        finalRate2 * 2
                    except:
                        return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
                    else:
                        return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
            else:
                realcatchRate = catchRate
                catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
                catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
                if catch_value >= 255 or catch_value2 >= 255:
                    finalRate = 0.1
                else:
                    minRate = getCatchRate(catch_value)
                    maxRate = getCatchRate(catch_value2)

                    finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                    finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

                try:
                    finalRate2 * 2
                except:
                    return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
                else:
                    return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
        else:
            realcatchRate = catchRate - 20
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
            else:
                return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))                
    elif ballType == "Fastball":
        if basespd >= 100:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
            else:
                return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
        else:
                realcatchRate = catchRate
                catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, "Pokeball", types)
                catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, "Pokeball", types)
                if catch_value >= 255 or catch_value2 >= 255:
                    finalRate = 0.1
                else:
                    minRate = getCatchRate(catch_value)
                    maxRate = getCatchRate(catch_value2)

                    finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                    finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

                try:
                    finalRate2 * 2
                except:
                    return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
                else:
                    return "Fastball", (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))  
    elif ballType == "Moonball":
        if Mostone == 1:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
            else:
                return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
        else:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, "Pokeball", types)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, "Pokeball", types)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
            else:
                return "Moonball", (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
    else:
        realcatchRate = catchRate
        catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
        catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
        if catch_value >= 255 or catch_value2 >= 255:
            finalRate = 0.1
        else:
            minRate = getCatchRate(catch_value)
            maxRate = getCatchRate(catch_value2)

            finalRate = ((minRate + 1) / (2 ** 16)) ** 4
            finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

        try:
            finalRate2 * 2
        except:
            return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
        else:
            return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))

def gmaxmain(pokename, ballType):
    ballType = ballType.capitalize()
    pokename = pokename.capitalize()
    pokeHP = 0
    BasepokeHp = 0
    catchRate = 0
    realcatchRate = 0
    weight = 0
    basespd = 0
    Mostone = 0
    types = ''
    
    fileOpen = open('E:/bulbapedia_data.csv', newline='')
    fileData = csv.reader(fileOpen)
    for row in fileData:
        for name in row:
            if name == pokename:
                types = [row[3]]
                if row[4] != "Unknown":
                    types.append(row[4])
                pokeHP = int(row[5])
                basespd = int(row[10])
                catchRate = int(3)
                weight = float(row[19])
                Mostone = int(row[24])
        if name not in row:
                types = "Fire"
                pokeHP = 5
                catchRate = 0

    BasepokeHp = pokeHP
    if ballType == "Heavyball":
        if weight >= 99.9:
            if weight >= 199.9:
                if weight >= 299.9:
                    if weight > 300.0:
                        realcatchRate = catchRate + 30
                        catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
                        catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
                        if catch_value >= 255 or catch_value2 >= 255:
                            finalRate = 0.1
                        else:
                            minRate = getCatchRate(catch_value)
                            maxRate = getCatchRate(catch_value2)

                            finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                            finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

                        try:
                            finalRate2 * 2
                        except:
                            return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
                        else:
                            return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
                else:
                    realcatchRate = catchRate + 20
                    catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
                    catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
                    if catch_value >= 255 or catch_value2 >= 255:
                        finalRate = 0.1
                    else:
                        minRate = getCatchRate(catch_value)
                        maxRate = getCatchRate(catch_value2)

                        finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                        finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

                    try:
                        finalRate2 * 2
                    except:
                        return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
                    else:
                        return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
            else:
                realcatchRate = catchRate
                catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
                catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
                if catch_value >= 255 or catch_value2 >= 255:
                    finalRate = 0.1
                else:
                    minRate = getCatchRate(catch_value)
                    maxRate = getCatchRate(catch_value2)

                    finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                    finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

                try:
                    finalRate2 * 2
                except:
                    return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
                else:
                    return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
        else:
            realcatchRate = catchRate - 20
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
            else:
                return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))                
    elif ballType == "Fastball":
        if basespd >= 100:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
            else:
                return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
        else:
                realcatchRate = catchRate
                catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, "Pokeball", types)
                catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, "Pokeball", types)
                if catch_value >= 255 or catch_value2 >= 255:
                    finalRate = 0.1
                else:
                    minRate = getCatchRate(catch_value)
                    maxRate = getCatchRate(catch_value2)

                    finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                    finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

                try:
                    finalRate2 * 2
                except:
                    return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
                else:
                    return "Fastball", (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))  
    elif ballType == "Moonball":
        if Mostone == 1:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
            else:
                return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
        else:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, "Pokeball", types)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, "Pokeball", types)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = ((minRate + 1) / (2 ** 16)) ** 4
                finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
            else:
                return "Moonball", (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))
    else:
        realcatchRate = catchRate
        catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types)
        catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types)
        if catch_value >= 255 or catch_value2 >= 255:
            finalRate = 0.1
        else:
            minRate = getCatchRate(catch_value)
            maxRate = getCatchRate(catch_value2)

            finalRate = ((minRate + 1) / (2 ** 16)) ** 4
            finalRate2 = ((maxRate + 1) / (2 ** 16)) ** 4

        try:
            finalRate2 * 2
        except:
            return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.0)
        else:
            return ballType.capitalize(), (float(round(finalRate * 100, 1))), (float(round(finalRate2 * 100, 1)))

def ballRate(ballType, types):

    ballDict = {'MASTERBALL': 255, 'DUSKBALL': 3, 'ULTRABALL': 2, 'REPEATBALL': 3.5, 'BEASTBALL': 0.1, 'GREATBALL': 1.5, 'SPORTSBALL': 1.5, 'SAFARIBALL':1.5, 'FASTBALL':4, 'MOONBALL':4}

    for key, value in ballDict.items():
        if ballType.upper() == key:
            return value

    if ballType.upper() != 'NETBALL':
        return 1

    if ("Water" in types) or ("Bug" in types):
        return 3.5

    return 1
    
def getHealth(hp, level):
    return (((15.5 + (2 * hp) + 100) * level) / 100) + 10

def getCatchValue(maxHP, realcatchRate, ballType, types):
    return ((3 * maxHP - 2 * 1) * (realcatchRate * ballRate(ballType, types))) / (3 * maxHP)

def getCatchRate(catchValue):
    if catchValue == 0:
        return 0
    else:
        CR = (1048560 / (((16711680 / catchValue))**0.25))   
        return CR
        
def pokedex(pokename):
    pokename = pokename.capitalize()
    dexentry = ''
    generation = ''
    types = ''
    pokeHP = 0
    pokeAtk = 0
    pokeDef = 0
    pokeSpA = 0
    pokeSPD = 0
    pokeSpeed = 0
    Stattotal = 0
    catchRate = 0
    Ability1 = ''
    Ability2 = ''
    HAbility = ''
    MaleRate = 0.0
    FemaleRate = 0.0
    Height = 0.0
    Weight = 0.0
    EggGrp1 = ''
    EggGrp2 = ''
    SwDens = ''
    ShDens = ''
    
    fileOpen = open('E:/bulbapedia_data.csv', newline='')
    fileData = csv.reader(fileOpen)
    for row in fileData:
        for name in row:
            if name == pokename:
                dexentry = row[0]
                generation = row[2]
                types = row[3]
                if row[4] != "Unknown":
                    types = row[3] + " / " +row[4]
                    pokeHp = int(row[5])
                    pokeAtk = int(row[6])
                    pokeDef = int(row[7])
                    pokeSpA = int(row[8])
                    pokeSPD = int(row[9])
                    pokeSpeed = int(row[10])
                    Stattotal = int(row[11])
                    catchRate = int(row[12])
                    Ability1 = row[13]
                    if row[14] == "Unknown":
                        Ability2 = "Unknown"
                        HAbility = row[15]
                        MaleRate = float(row[16])
                        FemaleRate = float(row[17])
                        Height = float(row[18])
                        Weight = float(row[19])
                        EggGrp1 = row[20]
                        if row[21] == "Unknown":
                            EggGrp2 = " "
                            SwDens = row[22]
                            ShDens = row[23]
                            return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                        elif row[21] != "Unknown":
                            EggGrp2 = row[21]
                            SwDens = row[22]
                            ShDens = row[23]
                            return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                    elif row[14] != "Unknown":
                        Ability2 = row[14]
                        HAbility = row[15]
                        MaleRate = float(row[16])
                        FemaleRate = float(row[17])
                        Height = float(row[18])
                        Weight = float(row[19])
                        EggGrp1 = row[20]
                        if row[21] == "Unknown":
                            EggGrp2 = " "
                            if row[22] == "Unknown":
                                SwDens = row[22]
                                ShDens = row[23]
                                return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                            elif row[22] != "Unknown":
                                SwDens = row[22]
                                ShDens = row[23]
                                return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                        elif row[21] != "Unknown":
                            EggGrp2 = row[21]
                            if row[22] == "Unknown":
                                SwDens = row[22]
                                ShDens = row[23]
                                return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                            elif row[22] != "Unknown":
                                SwDens = row[22]
                                ShDens = row[23]
                                return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                else:
                    row[4] = "-" 
                    types= row[3]+" / "+row[4]
                    pokeHp = int(row[5])
                    pokeAtk = int(row[6])
                    pokeDef = int(row[7])
                    pokeSpA = int(row[8])
                    pokeSPD = int(row[9])
                    pokeSpeed = int(row[10])
                    Stattotal = int(row[11])
                    catchRate = int(row[12])
                    Ability1 = row[13]
                    if row[14] == "Unknown":
                        Ability2 = "Unknown"
                        HAbility = row[15]
                        MaleRate = float(row[16])
                        FemaleRate = float(row[17])
                        Height = float(row[18])
                        Weight = float(row[19])
                        EggGrp1 = row[20]
                        if row[21] == "Unknown":
                            EggGrp2 = " "
                            SwDens = row[22]
                            ShDens = row[23]
                            return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                        elif row[21] != "Unknown":
                            EggGrp2 = row[21]
                            SwDens = row[22]
                            ShDens = row[23]
                            return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                    elif row[14] != "Unknown":
                        Ability2 = row[14]
                        HAbility = row[15]
                        MaleRate = float(row[16])
                        FemaleRate = float(row[17])
                        Height = float(row[18])
                        Weight = float(row[19])
                        EggGrp1 = row[20]
                        if row[21] == "Unknown":
                            EggGrp2 = " "
                            SwDens = row[22]
                            ShDens = row[23]
                            return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                        elif row[21] != "Unknown":
                            EggGrp2 = row[21]
                            SwDens = row[22]
                            ShDens = row[23]
                            return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)

def alolanpokedex(pokename):
    pokename = pokename.capitalize()
    dexentry = ''
    generation = ''
    types = ''
    pokeHP = 0
    pokeAtk = 0
    pokeDef = 0
    pokeSpA = 0
    pokeSPD = 0
    pokeSpeed = 0
    Stattotal = 0
    catchRate = 0
    Ability1 = ''
    Ability2 = ''
    HAbility = ''
    MaleRate = 0.0
    FemaleRate = 0.0
    Height = 0.0
    Weight = 0.0
    EggGrp1 = ''
    EggGrp2 = ''
    SwDens = ''
    ShDens = ''

    fileOpen = open('E:/Alolan.csv', newline='')
    fileData = csv.reader(fileOpen)
    for row in fileData:
        for name in row:
            if name == pokename:
                dexentry = row[0]
                generation = row[2]
                types = row[3]
                if row[4] != "Unknown":
                    types = row[3] + " / " +row[4]
                    pokeHp = int(row[5])
                    pokeAtk = int(row[6])
                    pokeDef = int(row[7])
                    pokeSpA = int(row[8])
                    pokeSPD = int(row[9])
                    pokeSpeed = int(row[10])
                    Stattotal = int(row[11])
                    catchRate = int(row[12])
                    Ability1 = row[13]
                    if row[14] == "Unknown":
                        Ability2 = "Unknown"
                        HAbility = row[15]
                        MaleRate = float(row[16])
                        FemaleRate = float(row[17])
                        Height = float(row[18])
                        Weight = float(row[19])
                        EggGrp1 = row[20]
                        if row[21] == "Unknown":
                            EggGrp2 = " "
                            SwDens = row[22]
                            ShDens = row[23]
                            return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                        elif row[21] != "Unknown":
                            EggGrp2 = row[21]
                            SwDens = row[22]
                            ShDens = row[23]
                            return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                    elif row[14] != "Unknown":
                        Ability2 = row[14]
                        HAbility = row[15]
                        MaleRate = float(row[16])
                        FemaleRate = float(row[17])
                        Height = float(row[18])
                        Weight = float(row[19])
                        EggGrp1 = row[20]
                        if row[21] == "Unknown":
                            EggGrp2 = " "
                            if row[22] == "Unknown":
                                SwDens = row[22]
                                ShDens = row[23]
                                return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                            elif row[22] != "Unknown":
                                SwDens = row[22]
                                ShDens = row[23]
                                return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                        elif row[21] != "Unknown":
                            EggGrp2 = row[21]
                            if row[22] == "Unknown":
                                SwDens = row[22]
                                ShDens = row[23]
                                return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                            elif row[22] != "Unknown":
                                SwDens = row[22]
                                ShDens = row[23]
                                return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                else:
                    row[4] = "-" 
                    types= row[3]+" / "+row[4]
                    pokeHp = int(row[5])
                    pokeAtk = int(row[6])
                    pokeDef = int(row[7])
                    pokeSpA = int(row[8])
                    pokeSPD = int(row[9])
                    pokeSpeed = int(row[10])
                    Stattotal = int(row[11])
                    catchRate = int(row[12])
                    Ability1 = row[13]
                    if row[14] == "Unknown":
                        Ability2 = " "
                        HAbility = row[15]
                        MaleRate = float(row[16])
                        FemaleRate = float(row[17])
                        Height = float(row[18])
                        Weight = float(row[19])
                        EggGrp1 = row[20]
                        if row[21] == "Unknown":
                            EggGrp2 = " "
                            SwDens = row[22]
                            ShDens = row[23]
                            return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                        elif row[21] != "Unknown":
                            EggGrp2 = row[21]
                            SwDens = row[22]
                            ShDens = row[23]
                            return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                    elif row[14] != "Unknown":
                        Ability2 = row[14]
                        HAbility = row[15]
                        MaleRate = float(row[16])
                        FemaleRate = float(row[17])
                        Height = float(row[18])
                        Weight = float(row[19])
                        EggGrp1 = row[20]
                        if row[21] == "Unknown":
                            EggGrp2 = " "
                            SwDens = row[22]
                            ShDens = row[23]
                            return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                        elif row[21] != "Unknown":
                            EggGrp2 = row[21]
                            SwDens = row[22]
                            ShDens = row[23]
                            return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)

def galarianpokedex(pokename):
    pokename = pokename.capitalize()
    dexentry = ''
    generation = ''
    types = ''
    pokeHP = 0
    pokeAtk = 0
    pokeDef = 0
    pokeSpA = 0
    pokeSPD = 0
    pokeSpeed = 0
    Stattotal = 0
    catchRate = 0
    Ability1 = ''
    Ability2 = ''
    HAbility = ''
    MaleRate = 0.0
    FemaleRate = 0.0
    Height = 0.0
    Weight = 0.0
    EggGrp1 = ''
    EggGrp2 = ''
    SwDens = ''
    ShDens = ''

    fileOpen = open('E:/galariandata.csv', newline='')
    fileData = csv.reader(fileOpen)
    for row in fileData:
        for name in row:
            if name == pokename:
                dexentry = row[0]
                generation = row[2]
                types = row[3]
                if row[4] != "Unknown":
                    types = row[3] + " / " +row[4]
                    pokeHp = int(row[5])
                    pokeAtk = int(row[6])
                    pokeDef = int(row[7])
                    pokeSpA = int(row[8])
                    pokeSPD = int(row[9])
                    pokeSpeed = int(row[10])
                    Stattotal = int(row[11])
                    catchRate = int(row[12])
                    Ability1 = row[13]
                    if row[14] == "Unknown":
                        Ability2 = "Unknown"
                        HAbility = row[15]
                        MaleRate = float(row[16])
                        FemaleRate = float(row[17])
                        Height = float(row[18])
                        Weight = float(row[19])
                        EggGrp1 = row[20]
                        if row[21] == "Unknown":
                            EggGrp2 = " "
                            SwDens = row[22]
                            ShDens = row[23]
                            return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                        elif row[21] != "Unknown":
                            EggGrp2 = row[21]
                            SwDens = row[22]
                            ShDens = row[23]
                            return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                    elif row[14] != "Unknown":
                        Ability2 = row[14]
                        HAbility = row[15]
                        MaleRate = float(row[16])
                        FemaleRate = float(row[17])
                        Height = float(row[18])
                        Weight = float(row[19])
                        EggGrp1 = row[20]
                        if row[21] == "Unknown":
                            EggGrp2 = " "
                            if row[22] == "Unknown":
                                SwDens = row[22]
                                ShDens = row[23]
                                return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                            elif row[22] != "Unknown":
                                SwDens = row[22]
                                ShDens = row[23]
                                return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                        elif row[21] != "Unknown":
                            EggGrp2 = row[21]
                            if row[22] == "Unknown":
                                SwDens = row[22]
                                ShDens = row[23]
                                return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                            elif row[22] != "Unknown":
                                SwDens = row[22]
                                ShDens = row[23]
                                return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                elif row[4] == "Unknown":
                    row[4] = "-" 
                    types= row[3]+" / "+row[4]
                    pokeHp = int(row[5])
                    pokeAtk = int(row[6])
                    pokeDef = int(row[7])
                    pokeSpA = int(row[8])
                    pokeSPD = int(row[9])
                    pokeSpeed = int(row[10])
                    Stattotal = int(row[11])
                    catchRate = int(row[12])
                    Ability1 = row[13]
                    if row[14] == "Unknown":
                        Ability2 = "Unknown"
                        HAbility = row[15]
                        MaleRate = float(row[16])
                        FemaleRate = float(row[17])
                        Height = float(row[18])
                        Weight = float(row[19])
                        EggGrp1 = row[20]
                        if row[21] == "Unknown":
                            EggGrp2 = " "
                            SwDens = row[22]
                            ShDens = row[23]
                            return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                        elif row[21] != "Unknown":
                            EggGrp2 = row[21]
                            SwDens = row[22]
                            ShDens = row[23]
                            return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                    elif row[14] != "Unknown":
                        Ability2 = row[14]
                        HAbility = row[15]
                        MaleRate = float(row[16])
                        FemaleRate = float(row[17])
                        Height = float(row[18])
                        Weight = float(row[19])
                        EggGrp1 = row[20]
                        if row[21] == "Unknown":
                            EggGrp2 = " "
                            SwDens = row[22]
                            ShDens = row[23]
                            return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                        elif row[21] != "Unknown":
                            EggGrp2 = row[21]
                            SwDens = row[22]
                            ShDens = row[23]
                            return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)

def ball(ballName):
    ballName = ballName.capitalize()
    Multiplier = ''
    Condition = ''
    Addeffect = ''

    
    fileOpen = open('E:/pokeballdata.csv', newline='')
    fileData = csv.reader(fileOpen)
    for row in fileData:
        for name in row:
            if name == ballName:
                Multiplier = row[1]
                Condition = row[2]
                Addeffect = row[3]
                return (Multiplier, Condition, Addeffect)

def dennumber(dennum):
    Swha = ''
    Shha = ''
    MGame = ''
    IoA = ''
    TCT = ''
    
    fileOpen = open('E:/NumDen.csv', newline='')
    fileData = csv.reader(fileOpen)
    for row in fileData:
        for Den in row:
            if Den == dennum:
                Swha = row[1]
                Shha = row[2]
                MGame = row[3]
                IoA = row[4]
                TCT = row[5]
                return (Swha, Shha, MGame, IoA, TCT)

def denname(dennamez):
    dennamez = dennamez.capitalize()
    Swha = ''
    Shha = ''
    Swnonha = ''
    Shnonha = ''
    
    fileOpen = open('E:/Denpokename.csv', newline='')
    fileData = csv.reader(fileOpen)
    for row in fileData:
        for Name in row:
            if Name == dennamez:
                Swnonha = row[1]
                Shnonha = row[2]
                Swha = row[3]
                Shha = row[4]
                return (Swnonha, Shnonha, Swha, Shha)

def getKey(item):
    return item[1]

def getNKey(item):
    return item[0]
                
def setup(client):
    client.add_cog(Pokemon(client))