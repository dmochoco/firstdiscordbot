import discord
from discord.ext import commands, tasks
from itertools import cycle
import random

# command is activated using '!' followed by command
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# bot status will cycle between this list
bot_status = cycle(["Type '!magic_eightball' and ask a question!", "Type '!eightball' and ask a question!", "Type '!8ball' and ask a question!", "Status Four"])

# function that changes the status of the bot and loops for every 10 seconds
@tasks.loop(seconds=10) 
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))


@client.event
async def on_ready():
    print("Success! Bot is connected to Discord")
    change_status.start()

# !ping function, bot sends message "Pong!" to channel, also sends latency of bot
@client.command()
async def ping(ctx):  
    bot_latency = round(client.latency * 1000)
    await ctx.send(f"Pong! {bot_latency} ms.")

# !magic_eightball function that takes a question from the uers
# and provides a random response
@client.command(aliases=["8ball", "eightball"]) # aliases are alternative names you can use in discord
async def magic_eightball(ctx, *, question): 
    with open("responses/eightball_responses.txt", "r") as f:  # opens the file as f

        # define variable called random_responses initialize it is a list of f.readlines(), which treats eightball responses as a python list
        random_responses = f.readlines()

        # define variable response and picks a random choice from the random responses list
        response = random.choice(random_responses)

    await ctx.send(response)

client.run(
    #TOKEN GOES HERE)
