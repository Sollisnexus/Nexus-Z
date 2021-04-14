import discord
import random
import asyncio
import asyncpg
from discord.ext import commands
from discord.ext.commands import UserConverter

async def get_delete(self, message):
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            try:
                search = await connection.fetchval("SELECT switch FROM friendcodes WHERE guildid = "+str(message.guild.id)+" ;")
            except:
                return 'False'
            else:
                return search

async def addtodatabase(self, ctx):
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            enteruser = await connection.execute("INSERT INTO friendcodes (guildid, userid) VALUES ('"+str(ctx.guild.id)+"', '"+str(ctx.author.id)+"');")
            usercheck = await connection.fetchval("SELECT unique_id FROM friendcodes WHERE guildid = '"+str(ctx.guild.id)+"' AND userid = '"+str(ctx.author.id)+"';")
            return usercheck

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
        await ctx.send(embed=embed)

    @commands.command(name="nexusz?")
    @commands.cooldown(rate=1, per=5.0)
    async def nexusz(self, ctx):
        embed = discord.Embed(title="", description="", color=0x2962FF)
        embed.set_image(url="https://thumbs.gfycat.com/RegularInnocentBug-size_restricted.gif")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(rate=1, per=5.0)
    async def freepokemon(self, ctx):
        embed = discord.Embed(title="", description="", color=0x2962FF)
        embed.set_image(url="https://cdn.discordapp.com/attachments/676543990853795840/734577723804221503/SPOILER_YouFool.gif")
        await ctx.send(embed=embed)

    @commands.group(case_insensitive=True)
    async def fc(self, ctx):
        if ctx.invoked_subcommand is None:
            responce = str(ctx.message.content)
            content = responce.split()
            try:
                content[1]
            except:
                fc = await seefc(self, ctx)
                Friend = discord.Embed(title= str(ctx.author) + "'s Friend Codes", description="", color=0x2962FF)
                Friend.set_thumbnail(url = ctx.author.avatar_url)
                if fc[0] != None:
                    Friend.add_field(name="Switch 1:", value=str(fc[0]), inline=True)
                if fc[1] != None:
                    Friend.add_field(name="Switch 2:", value=str(fc[1]), inline=True)
                if fc[2] != None:
                    Friend.add_field(name="Switch 3:", value=str(fc[2]), inline=True)
                if fc[3] != None:
                    Friend.add_field(name="Switch 4:", value=str(fc[3]), inline=True)
                if fc[4] != None:
                    Friend.add_field(name="Switch 5:", value=str(fc[4]), inline=True)
                if fc[5] != None:
                    Friend.add_field(name="Switch 6:", value=str(fc[5]), inline=True)
                if fc[6] != None:
                    Friend.add_field(name="Switch 7:", value=str(fc[6]), inline=True)
                if fc[7] != None:
                    Friend.add_field(name="Switch 8:", value=str(fc[7]), inline=True)
                if fc[8] != None:
                    Friend.add_field(name="PoGo 1:", value=str(fc[8]), inline=True)
                if fc[9] != None:
                    Friend.add_field(name="Pogo 2:", value=str(fc[9]), inline=True)
                if fc[10] != None:
                    Friend.add_field(name="Pogo 3:", value=str(fc[10]), inline=True)
                if fc[11] != None:
                    Friend.add_field(name="Pogo 4:", value=str(fc[11]), inline=True)
                if fc[12] != None:
                    Friend.add_field(name="3DS 1:", value=str(fc[12]), inline=True)
                if fc[13] != None:
                    Friend.add_field(name="3DS 2:", value=str(fc[13]), inline=True)
                if fc[14] != None:
                    Friend.add_field(name="Shuffle:", value=str(fc[14]), inline=True)
                if fc[15] != None:
                    Friend.add_field(name="Master:", value=str(fc[15]), inline=True)
                if fc[16] != None:
                    Friend.add_field(name="Home:", value=str(fc[16]), inline=True)
                if fc[17] != None:
                    Friend.add_field(name="Cafemix:", value=str(fc[17]), inline=True)
                if fc[1:] == fc[:-1]:
                    await ctx.send("You don't have any friend codes set on this server.")
                    return

                Friend.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                await ctx.send(embed=Friend)

            else:
                if content[1].startswith("<") and content[1].endswith(">"):
                    converter = UserConverter()
                    member = await converter.convert(ctx, content[1])
                    fc = await seeotherfc(self, ctx, member.id)
                    Friend = discord.Embed(title= str(member) + "'s Friend Codes", description="", color=0x2962FF)
                    Friend.set_thumbnail(url = member.avatar_url)
                    if fc[0] != None:
                        Friend.add_field(name="Switch 1:", value=str(fc[0]), inline=True)
                    if fc[1] != None:
                        Friend.add_field(name="Switch 2:", value=str(fc[1]), inline=True)
                    if fc[2] != None:
                        Friend.add_field(name="Switch 3:", value=str(fc[2]), inline=True)
                    if fc[3] != None:
                        Friend.add_field(name="Switch 4:", value=str(fc[3]), inline=True)
                    if fc[4] != None:
                        Friend.add_field(name="Switch 5:", value=str(fc[4]), inline=True)
                    if fc[5] != None:
                        Friend.add_field(name="Switch 6:", value=str(fc[5]), inline=True)
                    if fc[6] != None:
                        Friend.add_field(name="Switch 7:", value=str(fc[6]), inline=True)
                    if fc[7] != None:
                        Friend.add_field(name="Switch 8:", value=str(fc[7]), inline=True)
                    if fc[8] != None:
                        Friend.add_field(name="PoGo 1:", value=str(fc[8]), inline=True)
                    if fc[9] != None:
                        Friend.add_field(name="Pogo 2:", value=str(fc[9]), inline=True)
                    if fc[10] != None:
                        Friend.add_field(name="Pogo 3:", value=str(fc[10]), inline=True)
                    if fc[11] != None:
                        Friend.add_field(name="Pogo 4:", value=str(fc[11]), inline=True)
                    if fc[12] != None:
                        Friend.add_field(name="3DS 1:", value=str(fc[12]), inline=True)
                    if fc[13] != None:
                        Friend.add_field(name="3DS 2:", value=str(fc[13]), inline=True)
                    if fc[14] != None:
                        Friend.add_field(name="Shuffle:", value=str(fc[14]), inline=True)
                    if fc[15] != None:
                        Friend.add_field(name="Master:", value=str(fc[15]), inline=True)
                    if fc[16] != None:
                        Friend.add_field(name="Home:", value=str(fc[16]), inline=True)
                    if fc[17] != None:
                        Friend.add_field(name="Cafemix:", value=str(fc[17]), inline=True)
                    if fc[1:] == fc[:-1]:
                        await ctx.send("This user doesn't have any friend codes set on this server.")
                        return

                    Friend.set_footer(text="Provided by Nexus-Z", icon_url="https://raw.githubusercontent.com/Sollisnexus/Sollisnexus.github.io/master/NexusZ/NexusZLogo_2.png")
                    await ctx.send(embed=Friend)

                else:
                    ctx.send("Please @ a real user to check if they have any friend codes on this server")

    @fc.command(aliases=["add"])
    async def set(self, ctx):
        responce = str(ctx.message.content)
        content = responce.split()
        if content[2] == "switch":
            slotnumber = await addswitchs(self, ctx, content[3])
            if slotnumber == 0:
                await ctx.send("Your friend code was not added because you are full on friend codes for switch!")
            if slotnumber != 0:
                await ctx.send("Your friend code was added into Switch slot "+str(slotnumber)+"!")
        elif content[2] == "pogo":
            slotnumber = await addpogo(self, ctx, content[3])
            if slotnumber == 0:
                await ctx.send("Your friend code was not added because you are full on friend codes for Pokemon Go!")
            if slotnumber != 0:
                await ctx.send("Your friend code was added into Pogo slot "+str(slotnumber)+"!")
        elif content[2] == "ds":
            slotnumber = await addds(self, ctx, content[3])
            if slotnumber == 0:
                await ctx.send("Your friend code was not added because you are full on friend codes for Pokemon Go!")
            if slotnumber != 0:
                await ctx.send("Your friend code was added into 3DS slot "+str(slotnumber)+"!")
        elif content[2] == "shuffle":
            slotnumber = await addshuffle(self, ctx, content[3])
            if slotnumber == 0:
                await ctx.send("Your friend code was not added because you are full on friend codes for Pokemon Go!")
            if slotnumber != 0:
                await ctx.send("Your friend code was added into Shuffle slot !")
        elif content[2] == "master":
            slotnumber = await addmaster(self, ctx, content[3])
            if slotnumber == 0:
                await ctx.send("Your friend code was not added because you are full on friend codes for Pokemon Go!")
            if slotnumber != 0:
                await ctx.send("Your friend code was added into Master slot!")
        elif content[2] == "home":
            slotnumber = await addhome(self, ctx, content[3])
            if slotnumber == 0:
                await ctx.send("Your friend code was not added because you are full on friend codes for Pokemon Go!")
            if slotnumber != 0:
                await ctx.send("Your friend code was added into Home slot!")
        elif content[2] == "cafemix":
            slotnumber = await addcafemix(self, ctx, content[3])
            if slotnumber == 0:
                await ctx.send("Your friend code was not added because you are full on friend codes for Pokemon Go!")
            if slotnumber != 0:
                await ctx.send("Your friend code was added into Cafemix slot!")
        else:
            await ctx.send("Are you sure that's a Switch/3DS or Pokemon game?")

    @fc.command()
    async def delete(self, ctx):
        responce = str(ctx.message.content)
        content = responce.split()
        x = content[2]
        if content[2].startswith("switch"):
            removed = await deleteswitch(self, ctx, x[-1])
            if removed == "True":
                await ctx.send("Friend Code for Switch Slot #"+str(x[-1])+" has been removed!")
            else:
                await ctx.send("Friend Code for Switch has not been removed due to not existing!")
        elif content[2].startswith("pogo"):
            removed = await deletepogo(self, ctx, x[-1])
            if removed == "True":
                await ctx.send("Friend Code for PoGo Slot #"+str(x[-1])+" has been removed!")
            else:
                await ctx.send("Friend Code for PoGo has not been removed due to not existing!")
        elif content[2].startswith("ds"):
            removed = await deleteds(self, ctx, x[-1])
            if removed == "True":
                await ctx.send("Friend Code for 3DS Slot #"+str(x[-1])+" has been removed!")
            else:
                await ctx.send("Friend Code for 3DS has not been removed due to not existing!")
        elif content[2].startswith("shuffle"):
            removed = await deleteshuffle(self, ctx)
            if removed == "True":
                await ctx.send("Friend Code for Shuffle Slot has been removed!")
            else:
                await ctx.send("Friend Code for Switch has not been removed due to not existing!")
        elif content[2].startswith("master"):
            removed = await deletemaster(self, ctx)
            if removed == "True":
                await ctx.send("Friend Code for Master Slot has been removed!")
            else:
                await ctx.send("Friend Code for Master has not been removed due to not existing!")
        elif content[2].startswith("home"):
            removed = await deletehome(self, ctx)
            if removed == "True":
                await ctx.send("Friend Code for Home Slot has been removed!")
            else:
                await ctx.send("Friend Code for Home has not been removed due to not existing!")
        elif content[2].startswith("cafemix"):
            removed = await deletecafemix(self, ctx)
            if removed == "True":
                await ctx.send("Friend Code for Cafemix Slot has been removed!")
            else:
                await ctx.send("Friend Code for Cafemix has not been removed due to not existing!")
        elif content[2] == "all":
            removed = await deleteall(self, ctx)
            if removed == "True":
                await ctx.send("All friend codes have been removed!")
            else:
                await ctx.send("All friend codes not removed due to not existing!")
        else:
            await ctx.send("Are you sure that's a Switch/3DS or Pokemon game?")

    @fc.error
    async def fc_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            print(error)

    @set.error
    async def set_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            print(error)

    @delete.error
    async def delete_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            print(error)

    @commands.Cog.listener()#(name='help', help='Displays further explaination for commands')
    async def on_message(self, message):
    #async def help (self, ctx):
        if str(message.author) == self.client.user:
            return

        if message.author.bot and str(message.author.id) == "760573976757010463":
            ctx = await self.client.get_context(message)
            id = message.content.split()
            converter = UserConverter()
            member = await converter.convert(ctx, id[1])
            await member.send("Thanks for voting for me, here's a 🍪")
            return

        if message.author.bot:
            return

    @addcommand.error
    async def addcommand_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            #if get_switch(self, ctx) == "True":
            #    await ctx.message.switch()
            await ctx.send("Please wait this command is still on cooldown", switch_after=5)

    @nexusz.error
    async def nexusz_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            #if get_switch(self, ctx) == "True":
            #   await ctx.message.switch()
            await ctx.send("Please wait this command is still on cooldown", switch_after=5)

    @freepokemon.error
    async def freepokemon_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            #   await ctx.message.switch()
            await ctx.send("Please wait this command is still on cooldown", switch_after=5)

    @commands.command()
    async def test(self, ctx, msg):
        responce = str(ctx.message.content)
        Msgres = "Normal"
        content = responce.split()
        name = content[1].capitalize()
        if name.endswith("*"):
            Msgres = "Shiny"
            name = name.replace("*", "")
        await ctx.send(Msgres +" "+ name)

async def addswitchs(self, ctx, friendcode):
    codeadded = "False"
    slot = 0
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():            
            usercheck = await connection.fetchval("SELECT unique_id FROM friendcodes WHERE guildid = '"+str(ctx.guild.id)+"' AND userid = '"+str(ctx.author.id)+"';")
            if usercheck == None:
                enteruser = await addtodatabase(self, ctx)
                usercheck = enteruser
            check1 = await connection.fetchval("SELECT switch1 FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
            check2 = await connection.fetchval("SELECT switch2 FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
            check3 = await connection.fetchval("SELECT switch3 FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
            check4 = await connection.fetchval("SELECT switch4 FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
            check5 = await connection.fetchval("SELECT switch5 FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
            check6 = await connection.fetchval("SELECT switch6 FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
            check7 = await connection.fetchval("SELECT switch7 FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
            check8 = await connection.fetchval("SELECT switch8 FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
            if check1 == None and codeadded == "False":
                await connection.execute("UPDATE friendcodes SET switch1 = '"+str(friendcode)+"' WHERE unique_id = '"+str(usercheck)+"';")
                codeadded = "True"
                slot = 1
            if check2 == None and codeadded == "False":
                await connection.execute("UPDATE friendcodes SET switch2 = '"+str(friendcode)+"' WHERE unique_id = '"+str(usercheck)+"';")
                codeadded = "True"
                slot = 2
            if check3 == None and codeadded == "False":
                await connection.execute("UPDATE friendcodes SET switch3 = '"+str(friendcode)+"' WHERE unique_id = '"+str(usercheck)+"';")
                codeadded = "True"
                slot = 3
            if check4 == None and codeadded == "False":
                await connection.execute("UPDATE friendcodes SET switch4 = '"+str(friendcode)+"' WHERE unique_id = '"+str(usercheck)+"';")
                codeadded = "True"
                slot = 4
            if check5 == None and codeadded == "False":
                await connection.execute("UPDATE friendcodes SET switch5 = '"+str(friendcode)+"' WHERE unique_id = '"+str(usercheck)+"';")
                codeadded = "True"
                slot = 5
            if check6 == None and codeadded == "False":
                await connection.execute("UPDATE friendcodes SET switch6 = '"+str(friendcode)+"' WHERE unique_id = '"+str(usercheck)+"';")
                codeadded = "True"
                slot = 6
            if check7 == None and codeadded == "False":
                await connection.execute("UPDATE friendcodes SET switch7 = '"+str(friendcode)+"' WHERE unique_id = '"+str(usercheck)+"';")
                codeadded = "True"
                slot = 7
            if check8 == None and codeadded == "False":
                await connection.execute("UPDATE friendcodes SET switch8 = '"+str(friendcode)+"' WHERE unique_id = '"+str(usercheck)+"';")
                codeadded = "True"
                slot = 8

            return slot

async def addpogo(self, ctx, friendcode):
    codeadded = "False"
    slot = 0
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():            
            usercheck = await connection.fetchval("SELECT unique_id FROM friendcodes WHERE guildid = '"+str(ctx.guild.id)+"' AND userid = '"+str(ctx.author.id)+"';")
            if usercheck == None:
                enteruser = await addtodatabase(self, ctx)
                usercheck = enteruser
            check1 = await connection.fetchval("SELECT pogo1 FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
            check2 = await connection.fetchval("SELECT pogo2 FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
            check3 = await connection.fetchval("SELECT pogo3 FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
            check4 = await connection.fetchval("SELECT pogo4 FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
            if check1 == None and codeadded == "False":
                await connection.execute("UPDATE friendcodes SET pogo1 = '"+str(friendcode)+"' WHERE unique_id = '"+str(usercheck)+"';")
                codeadded = "True"
                slot = 1
            if check2 == None and codeadded == "False":
                await connection.execute("UPDATE friendcodes SET pogo2 = '"+str(friendcode)+"' WHERE unique_id = '"+str(usercheck)+"';")
                codeadded = "True"
                slot = 2
            if check3 == None and codeadded == "False":
                await connection.execute("UPDATE friendcodes SET pogo3 = '"+str(friendcode)+"' WHERE unique_id = '"+str(usercheck)+"';")
                codeadded = "True"
                slot = 3
            if check4 == None and codeadded == "False":
                await connection.execute("UPDATE friendcodes SET pogo4 = '"+str(friendcode)+"' WHERE unique_id = '"+str(usercheck)+"';")
                codeadded = "True"
                slot = 4

            return slot

async def addds(self, ctx, friendcode):
    codeadded = "False"
    slot = 0
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():            
            usercheck = await connection.fetchval("SELECT unique_id FROM friendcodes WHERE guildid = '"+str(ctx.guild.id)+"' AND userid = '"+str(ctx.author.id)+"';")
            if usercheck == None:
                enteruser = await addtodatabase(self, ctx)
                usercheck = enteruser
            usercheck = await connection.fetchval("SELECT unique_id FROM friendcodes WHERE guildid = '"+str(ctx.guild.id)+"' AND userid = '"+str(ctx.author.id)+"';")
            check1 = await connection.fetchval("SELECT ds1 FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
            check2 = await connection.fetchval("SELECT ds2 FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
            if check1 == None and codeadded == "False":
                await connection.execute("UPDATE friendcodes SET ds1 = '"+str(friendcode)+"' WHERE unique_id = '"+str(usercheck)+"';")
                codeadded = "True"
                slot = 1
            if check2 == None and codeadded == "False":
                await connection.execute("UPDATE friendcodes SET ds2 = '"+str(friendcode)+"' WHERE unique_id = '"+str(usercheck)+"';")
                codeadded = "True"
                slot = 2

            return slot

async def addshuffle(self, ctx, friendcode):
    codeadded = "False"
    slot = 0
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():            
            usercheck = await connection.fetchval("SELECT unique_id FROM friendcodes WHERE guildid = '"+str(ctx.guild.id)+"' AND userid = '"+str(ctx.author.id)+"';")
            if usercheck == None:
                enteruser = await addtodatabase(self, ctx)
                usercheck = enteruser
            check1 = await connection.fetchval("SELECT shuffle FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
            if check1 == None and codeadded == "False":
                await connection.execute("UPDATE friendcodes SET shuffle = '"+str(friendcode)+"' WHERE unique_id = '"+str(usercheck)+"';")
                codeadded = "True"
                slot = 1

            return slot

async def addmaster(self, ctx, friendcode):
    codeadded = "False"
    slot = 0
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():            
            usercheck = await connection.fetchval("SELECT unique_id FROM friendcodes WHERE guildid = '"+str(ctx.guild.id)+"' AND userid = '"+str(ctx.author.id)+"';")
            if usercheck == None:
                enteruser = await addtodatabase(self, ctx)
                usercheck = enteruser
            check1 = await connection.fetchval("SELECT master FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
            if check1 == None and codeadded == "False":
                await connection.execute("UPDATE friendcodes SET master = '"+str(friendcode)+"' WHERE unique_id = '"+str(usercheck)+"';")
                codeadded = "True"
                slot = 1

            return slot

async def addhome(self, ctx, friendcode):
    codeadded = "False"
    slot = 0
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():            
            usercheck = await connection.fetchval("SELECT unique_id FROM friendcodes WHERE guildid = '"+str(ctx.guild.id)+"' AND userid = '"+str(ctx.author.id)+"';")
            if usercheck == None:
                enteruser = await addtodatabase(self, ctx)
                usercheck = enteruser
            check1 = await connection.fetchval("SELECT home FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
            if check1 == None and codeadded == "False":
                await connection.execute("UPDATE friendcodes SET home = '"+str(friendcode)+"' WHERE unique_id = '"+str(usercheck)+"';")
                codeadded = "True"
                slot = 1

            return slot

async def addcafemix(self, ctx, friendcode):
    codeadded = "False"
    slot = 0
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():            
            usercheck = await connection.fetchval("SELECT unique_id FROM friendcodes WHERE guildid = '"+str(ctx.guild.id)+"' AND userid = '"+str(ctx.author.id)+"';")
            if usercheck == None:
                enteruser = await addtodatabase(self, ctx)
                usercheck = enteruser
            check1 = await connection.fetchval("SELECT cafemix FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
            if check1 == None and codeadded == "False":
                await connection.execute("UPDATE friendcodes SET cafemix = '"+str(friendcode)+"' WHERE unique_id = '"+str(usercheck)+"';")
                codeadded = "True"
                slot = 1

            return slot


async def deleteswitch(self, ctx, slotnum):
    slot = slotnum
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            usercheck = await connection.fetchval("SELECT unique_id FROM friendcodes WHERE guildid = '"+str(ctx.guild.id)+"' AND userid = '"+str(ctx.author.id)+"';")
            if usercheck == None:
                return "False"
            else:
                try:
                    check1 = await connection.fetchval("SELECT switch"+str(slot)+" FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
                except:
                    return "False"
                else:
                    if check1 is not None:
                        await connection.execute("UPDATE friendcodes SET switch"+str(slot)+" = NULL WHERE unique_id = '"+str(usercheck)+"' ;")
                        return "True"
                    else:
                        return "False"

async def deletepogo(self, ctx, slotnum):
    slot = slotnum
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            usercheck = await connection.fetchval("SELECT unique_id FROM friendcodes WHERE guildid = '"+str(ctx.guild.id)+"' AND userid = '"+str(ctx.author.id)+"';")
            if usercheck == None:
                return "False"
            else:
                try:
                    check1 = await connection.fetchval("SELECT pogo"+str(slot)+" FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
                except:
                    return "False"
                else:
                    if check1 is not None:
                        await connection.execute("UPDATE friendcodes SET pogo"+str(slot)+" = NULL WHERE unique_id = '"+str(usercheck)+"' ;")
                        return "True"
                    else:
                        return "False"

async def deleteds(self, ctx, slotnum):
    slot = slotnum
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            usercheck = await connection.fetchval("SELECT unique_id FROM friendcodes WHERE guildid = '"+str(ctx.guild.id)+"' AND userid = '"+str(ctx.author.id)+"';")
            if usercheck == None:
                return "False"
            else:
                try:
                    check1 = await connection.fetchval("SELECT ds"+str(slot)+" FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
                except:
                    return "False"
                else:
                    if check1 is not None:
                        await connection.execute("UPDATE friendcodes SET ds"+str(slot)+" = NULL WHERE unique_id = '"+str(usercheck)+"' ;")
                        return "True"
                    else:
                        return "False"

async def deleteshuffle(self, ctx):
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            usercheck = await connection.fetchval("SELECT unique_id FROM friendcodes WHERE guildid = '"+str(ctx.guild.id)+"' AND userid = '"+str(ctx.author.id)+"';")
            if usercheck == None:
                return "False"
            else:
                check1 = await connection.fetchval("SELECT shuffle FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
                if check1 is not None:
                    await connection.execute("UPDATE friendcodes SET shuffle = NULL WHERE unique_id = '"+str(usercheck)+"' ;")
                    return "True"
                else:
                    return "False"

async def deletemaster(self, ctx):
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            usercheck = await connection.fetchval("SELECT unique_id FROM friendcodes WHERE guildid = '"+str(ctx.guild.id)+"' AND userid = '"+str(ctx.author.id)+"';")
            if usercheck == None:
                return "False"
            else:
                check1 = await connection.fetchval("SELECT master FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
                if check1 is not None:
                    await connection.execute("UPDATE friendcodes SET master = NULL WHERE unique_id = '"+str(usercheck)+"' ;")
                    return "True"
                else:
                    return "False"

async def deletehome(self, ctx):
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            usercheck = await connection.fetchval("SELECT unique_id FROM friendcodes WHERE guildid = '"+str(ctx.guild.id)+"' AND userid = '"+str(ctx.author.id)+"';")
            if usercheck == None:
                return "False"
            else:
                check1 = await connection.fetchval("SELECT home FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
                if check1 is not None:
                    await connection.execute("UPDATE friendcodes SET home = NULL WHERE unique_id = '"+str(usercheck)+"' ;")
                    return "True"
                else:
                    return "False"

async def deletecafemix(self, ctx):
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            usercheck = await connection.fetchval("SELECT unique_id FROM friendcodes WHERE guildid = '"+str(ctx.guild.id)+"' AND userid = '"+str(ctx.author.id)+"';")
            if usercheck == None:
                return "False"
            else:
                check1 = await connection.fetchval("SELECT cafemix FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
                if check1 is not None:
                    await connection.execute("UPDATE friendcodes SET cafemix = NULL WHERE unique_id = '"+str(usercheck)+"' ;")
                    return "True"
                else:
                    return "False"

async def deleteall(self, ctx):
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            usercheck = await connection.fetchval("SELECT unique_id FROM friendcodes WHERE guildid = '"+str(ctx.guild.id)+"' AND userid = '"+str(ctx.author.id)+"';")
            if usercheck == None:
                return "False"
            else:
                await connection.execute("DELETE FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
                return "True"


async def seefc(self, ctx):
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            try:
                usercheck = await connection.fetchval("SELECT unique_id FROM friendcodes WHERE guildid = '"+str(ctx.guild.id)+"' AND userid = '"+str(ctx.author.id)+"';")
            except:
                return [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            else:
                if usercheck == None:
                    return [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
                else:
                    fclistcheck = await connection.fetchrow("SELECT * FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
                    codes = list(fclistcheck.values())
                    del codes[:3]
                    return codes

async def seeotherfc(self, ctx, checkid):
    # retrieve an individual connection from our pool, defined later
    async with self.client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            usercheck = await connection.fetchval("SELECT unique_id FROM friendcodes WHERE guildid = '"+str(ctx.guild.id)+"' AND userid = '"+str(checkid)+"';")
            if usercheck == None:
                return [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            else:
                fclistcheck = await connection.fetchrow("SELECT * FROM friendcodes WHERE unique_id = '"+str(usercheck)+"' ;")
                codes = list(fclistcheck.values())
                del codes[:3]
                return codes
  
def setup(client):
    client.add_cog(Replies(client))
