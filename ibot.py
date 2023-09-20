import discord 
from discord.ext import commands 
# import random

client = commands.Bot(command_prefix="@")


cogs = ['Cog.Utils']

for cog in cogs:
    try:
        client .load_extension(cog)
    except Exception as e :
        print(f'G bisa ngeload cog nya cok {cog} : {str(e)}')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type = discord.ActivityType.watching, name = 'Grafik Saham'))
    print("Bot nya dah panas cok !")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # brooklyn_99_quotes = ['Test...."']

    if message.content == '<@!786264617508536381>':
        # response = random.choice(brooklyn_99_quotes)
        await message.channel.send(f'{message.author.mention} Helloo..."')
    await client.process_commands(message) #supaya commandnya jln

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms {ctx.message.author.mention}')

@client.command()
async def hi(ctx):
    await ctx.send('Hi, Lets play Dota')

@client.command()
async def say(ctx,*,message = None):
    if message == None :
        await  ctx.send('Testing 1 2 3')
    await ctx.send(message)

@client.command()
async def checkid(ctx,user: discord.User =  None):
    if user == None :
        await ctx.send('Please fill ur Username')
    await ctx.send(user.id)

client.run('Nzg2MjY0NjE3NTA4NTM2Mzgx.X9D3_A.ZhJLfpg5Q-DlMtzc0Gyd3MsjK7Y')
