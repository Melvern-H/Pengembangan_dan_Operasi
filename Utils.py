import discord 
from discord.ext import commands 

class Utils(commands.Cog):
    
    def __init__(self,client):
        self.client = client
    
    @commands.command()
    async def userinfo(self,ctx,user : discord.User = None):
        if user is None :
            await ctx.send('Diisi dong usernya sayang :(')
            return

        embed = discord.Embed(title = 'Userinfo', description = f'Here is some information about {user.mention}', colour = discord.Colour.green())

        if user.id == 444782522509819904 :
            user.bot = 'Helloo !!!'
        elif user.id == 434373779788005377 :
            user.bot = 'Testing'
        elif user.id == 192993386305683457 :
            user.bot = 'This is a bot'
        elif user.id == 400890123677335553 :
            user.bot = 'Let's play Dota'

        embed.add_field(name = user, value = f'- User\'s name : {user.name}\n - User\'s ID : {user.id}\n - User\'s discrim : #{user.discriminator}\n - User is a bot : {user.bot}\n\n Note : Ingat kata ibot "Jangan beli bkb, bkb gadak demeg bwangg !!!"')

        embed.set_thumbnail(url = user.avatar_url)

        await ctx.send(':wave:', embed = embed)

def setup(client):
    client.add_cog(Utils(client))
