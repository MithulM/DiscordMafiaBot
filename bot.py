import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='m:')

for extension in os.listdir('./cogs'):
    if extension.endswith('.py'):
        client.load_extension(f'cogs.{extension[:-3]}')

@client.command()
async def reload(ctx, extension="all"):
    if (extension == "all"):
        for extension in os.listdir('./cogs'):
            if extension.endswith('.py'):
                client.unload_extension(f'cogs.{extension[:-3]}')
        for extension in os.listdir('./cogs'):
            if extension.endswith('.py'):
                client.load_extension(f'cogs.{extension[:-3]}')
        await ctx.send(f'Reloaded all cogs')
    else:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'Reloaded {extension}')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension}')

@load.error
async def load_error(ctx, error):
    if (isinstance(error, commands.MissingRequiredArgument)):
        await ctx.send('Please specify a cog to load.')

client.run("NzUwOTM5MzUyNjc4NTMxMTk0.X1B0xQ.H2iZqD1q6daR-pA_ZlA29UfWgI0")