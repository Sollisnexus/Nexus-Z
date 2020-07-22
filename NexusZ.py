import discord
import json
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '%')
Modulename = ""
status = cycle(['%help for commands','Pokemon SW/SH'])
client.remove_command('help')

@client.command(name='load <module>', help='Loads a selected module')
@commands.has_role('Owner')
async def load(ctx, extension):
    Modulename = str(extension)
    await ctx.author.message.delete()
    client.load_extension(f'cogs.{extension}')    
    if commands.CommandInvokeError == True:
        return
    await ctx.send(Modulename +' module has been loaded')
    

@client.command(name='unload <module>', help='Unloads a selected module')
@commands.has_role('Owner')
async def unload (ctx, extension):
    Modulename = str(extension)
    await ctx.author.message.delete()
    client.unload_extension(f'cogs.{extension}') 
    if commands.CommandInvokeError == True:
        return
    await ctx.send(Modulename +' module has been unloaded')
    
	
@client.command(name='reload <module>', help='Reloads a selected module')
@commands.has_role('Owner')
async def reload(ctx, extension):
    Modulename = str(extension)
    await ctx.author.message.delete()
    client.unload_extension(f'cogs.{extension}')
    if commands.CommandInvokeError == True:
        return
    client.load_extension(f'cogs.{extension}')
    if commands.CommandInvokeError == True:
        return
    await ctx.send(Modulename +' module has been reloaded')

        
for filename in os.listdir('E:/cogs'):
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
        await ctx.author.message.delete()
        await ctx.send('This command is unloaded or does not exist!')

@client.event
async def on_ready():
    change_status.start()

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
    
client.run('Token Here')
