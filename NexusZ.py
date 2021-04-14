import discord
import json
import os
import asyncio
import asyncpg
from dotenv import load_dotenv
from discord.ext import commands, tasks
from itertools import cycle

load_dotenv('.env')

intents = discord.Intents.default()
intents.members = False

async def get_prefix(client, message):
    # retrieve an individual connection from our pool, defined later
    async with client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            try:
                search = await connection.fetchval("SELECT prefix FROM prefixes WHERE guildid = "+str(message.guild.id)+" ;")
            except:
                return '%'
            else:
                return search

async def get_delete(client, message):
    # retrieve an individual connection from our pool, defined later
    async with client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            try:
                search = await connection.fetchval("SELECT delete FROM deletion WHERE guildid = "+str(message.guild.id)+" ;")
            except:
                return 'False'
            else:
                return search

def is_guild_owner():
    def predicate(ctx):
        return ctx.guild is not None and ctx.guild.owner_id == ctx.author.id
    return commands.check(predicate)

client = commands.Bot(command_prefix = get_prefix, case_insensitive=True, intents=intents) #AutoShardedBot
Modulename = ""
POSTGRES_INFO = {"user": "", "password": "", "database": "", "host": ""}
status = cycle(['<>help for commands','Pokemon SW/SH','Pokemon Go'])
client.remove_command('help')


@client.command()
@commands.check_any(commands.is_owner())
async def load(ctx, extension):
    Modulename = str(extension)

    client.load_extension(f'cogs.{extension}')
    if commands.CommandInvokeError == True:
        return
    await ctx.message.delete()
    await ctx.send(Modulename +' module has been loaded', delete_after=5)


@client.command()
@commands.check_any(commands.is_owner())
async def unload (ctx, extension):
    Modulename = str(extension)

    client.unload_extension(f'cogs.{extension}')
    if commands.CommandInvokeError == True:
        return
    await ctx.message.delete()
    await ctx.send(Modulename +' module has been unloaded', delete_after=5)


@client.command()
@commands.check_any(commands.is_owner())
async def reload(ctx, extension):
    Modulename = str(extension)

    client.unload_extension(f'cogs.{extension}')
    if commands.CommandInvokeError == True:
        return
    client.load_extension(f'cogs.{extension}')
    if commands.CommandInvokeError == True:
        return
    await ctx.message.delete()
    await ctx.send(Modulename +' module has been reloaded', delete_after=5)


for filename in os.listdir('C:/Users/Administrator/Documents/cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send('The module is already loaded.', delete_after=5)
    elif isinstance(error, commands.CheckAnyFailure):
        await ctx.message.delete()
        await ctx.send("You are not allowed to run this command", delete_after=5)

@unload.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send('The module is already unloaded.', delete_after=5)
    elif isinstance(error, commands.CheckAnyFailure):
        await ctx.message.delete()
        await ctx.send("You are not allowed to run this command", delete_after=5)

@reload.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send('The module is already unloaded/loaded.', delete_after=5)
    elif isinstance(error, commands.CheckAnyFailure):
        await ctx.message.delete()
        await ctx.send("You are not allowed to run this command", delete_after=5)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    #elif isinstance(error, commands.MissingPermissions):
    #    print(str(ctx.guild.id))
    #    print(str(ctx.author) + "has no premssions for whatever they're doing, go ask them if they need assistance")

@client.event
async def on_ready():
    try:
        change_status.start()
    except:
        print('Connected!')
        print('Username: {0.name}\nID: {0.id}'.format(client.user))
    else:
        print('Connected!')
        print('Username: {0.name}\nID: {0.id}'.format(client.user))

@client.event
async def on_guild_join(guild):
    # retrieve an individual connection from our pool, defined later
    async with client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            await connection.execute("INSERT INTO prefixes (guildid, prefix) VALUES ('"+str(guild.id)+"', '%');")
            await connection.execute("INSERT INTO deletion (guildid, delete) VALUES ('"+str(guild.id)+"', 'False');")
            await connection.execute("INSERT INTO guildhostchannel (guildid, guildchannelid) VALUES ('"+str(guild.id)+"', 'None');")
@client.event
async def on_guild_remove(guild):
    # retrieve an individual connection from our pool, defined later
    async with client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            await connection.execute("DELETE FROM prefixes WHERE guildid = '"+str(guild.id)+"';")
            await connection.execute("DELETE FROM deletion WHERE guildid = '"+str(guild.id)+"';")
            await connection.execute("DELETE FROM guildhostchannel WHERE guildid = '"+str(guild.id)+"';")

@client.command()
@commands.check_any(commands.is_owner(), is_guild_owner())
async def changeprefix(ctx, prefix):
    # retrieve an individual connection from our pool, defined later
    async with client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            await connection.execute("UPDATE prefixes SET prefix = '"+str(prefix)+"' WHERE guildid = '"+str(ctx.guild.id)+"';")

            await ctx.send(f"My prefix changed on this server has been changed to: {prefix}")

@client.command()
@commands.check_any(commands.is_owner(), is_guild_owner())
async def changedelete(ctx, statement):
    ON = ["True","true","yes","Yes","y","Y"]
    OFF = ["False","false","No","no","n","N"]
    if statement in ON:
        # retrieve an individual connection from our pool, defined later
        async with client.pool.acquire() as connection:
            # create a transaction for that connection
            async with connection.transaction():
                await connection.execute("UPDATE deletion SET delete = 'True' WHERE guildid = '"+str(ctx.guild.id)+"';")
                await ctx.send(f"My message deletion on this server has been changed to True")

    elif statement in OFF:
        # retrieve an individual connection from our pool, defined later
        async with client.pool.acquire() as connection:
            # create a transaction for that connection
            async with connection.transaction():
                await connection.execute("UPDATE deletion SET delete = 'False' WHERE guildid = '"+str(ctx.guild.id)+"';")
                await ctx.send(f"My message deletion on this server has been changed to False")

    else:
        await ctx.send("Please enter a statment of either True or False to allow or disallow message deletion from this bot\nExamples: True/False , Yes/No, Y/N")

@client.command()
@commands.check_any(commands.is_owner(), is_guild_owner())
async def changehost(ctx, message):
    # retrieve an individual connection from our pool, defined later
    async with client.pool.acquire() as connection:
        # create a transaction for that connection
        async with connection.transaction():
            await connection.execute("UPDATE guildhostchannel SET guildchannelid = '"+str(message)+"' WHERE guildid = '"+str(ctx.guild.id)+"';")
            await ctx.send("The server's hosting channel is now, "+str(message)+" , Make sure this bot has permissions to post in that channel.")

@changeprefix.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckAnyFailure):
        if (ctx.message.guild is not None):
            await ctx.message.delete()
            await ctx.send("You are not allowed to run this command", delete_after=5)
        else:
            await ctx.send("You are not allowed to run this command", delete_after=5)

@changedelete.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckAnyFailure):
        if (ctx.message.guild is not None):
            await ctx.message.delete()
            await ctx.send("You are not allowed to run this command", delete_after=5)
        else:
            await ctx.send("You are not allowed to run this command", delete_after=5)

@changehost.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckAnyFailure):
        if (ctx.message.guild is not None):
            await ctx.message.delete()
            await ctx.send("You are not allowed to run this command", delete_after=5)
        else:
            await ctx.send("You are not allowed to run this command", delete_after=5)

@tasks.loop(seconds=4)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

loop = asyncio.get_event_loop()
client.pool = loop.run_until_complete(asyncpg.create_pool(**POSTGRES_INFO))
client.run(os.getenv('NexuszToken'))
