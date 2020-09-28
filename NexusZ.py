import discord
import json
import os
from discord.ext import commands, tasks
from itertools import cycle

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

client = commands.Bot(command_prefix = get_prefix) #AutoShardedBot
Modulename = ""
status = cycle(['<>help for commands','Pokemon SW/SH','Pokemon Go'])
client.remove_command('help')


@client.command()
async def load(ctx, extension):
    Modulename = str(extension)

    client.load_extension(f'cogs.{extension}')
    if commands.CommandInvokeError == True:
        return
    await ctx.send(Modulename +' module has been loaded')


@client.command()
async def unload (ctx, extension):
    Modulename = str(extension)

    client.unload_extension(f'cogs.{extension}')
    if commands.CommandInvokeError == True:
        return
    await ctx.send(Modulename +' module has been unloaded')


@client.command()
async def reload(ctx, extension):
    Modulename = str(extension)

    client.unload_extension(f'cogs.{extension}')
    if commands.CommandInvokeError == True:
        return
    client.load_extension(f'cogs.{extension}')
    if commands.CommandInvokeError == True:
        return
    await ctx.send(Modulename +' module has been reloaded')


for filename in os.listdir('C:/Users/Administrator/Documents/cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')


@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send('The module is already loaded.')

@unload.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send('The module is already unloaded.')

@reload.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send('The module is already unloaded/loaded.')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        # await ctx.message.delete()
        print('Someone Tried a command that does not exist or help was triggered!')
        return


@client.event
async def on_ready():
    change_status.start()
    print('Connected!')
    print('Username: {0.name}\nID: {0.id}'.format(client.user))

@client.event
async def on_guild_join(guild):
    with open('C:/Users/Administrator/Documents/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '%'

    with open('C:/Users/Administrator/Documents/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('C:/Users/Administrator/Documents/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('C:/Users/Administrator/Documents/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command()
@commands.check_any(commands.is_owner(), is_guild_owner())
async def changeprefix(ctx, prefix):
    with open('C:/Users/Administrator/Documents/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('C:/Users/Administrator/Documents/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


    await ctx.send(f"My prefix changed on this server has been changed to: {prefix}")

@tasks.loop(seconds=4)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

client.run('')
