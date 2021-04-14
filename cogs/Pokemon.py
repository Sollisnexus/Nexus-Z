import discord
import string
import math
import csv
import os
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

async def guildhostchannel(self, ctx):
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            channeltosend = await connection.fetchval("SELECT guildchannelid FROM guildhostchannel WHERE guildid = '"+str(ctx.guild.id)+"' ;")
            return channeltosend

class Pokemon(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Pokemon online.')

        # Commands
    @commands.group(case_insensitive=True, aliases=["c"])
    async def catch(self, ctx):
        if ctx.invoked_subcommand is None:
            responce = str(ctx.message.content)
            if not responce.lower().endswith('ball'):
                responce = responce + " ball"
            content = responce.split()
            isshiny = "Normal"
            twoword = ["mime","mime*","rime","rime*","koko","koko*","lele","lele*","bulu","bulu*","fini","fini*","null","null*","jr","jr*","jr.","jr.*"]
            try:
                (content[3].endswith('ball') and content[2].lower() not in twoword) or content[4].endswith('ball') or content[5].endswith('ball')
            except:
                Name = string.capwords(content[1])
                if Name.endswith("*"):
                    isshiny = "Shiny"
                    Name = Name.replace("*", "")
                if Name == "Tapu":
                    Tapu = ["koko","lele","bulu","fini"]
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].lower() in Tapu:
                        Name = Name + " " +string.capwords(content[2])
                if Name == "Mr.":
                    Name = "Mr"
                if Name == "Mr":
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        content[2] = content[2].replace("*", "")
                    FLCap = string.capwords(content[1])
                    FLLCap = string.capwords(content[2])
                    RName = content[1] + content[2].lower()
                    if RName =="Mr.mime" or RName == "mr.mime":
                        RName = "Mrmime"
                    if RName == "Mr.rime" or RName == "mr.rime":
                        RName = "Mrrime"
                    LName = FLCap+content[2].lower()
                    if LName == "Mrmime" or LName =="Mr.mime":
                        LName = "Mrmime"
                    if LName == "Mrrime" or LName =="Mr.rime":
                        LName = "Mrrime"
                    RealN= FLCap+". "+FLLCap
                    if RealN == "Mr.. Mime":
                        RealN = "Mr. Mime"
                    if RealN == "Mr.. Rime":
                        RealN = "Mr. Rime"
                    msg = list(await main(self, str(RName), str("pokeball")))
                    msg1= list(await main(self, str(RName), str("greatball")))
                    msg2= list(await main(self, str(RName), str("ultraball")))
                    msg3= list(await main(self, str(RName), str("duskball")))
                    msg4= list(await main(self, str(RName), str("repeatball")))
                    msg5= list(await main(self, str(RName), str("netball")))
                    msg6= list(await main(self, str(RName), str("Apriball")))
                    msg7= list(await main(self, str(RName), str("beastball")))
                    msg[0]= "Poke Ball"
                    msg1[0]= "Great Ball"
                    msg2[0]= "Ultra Ball"
                    msg3[0]= "Dusk Ball"
                    msg4[0]= "Repeat Ball"
                    msg5[0]= "Net Ball"
                    msg6[0]= "Apri Ball"
                    msg7[0]= "Beast Ball"
                    msg.append("<:xPoke:761255796839153767>")
                    msg1.append("<:xGreat:761255796721188924>")
                    msg2.append("<:xUltra:761277085083369546>")
                    msg3.append("<:xDusk:761255796859469824> ")
                    msg4.append("<:xRepeat:761255796947681300>")
                    msg5.append("<:xNet:761255796666400769>")
                    msg6.append("<:xFriend:761255796750680124>")
                    msg7.append("<:xBeast:761255796675444736>")
                    List2 = [(msg),(msg1),(msg2),(msg3),(msg4),(msg5),(msg6),(msg7)]
                    List = sorted(List2, key=getNKey)
                    Test = sorted(List, key=getKey, reverse=True)
                    msg = Test[0]
                    msg1 = Test[1]
                    msg2 = Test[2]
                    msg3 = Test[3]
                    msg4 = Test[4]
                    msg5 = Test[5]
                    msg6 = Test[6]
                    msg7 = Test[7]
                    embed = discord.Embed(title= RealN + "'s Capture Odds", description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+str(LName)+".png")
                    embed.add_field(name= "Ball Type", value=str(msg[3]) + " " + str(msg[0])+"\n"+str(msg1[3]) + " " + str(msg1[0])+"\n"+str(msg2[3]) + " " + str(msg2[0])+"\n"+str(msg3[3]) + " " + str(msg3[0])+"\n"+str(msg4[3]) + " " + str(msg4[0])+"\n"+str(msg5[3]) + " " + str(msg5[0])+"\n"+str(msg6[3]) + " " + str(msg6[0])+"\n"+str(msg7[3]) + " " + str(msg7[0])+"\n", inline=True)
                    embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%\n" + str(msg1[1])+"% - "+str(msg1[2])+"%\n" + str(msg2[1])+"% - "+str(msg2[2])+"%\n" + str(msg3[1])+"% - "+str(msg3[2])+"%\n" + str(msg4[1])+"% - "+str(msg4[2])+"%\n" + str(msg5[1])+"% - "+str(msg5[2])+"%\n" + str(msg6[1])+"% - "+str(msg6[2])+"%\n" + str(msg7[1])+"% - "+str(msg7[2])+"%**\n", inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                elif Name == "Mime":
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        content[2] = content[2].replace("*", "")
                    RName = "Mimejr"
                    msg = list(await main(self, str(RName), str("pokeball")))
                    msg1= list(await main(self, str(RName), str("greatball")))
                    msg2= list(await main(self, str(RName), str("ultraball")))
                    msg3= list(await main(self, str(RName), str("duskball")))
                    msg4= list(await main(self, str(RName), str("repeatball")))
                    msg5= list(await main(self, str(RName), str("netball")))
                    msg6= list(await main(self, str(RName), str("Apriball")))
                    msg7= list(await main(self, str(RName), str("beastball")))
                    msg[0]= "Poke Ball"
                    msg1[0]= "Great Ball"
                    msg2[0]= "Ultra Ball"
                    msg3[0]= "Dusk Ball"
                    msg4[0]= "Repeat Ball"
                    msg5[0]= "Net Ball"
                    msg6[0]= "Apri Ball"
                    msg7[0]= "Beast Ball"
                    msg.append("<:xPoke:761255796839153767>")
                    msg1.append("<:xGreat:761255796721188924>")
                    msg2.append("<:xUltra:761277085083369546>")
                    msg3.append("<:xDusk:761255796859469824> ")
                    msg4.append("<:xRepeat:761255796947681300>")
                    msg5.append("<:xNet:761255796666400769>")
                    msg6.append("<:xFriend:761255796750680124>")
                    msg7.append("<:xBeast:761255796675444736>")
                    List2 = [(msg),(msg1),(msg2),(msg3),(msg4),(msg5),(msg6),(msg7)]
                    List = sorted(List2, key=getNKey)
                    Test = sorted(List, key=getKey, reverse=True)
                    msg = Test[0]
                    msg1 = Test[1]
                    msg2 = Test[2]
                    msg3 = Test[3]
                    msg4 = Test[4]
                    msg5 = Test[5]
                    msg6 = Test[6]
                    msg7 = Test[7]
                    embed = discord.Embed(title= "Mime Jr.'s Capture Odds", description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Mimejr.png")
                    embed.add_field(name= "Ball Type", value=str(msg[3]) + " " + str(msg[0])+"\n"+str(msg1[3]) + " " + str(msg1[0])+"\n"+str(msg2[3]) + " " + str(msg2[0])+"\n"+str(msg3[3]) + " " + str(msg3[0])+"\n"+str(msg4[3]) + " " + str(msg4[0])+"\n"+str(msg5[3]) + " " + str(msg5[0])+"\n"+str(msg6[3]) + " " + str(msg6[0])+"\n"+str(msg7[3]) + " " + str(msg7[0])+"\n", inline=True)
                    embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%\n" + str(msg1[1])+"% - "+str(msg1[2])+"%\n" + str(msg2[1])+"% - "+str(msg2[2])+"%\n" + str(msg3[1])+"% - "+str(msg3[2])+"%\n" + str(msg4[1])+"% - "+str(msg4[2])+"%\n" + str(msg5[1])+"% - "+str(msg5[2])+"%\n" + str(msg6[1])+"% - "+str(msg6[2])+"%\n" + str(msg7[1])+"% - "+str(msg7[2])+"%**\n", inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                elif Name == "Type:":
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        content[2] = content[2].replace("*", "")
                    TName = "Type-null"
                    msg = list(await main(self, str(TName), str("pokeball")))
                    msg1= list(await main(self, str(TName), str("greatball")))
                    msg2= list(await main(self, str(TName), str("ultraball")))
                    msg3= list(await main(self, str(TName), str("duskball")))
                    msg4= list(await main(self, str(TName), str("repeatball")))
                    msg5= list(await main(self, str(TName), str("netball")))
                    msg6= list(await main(self, str(TName), str("Apriball")))
                    msg7= list(await main(self, str(TName), str("beastball")))
                    msg[0]= "Poke Ball"
                    msg1[0]= "Great Ball"
                    msg2[0]= "Ultra Ball"
                    msg3[0]= "Dusk Ball"
                    msg4[0]= "Repeat Ball"
                    msg5[0]= "Net Ball"
                    msg6[0]= "Apri Ball"
                    msg7[0]= "Beast Ball"
                    msg.append("<:xPoke:761255796839153767>")
                    msg1.append("<:xGreat:761255796721188924>")
                    msg2.append("<:xUltra:761277085083369546>")
                    msg3.append("<:xDusk:761255796859469824> ")
                    msg4.append("<:xRepeat:761255796947681300>")
                    msg5.append("<:xNet:761255796666400769>")
                    msg6.append("<:xFriend:761255796750680124>")
                    msg7.append("<:xBeast:761255796675444736>")
                    List2 = [(msg),(msg1),(msg2),(msg3),(msg4),(msg5),(msg6),(msg7)]
                    List = sorted(List2, key=getNKey)
                    Test = sorted(List, key=getKey, reverse=True)
                    msg = Test[0]
                    msg1 = Test[1]
                    msg2 = Test[2]
                    msg3 = Test[3]
                    msg4 = Test[4]
                    msg5 = Test[5]
                    msg6 = Test[6]
                    msg7 = Test[7]
                    embed = discord.Embed(title= "Type: Null's Capture Odds", description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+TName+".png")
                    embed.add_field(name= "Ball Type", value=str(msg[3]) + " " + str(msg[0])+"\n"+str(msg1[3]) + " " + str(msg1[0])+"\n"+str(msg2[3]) + " " + str(msg2[0])+"\n"+str(msg3[3]) + " " + str(msg3[0])+"\n"+str(msg4[3]) + " " + str(msg4[0])+"\n"+str(msg5[3]) + " " + str(msg5[0])+"\n"+str(msg6[3]) + " " + str(msg6[0])+"\n"+str(msg7[3]) + " " + str(msg7[0])+"\n", inline=True)
                    embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%\n" + str(msg1[1])+"% - "+str(msg1[2])+"%\n" + str(msg2[1])+"% - "+str(msg2[2])+"%\n" + str(msg3[1])+"% - "+str(msg3[2])+"%\n" + str(msg4[1])+"% - "+str(msg4[2])+"%\n" + str(msg5[1])+"% - "+str(msg5[2])+"%\n" + str(msg6[1])+"% - "+str(msg6[2])+"%\n" + str(msg7[1])+"% - "+str(msg7[2])+"%**\n", inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                elif Name.startswith("Nidoran\U00002640"):
                    Name = "Nidoranf"
                    msg = list(await main(self, str(Name), str("pokeball")))
                    msg1= list(await main(self, str(Name), str("greatball")))
                    msg2= list(await main(self, str(Name), str("ultraball")))
                    msg3= list(await main(self, str(Name), str("duskball")))
                    msg4= list(await main(self, str(Name), str("repeatball")))
                    msg5= list(await main(self, str(Name), str("netball")))
                    msg6= list(await main(self, str(Name), str("Apriball")))
                    msg7= list(await main(self, str(Name), str("beastball")))
                    msg[0]= "Poke Ball"
                    msg1[0]= "Great Ball"
                    msg2[0]= "Ultra Ball"
                    msg3[0]= "Dusk Ball"
                    msg4[0]= "Repeat Ball"
                    msg5[0]= "Net Ball"
                    msg6[0]= "Apri Ball"
                    msg7[0]= "Beast Ball"
                    msg.append("<:xPoke:761255796839153767>")
                    msg1.append("<:xGreat:761255796721188924>")
                    msg2.append("<:xUltra:761277085083369546>")
                    msg3.append("<:xDusk:761255796859469824> ")
                    msg4.append("<:xRepeat:761255796947681300>")
                    msg5.append("<:xNet:761255796666400769>")
                    msg6.append("<:xFriend:761255796750680124>")
                    msg7.append("<:xBeast:761255796675444736>")
                    List2 = [(msg),(msg1),(msg2),(msg3),(msg4),(msg5),(msg6),(msg7)]
                    List = sorted(List2, key=getNKey)
                    Test = sorted(List, key=getKey, reverse=True)
                    msg = Test[0]
                    msg1 = Test[1]
                    msg2 = Test[2]
                    msg3 = Test[3]
                    msg4 = Test[4]
                    msg5 = Test[5]
                    msg6 = Test[6]
                    msg7 = Test[7]
                    embed = discord.Embed(title= "Nidoran♀️'s Capture Odds", description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name= "Ball Type", value=str(msg[3]) + " " + str(msg[0])+"\n"+str(msg1[3]) + " " + str(msg1[0])+"\n"+str(msg2[3]) + " " + str(msg2[0])+"\n"+str(msg3[3]) + " " + str(msg3[0])+"\n"+str(msg4[3]) + " " + str(msg4[0])+"\n"+str(msg5[3]) + " " + str(msg5[0])+"\n"+str(msg6[3]) + " " + str(msg6[0])+"\n"+str(msg7[3]) + " " + str(msg7[0])+"\n", inline=True)
                    embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%\n" + str(msg1[1])+"% - "+str(msg1[2])+"%\n" + str(msg2[1])+"% - "+str(msg2[2])+"%\n" + str(msg3[1])+"% - "+str(msg3[2])+"%\n" + str(msg4[1])+"% - "+str(msg4[2])+"%\n" + str(msg5[1])+"% - "+str(msg5[2])+"%\n" + str(msg6[1])+"% - "+str(msg6[2])+"%\n" + str(msg7[1])+"% - "+str(msg7[2])+"%**\n", inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                elif Name.startswith("Nidoran\U00002642"):
                    Name = "Nidoranm"
                    msg = list(await main(self, str(Name), str("pokeball")))
                    msg1= list(await main(self, str(Name), str("greatball")))
                    msg2= list(await main(self, str(Name), str("ultraball")))
                    msg3= list(await main(self, str(Name), str("duskball")))
                    msg4= list(await main(self, str(Name), str("repeatball")))
                    msg5= list(await main(self, str(Name), str("netball")))
                    msg6= list(await main(self, str(Name), str("Apriball")))
                    msg7= list(await main(self, str(Name), str("beastball")))
                    msg[0]= "Poke Ball"
                    msg1[0]= "Great Ball"
                    msg2[0]= "Ultra Ball"
                    msg3[0]= "Dusk Ball"
                    msg4[0]= "Repeat Ball"
                    msg5[0]= "Net Ball"
                    msg6[0]= "Apri Ball"
                    msg7[0]= "Beast Ball"
                    msg.append("<:xPoke:761255796839153767>")
                    msg1.append("<:xGreat:761255796721188924>")
                    msg2.append("<:xUltra:761277085083369546>")
                    msg3.append("<:xDusk:761255796859469824> ")
                    msg4.append("<:xRepeat:761255796947681300>")
                    msg5.append("<:xNet:761255796666400769>")
                    msg6.append("<:xFriend:761255796750680124>")
                    msg7.append("<:xBeast:761255796675444736>")
                    List2 = [(msg),(msg1),(msg2),(msg3),(msg4),(msg5),(msg6),(msg7)]
                    List = sorted(List2, key=getNKey)
                    Test = sorted(List, key=getKey, reverse=True)
                    msg = Test[0]
                    msg1 = Test[1]
                    msg2 = Test[2]
                    msg3 = Test[3]
                    msg4 = Test[4]
                    msg5 = Test[5]
                    msg6 = Test[6]
                    msg7 = Test[7]
                    embed = discord.Embed(title= "Nidoran♂️'s Capture Odds", description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name= "Ball Type", value=str(msg[3]) + " " + str(msg[0])+"\n"+str(msg1[3]) + " " + str(msg1[0])+"\n"+str(msg2[3]) + " " + str(msg2[0])+"\n"+str(msg3[3]) + " " + str(msg3[0])+"\n"+str(msg4[3]) + " " + str(msg4[0])+"\n"+str(msg5[3]) + " " + str(msg5[0])+"\n"+str(msg6[3]) + " " + str(msg6[0])+"\n"+str(msg7[3]) + " " + str(msg7[0])+"\n", inline=True)
                    embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%\n" + str(msg1[1])+"% - "+str(msg1[2])+"%\n" + str(msg2[1])+"% - "+str(msg2[2])+"%\n" + str(msg3[1])+"% - "+str(msg3[2])+"%\n" + str(msg4[1])+"% - "+str(msg4[2])+"%\n" + str(msg5[1])+"% - "+str(msg5[2])+"%\n" + str(msg6[1])+"% - "+str(msg6[2])+"%\n" + str(msg7[1])+"% - "+str(msg7[2])+"%**\n", inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                else:
                    if Name == "Sirfetch’d":
                        Name = "Sirfetch'd"
                    if Name == "Farfetch’d":
                        Name = "Farfetch'd"
                    msg = list(await main(self, str(Name), str("pokeball")))
                    if msg[1] == 0.0:
                        await ctx.send("This Pokemon does not exist")
                    else:
                        msg1= list(await main(self, str(Name), str("greatball")))
                        msg2= list(await main(self, str(Name), str("ultraball")))
                        msg3= list(await main(self, str(Name), str("duskball")))
                        msg4= list(await main(self, str(Name), str("repeatball")))
                        msg5= list(await main(self, str(Name), str("netball")))
                        msg6= list(await main(self, str(Name), str("Apriball")))
                        msg7= list(await main(self, str(Name), str("beastball")))
                        msg[0]= "Poke Ball"
                        msg1[0]= "Great Ball"
                        msg2[0]= "Ultra Ball"
                        msg3[0]= "Dusk Ball"
                        msg4[0]= "Repeat Ball"
                        msg5[0]= "Net Ball"
                        msg6[0]= "Apri Ball"
                        msg7[0]= "Beast Ball"
                        msg.append("<:xPoke:761255796839153767>")
                        msg1.append("<:xGreat:761255796721188924>")
                        msg2.append("<:xUltra:761277085083369546>")
                        msg3.append("<:xDusk:761255796859469824>")
                        msg4.append("<:xRepeat:761255796947681300>")
                        msg5.append("<:xNet:761255796666400769>")
                        msg6.append("<:xFriend:761255796750680124>")
                        msg7.append("<:xBeast:761255796675444736>")
                        List2 = [(msg),(msg1),(msg2),(msg3),(msg4),(msg5),(msg6),(msg7)]
                        List = sorted(List2, key=getNKey)
                        Test = sorted(List, key=getKey, reverse=True)
                        msg = Test[0]
                        msg1 = Test[1]
                        msg2 = Test[2]
                        msg3 = Test[3]
                        msg4 = Test[4]
                        msg5 = Test[5]
                        msg6 = Test[6]
                        msg7 = Test[7]
                        if Name == "Porygon-z":
                            Name = "Porygon-Z"
                        if Name == "Farfetch'd":
                            embed = discord.Embed(title= Name + "'s Capture Odds", description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                            embed.add_field(name= "Ball Type", value=str(msg[3])+ " " + str(msg[0])+"\n"+str(msg1[3]) + " " + str(msg1[0])+"\n"+str(msg2[3]) + " " + str(msg2[0])+"\n"+str(msg3[3]) + " " + str(msg3[0])+"\n"+str(msg4[3]) + " " + str(msg4[0])+"\n"+str(msg5[3]) + " " + str(msg5[0])+"\n"+str(msg6[3]) + " " + str(msg6[0])+"\n"+str(msg7[3]) + " " + str(msg7[0])+"\n", inline=True)
                            embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%\n" + str(msg1[1])+"% - "+str(msg1[2])+"%\n" + str(msg2[1])+"% - "+str(msg2[2])+"%\n" + str(msg3[1])+"% - "+str(msg3[2])+"%\n" + str(msg4[1])+"% - "+str(msg4[2])+"%\n" + str(msg5[1])+"% - "+str(msg5[2])+"%\n" + str(msg6[1])+"% - "+str(msg6[2])+"%\n" + str(msg7[1])+"% - "+str(msg7[2])+"%**\n", inline=True)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            candelete = await get_delete(self, ctx)
                            if candelete == "True":
                                await ctx.message.delete()
                            await ctx.send(embed=embed)
                        else:
                            embed = discord.Embed(title= Name + "'s Capture Odds", description="", color=0x2962FF)
                            if Name == "Tapu Koko":
                                Name = "Tapu_Koko"
                            if Name == "Tapu Lele":
                                Name = "Tapu_Lele"
                            if Name == "Tapu Bulu":
                                Name = "Tapu_Bulu"
                            if Name == "Tapu Fini":
                                Name = "Tapu_Fini"
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                            embed.add_field(name= "Ball Type", value=str(msg[3]) + " " + str(msg[0])+"\n"+str(msg1[3]) + " " + str(msg1[0])+"\n"+str(msg2[3]) + " " + str(msg2[0])+"\n"+str(msg3[3]) + " " + str(msg3[0])+"\n"+str(msg4[3]) + " " + str(msg4[0])+"\n"+str(msg5[3]) + " " + str(msg5[0])+"\n"+str(msg6[3]) + " " + str(msg6[0])+"\n"+str(msg7[3]) + " " + str(msg7[0])+"\n", inline=True)
                            embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%\n" + str(msg1[1])+"% - "+str(msg1[2])+"%\n" + str(msg2[1])+"% - "+str(msg2[2])+"%\n" + str(msg3[1])+"% - "+str(msg3[2])+"%\n" + str(msg4[1])+"% - "+str(msg4[2])+"%\n" + str(msg5[1])+"% - "+str(msg5[2])+"%\n" + str(msg6[1])+"% - "+str(msg6[2])+"%\n" + str(msg7[1])+"% - "+str(msg7[2])+"%**\n", inline=True)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            candelete = await get_delete(self, ctx)
                            if candelete == "True":
                                await ctx.message.delete()
                            await ctx.send(embed=embed)
            else:
                Name = string.capwords(content[1])
                if Name.endswith("*"):
                    isshiny = "Shiny"
                    Name = Name.replace("*", "")
                Ballist = ["Pokeball","Greatball","Ultraball","Masterball","Safariball","Fastball","Levelball","Lureball","Heavyball","Loveball","Friendball","Moonball",
                           "Sportball","Netball","Nestball","Repeatball","Timerball","Luxuryball","Premierball","Diveball","Duskball","Healball","Quickball", "Dreamball", "Beastball"]

                Ballemoji = {"Poke":"<:xPoke:761255796839153767>","Great":"<:xGreat:761255796721188924>","Ultra":"<:xUltra:761277085083369546>","Master":"<:xMaster:761278001765416960>","Safari":"<:xSafari:761255796939554816>",
                "Fast":"<:xFast:761255796360609804>","Level":"<:xLevel:761255796738490378>","Lure":"<:xLure:761255796805599232>","Heavy":"<:xHeavy:761255796398096446>","Love":"<:xLove:761255796780564562>",
                "Friend":"<:xFriend:761255796750680124>","Moon":"<:xMoon:761255796624851015>","Sport":"<:xSport:761277653143257099>","Net":"<:xNet:761255796666400769>","Nest":"<:xNest:761255796688158814>",
                "Repeat":"<:xRepeat:761255796947681300>","Timer":"<:xTimer:761277585907777536>","Luxury":"<:xLuxury:761255796767457320>","Premier":"<:xPremier:761255796855930951>","Dive":"<:xDive:761255796587233310>",
                "Dusk":"<:xDusk:761255796859469824>","Heal":"<:xHeal:761255796516192328>","Quick":"<:xQuick:761255796926447646>", "Dream":"<:xDream:761255796666400819>", "Beast":"<:xBeast:761255796675444736>"}

                if Name == "Mr.":
                    Name = "Mr"
                if Name == "Mr":
                    FLCap = string.capwords(content[1])
                    FLLCap = string.capwords(content[2])
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        content[2] = content[2].replace("*", "")
                    RName = FLCap + content[2].lower()
                    RealN= FLCap+". "+FLLCap
                    LowN = content[1].lower()
                    LowM = content[2].lower()
                    Ball = string.capwords(content[3])+content[4]
                    Trueballname = string.capwords(content[3])
                    if Ball in Ballist:
                        Emojiball = Ballemoji[Trueballname]
                    else:
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                    if Ball in Ballist:
                        msg = await main(self, str(RName), str(Ball))
                        embed = discord.Embed(title= RealN + "'s Capture Odds", description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+RName+".png")
                        embed.add_field(name= "Ball Type", value=str(Emojiball)+ " " + str(Trueballname)+" Ball", inline=True)
                        embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%**", inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                        await ctx.send(embed=embed)
                    elif Ball not in Ballist:
                        await ctx.send("Either the Pokeball doesn't exist or you spelled the name or varient of the pokemon incorrect.")
                elif Name == "Mime":
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        content[2] = content[2].replace("*", "")
                    RName = "Mimejr"
                    Ball = string.capwords(content[3])+content[4]
                    Trueballname = string.capwords(content[3])
                    if Ball in Ballist:
                        Emojiball = Ballemoji[Trueballname]
                    else:
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                    if Ball in Ballist:
                        msg = await main(self, str(RName), str(Ball))
                        embed = discord.Embed(title= "Mime Jr.'s Capture Odds", description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Mimejr.png")
                        embed.add_field(name= "Ball Type", value=str(Emojiball)+ " " + str(Trueballname)+" Ball", inline=True)
                        embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%**", inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                        await ctx.send(embed=embed)
                    elif Ball not in Ballist:
                        await ctx.send("Either the Pokeball doesn't exist or you spelled the name or varient of the pokemon incorrect.")
                elif Name == "Type:":
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        content[2] = content[2].replace("*", "")
                    TName = "Type-null"
                    Ball = string.capwords(content[3])+content[4]
                    Trueballname = string.capwords(content[3])
                    if Ball in Ballist:
                        Emojiball = Ballemoji[Trueballname]
                    else:
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                    if Ball in Ballist:
                        msg = await main(self, str(TName), str(Ball))
                        embed = discord.Embed(title= "Type: Null's Capture Odds", description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+TName+".png")
                        embed.add_field(name= "Ball Type", value=str(Emojiball)+ " " + str(Trueballname)+" Ball", inline=True)
                        embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%**", inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                        await ctx.send(embed=embed)
                    elif Ball not in Ballist:
                        await ctx.send("Either the Pokeball doesn't exist or you spelled the name or varient of the pokemon incorrect.")
                elif Name.startswith("Nidoran\U00002640"):
                    Ball = string.capwords(content[2])+content[3]
                    Trueballname = string.capwords(content[2])
                    if Ball in Ballist:
                        Emojiball = Ballemoji[Trueballname]
                    else:
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                    if Ball in Ballist:
                        Name = "Nidoranf"
                        msg = await main(self, str(Name), str(Ball))
                        embed = discord.Embed(title= "Nidoran\U00002640's Capture Odds ", description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                        embed.add_field(name= "Ball Type", value=str(Emojiball)+ " " + str(Trueballname)+" Ball", inline=True)
                        embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%**", inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                        await ctx.send(embed=embed)
                    elif Ball not in Ballist:
                        await ctx.send("Either the Pokeball doesn't exist or you spelled the name or varient of the pokemon incorrect.")
                elif Name.startswith("Nidoran\U00002642"):
                    Ball = string.capwords(content[2])+content[3]
                    Trueballname = string.capwords(content[2])
                    if Ball in Ballist:
                        Emojiball = Ballemoji[Trueballname]
                    else:
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                    if Ball in Ballist:
                        Name = "Nidoranm"
                        msg = await main(self, str(Name), str(Ball))
                        embed = discord.Embed(title= "Nidoran♂️'s Capture Odds", description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                        embed.add_field(name= "Ball Type", value=str(Emojiball)+ " " + str(Trueballname)+" Ball", inline=True)
                        embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%**", inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                        await ctx.send(embed=embed)
                    elif Ball not in Ballist:
                        await ctx.send("Either the Pokeball doesn't exist or you spelled the name or varient of the pokemon incorrect.")
                elif Name == "Tapu":
                    Tapu = ["koko","lele","bulu","fini"]
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].lower() in Tapu:
                        Name = Name + " " +string.capwords(content[2])
                    Ball = string.capwords(content[3])+content[4]
                    Trueballname = string.capwords(content[3])
                    if Ball in Ballist:
                        Emojiball = Ballemoji[Trueballname]
                    else:
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                    if Ball in Ballist:
                        msg = await main(self, str(Name), str(Ball))
                        embed = discord.Embed(title= Name + "'s Capture Odds", description="", color=0x2962FF)
                        if Name == "Tapu Koko":
                            Name = "Tapu_Koko"
                        if Name == "Tapu Lele":
                            Name = "Tapu_Lele"
                        if Name == "Tapu Bulu":
                            Name = "Tapu_Bulu"
                        if Name == "Tapu Fini":
                            Name = "Tapu_Fini"
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                        embed.add_field(name= "Ball Type", value=str(Emojiball)+ " " + str(Trueballname)+" Ball", inline=True)
                        embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%**", inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                        await ctx.send(embed=embed)
                    elif Ball not in Ballist:
                        await ctx.send("Either the Pokeball doesn't exist or you spelled the name or varient of the pokemon incorrect.")
                else:
                    Ball = string.capwords(content[2])+content[3]
                    Trueballname = string.capwords(content[2])
                    if Ball in Ballist:
                        Emojiball = Ballemoji[Trueballname]
                    else:
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                    if Ball in Ballist:
                        if Name == "Sirfetch’d":
                            Name = "Sirfetch'd"
                        if Name == "Farfetch’d":
                            Name = "Farfetch'd"
                        msg = await main(self, str(Name), str(Ball))
                        if msg[1] == 0.0:
                            await ctx.send("This Pokemon does not exist")
                        else:
                            if Name == "Porygon-z":
                                Name = "Porygon-Z"
                            if Name == "Farfetch'd" or Name == "Farfetch’d":
                                Nfame = "Farfetchd"
                                embed = discord.Embed(title= Name + "'s Capture Odds", description="", color=0x2962FF)
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                                embed.add_field(name= "Ball Type", value=str(Emojiball)+ " " + str(Trueballname)+" Ball", inline=True)
                                embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%**", inline=True)
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                candelete = await get_delete(self, ctx)
                                if candelete == "True":
                                    await ctx.message.delete()
                                await ctx.send(embed=embed)
                            else:
                                embed = discord.Embed(title= Name + "'s Capture Odds", description="", color=0x2962FF)
                                if Name == "Tapu Koko":
                                    Name = "Tapu_Koko"
                                if Name == "Tapu Lele":
                                    Name = "Tapu_Lele"
                                if Name == "Tapu Bulu":
                                    Name = "Tapu_Bulu"
                                if Name == "Tapu Fini":
                                    Name = "Tapu_Fini"
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                                embed.add_field(name= "Ball Type", value=str(Emojiball)+ " " + str(Trueballname)+" Ball", inline=True)
                                embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%**", inline=True)
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                candelete = await get_delete(self, ctx)
                                if candelete == "True":
                                    await ctx.message.delete()
                                await ctx.send(embed=embed)
                    elif Ball not in Ballist:
                        await ctx.send("Either the Pokeball doesn't exist or you spelled the name or varient of the pokemon incorrect.")

    @catch.command(aliases=["gigantamax"])
    async def gmax(self, ctx):
        responce = str(ctx.message.content)
        if not responce.endswith('ball'):
            responce = responce + " ball"
        content = responce.split()
        isshiny = "Normal"
        if content[2].endswith("*"):
            isshiny = "Shiny"
            content[2] = content[2].replace("*", "")
        try:
            content[4].endswith('ball')
        except:
            GName = string.capwords(content[2])
            Listofgmax = ["Venusaur","Charizard","Blastoise","Butterfree","Pikachu","Meowth","Machamp","Gengar","Kingler","Lapras","Eevee","Snorlax","Garbodor",
                          "Melmetal","Rillaboom","Cinderace","Inteleon","Corviknight","Orbeetle","Drednaw","Coalossal","Flapple","Appletun","Sandaconda","Toxtricity",
                          "Centiskorch", "Hatterene","Grimmsnarl","Alcremie","Copperajah","Duraludon","Urshifu"]
            if GName in Listofgmax:
                msg = list(await gmaxmain(self, str(GName), str("pokeball")))
                msg1= list(await gmaxmain(self, str(GName), str("greatball")))
                msg2= list(await gmaxmain(self, str(GName), str("ultraball")))
                msg3= list(await gmaxmain(self, str(GName), str("duskball")))
                msg4= list(await gmaxmain(self, str(GName), str("repeatball")))
                msg5= list(await gmaxmain(self, str(GName), str("netball")))
                msg6= list(await gmaxmain(self, str(GName), str("apriball")))
                msg7= list(await gmaxmain(self, str(GName), str("beastball")))
                msg[0]= "Poke Ball"
                msg1[0]= "Great Ball"
                msg2[0]= "Ultra Ball"
                msg3[0]= "Dusk Ball"
                msg4[0]= "Repeat Ball"
                msg5[0]= "Net Ball"
                msg6[0]= "Apri Ball"
                msg7[0]= "Beast Ball"
                msg.append("<:xPoke:761255796839153767>")
                msg1.append("<:xGreat:761255796721188924>")
                msg2.append("<:xUltra:761277085083369546>")
                msg3.append("<:xDusk:761255796859469824> ")
                msg4.append("<:xRepeat:761255796947681300>")
                msg5.append("<:xNet:761255796666400769>")
                msg6.append("<:xFriend:761255796750680124>")
                msg7.append("<:xBeast:761255796675444736>")
                List2 = [(msg),(msg1),(msg2),(msg3),(msg4),(msg5),(msg6),(msg7)]
                List = sorted(List2, key=getNKey)
                Test = sorted(List, key=getKey, reverse=True)
                msg = Test[0]
                msg1 = Test[1]
                msg2 = Test[2]
                msg3 = Test[3]
                msg4 = Test[4]
                msg5 = Test[5]
                msg6 = Test[6]
                msg7 = Test[7]
                embed = discord.Embed(title= "Gmax " + GName + "'s Capture Odds", description="", color=0x2962FF)
                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Gmax/"+str(isshiny)+"/"+GName+".png")
                embed.add_field(name= "Ball Type", value=str(msg[3]) + " " + str(msg[0])+"\n"+str(msg1[3]) + " " + str(msg1[0])+"\n"+str(msg2[3]) + " " + str(msg2[0])+"\n"+str(msg3[3]) + " " + str(msg3[0])+"\n"+str(msg4[3]) + " " + str(msg4[0])+"\n"+str(msg5[3]) + " " + str(msg5[0])+"\n"+str(msg6[3]) + " " + str(msg6[0])+"\n"+str(msg7[3]) + " " + str(msg7[0])+"\n", inline=True)
                embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%\n" + str(msg1[1])+"% - "+str(msg1[2])+"%\n" + str(msg2[1])+"% - "+str(msg2[2])+"%\n" + str(msg3[1])+"% - "+str(msg3[2])+"%\n" + str(msg4[1])+"% - "+str(msg4[2])+"%\n" + str(msg5[1])+"% - "+str(msg5[2])+"%\n" + str(msg6[1])+"% - "+str(msg6[2])+"%\n" + str(msg7[1])+"% - "+str(msg7[2])+"%**\n", inline=True)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            else:
                await ctx.send('This Gmax Pokémon does not exist!')
        else:
            Ballist = ["Pokeball","Greatball","Ultraball","Masterball","Safariball","Fastball","Levelball","Lureball","Heavyball","Loveball","Friendball","Moonball",
                       "Sportball","Netball","Nestball","Repeatball","Timerball","Luxuryball","Premierball","Diveball","Duskball","Healball","Quickball", "Dreamball", "Beastball"]

            Ballemoji = {"Poke":"<:xPoke:761255796839153767>","Great":"<:xGreat:761255796721188924>","Ultra":"<:xUltra:761277085083369546>","Master":"<:xMaster:761278001765416960>","Safari":"<:xSafari:761255796939554816>",
            "Fast":"<:xFast:761255796360609804>","Level":"<:xLevel:761255796738490378>","Lure":"<:xLure:761255796805599232>","Heavy":"<:xHeavy:761255796398096446>","Love":"<:xLove:761255796780564562>",
            "Friend":"<:xFriend:761255796750680124>","Moon":"<:xMoon:761255796624851015>","Sport":"<:xSport:761277653143257099>","Net":"<:xNet:761255796666400769>","Nest":"<:xNest:761255796688158814>",
            "Repeat":"<:xRepeat:761255796947681300>","Timer":"<:xTimer:761277585907777536>","Luxury":"<:xLuxury:761255796767457320>","Premier":"<:xPremier:761255796855930951>","Dive":"<:xDive:761255796587233310>",
            "Dusk":"<:xDusk:761255796859469824>","Heal":"<:xHeal:761255796516192328>","Quick":"<:xQuick:761255796926447646>", "Dream":"<:xDream:761255796666400819>", "Beast":"<:xBeast:761255796675444736>"}

            GName = string.capwords(content[2])
            Listofgmax = ["Venusaur","Charizard","Blastoise","Butterfree","Pikachu","Meowth","Machamp","Gengar","Kingler","Lapras","Eevee","Snorlax","Garbodor",
                          "Melmetal","Rillaboom","Cinderace","Inteleon","Corviknight","Orbeetle","Drednaw","Coalossal","Flapple","Appletun","Sandaconda","Toxtricity",
                          "Centiskorch", "Hatterene","Grimmsnarl","Alcremie","Copperajah","Duraludon","Urshifu"]
            if GName in Listofgmax:
                Ball = string.capwords(content[3])+content[4]
                Trueballname = string.capwords(content[3])
                if Ball in Ballist:
                    Emojiball = Ballemoji[Trueballname]
                else:
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                if Ball in Ballist:
                    if Ball == "Heavyball":
                        msg = await gmaxmain(self, str(GName), str("Pokeball"))
                        embed = discord.Embed(title= "Gmax " + GName + "'s Capture Odds", description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Gmax/"+str(isshiny)+"/"+GName+".png")
                        embed.add_field(name= "Ball Type", value=str(Emojiball) + " " + str(Trueballname)+ " Ball", inline=True)
                        embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%**", inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        msg = await gmaxmain(self, str(GName), str(Ball))
                        embed = discord.Embed(title= "Gmax " + GName + "'s Capture Odds", description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Gmax/"+str(isshiny)+"/"+GName+".png")
                        embed.add_field(name= "Ball Type", value=str(Emojiball)+ " " + str(Trueballname)+" Ball", inline=True)
                        embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%**", inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                        await ctx.send(embed=embed)
                elif Ball not in Ballist:
                    await ctx.send("Either the Pokeball doesn't exist or you spelled the name or varient of the pokemon incorrect.")
            else:
                await ctx.send('This Gmax Pokémon does not exist!')

    @catch.command(aliases=["alola"])
    async def alolan(self, ctx):
        responce = str(ctx.message.content)
        if not responce.endswith('ball'):
            responce = responce + " ball"
        content = responce.split()
        isshiny = "Normal"
        if content[2].endswith("*"):
            isshiny = "Shiny"
            content[2] = content[2].replace("*", "")
        try:
            content[4].endswith('ball')
        except:
            GaName = string.capwords(content[2])
            Listofalola = ["Rattata","Raticate","Raichu","Sandshrew","Sandslash","Vulpix","Ninetails","Diglett","Dugtrio","Meowth","Persian","Geodude","Graveler",
                           "Golem","Grimer","Muk","Exeggutor","Marowak"]
            if GaName in Listofalola:
                    msg = list(await alolanmain(self, str(GaName), str("pokeball")))
                    msg1= list(await alolanmain(self, str(GaName), str("greatball")))
                    msg2= list(await alolanmain(self, str(GaName), str("ultraball")))
                    msg3= list(await alolanmain(self, str(GaName), str("duskball")))
                    msg4= list(await alolanmain(self, str(GaName), str("repeatball")))
                    msg5= list(await alolanmain(self, str(GaName), str("netball")))
                    msg6= list(await alolanmain(self, str(GaName), str("Apriball")))
                    msg7= list(await alolanmain(self, str(GaName), str("beastball")))
                    msg[0]= "Poke Ball"
                    msg1[0]= "Great Ball"
                    msg2[0]= "Ultra Ball"
                    msg3[0]= "Dusk Ball"
                    msg4[0]= "Repeat Ball"
                    msg5[0]= "Net Ball"
                    msg6[0]= "Apri Ball"
                    msg7[0]= "Beast Ball"
                    msg.append("<:xPoke:761255796839153767>")
                    msg1.append("<:xGreat:761255796721188924>")
                    msg2.append("<:xUltra:761277085083369546>")
                    msg3.append("<:xDusk:761255796859469824> ")
                    msg4.append("<:xRepeat:761255796947681300>")
                    msg5.append("<:xNet:761255796666400769>")
                    msg6.append("<:xFriend:761255796750680124>")
                    msg7.append("<:xBeast:761255796675444736>")
                    List2 = [(msg),(msg1),(msg2),(msg3),(msg4),(msg5),(msg6),(msg7)]
                    List = sorted(List2, key=getNKey)
                    Test = sorted(List, key=getKey, reverse=True)
                    msg = Test[0]
                    msg1 = Test[1]
                    msg2 = Test[2]
                    msg3 = Test[3]
                    msg4 = Test[4]
                    msg5 = Test[5]
                    msg6 = Test[6]
                    msg7 = Test[7]
                    embed = discord.Embed(title= "Alolan " + GaName + "'s Capture Odds", description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Alolan/"+str(isshiny)+"/"+GaName+".png")
                    embed.add_field(name= "Ball Type", value=str(msg[3]) + " " + str(msg[0])+"\n"+str(msg1[3]) + " " + str(msg1[0])+"\n"+str(msg2[3]) + " " + str(msg2[0])+"\n"+str(msg3[3]) + " " + str(msg3[0])+"\n"+str(msg4[3]) + " " + str(msg4[0])+"\n"+str(msg5[3]) + " " + str(msg5[0])+"\n"+str(msg6[3]) + " " + str(msg6[0])+"\n"+str(msg7[3]) + " " + str(msg7[0])+"\n", inline=True)
                    embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%\n" + str(msg1[1])+"% - "+str(msg1[2])+"%\n" + str(msg2[1])+"% - "+str(msg2[2])+"%\n" + str(msg3[1])+"% - "+str(msg3[2])+"%\n" + str(msg4[1])+"% - "+str(msg4[2])+"%\n" + str(msg5[1])+"% - "+str(msg5[2])+"%\n" + str(msg6[1])+"% - "+str(msg6[2])+"%\n" + str(msg7[1])+"% - "+str(msg7[2])+"%**\n", inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
            else:
                await ctx.send('This Alolan Pokémon does not exist!')
        else:
            Ballist = ["Pokeball","Greatball","Ultraball","Masterball","Safariball","Fastball","Levelball","Lureball","Heavyball","Loveball","Friendball","Moonball",
                       "Sportball","Netball","Nestball","Repeatball","Timerball","Luxuryball","Premierball","Diveball","Duskball","Healball","Quickball", "Dreamball", "Beastball"]

            Ballemoji = {"Poke":"<:xPoke:761255796839153767>","Great":"<:xGreat:761255796721188924>","Ultra":"<:xUltra:761277085083369546>","Master":"<:xMaster:761278001765416960>","Safari":"<:xSafari:761255796939554816>",
            "Fast":"<:xFast:761255796360609804>","Level":"<:xLevel:761255796738490378>","Lure":"<:xLure:761255796805599232>","Heavy":"<:xHeavy:761255796398096446>","Love":"<:xLove:761255796780564562>",
            "Friend":"<:xFriend:761255796750680124>","Moon":"<:xMoon:761255796624851015>","Sport":"<:xSport:761277653143257099>","Net":"<:xNet:761255796666400769>","Nest":"<:xNest:761255796688158814>",
            "Repeat":"<:xRepeat:761255796947681300>","Timer":"<:xTimer:761277585907777536>","Luxury":"<:xLuxury:761255796767457320>","Premier":"<:xPremier:761255796855930951>","Dive":"<:xDive:761255796587233310>",
            "Dusk":"<:xDusk:761255796859469824>","Heal":"<:xHeal:761255796516192328>","Quick":"<:xQuick:761255796926447646>", "Dream":"<:xDream:761255796666400819>", "Beast":"<:xBeast:761255796675444736>"}
            Ball = string.capwords(content[3])+content[4]
            Trueballname = string.capwords(content[3])
            if Ball in Ballist:
                Emojiball = Ballemoji[Trueballname]
            else:
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
            GaName = string.capwords(content[2])
            Listofalola = ["Rattata","Raticate","Raichu","Sandshrew","Sandslash","Vulpix","Ninetails","Diglett","Dugtrio","Meowth","Persian","Geodude","Graveler",
                           "Golem","Grimer","Muk","Exeggutor","Marowak"]
            if GaName in Listofalola:
                    Ball = string.capwords(content[3])+content[4]
                    if Ball in Ballist:
                        msg = await alolanmain(self, str(GaName), str(Ball))
                        embed = discord.Embed(title= "Alolan " + GaName + "'s Capture Odds", description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Alolan/"+str(isshiny)+"/"+GaName+".png")
                        embed.add_field(name= "Ball Type", value=str(Emojiball)+ " " + str(Trueballname)+" Ball", inline=True)
                        embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%**", inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                        await ctx.send(embed=embed)
                    elif Ball not in Ballist:
                        await ctx.send("Either the Pokeball doesn't exist or you spelled the name or varient of the pokemon incorrect.")
            else:
                await ctx.send('This Alolan Pokémon does not exist!')

    @catch.command(aliases=["galar"])
    async def galarian(self, ctx):
        responce = str(ctx.message.content)
        if not responce.endswith('ball'):
            responce = responce + " ball"
        content = responce.split()
        isshiny = "Normal"
        if content[2].endswith("*"):
            isshiny = "Shiny"
            content[2] = content[2].replace("*", "")
        try:
            (content[4].endswith('ball') and content[3].lower()!="mime" and content[3].lower()!="mime*") or content[5].endswith('ball')
        except:
            GlName = string.capwords(content[2])
            GlmName = string.capwords(content[2]) + " Mime"
            Listofgalar = ["Meowth","Ponyta","Rapidash","Slowpoke","Slowbro","Farfetch'd","Farfetch’d","Weezing","Mr Mime","Mr. Mime","Corsola","Zigzagoon","Linoone","Darumaka",
                           "Darmanitan","Yamask","Stunfisk","Slowking","Articuno","Moltres","Zapdos"]
            if GlName in Listofgalar or GlmName in Listofgalar:
                if GlName == "Mr.":
                    GlName = "Mr"
                if GlName == "Mr":
                    if content[3].endswith("*"):
                        isshiny = "Shiny"
                        content[3] = content[3].replace("*", "")
                    RGName = "Mrmime"
                    msg = list(await galarianmain(self, str(RGName), str("pokeball")))
                    msg1= list(await galarianmain(self, str(RGName), str("greatball")))
                    msg2= list(await galarianmain(self, str(RGName), str("ultraball")))
                    msg3= list(await galarianmain(self, str(RGName), str("duskball")))
                    msg4= list(await galarianmain(self, str(RGName), str("repeatball")))
                    msg5= list(await galarianmain(self, str(RGName), str("netball")))
                    msg6= list(await galarianmain(self, str(RGName), str("Apriball")))
                    msg7= list(await galarianmain(self, str(RGName), str("beastball")))
                    msg[0]= "Poke Ball"
                    msg1[0]= "Great Ball"
                    msg2[0]= "Ultra Ball"
                    msg3[0]= "Dusk Ball"
                    msg4[0]= "Repeat Ball"
                    msg5[0]= "Net Ball"
                    msg6[0]= "Apri Ball"
                    msg7[0]= "Beast Ball"
                    msg.append("<:xPoke:761255796839153767>")
                    msg1.append("<:xGreat:761255796721188924>")
                    msg2.append("<:xUltra:761277085083369546>")
                    msg3.append("<:xDusk:761255796859469824> ")
                    msg4.append("<:xRepeat:761255796947681300>")
                    msg5.append("<:xNet:761255796666400769>")
                    msg6.append("<:xFriend:761255796750680124>")
                    msg7.append("<:xBeast:761255796675444736>")
                    List2 = [(msg),(msg1),(msg2),(msg3),(msg4),(msg5),(msg6),(msg7)]
                    List = sorted(List2, key=getNKey)
                    Test = sorted(List, key=getKey, reverse=True)
                    msg = Test[0]
                    msg1 = Test[1]
                    msg2 = Test[2]
                    msg3 = Test[3]
                    msg4 = Test[4]
                    msg5 = Test[5]
                    msg6 = Test[6]
                    msg7 = Test[7]
                    embed = discord.Embed(title= "Galarian Mr. Mime's Capture Odds", description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/Mrmime.png")
                    embed.add_field(name= "Ball Type", value=str(msg[0])+"\n"+str(msg1[3]) + " " + str(msg1[0])+"\n"+str(msg2[3]) + " " + str(msg2[0])+"\n"+str(msg3[3]) + " " + str(msg3[0])+"\n"+str(msg4[3]) + " " + str(msg4[0])+"\n"+str(msg5[3]) + " " + str(msg5[0])+"\n"+str(msg6[3]) + " " + str(msg6[0])+"\n"+str(msg7[3]) + " " + str(msg7[0])+"\n", inline=True)
                    embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%\n" + str(msg1[1])+"% - "+str(msg1[2])+"%\n" + str(msg2[1])+"% - "+str(msg2[2])+"%\n" + str(msg3[1])+"% - "+str(msg3[2])+"%\n" + str(msg4[1])+"% - "+str(msg4[2])+"%\n" + str(msg5[1])+"% - "+str(msg5[2])+"%\n" + str(msg6[1])+"% - "+str(msg6[2])+"%\n" + str(msg7[1])+"% - "+str(msg7[2])+"%**\n", inline=True)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                elif GlName != "Mr":
                        if GlName == "Farfetch’d":
                            GlName = "Farfetch'd"
                        msg = list(await galarianmain(self, str(GlName), str("pokeball")))
                        msg1= list(await galarianmain(self, str(GlName), str("greatball")))
                        msg2= list(await galarianmain(self, str(GlName), str("ultraball")))
                        msg3= list(await galarianmain(self, str(GlName), str("duskball")))
                        msg4= list(await galarianmain(self, str(GlName), str("repeatball")))
                        msg5= list(await galarianmain(self, str(GlName), str("netball")))
                        msg6= list(await galarianmain(self, str(GlName), str("apriball")))
                        msg7= list(await galarianmain(self, str(GlName), str("beastball")))
                        msg[0]= "Poke Ball"
                        msg1[0]= "Great Ball"
                        msg2[0]= "Ultra Ball"
                        msg3[0]= "Dusk Ball"
                        msg4[0]= "Repeat Ball"
                        msg5[0]= "Net Ball"
                        msg6[0]= "Apri Ball"
                        msg7[0]= "Beast Ball"
                        msg.append("<:xPoke:761255796839153767>")
                        msg1.append("<:xGreat:761255796721188924>")
                        msg2.append("<:xUltra:761277085083369546>")
                        msg3.append("<:xDusk:761255796859469824> ")
                        msg4.append("<:xRepeat:761255796947681300>")
                        msg5.append("<:xNet:761255796666400769>")
                        msg6.append("<:xFriend:761255796750680124>")
                        msg7.append("<:xBeast:761255796675444736>")
                        List2 = [(msg),(msg1),(msg2),(msg3),(msg4),(msg5),(msg6),(msg7)]
                        List = sorted(List2, key=getNKey)
                        Test = sorted(List, key=getKey, reverse=True)
                        msg = Test[0]
                        msg1 = Test[1]
                        msg2 = Test[2]
                        msg3 = Test[3]
                        msg4 = Test[4]
                        msg5 = Test[5]
                        msg6 = Test[6]
                        msg7 = Test[7]
                        if GlName == "Farfetch'd":
                            GlfName = "Farfetchd"
                            embed = discord.Embed(title= "Galarian " + GlName + "'s Capture Odds", description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+GlfName+".png")
                            embed.add_field(name= "Ball Type", value=str(msg[3]) + " " + str(msg[0])+"\n"+str(msg1[3]) + " " + str(msg1[0])+"\n"+str(msg2[3]) + " " + str(msg2[0])+"\n"+str(msg3[3]) + " " + str(msg3[0])+"\n"+str(msg4[3]) + " " + str(msg4[0])+"\n"+str(msg5[3]) + " " + str(msg5[0])+"\n"+str(msg6[3]) + " " + str(msg6[0])+"\n"+str(msg7[3]) + " " + str(msg7[0])+"\n", inline=True)
                            embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%\n" + str(msg1[1])+"% - "+str(msg1[2])+"%\n" + str(msg2[1])+"% - "+str(msg2[2])+"%\n" + str(msg3[1])+"% - "+str(msg3[2])+"%\n" + str(msg4[1])+"% - "+str(msg4[2])+"%\n" + str(msg5[1])+"% - "+str(msg5[2])+"%\n" + str(msg6[1])+"% - "+str(msg6[2])+"%\n" + str(msg7[1])+"% - "+str(msg7[2])+"%**\n", inline=True)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            candelete = await get_delete(self, ctx)
                            if candelete == "True":
                                await ctx.message.delete()
                            await ctx.send(embed=embed)
                        else:
                            embed = discord.Embed(title= "Galarian " + GlName + "'s Capture Odds", description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+GlName+".png")
                            embed.add_field(name= "Ball Type", value=str(msg[3]) + " " + str(msg[0])+"\n"+str(msg1[3]) + " " + str(msg1[0])+"\n"+str(msg2[3]) + " " + str(msg2[0])+"\n"+str(msg3[3]) + " " + str(msg3[0])+"\n"+str(msg4[3]) + " " + str(msg4[0])+"\n"+str(msg5[3]) + " " + str(msg5[0])+"\n"+str(msg6[3]) + " " + str(msg6[0])+"\n"+str(msg7[3]) + " " + str(msg7[0])+"\n", inline=True)
                            embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%\n" + str(msg1[1])+"% - "+str(msg1[2])+"%\n" + str(msg2[1])+"% - "+str(msg2[2])+"%\n" + str(msg3[1])+"% - "+str(msg3[2])+"%\n" + str(msg4[1])+"% - "+str(msg4[2])+"%\n" + str(msg5[1])+"% - "+str(msg5[2])+"%\n" + str(msg6[1])+"% - "+str(msg6[2])+"%\n" + str(msg7[1])+"% - "+str(msg7[2])+"%**\n", inline=True)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            candelete = await get_delete(self, ctx)
                            if candelete == "True":
                                await ctx.message.delete()
                            await ctx.send(embed=embed)
        else:
            Ballist = ["Pokeball","Greatball","Ultraball","Masterball","Safariball","Fastball","Levelball","Lureball","Heavyball","Loveball","Friendball","Moonball",
                       "Sportball","Netball","Nestball","Repeatball","Timerball","Luxuryball","Premierball","Diveball","Duskball","Healball","Quickball", "Dreamball", "Beastball"]

            Ballemoji = {"Poke":"<:xPoke:761255796839153767>","Great":"<:xGreat:761255796721188924>","Ultra":"<:xUltra:761277085083369546>","Master":"<:xMaster:761278001765416960>","Safari":"<:xSafari:761255796939554816>",
            "Fast":"<:xFast:761255796360609804>","Level":"<:xLevel:761255796738490378>","Lure":"<:xLure:761255796805599232>","Heavy":"<:xHeavy:761255796398096446>","Love":"<:xLove:761255796780564562>",
            "Friend":"<:xFriend:761255796750680124>","Moon":"<:xMoon:761255796624851015>","Sport":"<:xSport:761277653143257099>","Net":"<:xNet:761255796666400769>","Nest":"<:xNest:761255796688158814>",
            "Repeat":"<:xRepeat:761255796947681300>","Timer":"<:xTimer:761277585907777536>","Luxury":"<:xLuxury:761255796767457320>","Premier":"<:xPremier:761255796855930951>","Dive":"<:xDive:761255796587233310>",
            "Dusk":"<:xDusk:761255796859469824>","Heal":"<:xHeal:761255796516192328>","Quick":"<:xQuick:761255796926447646>", "Dream":"<:xDream:761255796666400819>", "Beast":"<:xBeast:761255796675444736>"}

            GlName = string.capwords(content[2])
            GlmName = string.capwords(content[2]) + " Mime"
            Listofgalar = ["Meowth","Ponyta","Rapidash","Slowpoke","Slowbro","Farfetch'd","Farfetch’d","Weezing","Mr Mime","Corsola","Zigzagoon","Linoone","Darumaka",
                           "Darmanitan","Yamask","Stunfisk","Slowking","Articuno","Moltres","Zapdos"]
            if GlName in Listofgalar or GlmName in Listofgalar:
                if GlName == "Mr":
                    if content[3].endswith("*"):
                        isshiny = "Shiny"
                        content[3] = content[3].replace("*", "")
                    RGName = "Mrmime"
                    Ball = string.capwords(content[4])+content[5]
                    Trueballname = string.capwords(content[4])
                    if Ball in Ballist:
                        Emojiball = Ballemoji[Trueballname]
                    else:
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                    if Ball in Ballist:
                        msg = await galarianmain(self, str(RGName), str(Ball))
                        embed = discord.Embed(title= "Galarian Mr. Mime's Capture Odds", description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/Mrmime.png")
                        embed.add_field(name= "Ball Type", value=str(Emojiball)+ " " + str(Trueballname)+" Ball", inline=True)
                        embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%**", inline=True)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                        await ctx.send(embed=embed)
                    elif Ball not in Ballist:
                        await ctx.send("Either the Pokeball doesn't exist or you spelled the name or varient of the pokemon incorrect.")
                elif GlName != "Mr":
                    Ball = string.capwords(content[3])+content[4]
                    Trueballname = string.capwords(content[3])
                    if Ball in Ballist:
                        Emojiball = Ballemoji[Trueballname]
                    else:
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                    if Ball in Ballist:
                        msg = await galarianmain(self, str(GlName), str(Ball))
                        if GlName == "Farfetch'd" or GlName =="Farfetch’d":
                            GlfName = "Farfetchd"
                            embed = discord.Embed(title= "Galarian " + GlName + "'s Capture Odds", description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+GlfName+".png")
                            embed.add_field(name= "Ball Type", value=str(Emojiball)+ " " + str(Trueballname)+" Ball", inline=True)
                            embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%**", inline=True)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            candelete = await get_delete(self, ctx)
                            if candelete == "True":
                                await ctx.message.delete()
                            await ctx.send(embed=embed)
                        else:
                            embed = discord.Embed(title= "Galarian " + GlName + "'s Capture Odds", description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+GlName+".png")
                            embed.add_field(name= "Ball Type", value=str(Emojiball)+ " " + str(Trueballname)+" Ball", inline=True)
                            embed.add_field(name="Odds", value="**"+str(msg[1])+"% - "+str(msg[2])+"%**", inline=True)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            candelete = await get_delete(self, ctx)
                            if candelete == "True":
                                await ctx.message.delete()
                            await ctx.send(embed=embed)

    @commands.command(aliases=["p"])
    async def pokedex(self, ctx):
        if ctx.invoked_subcommand is None:
            responce = str(ctx.message.content)
            isshiny = "Normal"
            content = responce.split()
            if content[1].endswith("*"):
                isshiny = "Shiny"
                content[1] = content[1].replace("*", "")
            if content[1].lower() == "alolan":
                GaName = string.capwords(content[2])
                if GaName.endswith("*"):
                    isshiny = "Shiny"
                    GaName = GaName.replace("*", "")
                Listofalola = ["Rattata","Raticate","Raichu","Sandshrew","Sandslash","Vulpix","Ninetails","Diglett","Dugtrio","Meowth","Persian","Geodude","Graveler",
                               "Golem","Grimer","Muk","Exeggutor","Marowak"]
                if GaName in Listofalola:
                    AName = GaName
                    result = await alolanpokedex(self, str(AName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Alolan " + AName + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Alolan/"+str(isshiny)+"/"+GaName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                else:
                    await ctx.send('This Alolan Pokémon does not exist')
            elif content[1].lower() == "galarian":
                if content[2].endswith("*"):
                    isshiny = "Shiny"
                    content[2] = content[2].replace("*", "")
                GlName = string.capwords(content[2])
                GlmName = string.capwords(content[2]) + " Mime"
                Listofgalar = ["Meowth","Ponyta","Rapidash","Slowpoke","Slowbro","Farfetch'd","Farfetch’d","Weezing","Mr Mime","Mr. Mime","Articuno","Zapdos","Moltres","Slowking","Corsola","Zigzagoon","Linoone","Darumaka","Darmanitan","Yamask","Stunfisk"]
                if GlName in Listofgalar or GlmName in Listofgalar:
                    if GlName == "Mr" or GlName == "Mr.":
                        if content[3].endswith("*"):
                            isshiny = "Shiny"
                            content[3] = content[3].replace("*", "")
                        RGName = "Mrmime"
                        result = await galarianpokedex(self, str(RGName))
                        embed = discord.Embed(title= "#"+ str(result[0]) + "   Galarian " + GlmName + "   " + str(result[2]) , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+RGName+".png")
                        embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                        embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                        embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                        embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                        await ctx.send(embed=embed)
                    elif GlName != "Mr":
                        if GlName== "Darmanitan":
                            result = await galarianpokedex(self, str(GlName))
                            embed = discord.Embed(title= "#"+ str(result[0]) + "   Galarian " + GlName + "   " + str(result[2]) , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+GlName+".png")
                            embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                            embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                            embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                            embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            candelete = await get_delete(self, ctx)
                            if candelete == "True":
                                await ctx.message.delete()
                            await ctx.send(embed=embed)
                            GzzName = "Darmanitanzen"
                            result = await galarianpokedex(self, str(GzzName))
                            embed = discord.Embed(title= "#"+ str(result[0]) + "Galarian Darmanitan Zen Mode   " + str(result[2]) , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+GzzName+".png")
                            embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                            embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                            embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                            embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            await ctx.send(embed=embed)
                        else:
                            if GlName == "Farfetch’d":
                                GlName = "Farfetch'd"
                            result = await galarianpokedex(self, str(GlName))
                            if GlName == "Farfetch'd":
                                w = "Farfetchd"
                                embed = discord.Embed(title= "#"+ str(result[0]) + "   Galarian " + GlName + "   " + str(result[2]) , description="", color=0x2962FF)
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+w+".png")
                                embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                                embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                                embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                                embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                candelete = await get_delete(self, ctx)
                                if candelete == "True":
                                    await ctx.message.delete()
                                await ctx.send(embed=embed)
                            else:
                                embed = discord.Embed(title= "#"+ str(result[0]) + "   Galarian " + GlName + "   " + str(result[2]) , description="", color=0x2962FF)
                                embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+GlName+".png")
                                embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                                embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                                embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                                embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                candelete = await get_delete(self, ctx)
                                if candelete == "True":
                                    await ctx.message.delete()
                                await ctx.send(embed=embed)
                    else:
                        await ctx.send('This Galarian Pokemon does not exist!')
            else:
                Name = string.capwords(content[1])
                if Name == "Mr" or Name == "Mr.":
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2] == "mime":
                        RName = "Mrmime"
                        result = await pokedex(self, str(RName))
                        embed = discord.Embed(title= "#"+ str(result[0]) + "   Mr. Mime️   " + str(result[2]) , description="", color=0x2962FF)
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+RName+".png")
                        embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                        embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                        embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                        embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                        await ctx.send(embed=embed)
                    elif content[2] == 'rime':
                            RRName = "Mrrime"
                            result = await pokedex(self, str(RRName))
                            embed = discord.Embed(title= "#"+ str(result[0]) + "   Mr. Rime️   " + str(result[2]) , description="", color=0x2962FF)
                            embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+RRName+".png")
                            embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                            embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                            embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                            embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            candelete = await get_delete(self, ctx)
                            if candelete == "True":
                                await ctx.message.delete()
                            await ctx.send(embed=embed)
                elif Name == "Mime":
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        content[2] = content[2].replace("*", "")
                    RName = "Mimejr"
                    result = await pokedex(self, str(RName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "    " + Name + " Jr.  " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+RName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                elif Name == "Type:":
                    TName = "Type-null"
                    result = await pokedex(self, str(TName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + " Type: Null   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+TName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                elif Name.startswith("Nidoran\U00002640"):
                    Name = "Nidoranf"
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Nidoran♀️   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                elif Name.startswith("Nidoran\U00002642"):
                    Name = "Nidoranm"
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Nidoran♂️   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                elif Name== "Darmanitan":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Darmanitanzen"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Darmanitan Zen Mode   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Wormadam":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Plant Cloak   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Wormadams"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Sandy Cloak  " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                    GzzzName = "Wormadamt"
                    result = await pokedex(self, str(GzzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Trash Cloak  " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Kyogre":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Kyogreprimal"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Primal " + Name + "  " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Groudon":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Groudonprimal"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Primal " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Deoxys":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Normal Form   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Adeoxys"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Attack Form  " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                    GzzzName = "Ddeoxys"
                    result = await pokedex(self, str(GzzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Defense Form  " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                    GzzzzName = "Sdeoxys"
                    result = await pokedex(self, str(GzzzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Speed Form  " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Rotom":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Hrotom"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Heat " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                    GzzzName = "Wrotom"
                    result = await pokedex(self, str(GzzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Wash " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                    GzzzzName = "Frotom"
                    result = await pokedex(self, str(GzzzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Frost " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                    GzzzzzName = "Fanrotom"
                    result = await pokedex(self, str(GzzzzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Fan " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                    GzzzzzzName = "Mrotom"
                    result = await pokedex(self, str(GzzzzzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Mow " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzzzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Giratina":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Altered Form   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Ogiratina"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Origin Form  " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Shaymin":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Land Forme   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Sshaymin"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Sky Forme " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Tornadus":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Incarnate Forme   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Ttornadus"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Therian Forme   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Thundurus":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Incanate Forme   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Tthundurus"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Therian Forme   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Landorus":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Incarnate Forme   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Tlandorus"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Therian Forme   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Kyurem":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Blackkyurem"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Black " + Name + "  " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                    GzzzName = "Whitekyurem"
                    result = await pokedex(self, str(GzzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   White " + Name + "  " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Meloetta":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Aria Forme   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Pmeloetta"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Pirouette Forme   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Greninja":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Ashgreninja"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Ash-" + Name + "  " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Aegislash":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Shield Forme   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Baegislash"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Blade Forme   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Pumpkaboo":
                    GzzaName = "Tpumpkaboo"
                    result = await pokedex(self, str(GzzaName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Small Size " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzaName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Average Size " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                    GzzzName = "Lpumpkaboo"
                    result = await pokedex(self, str(GzzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Large Size " + Name + "  " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                    GzzzzName = "Spumpkaboo"
                    result = await pokedex(self, str(GzzzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Super Size " + Name + "  " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Gourgeist":
                    GzzvName = "Smgourgeist"
                    result = await pokedex(self, str(GzzvName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Small Size " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzvName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Average Size " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                    GzzName = "Lgourgeist"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Large Size " + Name + "  " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                    GzzzName = "Sgourgeist"
                    result = await pokedex(self, str(GzzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Super Size " + Name + "  " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Zygarde":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   50% Forme " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Tzygarde"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   10% Forme " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                    GzzzName = "Czygarde"
                    result = await pokedex(self, str(GzzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Complete Forme " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Hoopa":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Confined   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Uhoopa"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Unbound   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Lycanroc":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Midday Form " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Mlycanroc"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Midnight Form " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                    GzzzName = "Dlycanroc"
                    result = await pokedex(self, str(GzzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Dusk Forme " + Name + "  " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Wishiwashi":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Solo Form " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Swishiwashi"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   School Form" + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Necrozma":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Dmnecrozma"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Dusk Mane " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                    GzzzName = "Dwnecrozma"
                    result = await pokedex(self, str(GzzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Dawn Wing " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                    GzzzzName = "Unecrozma"
                    result = await pokedex(self, str(GzzzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Ultra " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Eiscue":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Ice Face " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Neiscue"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Noice Face " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Zacian":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + ": Hero of Many Battles   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Czacian"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Crowned " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Zamazenta":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + ": Hero of Many Battles   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Czamazenta"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   Crowned " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Urshifu":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " 'Single Strike Style'   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzzName = "Rurshifu"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " 'Rapid Strike Style'  " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                elif Name == "Calyrex":
                    result = await pokedex(self, str(Name))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GzName = "Calyrexicerider"
                    result = await pokedex(self, str(GzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Ice Rider   " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                    GzzName = "Calyrexshadowrider"
                    result = await pokedex(self, str(GzzName))
                    embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + " Shadow Rider    " + str(result[2]) , description="", color=0x2962FF)
                    embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+GzzName+".png")
                    embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                    embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                    embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                    embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                else:
                    if Name == "Sirfetch’d":
                        Name = "Sirfetch'd"
                    if Name == "Farfetch’d":
                        Name = "Farfetch'd"
                    if Name == "Tapu":
                        Tapu = ["koko","lele","bulu","fini"]
                        if content[2].endswith("*"):
                            isshiny = "Shiny"
                            content[2] = content[2].replace("*", "")
                        if content[2].lower() in Tapu:
                            Name = Name + " " +string.capwords(content[2])
                    result = await pokedex(self, str(Name))
                    if Name == "Porygon-z":
                        Name = "Porygon-Z"
                    if result == None:
                        await ctx.send('This Pokémon does not exist!')
                    elif result != None:
                        embed = discord.Embed(title= "#"+ str(result[0]) + "   " + Name + "   " + str(result[2]) , description="", color=0x2962FF)
                        if Name == "Tapu Koko":
                            Name = "Tapu_Koko"
                        if Name == "Tapu Lele":
                            Name = "Tapu_Lele"
                        if Name == "Tapu Bulu":
                            Name = "Tapu_Bulu"
                        if Name == "Tapu Fini":
                            Name = "Tapu_Fini"
                        embed.set_thumbnail(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                        embed.add_field(name="Misc. info", value="Gender Ratio: \n**"+str(result[14])+"% M** / **"+str(result[15])+"% F**\nHeight/Weight: \n**"+str(result[16])+"m** / **"+str(result[17])+"kg**\nCatch Rate: **"+str(result[10])+"**\n**"+str(result[1])+"**\nEgg Groups: **\n"+str(result[18])+"\n"+str(result[19])+"**" , inline=True)
                        embed.add_field(name="Base Stats", value="HP: **"+str(result[3])+"**\nAtk: **"+str(result[4])+"**\nDef: **"+str(result[5])+"**\nSpA: **"+str(result[6])+"**\nSpD: **"+str(result[7])+"**\nSpe: **"+str(result[8])+"**\nTotal: **"+ str(result[9]) +"**", inline=True)
                        embed.add_field(name="Abilities", value="Ability 1: \n**" +str(result[11])+"**\nAbility 2: \n**"+str(result[12])+"**\nHidden Ability: \n**" + str(result[13]) +"**", inline=True)
                        embed.add_field(name="Dens", value="Sword: "+ str(result[20]) +"\nShield: " + str(result[21]), inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                        await ctx.send(embed=embed)

    @commands.command()
    async def natures(self, ctx):
        responce = str(ctx.message.content)
        embed = discord.Embed(title="", description="", color=0x2962FF)
        embed.set_image(url="https://static2.thegamerimages.com/wordpress/wp-content/uploads/2019/04/Nature-Charrt-via-Bulbapedia.jpg?")
        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
        candelete = await get_delete(self, ctx)
        if candelete == "True":
            await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(aliases=["b"])
    async def ball(self, ctx):
        responce = str(ctx.message.content)
        content = responce.split()
        BName = string.capwords(content[1])
        if BName.startswith("Cherish") or BName.startswith("Premier"):
            baln = BName[0:7]
            ballresult = await ball(self, str(baln))
            lbname = baln.lower()
            link = "https://serebii.net/itemdex/"+lbname+"ball.shtml"
            embed = discord.Embed(title= "**"+ baln + " Ball**", url=link, color=0x2962FF)
            embed.set_thumbnail(url= "https://img.pokemondb.net/sprites/items/"+lbname+"-ball.png")
            embed.add_field(name= "**Info:**", value="**Ball Modifier**: `"+ballresult[0]+"`\n**Ball Conditions**: `"+ballresult[1]+"`\n**Ball Effects**: `"+ballresult[2]+"`", inline=True)
            if baln == "Cherish":
                embed.set_image(url="https://media2.giphy.com/media/jnEBXaTewyLpqIttNi/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.send(embed=embed)
            elif baln == "Premier":
                embed.set_image(url="https://media0.giphy.com/media/RISohRZRfEQ4sJFZvw/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.send(embed=embed)
        elif BName.startswith("Friend") or BName.startswith("Luxury") or BName.startswith("Master") or BName.startswith("Repeat") or BName.startswith("Safari"):
            baln = BName[0:6]
            ballresult = await ball(self, str(baln))
            lbname = baln.lower()
            link = "https://serebii.net/itemdex/"+lbname+"ball.shtml"
            embed = discord.Embed(title= "**"+ baln + " Ball**", url=link, color=0x2962FF)
            embed.set_thumbnail(url= "https://img.pokemondb.net/sprites/items/"+lbname+"-ball.png")
            embed.add_field(name= "**Info:**", value="**Ball Modifier**: `"+ballresult[0]+"`\n**Ball Conditions**: `"+ballresult[1]+"`\n**Ball Effects**: `"+ballresult[2]+"`", inline=True)
            if baln == "Friend":
                embed.set_image(url="https://media0.giphy.com/media/f7Yl1vFzJqAudkJLTZ/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif baln == "Luxury":
                embed.set_image(url="https://media0.giphy.com/media/l29PJ0F8w8tvqPOZsn/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif baln == "Master":
                embed.set_image(url="https://media0.giphy.com/media/ggKzsZLL9d3xv6gsaQ/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif baln == "Repeat":
                embed.set_image(url="https://media2.giphy.com/media/lrzfd4lZI8BdWdJVHw/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif baln == "Safari":
                embed.set_image(url="https://media2.giphy.com/media/ihYy3vbNBdSZ12oPFv/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
        elif BName.startswith("Beast") or BName.startswith("Dream") or BName.startswith("Great") or BName.startswith("Heavy") or BName.startswith("Level") or BName.startswith("Quick") or BName.startswith("Timer") or BName.startswith("Ultra") or BName.startswith("Sport"):
            baln = BName[0:5]
            ballresult = await ball(self, str(baln))
            lbname = baln.lower()
            link = "https://serebii.net/itemdex/"+lbname+"ball.shtml"
            embed = discord.Embed(title= "**"+ baln + " Ball**", url=link, color=0x2962FF)
            embed.set_thumbnail(url= "https://img.pokemondb.net/sprites/items/"+lbname+"-ball.png")
            embed.add_field(name= "**Info:**", value="**Ball Modifier**: `"+ballresult[0]+"`\n**Ball Conditions**: `"+ballresult[1]+"`\n**Ball Effects**: `"+ballresult[2]+"`", inline=True)
            if baln == "Beast":
                embed.set_image(url="https://media0.giphy.com/media/Q8UsFRwVcAxBnXNo8q/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            if baln == "Dream":
                embed.set_image(url="https://media3.giphy.com/media/cMbaN5Pxe6ZX1RZmhV/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            if baln == "Great":
                embed.set_image(url="https://media0.giphy.com/media/J4h1EfSfBSDqQYqGs5/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            if baln == "Heavy":
                embed.set_image(url="https://media2.giphy.com/media/kDYfi0nctLKmrTjAVQ/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            if baln == "Level":
                embed.set_image(url="https://media0.giphy.com/media/MESCIFEPTDOHtiDAN9/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            if baln == "Quick":
                embed.set_image(url="https://media3.giphy.com/media/Sw0njjABoq2RwdZ021/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            if baln == "Timer":
                embed.set_image(url="https://media2.giphy.com/media/YonSDJD7IqH5ZR6Rty/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            if baln == "Ultra":
                embed.set_image(url="https://media2.giphy.com/media/kcUFH2HoOL2sVqAc0u/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif baln == "Sport":
                embed.set_image(url="https://media1.giphy.com/media/ihSCEcioiNza0EkPJ8/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
        elif BName.startswith("Dive") or BName.startswith("Dusk") or BName.startswith("Fast") or BName.startswith("Heal") or BName.startswith("Love") or BName.startswith("Lure") or BName.startswith("Moon") or BName.startswith("Nest") or BName.startswith("Poke"):
            baln = BName[0:4]
            ballresult = await ball(self, str(baln))
            lbname = baln.lower()
            link = "https://serebii.net/itemdex/"+lbname+"ball.shtml"
            embed = discord.Embed(title= "**"+ baln + " Ball**", url=link, color=0x2962FF)
            embed.set_thumbnail(url= "https://img.pokemondb.net/sprites/items/"+lbname+"-ball.png")
            embed.add_field(name= "**Info:**", value="**Ball Modifier**: `"+ballresult[0]+"`\n**Ball Conditions**: `"+ballresult[1]+"`\n**Ball Effects**: `"+ballresult[2]+"`", inline=True)
            if baln == "Dive":
                embed.set_image(url="https://media1.giphy.com/media/Q5M0qlYbqWlhvK34H4/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif baln == "Dusk":
                embed.set_image(url="https://media2.giphy.com/media/dUT8l6lgavNTVdAk9V/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif baln == "Fast":
                embed.set_image(url="https://media2.giphy.com/media/VdKewUvAPbzGrsIpC3/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif baln == "Heal":
                embed.set_image(url="https://media2.giphy.com/media/gj5rnzcbdiKaugdDJ1/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif baln == "Love":
                embed.set_image(url="https://media0.giphy.com/media/WrTdRwsteoMFjtyak5/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif baln == "Lure":
                embed.set_image(url="https://media2.giphy.com/media/eJGGUpd33e4FAQFetJ/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif baln == "Moon":
                embed.set_image(url="https://media0.giphy.com/media/Pns9GA5WRrMKBib3Ns/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif baln == "Nest":
                embed.set_image(url="https://media0.giphy.com/media/VJwZtnk8eBBwddOBpJ/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
            elif baln == "Poke":
                embed.set_image(url="https://media3.giphy.com/media/YMSzuD6AtcUWC7Ejvv/giphy.gif")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
        elif BName.startswith("Net"):
            baln = BName[0:3]
            ballresult = await ball(self, str(baln))
            lbname = baln.lower()
            link = "https://serebii.net/itemdex/"+lbname+"ball.shtml"
            embed = discord.Embed(title= "**"+ baln + " Ball**", url=link, color=0x2962FF)
            embed.set_thumbnail(url= "https://img.pokemondb.net/sprites/items/"+lbname+"-ball.png")
            embed.add_field(name= "**Info:**", value="**Ball Modifier**: `"+ballresult[0]+"`\n**Ball Conditions**: `"+ballresult[1]+"`\n**Ball Effects**: `"+ballresult[2]+"`", inline=True)
            embed.set_image(url="https://media3.giphy.com/media/iJhvFRLVMXNk7tJzVC/giphy.gif")
            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send(embed=embed)
        else:
            await ctx.send("The Poké-Ball requested was not found or doesn't exist.")

    @commands.command(aliases=["d"])
    async def den(self, ctx):
        responce = str(ctx.message.content)
        content = responce.split()
        res = content[1].isdigit()
        isshiny = "Normal"
        Den = string.capwords(content[1])
        if Den.endswith("*"):
            isshiny = "Shiny"
            Den = Den.replace("*", "")
        if res == True:
            result = await dennumber(self, str(Den))
            if result == None:
                await ctx.send("This den does not exist")
            else:
                link = "https://www.serebii.net/swordshield/maxraidbattles/den"+Den+".shtml"
                embed = discord.Embed(title= "Den "+ Den + ":", url=link, color=0x2962FF)
                embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/Dens/den"+str(Den)+".png")
                embed.add_field(name="Sword HA:", value=str(result[0]), inline=True)
                embed.add_field(name="Shield HA:", value=str(result[1]), inline=True)
                embed.add_field(name="Wild Area Location:", value="Wild Area: "+ str(result[2]) +"\nIsle of Armor: "+ str(result[3]) +"\nThe Crown Tundra: " + str(result[4]) + " ", inline=False)
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                    await ctx.message.delete()
                await ctx.send(embed=embed)
        elif res != True:
            Gnm = Den
            if Den == "Farfetch'd" or Den == "Farfetch’d" or Gnm == "Mr" or Gnm == "Mr.":
                if Den =="Farfetch'd" or Den == "Farfetch’d":
                    g = "Farfetchd"
                    result = await denname(self, str(g))
                    embed = discord.Embed(title= "Galarian "+ Den + " is in the following dens:", color=0x2962FF)
                    embed.set_thumbnail(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+str(g)+".png")
                    embed.add_field(name="Sword:", value=str(result[0]), inline=False)
                    embed.add_field(name="Sword HA:", value=str(result[2]), inline=False)
                    embed.add_field(name="Shield:", value=str(result[1]), inline=False)
                    embed.add_field(name="Shield HA:", value=str(result[3]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                elif Gnm == "Mr" or Gnm =="Mr.":
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        content[2] = content[2].replace("*", "")
                    Gnm = Gnm + " " + content[2].lower()
                    if Gnm == "Mr mime" or Gnm == "Mr. mime":
                        g = "Mrmime"
                        result = await denname(self, str(g))
                        embed = discord.Embed(title= "Galarian Mr. Mime is in the following dens:", color=0x2962FF)
                        embed.set_thumbnail(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/Mrmime.png")
                        embed.add_field(name="Sword:", value=str(result[0]), inline=False)
                        embed.add_field(name="Sword HA:", value=str(result[2]), inline=False)
                        embed.add_field(name="Shield:", value=str(result[1]), inline=False)
                        embed.add_field(name="Shield HA:", value=str(result[3]), inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                        await ctx.send(embed=embed)
                    elif Gnm == "Mr rime" or Gnm == "Mr. rime":
                        g = "Mrrime"
                        result = await denname(self, str(g))
                        embed = discord.Embed(title= "Mr. Rime is in the following dens:", color=0x2962FF)
                        embed.set_thumbnail(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Mrrime.png")
                        embed.add_field(name="Sword:", value=str(result[0]), inline=False)
                        embed.add_field(name="Sword HA:", value=str(result[2]), inline=False)
                        embed.add_field(name="Shield:", value=str(result[1]), inline=False)
                        embed.add_field(name="Shield HA:", value=str(result[3]), inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                        await ctx.send(embed=embed)
            elif Den =="Gmax" or Den == "Gigantamax":
                gmaxlist = ["Venusaur","Charizard","Blastoise","Butterfree","Machamp","Gengar","Kingler","Lapras","Snorlax","Garbodor","Corviknight","Orbeetle","Drednaw","Coalossal","Flapple",
                "Appletun","Sandaconda","Toxtricity","Centiskorch","Hatterene","Grimmsnarl","Alcremie","Copperajah","Duraludon"]
                
                try:
                    content[2]
                except:
                    await ctx.send("I don't know which Gmax/Gigantamax Pokemon you are asking for.")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() in gmaxlist:                                                                  
                        Den = content[2].capitalize()
                        result = await gmaxdenname(self, str(Den))
                        embed = discord.Embed(title= "Gmax "+ Den + " is in the following dens:", color=0x2962FF)
                        embed.set_thumbnail(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Gmax/"+str(isshiny)+"/"+Den+".png")
                        embed.add_field(name="Sword:", value=str(result[0]), inline=False)
                        embed.add_field(name="Sword HA:", value=str(result[2]), inline=False)
                        embed.add_field(name="Shield:", value=str(result[1]), inline=False)
                        embed.add_field(name="Shield HA:", value=str(result[3]), inline=False)
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                            await ctx.message.delete()
                        await ctx.send(embed=embed)
                    elif content[2].capitalize() not in gmaxlist:
                        await ctx.send('The Gmax Pokemon "' +str(content[2])+ '" Either does not exist or is not obtainable within a den.')
                                
            else:
                if Den == "Mime":
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        content[2] = content[2].replace("*", "")
                    g = "Mimejr"
                    result = await denname(self, str(g))
                    embed = discord.Embed(title= "Mime Jr. is in the following dens:", color=0x2962FF)
                    embed.set_thumbnail(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Mimejr.png")
                    embed.add_field(name="Sword:", value=str(result[0]), inline=False)
                    embed.add_field(name="Sword HA:", value=str(result[2]), inline=False)
                    embed.add_field(name="Shield:", value=str(result[1]), inline=False)
                    embed.add_field(name="Shield HA:", value=str(result[3]), inline=False)
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                        await ctx.message.delete()
                    await ctx.send(embed=embed)
                else:
                    if Den.startswith("Nidoran\U00002640"):
                        Den = "Nidoranf"
                    if Den.startswith("Nidoran\U00002642"):
                        Den = "Nidoranm"
                    result = await denname(self, str(Den))
                    if result == None:
                       await ctx.send("This Pokemon cannot be found in a Den")
                    else:
                        Glr = ["Meowth", "Ponyta", "Rapidash", "Slowpoke", "Weezing", "Corsola", "Zigzagoon", "Linoone", "Darumaka", "Darmanitan", "Yamask", "Stunfisk"]
                        if Den in Glr:
                            nenl = Den
                            embed = discord.Embed(title= "Galarian "+ Den + " is in the following dens:", color=0x2962FF)
                            embed.set_thumbnail(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+nenl+".png")
                            embed.add_field(name="Sword:", value=str(result[0]), inline=False)
                            embed.add_field(name="Sword HA:", value=str(result[2]), inline=False)
                            embed.add_field(name="Shield:", value=str(result[1]), inline=False)
                            embed.add_field(name="Shield HA:", value=str(result[3]), inline=False)
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            candelete = await get_delete(self, ctx)
                            if candelete == "True":
                                await ctx.message.delete()
                            await ctx.send(embed=embed)
                        elif Den not in Glr:
                            if Den == "Nidoranf":
                                Den1 = "Nidoranf"
                                embed = discord.Embed(title= "Nidoran\U00002640 is in the following dens:", color=0x2962FF)
                                embed.set_thumbnail(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Den1+".png")
                                embed.add_field(name="Sword:", value=str(result[0]), inline=False)
                                embed.add_field(name="Sword HA:", value=str(result[2]), inline=False)
                                embed.add_field(name="Shield:", value=str(result[1]), inline=False)
                                embed.add_field(name="Shield HA:", value=str(result[3]), inline=False)
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                candelete = await get_delete(self, ctx)
                                if candelete == "True":
                                    await ctx.message.delete()
                                await ctx.send(embed=embed)
                            elif Den == "Nidoranm":
                                Den1 = "Nidoranm"
                                embed = discord.Embed(title= "Nidoran\U00002642 is in the following dens:", color=0x2962FF)
                                embed.set_thumbnail(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Den1+".png")
                                embed.add_field(name="Sword:", value=str(result[0]), inline=False)
                                embed.add_field(name="Sword HA:", value=str(result[2]), inline=False)
                                embed.add_field(name="Shield:", value=str(result[1]), inline=False)
                                embed.add_field(name="Shield HA:", value=str(result[3]), inline=False)
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                candelete = await get_delete(self, ctx)
                                if candelete == "True":
                                    await ctx.message.delete()
                                await ctx.send(embed=embed)
                            elif Den == "Chansey":
                                Den1 = Den
                                embed = discord.Embed(title= Den + " is in the following dens:", color=0x2962FF)
                                embed.set_thumbnail(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Den1+".png")
                                embed.add_field(name="Sword:", value=str(result[0]), inline=False)
                                embed.add_field(name="Sword (cont.):", value=str(result[4]), inline=False)
                                embed.add_field(name="Sword HA", value=str(result[2]), inline=False)
                                embed.add_field(name="Shield:", value=str(result[1]), inline=False)
                                embed.add_field(name="Shield (cont.):", value=str(result[5]), inline=False)
                                embed.add_field(name="Shield HA", value=str(result[3]), inline=False)
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                candelete = await get_delete(self, ctx)
                                if candelete == "True":
                                    await ctx.message.delete()
                                await ctx.send(embed=embed)
                            elif Den == "Audino":
                                Den1 = Den
                                embed = discord.Embed(title= Den + " is in the following dens:", color=0x2962FF)
                                embed.set_thumbnail(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Den1+".png")
                                embed.add_field(name="Sword:", value=str(result[0]), inline=False)
                                embed.add_field(name="Sword HA:", value=str(result[2]), inline=False)
                                embed.add_field(name="Sword HA (cont.)", value=str(result[6]), inline=False)
                                embed.add_field(name="Shield:", value=str(result[1]), inline=False)
                                embed.add_field(name="Shield HA:", value=str(result[3]), inline=False)
                                embed.add_field(name="Shield HA (cont.)", value=str(result[7]), inline=False)
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                candelete = await get_delete(self, ctx)
                                if candelete == "True":
                                    await ctx.message.delete()
                                await ctx.send(embed=embed)
                            elif Den == "Delibird":
                                Den1 = Den
                                embed = discord.Embed(title= Den + " is in the following dens:", color=0x2962FF)
                                embed.set_thumbnail(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Den1+".png")
                                embed.add_field(name="Sword:", value=str(result[0]), inline=False)
                                embed.add_field(name="Sword HA:", value=str(result[2]), inline=False)
                                embed.add_field(name="Sword HA (cont.)", value=str(result[6]), inline=False)
                                embed.add_field(name="Shield:", value=str(result[1]), inline=False)
                                embed.add_field(name="Shield HA:", value=str(result[3]), inline=False)
                                embed.add_field(name="Shield HA (cont.)", value=str(result[7]), inline=False)
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                candelete = await get_delete(self, ctx)
                                if candelete == "True":
                                    await ctx.message.delete()
                                await ctx.send(embed=embed)
                            else:
                                Den1 = Den
                                embed = discord.Embed(title= Den + " is in the following dens:", color=0x2962FF)
                                embed.set_thumbnail(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Den1+".png")
                                embed.add_field(name="Sword:", value=str(result[0]), inline=False)
                                embed.add_field(name="Sword HA:", value=str(result[2]), inline=False)
                                embed.add_field(name="Shield:", value=str(result[1]), inline=False)
                                embed.add_field(name="Shield HA:", value=str(result[3]), inline=False)
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                candelete = await get_delete(self, ctx)
                                if candelete == "True":
                                    await ctx.message.delete()
                                await ctx.send(embed=embed)

    @commands.command(aliases=["s"])
    async def sprite(self, ctx):
        responce = str(ctx.message.content)
        isshiny = "Normal"
        shinycheck = ""
        content = responce.split()
        if content[1].lower() == "alolan":
            if content[2].endswith("*"):
                isshiny = "Shiny"
                shinycheck = "Shiny"
                content[2] = content[2].replace("*", "")
            GaName = string.capwords(content[2])
            Listofalola = ["Rattata","Raticate","Raichu","Sandshrew","Sandslash","Vulpix","Ninetails","Diglett","Dugtrio","Meowth","Persian","Geodude","Graveler",
                           "Golem","Grimer","Muk","Exeggutor","Marowak"]
            if GaName in Listofalola:
                embed = discord.Embed(title= str(shinycheck) + " Alolan " + GaName , description="", color=0x2962FF)
                embed.set_image(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Alolan/"+str(isshiny)+"/"+GaName+".png?size=200")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                   await ctx.message.delete()
                await ctx.send(embed=embed)
            else:
                await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
        elif content[1].lower() == "galarian" or content[1].lower() == "galar":
            if content[2].endswith("*"):
                isshiny = "Shiny"
                shinycheck = "Shiny"
                content[2] = content[2].replace("*", "")
            GlName = string.capwords(content[2])
            GlmName = string.capwords(content[2]) + " Mime"
            Listofgalar = ["Meowth","Ponyta","Rapidash","Slowpoke","Slowbro","Farfetch'd","Farfetch’d","Weezing","Mr Mime","Articuno","Zapdos","Moltres","Slowking","Corsola","Zigzagoon","Linoone","Darumaka","Darmanitan", "Zen","Yamask","Stunfisk"]
            if GlName in Listofgalar or GlmName in Listofgalar:
                if GlName == "Mr" or GlName == "Mr.":
                    if content[3].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[3] = content[3].replace("*", "")
                    RGName = "Mrmime"
                    embed = discord.Embed(title= str(shinycheck) + " Galarian " + GlmName, description="", color=0x2962FF)
                    embed.set_image(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+RGName+".png?size=200")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                       await ctx.message.delete()
                    await ctx.send(embed=embed)
                else:
                    if GlName == "Farfetch’d":
                        GlName = "Farfetch'd"
                    if GlName == "Zen":
                        try:
                            content[3]
                        except:
                            await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                        else:
                            if content[3].endswith("*"):
                                isshiny = "Shiny"
                                shinycheck = "Shiny"
                                content[3] = content[3].replace("*", "")
                            if content[3].capitalize() == "Darmanitan":
                                GzzName = "Darmanitanzen"
                                embed = discord.Embed(title= str(shinycheck) + " Galarian Darmanitan Zen Mode", description="", color=0x2962FF)
                                embed.set_image(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+GzzName+".png?size=200")
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                await ctx.send(embed=embed)
                            else:
                                await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                    elif GlName == "Farfetch'd":
                        embed = discord.Embed(title= str(shinycheck) + " Galarian " + GlName, description="", color=0x2962FF)
                        embed.set_image(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/Farfetchd.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(title= str(shinycheck) + " Galarian " + GlName, description="", color=0x2962FF)
                        embed.set_image(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Galarian/"+str(isshiny)+"/"+GlName+".png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
            else:
                await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
        elif content[1].lower() == "gmax":
            if content[2].endswith("*"):
                isshiny = "Shiny"
                shinycheck = "Shiny"
                content[2] = content[2].replace("*", "")
            GName = string.capwords(content[2])
            Listofgmax = ["Venusaur","Charizard","Blastoise","Butterfree","Pikachu","Meowth","Machamp","Gengar","Kingler","Lapras","Eevee","Snorlax","Garbodor",
                          "Melmetal","Rillaboom","Cinderace","Inteleon","Corviknight","Orbeetle","Drednaw","Coalossal","Flapple","Appletun","Sandaconda","Toxtricity",
                          "Centiskorch", "Hatterene","Grimmsnarl","Alcremie","Copperajah","Duraludon","Urshifu"]
            if GName in Listofgmax:
                if GName == "Urshifu":
                    embed = discord.Embed(title= str(shinycheck)+ " Gmax " + GName + " (Single Strike Style)", description="", color=0x2962FF)
                    embed.set_image(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Gmax/"+str(isshiny)+"/"+GName+".png")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                       await ctx.message.delete()
                    await ctx.send(embed=embed)
                    GZame = "Rurshifu"
                    embed = discord.Embed(title= str(shinycheck)+ " Gmax " + GZame + " (Rapid Strike Style)", description="", color=0x2962FF)
                    embed.set_image(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Gmax/"+str(isshiny)+"/"+GZame+".png")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title= str(shinycheck)+ " Gmax " + GName, description="", color=0x2962FF)
                    embed.set_image(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Gmax/"+str(isshiny)+"/"+GName+".png")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                       await ctx.message.delete()
                    await ctx.send(embed=embed)
            else:
                await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
        elif content[1].lower() == "mega":
            if content[2].endswith("*"):
                isshiny = "Shiny"
                shinycheck = "Shiny"
                content[2] = content[2].replace("*", "")
            MName = string.capwords(content[2])
            Listofgmax = ["Venusaur","Charizard","Blastoise","Beedrill","Pidgeot","Alakazam","Slowbro","Gengar","Kangaskhan","Pinsir","Gyarados","Aerodactyl","Mewtwo","Ampharos","Steelix","Scizor","Heracross","Houndoom","Tyranitar","Sceptile","Blaziken","Swampert","Gardevoir","Sableye","Mawile","Aggron","Medicham","Manectric","Sharpedo","Camerupt","Altaria","Banette","Absol","Glalie","Salamence","Metagross","Latias","Latios","Rayquaza","Lopunny","Garchomp","Lucario","Abomasnow","Gallade","Audino","Diancie"]
            if MName in Listofgmax:
                if MName == "Charizard":
                    try:
                        content[3]
                    except:
                        await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                    else:
                        if content[3].capitalize() == "X":
                            embed = discord.Embed(title=str(shinycheck)+" Mega " + MName + " X", description="", color=0x2962FF)
                            embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/Xcharizard.png")
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            candelete = await get_delete(self, ctx)
                            if candelete == "True":
                               await ctx.message.delete()
                            await ctx.send(embed=embed)
                        elif content[3].capitalize() == "Y":
                            embed = discord.Embed(title=str(shinycheck)+" Mega " + MName + " Y", description="", color=0x2962FF)
                            embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/Ycharizard.png")
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            candelete = await get_delete(self, ctx)
                            if candelete == "True":
                               await ctx.message.delete()
                            await ctx.send(embed=embed)
                        else:
                            await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                elif MName == "Mewtwo":
                    try:
                        content[3]
                    except:
                        await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                    else:
                        if content[3].capitalize() == "X":
                            embed = discord.Embed(title=str(shinycheck)+" Mega " + MName + " X", description="", color=0x2962FF)
                            embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/Xmewtwo.png")
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            candelete = await get_delete(self, ctx)
                            if candelete == "True":
                               await ctx.message.delete()
                            await ctx.send(embed=embed)
                        elif content[3].capitalize() == "Y":
                            embed = discord.Embed(title=str(shinycheck)+" Mega " + MName + " Y", description="", color=0x2962FF)
                            embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/Ymewtwo.png")
                            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                            candelete = await get_delete(self, ctx)
                            if candelete == "True":
                               await ctx.message.delete()
                            await ctx.send(embed=embed)
                        else:
                            await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    embed = discord.Embed(title=str(shinycheck)+" Mega " + MName, description="", color=0x2962FF)
                    embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/Mega/"+str(isshiny)+"/"+MName+".png")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                       await ctx.message.delete()
                    await ctx.send(embed=embed)
            else:
                await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
        else:
            if content[1].endswith("*"):
                isshiny = "Shiny"
                shinycheck = "Shiny"
                content[1] = content[1].replace("*", "")
            Name = content[1].capitalize()
            if Name == "Tapu":
                Tapu = ["koko","lele","bulu","fini"]
                if content[2].endswith("*"):
                    isshiny = "Shiny"
                    shinycheck = "Shiny"
                    content[2] = content[2].replace("*", "")
                if content[2].lower() in Tapu:
                    Name = Name + " " +string.capwords(content[2])
            if Name == "Mr.":
                Name = "Mr"
            if Name == "Mr":
                if content[2].endswith("*"):
                    isshiny = "Shiny"
                    shinycheck = "Shiny"
                    content[2] = content[2].replace("*", "")
                FLCap = string.capwords(content[1])
                FLLCap = string.capwords(content[2])
                RName = content[1] + content[2].lower()
                if RName =="Mr.mime" or RName == "mr.mime":
                    RName = "Mrmime"
                if RName == "Mr.rime" or RName == "mr.rime":
                    RName = "Mrrime"
                LName = FLCap+content[2].lower()
                if LName == "Mrmime" or LName =="Mr.mime":
                    LName = "Mrmime"
                if LName == "Mrrime" or LName =="Mr.rime":
                    LName = "Mrrime"
                RealN= FLCap+". "+FLLCap
                if RealN == "Mr.. Mime":
                    RealN = "Mr. Mime"
                if RealN == "Mr.. Rime":
                    RealN = "Mr. Rime"
            if Name == "Sirfetch’d":
                Name = "Sirfetch'd"
            if Name == "Farfetch’d":
                Name = "Farfetch'd"
            if Name == "Porygon-z":
                Name = "Porygon-Z"
            if Name == "Mr":
                embed = discord.Embed(title= str(shinycheck)+ " " + RealN, description="", color=0x2962FF)
                embed.set_image(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+LName+".png")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                   await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Mime":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Jr" or content[2].capitalize() == "Jr.":
                        TName = "Mimejr"
                        embed = discord.Embed(title= str(shinycheck)+ " Mime Jr.", description="", color=0x2962FF)
                        embed.set_image(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+TName+".png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Type:":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Null":
                        TName = "Type-null"
                        embed = discord.Embed(title= str(shinycheck)+ " Type: Null", description="", color=0x2962FF)
                        embed.set_image(url= "https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+TName+".png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name.startswith("Nidoran\U00002640"):
                embed = discord.Embed(title=str(shinycheck)+ " Nidoran♀️ ", description="", color=0x2962FF)
                embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Nidoranf.png")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                   await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name.startswith("Nidoran\U00002642"):
                embed = discord.Embed(title=str(shinycheck)+ " Nidoran♂️ ", description="", color=0x2962FF)
                embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Nidoranm.png")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                   await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Sunny":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Castform":
                        embed = discord.Embed(title=str(shinycheck)+" Sunny Castform", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Sunnycastform.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Rainy":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Castform":
                        embed = discord.Embed(title=str(shinycheck)+" Rainy Castform", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Rainycastform.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Snowy":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Castform":
                        embed = discord.Embed(title=str(shinycheck)+" Snowy Castform", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Snowycastform.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Primal":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Kyogre":
                        embed = discord.Embed(title=str(shinycheck)+" Primal Kyogre", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Kyogreprimal.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    elif content[2].capitalize() == "Groudon":
                        embed = discord.Embed(title=str(shinycheck)+" Primal Groudon", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Groudonprimal.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Attack":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Deoxys":
                        embed = discord.Embed(title=str(shinycheck)+" Attack Form Deoxys", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Adeoxys.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Defense":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Deoxys":
                        embed = discord.Embed(title=str(shinycheck)+" Defense Fork Deoxys", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Ddeoxys.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Speed":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Deoxys":
                        embed = discord.Embed(title=str(shinycheck)+" Speed Form Deoxys", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Sdeoxys.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Burmy": #random image of the three forms via random
                embed = discord.Embed(title=str(shinycheck)+" Burmy", description="", color=0x2962FF)
                embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Burmy.png")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                   await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Wormadam": #random image of the three forms via random
                embed = discord.Embed(title=str(shinycheck)+" Wormadam", description="", color=0x2962FF)
                embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Wormadam.png")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                   await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Sunshine":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Cherrim":
                        embed = discord.Embed(title=str(shinycheck)+ " Cherrim Sunshine Form", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Scherrim.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Shellos":
                embed = discord.Embed(title=str(shinycheck)+" Shellos", description="", color=0x2962FF)
                embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Shellos.png")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                   await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Gastrodon":
                embed = discord.Embed(title=str(shinycheck)+" Gastrodon", description="", color=0x2962FF)
                embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Gastrodon.png")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                   await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Heat":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Rotom":
                        embed = discord.Embed(title=str(shinycheck)+" Heat Rotom", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Hrotom.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Wash":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Rotom":
                        embed = discord.Embed(title=str(shinycheck)+" Wash Rotom", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Wrotom.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Frost":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Rotom":
                        embed = discord.Embed(title=str(shinycheck)+" Frost Rotom", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Frotom.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Fan":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Rotom":
                        embed = discord.Embed(title=str(shinycheck)+" Fan Rotom", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Fanrotom.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Mow":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Rotom":
                        embed = discord.Embed(title=str(shinycheck)+" Mow Rotom", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Mrotom.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Origin":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Giratina":
                        embed = discord.Embed(title=str(shinycheck)+" Origin Forme Giratina", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Ogiratina.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Sky":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Shaymin":
                        embed = discord.Embed(title=str(shinycheck)+" Sky Form Shamin", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Sshaymin.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Zen":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Darmanitan":
                        embed = discord.Embed(title=str(shinycheck)+" Zen Mode Darmanitan", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Darmanitanzen.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Basculin":
                embed = discord.Embed(title=str(shinycheck)+" Basculin", description="", color=0x2962FF)
                embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Basculin.png")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                   await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Deerling": #random image of the four forms via random
                embed = discord.Embed(title=str(shinycheck)+" Deerling", description="", color=0x2962FF)
                embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Deerling.png")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                   await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Sawsbuck": #random image of the four forms via random
                embed = discord.Embed(title=str(shinycheck)+" Sawsbuck", description="", color=0x2962FF)
                embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Sawsbuck.png")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                   await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Therian":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2] == "Tornadus":
                        embed = discord.Embed(title=str(shinycheck)+ " Therian Tornadus", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Ttornadus.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    elif content[2] == "Thundurus":
                        embed = discord.Embed(title=str(shinycheck)+" Therian Thundurus", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Tthundurus.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    elif content[2] == "Landorus":
                        embed = discord.Embed(title=str(shinycheck)+" Therian Landorus", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Tlandorus.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Black":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Kyreum":
                        embed = discord.Embed(title=str(shinycheck)+" Black Kyreum", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Blackkyurem.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "White":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Kyreum":
                        embed = discord.Embed(title=str(shinycheck)+" White Kyreum", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Whitekyurem.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Resolute":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Keldeo":
                        embed = discord.Embed(title=str(shinycheck)+" Keldeo Resolute Form", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Rkeldeo.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Pirouette":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Meloetta":
                        embed = discord.Embed(title=str(shinycheck)+" Meloetta Pirouette Form", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Pmeloetta.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Ash":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Greninja":
                        embed = discord.Embed(title=str(shinycheck)+ " Ash-Geninja", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Ashgreninja.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Blade":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Aegislash":
                        embed = discord.Embed(title=str(shinycheck)+" Blade Form", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Baegislash.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "10%":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Zygarde":
                        embed = discord.Embed(title=str(shinycheck)+" 10% Zygarde", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Tzygarde.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Complete":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Zygarde":
                        embed = discord.Embed(title=str(shinycheck)+" Zygarde Complete Form", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Czygarde.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Unbound":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Hoopa":
                        embed = discord.Embed(title=str(shinycheck)+" Unbound Hoopa", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Uhoopa.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
            elif Name == "Balie":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Oricorio":
                        embed = discord.Embed(title=str(shinycheck)+" Oricorio Balie Style", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Boricorio.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Pom-Pom":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Oricorio":
                        embed = discord.Embed(title=str(shinycheck)+" Oricorio Pom-Pom Style", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Poricorio.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Pa'u":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Oricorio":
                        embed = discord.Embed(title=str(shinycheck)+" Oricorio Pa'u Style", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Paoricorio.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Sensu":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Oricorio":
                        embed = discord.Embed(title=str(shinycheck)+" Oricorio Sensu Style", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Soricorio.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Dusk":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Lycanroc":
                        embed = discord.Embed(title=str(shinycheck)+" Dusk Lycanroc", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Dlycanroc")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    elif content[2].capitalize() == "Mane":
                        try:
                            content[3]
                        except:
                            await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
                        else:
                            if content[3].endswith("*"):
                                isshiny = "Shiny"
                                shinycheck = "Shiny"
                                content[3] = content[3].replace("*", "")
                            if content[3].capitalize() == "Necrozma":
                                embed = discord.Embed(title=str(shinycheck)+" Dusk Mane Necrozma", description="", color=0x2962FF)
                                embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Dmnecrozma.png")
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                candelete = await get_delete(self, ctx)
                                if candelete == "True":
                                   await ctx.message.delete()
                                await ctx.send(embed=embed)
                            else:
                                await ctx.send("The Pokemon with the name "+str(Name)+" "+content[2]+" "+content[3]+" does not exist!")
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Midnight":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Lycanroc":
                        embed = discord.Embed(title=str(shinycheck)+" Midnight Lycanroc", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Mlycanroc.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Dawn":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].capitalize() == "Wings":
                        try:
                            content[3]
                        except:
                            await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                        else:
                            if content[3].endswith("*"):
                                isshiny = "Shiny"
                                shinycheck = "Shiny"
                                content[3] = content[3].replace("*", "")
                            if content[3].capitalize() == "Necrozma":
                                embed = discord.Embed(title=str(shinycheck)+" Dawn Wings Necrozma", description="", color=0x2962FF)
                                embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Dwnecrozma.png")
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                candelete = await get_delete(self, ctx)
                                if candelete == "True":
                                   await ctx.message.delete()
                                await ctx.send(embed=embed)
                            else:
                                await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+" "+content[3].capitalize()+"' does not exist!")
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "School":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Wishiwashi":
                        embed = discord.Embed(title=str(shinycheck)+" Wishiwashi School Form", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Swishiwashi.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Ultra":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Necrozma":
                        embed = discord.Embed(title=str(shinycheck)+" Ultra Necrozma", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Unecrozma.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Toxtricity": #random image of the two forms via random?
                embed = discord.Embed(title=str(shinycheck)+" Toxtricirty Amp'd/Low-Key", description="", color=0x2962FF)
                embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Toxtricity.png")
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                   await ctx.message.delete()
                await ctx.send(embed=embed)
            elif Name == "Noice":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                    if content[2].capitalize() == "Eiscue":
                        embed = discord.Embed(title=str(shinycheck)+" Eiscue Noice Form", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Neiscue.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Crowned":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2] == "Zacian":
                        embed = discord.Embed(title=str(shinycheck)+ "Crowned Attack Zacian", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Czacian.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    elif content[2] == "Zamazenta":
                        embed = discord.Embed(title=str(shinycheck)+" Crowned Shield Zamazenta", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Czamazenta.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Urshifu":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].lower == "rapid":
                        embed = discord.Embed(title=str(shinycheck)+" Urshifu Rapid Strike Style", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Rurshifu.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(title=str(shinycheck)+" Urishifu Single Strike Style", description="", color=0x2962FF)
                        embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Urishifu.png")
                        embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                        candelete = await get_delete(self, ctx)
                        if candelete == "True":
                           await ctx.message.delete()
                        await ctx.send(embed=embed)
            elif Name == "Dada":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].endswith("*"):
                        isshiny = "Shiny"
                        shinycheck = "Shiny"
                        content[2] = content[2].replace("*", "")
                if content[2].capitalize() == "Zarude":
                    embed = discord.Embed(title=str(shinycheck)+ "Dada Zarude", description="", color=0x2962FF)
                    embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Dzarude.png")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                       await ctx.message.delete()
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
            elif Name == "Shadow":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].capitalize() == "Rider":
                        try:
                            content[3]
                        except:
                            await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
                        else:
                            if content[3].endswith("*"):
                                isshiny = "Shiny"
                                shinycheck = "Shiny"
                                content[3] = content[2].replace("*", "")
                            if content[3].capitalize() == "Calyrex":
                                embed = discord.Embed(title=str(shinycheck)+" Shadow Rider Calyrex", description="", color=0x2962FF)
                                embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Calyrexshadowrider.png")
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                candelete = await get_delete(self, ctx)
                                if candelete == "True":
                                   await ctx.message.delete()
                                await ctx.send(embed=embed)
                            else:
                                await ctx.send("The Pokemon with the name "+str(Name)+" "+content[2]+" "+content[3]+" does not exist!")
            elif Name == "Ice":
                try:
                    content[2]
                except:
                    await ctx.send("The Pokemon with the name "+str(Name)+" does not exist!")
                else:
                    if content[2].capitalize() == "Rider":
                        try:
                            content[3]
                        except:
                            await ctx.send("The Pokemon with the name '"+str(Name)+" "+content[2].capitalize()+"' does not exist!")
                        else:
                            if content[3].endswith("*"):
                                isshiny = "Shiny"
                                shinycheck = "Shiny"
                                content[3] = content[2].replace("*", "")
                            if content[3].capitalize() == "Calyrex":
                                embed = discord.Embed(title=str(shinycheck)+" Ice Rider Calyrex", description="", color=0x2962FF)
                                embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/Calyrexicerider.png")
                                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                                candelete = await get_delete(self, ctx)
                                if candelete == "True":
                                   await ctx.message.delete()
                                await ctx.send(embed=embed)
                            else:
                                await ctx.send("The Pokemon with the name "+str(Name)+" "+content[2]+" "+content[3]+" does not exist!")
            else:
                insidelist = await namecheck(self, Name)
                if insidelist != None:
                    embed = discord.Embed(title= str(shinycheck)+" "+ Name , description="", color=0x2962FF)
                    if Name == "Tapu Koko":
                        Name = "Tapu_Koko"
                    if Name == "Tapu Lele":
                        Name = "Tapu_Lele"
                    if Name == "Tapu Bulu":
                        Name = "Tapu_Bulu"
                    if Name == "Tapu Fini":
                        Name = "Tapu_Fini"
                    embed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/PokemonImages/"+str(isshiny)+"/"+Name+".png")
                    embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    candelete = await get_delete(self, ctx)
                    if candelete == "True":
                       await ctx.message.delete()
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("The Pokemon with the name '"+str(Name)+"` does not exist!")

    @commands.command(aliases=["m"])
    async def move(self, ctx):
        responce = str(ctx.message.content)
        content = responce.split()
        try:
            content[2]
        except:
            result = await movedatagrab(self, content[1].title())
            #return (effect, description, movetype, catergory, power, accuracry, powerpoints, priority, gmaxpower,flag1,flag2,flag3,flag4,flag5,flag6,imageurl)
            
            if result[9] == "TRUE":
                flag1 = "Makes Contact"
            if result[9] == "FALSE":
                flag1 = "Does not make Contact"
            if result[10] == "TRUE":
                flag2 = "Affected by Protect"
            if result[10] == "FALSE":
                flag2 = "Not affected by Protect"
            if result[11] == "TRUE":
                flag3 = "Affected by Magic Coat"
            if result[11] == "FALSE":
                flag3 = "Not affected by Magic Coat"
            if result[12] == "TRUE":
                flag4 = "Affected by Snatch"
            if result[12] == "FALSE":
                flag4 = "Not affected by Snatch"
            if result[13] == "TRUE":
                flag5 = "Affected by Mirror Move"
            if result[13] == "FALSE":
                flag5 = "Not affected by Mirror Move"
            if result[14] == "TRUE":
                flag6 = "Affected by King's Rock"
            if result[14] == "FALSE":
                flag6 = "Not affected by King's Rock"
            
            if content[1].title() == "Trick-Or-Treat":
                    content[1] = "Trick-or-Treat"
            
            embed = discord.Embed(title= content[1].title(), color=0x2962FF)
            embed.add_field(name="Base Power:", value=str(result[4]), inline=True)
            embed.add_field(name="G-max Power:", value=str(result[8]), inline=True)
            embed.add_field(name="Accuracy:", value=str(result[5]), inline=True)
            embed.add_field(name="Category", value=str(result[3]), inline=True)
            embed.add_field(name="Type:", value=str(result[2]), inline=True)
            embed.add_field(name="Power Points (PP)", value=str(result[6]), inline=True)
            embed.add_field(name="Priority:", value=str(result[7]), inline=True)
            embed.add_field(name="In-Game Desciption:", value=str(result[1]), inline=False)
            embed.add_field(name="Technical Description:", value=str(result[0]), inline=False)
            embed.add_field(name="Other Properties:", value=flag1+"\n"+flag2+"\n"+flag3+"\n"+flag4+"\n"+flag5+"\n"+flag6, inline=False)
            embed.set_image(url=result[15])
            embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
            candelete = await get_delete(self, ctx)
            if candelete == "True":
               await ctx.message.delete()
            await ctx.send(embed=embed)
        else:
            try:
                content[3]
            except:
                twowordmove = content[1].title() + " " + content[2].title()
                result = await movedatagrab(self, twowordmove)
                #return (effect, description, movetype, catergory, power, accuracry, powerpoints, priority, gmaxpower,flag1,flag2,flag3,flag4,flag5,flag6,imageurl)
                
                if result[9] == "TRUE":
                    flag1 = "Makes Contact"
                if result[9] == "FALSE":
                    flag1 = "Does not make Contact"
                if result[10] == "TRUE":
                    flag2 = "Affected by Protect"
                if result[10] == "FALSE":
                    flag2 = "Not affected by Protect"
                if result[11] == "TRUE":
                    flag3 = "Affected by Magic Coat"
                if result[11] == "FALSE":
                    flag3 = "Not affected by Magic Coat"
                if result[12] == "TRUE":
                    flag4 = "Affected by Snatch"
                if result[12] == "FALSE":
                    flag4 = "Not affected by Snatch"
                if result[13] == "TRUE":
                    flag5 = "Affected by Mirror Move"
                if result[13] == "FALSE":
                    flag5 = "Not affected by Mirror Move"
                if result[14] == "TRUE":
                    flag6 = "Affected by King's Rock"
                if result[14] == "FALSE":
                    flag6 = "Not affected by King's Rock"
                
                if twowordmove == "King'S Sheild":
                    twowordmove = "King's Shield"
                if twowordmove == "Land'S Wrath":
                    twowordmove = "Land's Wrath"
                
                embed = discord.Embed(title= twowordmove, color=0x2962FF)
                embed.add_field(name="Base Power:", value=str(result[4]), inline=True)
                embed.add_field(name="G-max Power:", value=str(result[8]), inline=True)
                embed.add_field(name="Accuracy:", value=str(result[5]), inline=True)
                embed.add_field(name="Category", value=str(result[3]), inline=True)
                embed.add_field(name="Type:", value=str(result[2]), inline=True)
                embed.add_field(name="Power Points (PP)", value=str(result[6]), inline=True)
                embed.add_field(name="Priority:", value=str(result[7]), inline=True)
                embed.add_field(name="In-Game Desciption:", value=str(result[1]), inline=False)
                embed.add_field(name="Technical Description:", value=str(result[0]), inline=False)
                embed.add_field(name="Other Properties:", value=flag1+"\n"+flag2+"\n"+flag3+"\n"+flag4+"\n"+flag5+"\n"+flag6, inline=False)
                embed.set_image(url=result[15])
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                   await ctx.message.delete()
                await ctx.send(embed=embed)
            else:
                threewordmove = content[1].title() + " " + content[2].title() + " " + content[3].title()
                if threewordmove == "Light That Burns":
                    threewordmove = "Light That Burns the Sky"
                result = await movedatagrab(self, threewordmove)
                #return (effect, description, movetype, catergory, power, accuracry, powerpoints, priority, gmaxpower,flag1,flag2,flag3,flag4,flag5,flag6,imageurl)
                
                if result[9] == "TRUE":
                    flag1 = "Makes Contact"
                if result[9] == "FALSE":
                    flag1 = "Does not make Contact"
                if result[10] == "TRUE":
                    flag2 = "Affected by Protect"
                if result[10] == "FALSE":
                    flag2 = "Not affected by Protect"
                if result[11] == "TRUE":
                    flag3 = "Affected by Magic Coat"
                if result[11] == "FALSE":
                    flag3 = "Not affected by Magic Coat"
                if result[12] == "TRUE":
                    flag4 = "Affected by Snatch"
                if result[12] == "FALSE":
                    flag4 = "Not affected by Snatch"
                if result[13] == "TRUE":
                    flag5 = "Affected by Mirror Move"
                if result[13] == "FALSE":
                    flag5 = "Not affected by Mirror Move"
                if result[14] == "TRUE":
                    flag6 = "Affected by King's Rock"
                if result[14] == "FALSE":
                    flag6 = "Not affected by King's Rock"
                if threewordmove == "Let'S Snuggle Forever":
                    threewordmove = "Let's Snuggle Forever"
                embed = discord.Embed(title= threewordmove, color=0x2962FF)
                embed.add_field(name="Base Power:", value=str(result[4]), inline=True)
                embed.add_field(name="G-max Power:", value=str(result[8]), inline=True)
                embed.add_field(name="Accuracy:", value=str(result[5]), inline=True)
                embed.add_field(name="Category", value=str(result[3]), inline=True)
                embed.add_field(name="Type:", value=str(result[2]), inline=True)
                embed.add_field(name="Power Points (PP)", value=str(result[6]), inline=True)
                embed.add_field(name="Priority:", value=str(result[7]), inline=True)
                embed.add_field(name="In-Game Desciption:", value=str(result[1]), inline=False)
                embed.add_field(name="Technical Description:", value=str(result[0]), inline=False)
                embed.add_field(name="Other Properties:", value=flag1+"\n"+flag2+"\n"+flag3+"\n"+flag4+"\n"+flag5+"\n"+flag6, inline=False)
                embed.set_image(url=result[15])
                embed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                candelete = await get_delete(self, ctx)
                if candelete == "True":
                   await ctx.message.delete()
                await ctx.send(embed=embed)
            
    @commands.command()
    async def host(self, ctx):
        await ctx.message.delete()
        await ctx.send("Please check your Private messages "+ctx.message.author.mention+" , I sent you a message!~", delete_after=20)

        def check(m):
            return m.author == ctx.message.author and m.channel.type == discord.ChannelType.private

        await ctx.author.send('Would you like this to be an embed (Yes/No)?')
        await ctx.author.send("Embedded would be ideal for Single Den/Pokemon, while non-embed is ideal for Multi-dens")
        msg = await self.client.wait_for('message', check=check)
        if msg.content.lower() == "yes":
            await ctx.author.send("Are you hosting a Pokemon Only? Or a Den?")
            msg2 = await self.client.wait_for('message', check=check)
            if msg2.content.lower() == "pokemon":
                await ctx.author.send('What would you like the title to be?')
                pokemsg1 = await self.client.wait_for('message', check=check)

                await ctx.author.send("What would you like the embed's color to be to be? (Use Decimal | Example: 2712319 is Royal Blue)")
                await ctx.author.send("Use This site to help with color choices https://www.mathsisfun.com/hexadecimal-decimal-colors.html")
                pokemsg2 = await self.client.wait_for('message', check=check)

                await ctx.author.send("What is the switch name?")
                pokemsg7 = await self.client.wait_for('message', check=check)

                await ctx.author.send("What is your IGN?")
                pokemsg8 = await self.client.wait_for('message', check=check)

                await ctx.author.send("What's the Pokemon are you hosting?")
                pokemsg3 = await self.client.wait_for('message', check=check)

                await ctx.author.send("What's the Friend Code for the Host?")
                pokemsg4 = await self.client.wait_for('message', check=check)

                await ctx.author.send("What's The Room Code if any (If None type None)")
                pokemsg5 = await self.client.wait_for('message', check=check)

                await ctx.author.send("What information would you like about hosting the pokemon to have? (NOTE: Limited to 1024 characters)")
                pokemsg6 = await self.client.wait_for('message', check=check)

                pokeembed = discord.Embed(title=""+str(pokemsg1.content), description="hosted by "+ str(ctx.author.mention), color=int(pokemsg2.content)) #name="", value="", inline=False
                pokeembed.set_thumbnail(url=ctx.author.avatar_url)
                pokeembed.add_field(name="Pokemon:", value=str(pokemsg3.content), inline=True)
                pokeembed.add_field(name="Host Friend Code:", value=str(pokemsg4.content),inline=True)
                pokeembed.add_field(name="Room Code:", value=str(pokemsg5.content),inline=True)
                pokeembed.add_field(name="Switch Name:", value=str(pokemsg7.content),inline=True)
                pokeembed.add_field(name="IGN Name:", value=str(pokemsg8.content),inline=True)
                pokeembed.add_field(name="Information:", value=str(pokemsg6.content), inline=False)
                pokeembed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                hostchannel = await guildhostchannel(self, ctx)
                if hostchannel == "None":
                    await ctx.author.send("Please message your server admin to setup a hosting channel for me and then once that is setup come back to me to setup without issues")
                else:
                    hoststrremove1 = hostchannel.replace('<#', '')
                    hoststrremove2 = hoststrremove1.replace('>', '')
                    hostsendchannel = hoststrremove2
                    channelsend = self.client.get_channel(int(hostsendchannel))
                    hosting = await channelsend.send(ctx.author.mention + "'s Host",embed = pokeembed)
                    await hosting.add_reaction('❌')

                    def check(reaction, user):
                        return user == ctx.message.author and str(reaction.emoji) ==  '❌' and ctx.author == ctx.message.author

                    reaction, user = await self.client.wait_for('reaction_add', check=check)

                    if reaction.emoji == '❌':
                        await hosting.delete()

            elif msg2.content.lower() == "den":
                await ctx.author.send('What would you like the title to be?')
                pokemsg1 = await self.client.wait_for('message', check=check)

                await ctx.author.send("What would you like the embed's color to be to be? (Use Decimal | Example: 2712319 is Royal Blue)")
                await ctx.author.send("Use This site to help with color choices https://www.mathsisfun.com/hexadecimal-decimal-colors.html")
                pokemsg2 = await self.client.wait_for('message', check=check)

                await ctx.author.send("What is the switch name?")
                pokemsg7 = await self.client.wait_for('message', check=check)

                await ctx.author.send("What is your IGN?")
                pokemsg8 = await self.client.wait_for('message', check=check)

                await ctx.author.send("What Den are you hosting?")
                pokemsg3 = await self.client.wait_for('message', check=check)

                await ctx.author.send("What's the Friend Code for the Host?")
                pokemsg4 = await self.client.wait_for('message', check=check)

                await ctx.author.send("What's The Room Code if any (If None type None)")
                pokemsg5 = await self.client.wait_for('message', check=check)

                await ctx.author.send("What information would you like about hosting the den to have? (NOTE: Limited to 1024 characters)")
                pokemsg6 = await self.client.wait_for('message', check=check)

                pokeembed = discord.Embed(title=""+str(pokemsg1.content), description="hosted by "+ str(ctx.author.mention), color=int(pokemsg2.content)) #name="", value="", inline=False
                pokeembed.set_thumbnail(url=ctx.author.avatar_url)
                pokeembed.add_field(name="Den #:", value=str(pokemsg3.content), inline=True)
                if pokemsg3.content.isdigit() and int(pokemsg3.content) <= 197 and int(pokemsg3.content) > 0:
                    pokeembed.set_image(url="https://raw.githubusercontent.com/Sollisnexus/Nexus-Z/master/Dens/den"+str(pokemsg3.content)+".png")
                pokeembed.add_field(name="Host Friend Code:", value=str(pokemsg4.content),inline=True)
                pokeembed.add_field(name="Room Code:", value=str(pokemsg5.content),inline=True)
                pokeembed.add_field(name="Switch Name:", value=str(pokemsg7.content),inline=True)
                pokeembed.add_field(name="IGN Name:", value=str(pokemsg8.content),inline=True)
                pokeembed.add_field(name="Information:", value=str(pokemsg6.content), inline=False)
                pokeembed.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                hostchannel = await guildhostchannel(self, ctx)
                if hostchannel == "None":
                    await ctx.author.send("Please message your server admin to setup a hosting channel for me and then once that is setup come back to me to setup without issues")
                else:
                    hoststrremove1 = hostchannel.replace('<#', '')
                    hoststrremove2 = hoststrremove1.replace('>', '')
                    hostsendchannel = hoststrremove2
                    channelsend = self.client.get_channel(int(hostsendchannel))
                    hosting = await channelsend.send(ctx.author.mention + "'s Host",embed = pokeembed)
                    await hosting.add_reaction('❌')

                    def check(reaction, user):
                        return user == ctx.message.author and str(reaction.emoji) ==  '❌' and ctx.author == ctx.message.author

                    reaction, user = await self.client.wait_for('reaction_add', check=check)

                    if reaction.emoji == '❌':
                        await hosting.delete()

            else:
                await ctx.author.send("I was looking for Pokemon or Den, please redo this command to try again")

        elif msg.content.lower() == "no":
            hostchannel = await guildhostchannel(self, ctx)
            if hostchannel == "None":
                await ctx.author.send("Please message your server admin to setup a hosting channel for me and then once that is setup come back to me to setup without issues")
            else:
                hoststrremove1 = hostchannel.replace('<#', '')
                hoststrremove2 = hoststrremove1.replace('>', '')
                hostsendchannel = hoststrremove2
                channelsend = self.client.get_channel(int(hostsendchannel))
                await ctx.author.send("Please enter your den information so that it'll be posted in "+str(hostchannel)+"!~")
                msg3 = await self.client.wait_for('message', check=check)
                multihost = await channelsend.send(ctx.author.mention + "'s Host\n\n" + msg3.content)
                await multihost.add_reaction('❌')

                def check(reaction, user):
                    return user == ctx.message.author and str(reaction.emoji) ==  '❌' and ctx.author == ctx.message.author

                reaction, user = await self.client.wait_for('reaction_add', check=check)

                if reaction.emoji == '❌':
                    await multihost.delete()
        else:
            await ctx.author.send("Error... was not `yes` or `no` please redo the command to start again")


    @ball.error
    async def ball_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            print(error)
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send("Please insert the name of the Poke ball")
        elif isinstance(error, commands.TooManyArguments):
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send("Are you sure that's a Poke ball?")

    @pokedex.error
    async def pokedex_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send("Are you sure you entered the Pokemon name (with/without varient) correctly?\n\n Do '<>help pokedex' for examples if confused")

    @catch.error
    async def catch_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send("Are you sure you entered the Pokemon name (with/without varient) correctly? \n\n Do '<>help catch' for examples if confused")

    @den.error
    async def den_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            print(error)
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send("Please make sure you entered the name or a correct den value. if you did please contact my owner.\n\n Do '<>help den' for examples if confused")

    @sprite.error
    async def sprite_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            print(error)
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send("Please insert the correct name of the Pokemon you want the sprite for. \n\n Do '<>help sprite' for examples if confused")

    @move.error
    async def move_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            print(error)
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send("Please insert the correct name of the Move you want the information for. \n\n Do '<>help move' for examples if confused")
            
    @host.error
    async def host_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            print(error)
            candelete = await get_delete(self, ctx)
            if candelete == "True":
                await ctx.message.delete()
            await ctx.send("An error has occured please message Sollisnexus#3037 about this issue and he'll get back to you as soon as he can!~")


async def main(self, pokename, ballType):
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

    if pokename == "Tapu koko":
        pokename = "Tapu Koko"
    if pokename == "Tapu lele":
        pokename = "Tapu Lele"
    if pokename == "Tapu bulu":
        pokename = "Tapu Bulu"
    if pokename == "Tapu fini":
        pokename = "Tapu Fini"
    if pokename == "Farfetch'd":
        pokename = "Farfetch''d"
    if pokename == "Sirfetch'd":
        pokename = "Sirfetch''d"
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM pokedex WHERE name = '"+str(pokename)+"';"))
            row = list(prerow.values())
            types = [row[3]]
            if row[4] != "Unknown":
                types.append(row[4])
            pokeHP = int(row[5])
            basespd = int(row[10])
            catchRate = int(row[12])
            weight = float(row[19])
            Mostone = int(row[24])
            #name not in row:
            #        types = "Fire"
            #        pokeHP = 5
            #        catchRate = 0

    BasepokeHp = pokeHP
    if ballType == "Fastball":
        UB = ["Nihilego", "Buzzwole", "Pheromosa", "Xurtitree", "Celesteela", "Kartana", "Guzzlord", "Poipole", "Naganadel", "Stackataka", "Blacephalon"]
        if pokename in UB:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types, pokename)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types, pokename)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = (minRate/65536) ** 4
                finalRate2 = (maxRate/65536) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.00)
            else:
                return ballType.capitalize(), (float(round(finalRate * 100, 2))), (float(round(finalRate2 * 100, 2)))
        if basespd >= 100:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types, pokename)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types, pokename)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = (minRate/65536) ** 4
                finalRate2 = (maxRate/65536) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.00)
            else:
                return ballType.capitalize(), (float(round(finalRate * 100, 2))), (float(round(finalRate2 * 100, 2)))
        else:
                realcatchRate = catchRate
                catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, "Pokeball", types, pokename)
                catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, "Pokeball", types, pokename)
                if catch_value >= 255 or catch_value2 >= 255:
                    finalRate = 0.1
                else:
                    minRate = getCatchRate(catch_value)
                    maxRate = getCatchRate(catch_value2)

                    finalRate = (minRate/65536) ** 4
                    finalRate2 = (maxRate/65536) ** 4

                try:
                    finalRate2 * 2
                except:
                    return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.00)
                else:
                    return "Fastball", (float(round(finalRate * 100, 2))), (float(round(finalRate2 * 100, 2)))
    elif ballType == "Moonball":
        if Mostone == 1:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types, pokename)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types, pokename)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = (minRate/65536) ** 4
                finalRate2 = (maxRate/65536) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.00)
            else:
                return ballType.capitalize(), (float(round(finalRate * 100, 2))), (float(round(finalRate2 * 100, 2)))
        else:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, "Pokeball", types, pokename)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, "Pokeball", types, pokename)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = (minRate/65536) ** 4
                finalRate2 = (maxRate/65536) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.00)
            else:
                return "Moonball", (float(round(finalRate * 100, 2))), (float(round(finalRate2 * 100, 2)))
    else:
        realcatchRate = catchRate
        catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types, pokename)
        catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types, pokename)

        if catch_value >= 255 or catch_value2 >= 255:
            finalRate = 0.1
        else:
            minRate = getCatchRate(catch_value)
            maxRate = getCatchRate(catch_value2)


            finalRate = (minRate/65536) ** 4
            finalRate2 = (maxRate/65536) ** 4

        try:
            finalRate2 * 2
        except:
            return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.00)
        else:
            return ballType.capitalize(), (float(round(finalRate * 100, 2))), (float(round(finalRate2 * 100, 2))) ###

async def alolanmain(self, pokename, ballType):
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

    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM alolapokedex WHERE name = '"+str(pokename)+"';"))
            row = list(prerow.values())
            types = [row[3]]
            if row[4] != "Unknown":
                types.append(row[4])
            pokeHP = int(row[5])
            basespd = int(row[10])
            catchRate = int(row[12])
            weight = float(row[19])
            Mostone = int(row[24])
    #if name not in row:
    #        types = "Fire"
    #        pokeHP = 5
    #        catchRate = 0

    BasepokeHp = pokeHP
    if ballType == "Fastball":
        if basespd >= 100:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types, pokename)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types, pokename)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = (minRate/65536) ** 4
                finalRate2 = (maxRate/65536) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.00)
            else:
                return ballType.capitalize(), (float(round(finalRate * 100, 2))), (float(round(finalRate2 * 100, 2)))
        else:
                realcatchRate = catchRate
                catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, "Pokeball", types, pokename)
                catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, "Pokeball", types, pokename)
                if catch_value >= 255 or catch_value2 >= 255:
                    finalRate = 0.1
                else:
                    minRate = getCatchRate(catch_value)
                    maxRate = getCatchRate(catch_value2)

                    finalRate = (minRate/65536) ** 4
                    finalRate2 = (maxRate/65536) ** 4

                try:
                    finalRate2 * 2
                except:
                    return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.00)
                else:
                    return "Fastball", (float(round(finalRate * 100, 2))), (float(round(finalRate2 * 100, 2)))
    elif ballType == "Moonball":
        if Mostone == 1:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types, pokename)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types, pokename)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = (minRate/65536) ** 4
                finalRate2 = (maxRate/65536) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.00)
            else:
                return ballType.capitalize(), (float(round(finalRate * 100, 2))), (float(round(finalRate2 * 100, 2)))
        else:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, "Pokeball", types, pokename)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, "Pokeball", types, pokename)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = (minRate/65536) ** 4
                finalRate2 = (maxRate/65536) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.00)
            else:
                return "Moonball", (float(round(finalRate * 100, 2))), (float(round(finalRate2 * 100, 2)))
    else:
        realcatchRate = catchRate
        catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types, pokename)
        catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types, pokename)
        if catch_value >= 255 or catch_value2 >= 255:
            finalRate = 0.1
        else:
            minRate = getCatchRate(catch_value)
            maxRate = getCatchRate(catch_value2)

            finalRate = (minRate/65536) ** 4
            finalRate2 = (maxRate/65536) ** 4

        try:
            finalRate2 * 2
        except:
            return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.00)
        else:
            return ballType.capitalize(), (float(round(finalRate * 100, 2))), (float(round(finalRate2 * 100, 2))) ###

async def galarianmain(self, pokename, ballType):
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

    if pokename == "Farfetch'd":
        pokename = "Farfetch''d"
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM galarpokedex WHERE name = '"+str(pokename)+"';"))
            row = list(prerow.values())
            types = [row[3]]
            if row[4] != "Unknown":
                types.append(row[4])
            pokeHP = int(row[5])
            basespd = int(row[10])
            catchRate = int(row[12])
            weight = float(row[19])
            Mostone = int(row[24])
    #if name not in row:
    #        types = "Fire"
    #        pokeHP = 5
    #        catchRate = 0

    BasepokeHp = pokeHP
    if ballType == "Fastball":
        if basespd >= 100:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types, pokename)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types, pokename)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = (minRate/65536) ** 4
                finalRate2 = (maxRate/65536) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.00)
            else:
                return ballType.capitalize(), (float(round(finalRate * 100, 2))), (float(round(finalRate2 * 100, 2)))
        else:
                realcatchRate = catchRate
                catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, "Pokeball", types, pokename)
                catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, "Pokeball", types, pokename)
                if catch_value >= 255 or catch_value2 >= 255:
                    finalRate = 0.1
                else:
                    minRate = getCatchRate(catch_value)
                    maxRate = getCatchRate(catch_value2)

                    finalRate = (minRate/65536) ** 4
                    finalRate2 = (maxRate/65536) ** 4

                try:
                    finalRate2 * 2
                except:
                    return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.00)
                else:
                    return "Fastball", (float(round(finalRate * 100, 2))), (float(round(finalRate2 * 100, 2)))
    elif ballType == "Moonball":
        if Mostone == 1:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types, pokename)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types, pokename)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = (minRate/65536) ** 4
                finalRate2 = (maxRate/65536) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.00)
            else:
                return ballType.capitalize(), (float(round(finalRate * 100, 2))), (float(round(finalRate2 * 100, 2)))
        else:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, "Pokeball", types, pokename)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, "Pokeball", types, pokename)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = (minRate/65536) ** 4
                finalRate2 = (maxRate/65536) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.00)
            else:
                return "Moonball", (float(round(finalRate * 100, 2))), (float(round(finalRate2 * 100, 2)))
    else:
        realcatchRate = catchRate
        catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types, pokename)
        catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types, pokename)
        if catch_value >= 255 or catch_value2 >= 255:
            finalRate = 0.1
        else:
            minRate = getCatchRate(catch_value)
            maxRate = getCatchRate(catch_value2)

            finalRate = (minRate/65536) ** 4
            finalRate2 = (maxRate/65536) ** 4

        try:
            finalRate2 * 2
        except:
            return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.00)
        else:
            return ballType.capitalize(), (float(round(finalRate * 100, 2))), (float(round(finalRate2 * 100, 2))) ###

async def gmaxmain(self, pokename, ballType):
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

    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM pokedex WHERE name = '"+str(pokename)+"';"))
            row = list(prerow.values())
            types = [row[3]]
            if row[4] != "Unknown":
                types.append(row[4])
            pokeHP = int(row[5])
            basespd = int(row[10])
            catchRate = int(3)
            weight = float(row[19])
            Mostone = int(row[24])
    #if name not in row:
    #        types = "Fire"
    #        pokeHP = 5
    #        catchRate = 0

    BasepokeHp = pokeHP
    if ballType == "Fastball":
        if basespd >= 100:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types, pokename)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types, pokename)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = (minRate/65536) ** 4
                finalRate2 = (maxRate/65536) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.00)
            else:
                return ballType.capitalize(), (float(round(finalRate * 100, 2))), (float(round(finalRate2 * 100, 2)))
        else:
                realcatchRate = catchRate
                catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, "Pokeball", types, pokename)
                catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, "Pokeball", types, pokename)
                if catch_value >= 255 or catch_value2 >= 255:
                    finalRate = 0.1
                else:
                    minRate = getCatchRate(catch_value)
                    maxRate = getCatchRate(catch_value2)

                    finalRate = (minRate/65536) ** 4
                    finalRate2 = (maxRate/65536) ** 4

                try:
                    finalRate2 * 2
                except:
                    return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.00)
                else:
                    return "Fastball", (float(round(finalRate * 100, 2))), (float(round(finalRate2 * 100, 2)))
    elif ballType == "Moonball":
        if Mostone == 1:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types, pokename)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types, pokename)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = (minRate/65536) ** 4
                finalRate2 = (maxRate/65536) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.00)
            else:
                return ballType.capitalize(), (float(round(finalRate * 100, 2))), (float(round(finalRate2 * 100, 2)))
        else:
            realcatchRate = catchRate
            catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, "Pokeball", types, pokename)
            catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, "Pokeball", types, pokename)
            if catch_value >= 255 or catch_value2 >= 255:
                finalRate = 0.1
            else:
                minRate = getCatchRate(catch_value)
                maxRate = getCatchRate(catch_value2)

                finalRate = (minRate/65536) ** 4
                finalRate2 = (maxRate/65536) ** 4

            try:
                finalRate2 * 2
            except:
                return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.00)
            else:
                return "Moonball", (float(round(finalRate * 100, 2))), (float(round(finalRate2 * 100, 2)))
    else:
        realcatchRate = catchRate
        catch_value = getCatchValue(getHealth(BasepokeHp, 15), realcatchRate, ballType, types, pokename)
        catch_value2 = getCatchValue(getHealth(BasepokeHp, 60), realcatchRate, ballType, types, pokename)
        if catch_value >= 255 or catch_value2 >= 255:
            finalRate = 0.1
        else:
            minRate = getCatchRate(catch_value)
            maxRate = getCatchRate(catch_value2)

            finalRate = (minRate/65536) ** 4
            finalRate2 = (maxRate/65536) ** 4

        try:
            finalRate2 * 2
        except:
            return ballType.capitalize(),(float(round(finalRate * 1000, 1))), float(100.00)
        else:
            return ballType.capitalize(), (float(round(finalRate * 100, 2))), (float(round(finalRate2 * 100, 2))) ###

def ballRate(ballType, types, pokename):

    UB = ["Nihilego", "Buzzwole", "Pheromosa", "Xurtitree", "Celesteela", "Kartana", "Guzzlord", "Poipole", "Naganadel", "Stackataka", "Blacephalon"]
    Ballmult = float(0.0)
    ballDict = {'QUICKBALL': 1.0, 'POKEBALL': 1.0, 'HEAVYBALL': 1.0, 'MASTERBALL': 255.0, 'DUSKBALL': 3.0, 'ULTRABALL': 2.0, 'REPEATBALL': 3.5, 'BEASTBALL': 0.1, 'GREATBALL': 1.5, 'SPORTBALL': 1.5, 'SAFARIBALL':1.5, 'FASTBALL':4.0, 'MOONBALL':4.0}

    for key, value in ballDict.items():
        if ballType.upper() == key:
            Ballmult = value

    if ballType.upper() == 'LEVELBALL' or ballType.upper() == 'FRIENDBALL' or ballType.upper() == 'LOVEBALL' or ballType.upper() == 'LUREBALL':
        Ballmult = 1.0

    if ballType.upper() == 'TIMERBALL' or ballType.upper() == 'DIVEBALL' or ballType.upper() == 'DREAMBALL' or ballType.upper() == 'HEALBALL':
        Ballmult = 1.0

    if ballType.upper() == 'APRIBALL' or ballType.upper() == 'NESTBALL' or ballType.upper() == 'PREMIERBALL' or ballType.upper() == 'LUXURYBALL':
        Ballmult = 1.0

    if ballType.upper() == 'NETBALL':
        if ("Water <:water:772863431534444595>" in types) or ("Bug <:bug:772863431409795112>" in types):
            Ballmult = 3.5
        else:
            Ballmult = 1.0

    if ballType.upper() == "BEASTBALL":
        if pokename in UB:
            Ballmult = 5.0
        else:
            Ballmult = 0.1

    if ballType.upper() != "BEASTBALL":
        if pokename in UB:
            Ballmult = 0.6

    return Ballmult

def getHealth(hp, level):
    return (((15.5 + (2 * hp) + 100) * level) / 100) + 10

def getCatchValue(maxHP, realcatchRate, ballType, types, pokename):
    CV = max(min((((3 * maxHP - 2 * 1) * (realcatchRate * ballRate(ballType, types, pokename))) / (3 * maxHP)),255),0)
    return CV

def getCatchRate(catchValue):
    if catchValue == 0:
        return 0
    else:
        CR = (65536 / (((255 / catchValue))**0.1875))
        return CR

async def pokedex(self, pokename):
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

    if pokename == "Tapu koko":
        pokename = "Tapu Koko"
    if pokename == "Tapu lele":
        pokename = "Tapu Lele"
    if pokename == "Tapu bulu":
        pokename = "Tapu Bulu"
    if pokename == "Tapu fini":
        pokename = "Tapu Fini"
    if pokename == "Farfetch'd":
        pokename = "Farfetch''d"
    if pokename == "Sirfetch'd":
        pokename = "Sirfetch''d"
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM pokedex WHERE name = '"+str(pokename)+"';"))
            row = list(prerow.values())
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
                    Ability2 = "\u200B"
                    HAbility = row[15]
                    if HAbility == "Unknown":
                        HAbility = "\u200B"
                    MaleRate = float(row[16])
                    FemaleRate = float(row[17])
                    Height = float(row[18])
                    Weight = float(row[19])
                    EggGrp1 = row[20]
                    if row[21] == "Unknown":
                        EggGrp2 = "\u200B"
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
                    if HAbility == "Unknown":
                        HAbility = "\u200B"
                    MaleRate = float(row[16])
                    FemaleRate = float(row[17])
                    Height = float(row[18])
                    Weight = float(row[19])
                    EggGrp1 = row[20]
                    if row[21] == "Unknown":
                        EggGrp2 = "\u200B"
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
                types= row[3]
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
                    Ability2 = "\u200B"
                    HAbility = row[15]
                    if HAbility == "Unknown":
                        HAbility = "\u200B"
                    MaleRate = float(row[16])
                    FemaleRate = float(row[17])
                    Height = float(row[18])
                    Weight = float(row[19])
                    EggGrp1 = row[20]
                    if row[21] == "Unknown":
                        EggGrp2 = "\u200B"
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
                    if HAbility == "Unknown":
                        HAbility = "\u200B"
                    MaleRate = float(row[16])
                    FemaleRate = float(row[17])
                    Height = float(row[18])
                    Weight = float(row[19])
                    EggGrp1 = row[20]
                    if row[21] == "Unknown":
                        EggGrp2 = "\u200B"
                        SwDens = row[22]
                        ShDens = row[23]
                        return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                    elif row[21] != "Unknown":
                        EggGrp2 = row[21]
                        SwDens = row[22]
                        ShDens = row[23]
                        return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens) ###

async def alolanpokedex(self, pokename):
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

    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM alolapokedex WHERE name = '"+str(pokename)+"';"))
            row = list(prerow.values())
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
                    Ability2 = "\u200B"
                    HAbility = row[15]
                    if HAbility == "Unknown":
                        HAbility = "\u200B"
                    MaleRate = float(row[16])
                    FemaleRate = float(row[17])
                    Height = float(row[18])
                    Weight = float(row[19])
                    EggGrp1 = row[20]
                    if row[21] == "Unknown":
                        EggGrp2 = "\u200B"
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
                    if HAbility == "Unknown":
                        HAbility = "\u200B"
                    MaleRate = float(row[16])
                    FemaleRate = float(row[17])
                    Height = float(row[18])
                    Weight = float(row[19])
                    EggGrp1 = row[20]
                    if row[21] == "Unknown":
                        EggGrp2 = "\u200B"
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
                types= row[3]
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
                    Ability2 = "\u200B"
                    HAbility = row[15]
                    if HAbility == "Unknown":
                        HAbility = "\u200B"
                    MaleRate = float(row[16])
                    FemaleRate = float(row[17])
                    Height = float(row[18])
                    Weight = float(row[19])
                    EggGrp1 = row[20]
                    if row[21] == "Unknown":
                        EggGrp2 = "\u200B"
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
                    if HAbility == "Unknown":
                        HAbility = "\u200B"
                    MaleRate = float(row[16])
                    FemaleRate = float(row[17])
                    Height = float(row[18])
                    Weight = float(row[19])
                    EggGrp1 = row[20]
                    if row[21] == "Unknown":
                        EggGrp2 = "\u200B"
                        SwDens = row[22]
                        ShDens = row[23]
                        return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                    elif row[21] != "Unknown":
                        EggGrp2 = row[21]
                        SwDens = row[22]
                        ShDens = row[23]
                        return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens) ###

async def galarianpokedex(self, pokename):
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
    
    if pokename == "Farfetch'd":
        pokename = "Farfetch''d"

    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM galarpokedex WHERE name = '"+str(pokename)+"';"))
            row = list(prerow.values())
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
                    Ability2 = "\u200B"
                    HAbility = row[15]
                    if HAbility == "Unknown":
                        HAbility = "\u200B"
                    MaleRate = float(row[16])
                    FemaleRate = float(row[17])
                    Height = float(row[18])
                    Weight = float(row[19])
                    EggGrp1 = row[20]
                    if row[21] == "Unknown":
                        EggGrp2 = "\u200B"
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
                    if HAbility == "Unknown":
                        HAbility = "\u200B"
                    MaleRate = float(row[16])
                    FemaleRate = float(row[17])
                    Height = float(row[18])
                    Weight = float(row[19])
                    EggGrp1 = row[20]
                    if row[21] == "Unknown":
                        EggGrp2 = "\u200B"
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
                types= row[3]
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
                    Ability2 = "\u200B"
                    HAbility = row[15]
                    if HAbility == "Unknown":
                        HAbility = "\u200B"
                    MaleRate = float(row[16])
                    FemaleRate = float(row[17])
                    Height = float(row[18])
                    Weight = float(row[19])
                    EggGrp1 = row[20]
                    if row[21] == "Unknown":
                        EggGrp2 = "\u200B"
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
                    if HAbility == "Unknown":
                        HAbility = "\u200B"
                    MaleRate = float(row[16])
                    FemaleRate = float(row[17])
                    Height = float(row[18])
                    Weight = float(row[19])
                    EggGrp1 = row[20]
                    if row[21] == "Unknown":
                        EggGrp2 = "\u200B"
                        SwDens = row[22]
                        ShDens = row[23]
                        return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)
                    elif row[21] != "Unknown":
                        EggGrp2 = row[21]
                        SwDens = row[22]
                        ShDens = row[23]
                        return (dexentry, generation, types, pokeHp, pokeAtk, pokeDef, pokeSpA, pokeSPD, pokeSpeed, Stattotal, catchRate, Ability1, Ability2, HAbility, MaleRate, FemaleRate, Height, Weight, EggGrp1, EggGrp2, SwDens, ShDens)

async def ball(self, ballName):
    ballName = ballName.capitalize()
    Multiplier = ''
    Condition = ''
    Addeffect = ''


    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM pokeballdata WHERE name = '"+str(ballName)+"';"))
            row = list(prerow.values())
            Multiplier = row[1]
            Condition = row[2]
            Addeffect = row[3]
            return (Multiplier, Condition, Addeffect)

async def dennumber(self, dennum):
    Swha = ''
    Shha = ''
    MGame = ''
    IoA = ''
    TCT = ''

    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM dennum WHERE den = '"+str(dennum)+"';"))
            row = list(prerow.values())
            Swha = row[1]
            Shha = row[2]
            MGame = row[3]
            IoA = row[4]
            TCT = row[5]
            return (Swha, Shha, MGame, IoA, TCT)

async def denname(self, dennamez):
    dennamez = dennamez.capitalize()
    Swha = ''
    Shha = ''
    Swnonha = ''
    Shnonha = ''

    if dennamez == "Farfetch'd":
        dennamez = "Farfetch''d"
    if dennamez == "Sirfetch'd":
        dennamez = "Sirfetch''d"

    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM denpokename WHERE name = '"+str(dennamez)+"';"))
            row = list(prerow.values())
            Swnonha = row[1]
            Shnonha = row[2]
            Swha = row[3]
            Shha = row[4]
            swextra = row[5]
            shextra = row[6]
            swhaextra = row[7]
            shhaextra = row[8]
            return (Swnonha, Shnonha, Swha, Shha, swextra, shextra, swhaextra, shhaextra)

async def gmaxdenname(self, dennamez):
    dennamez = dennamez.capitalize()
    Swha = ''
    Shha = ''
    Swnonha = ''
    Shnonha = ''

    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM dengmaxname WHERE name = '"+str(dennamez)+"';"))
            row = list(prerow.values())
            Swnonha = row[1]
            Shnonha = row[2]
            Swha = row[3]
            Shha = row[4]
            swextra = row[5]
            shextra = row[6]
            swhaextra = row[7]
            shhaextra = row[8]
            return (Swnonha, Shnonha, Swha, Shha, swextra, shextra, swhaextra, shhaextra)

async def namecheck(self, pokename):
    if pokename == "Farfetch'd":
        pokename = "Farfetch''d"
    if pokename == "Sirfetch'd":
        pokename = "Sirfetch''d"

# retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            test = await connection.fetchval("SELECT name FROM pokedex WHERE name = '"+str(pokename)+"';")
            return test

async def movedatagrab(self, movename):
    if movename == "Let'S Snuggle Forever":
        movename = "Let''s Snuggle Forever"
    if movename == "Trick-Or-Treat":
        movename = "Trick-or-Treat"
    if movename == "King'S Shield":
        movename = "King''s Shield"
    if movename == "Land'S Wrath":
        movename = "Land''s Wrath"
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            prerow = dict(await connection.fetchrow("SELECT * FROM movedex WHERE name = '"+str(movename)+"';"))
            row = list(prerow.values())
            effect = row[1]
            description = row[2]
            movetype = row[5]
            catergory = row[6]
            power = row[7]
            accuracry = row[8]
            powerpoints = row[9]
            priority = row[10]
            gmaxpower = row[11]
            flag1 = row[12]
            flag2 = row[13]
            flag3 = row[14]
            flag4 = row[15]
            flag5 = row[16]
            flag6 = row[17]
            imageurl = row[18]
            return (effect, description, movetype, catergory, power, accuracry, powerpoints, priority, gmaxpower,flag1,flag2,flag3,flag4,flag5,flag6,imageurl)

def getKey(item):
    return item[1]

def getNKey(item):
    return item[0]

def setup(client):
    client.add_cog(Pokemon(client))
