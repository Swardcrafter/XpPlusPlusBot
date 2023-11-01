from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.hybrid_command()
    async def ping(self, ctx):
        await ctx.reply(f"Pong")

async def setup(client):
    await client.add_cog(Ping(client))