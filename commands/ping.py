from discord.ext import commands

class Ping(commands.Cog):
	def __init__(self, client):
		self.client = client # sets the client variable so we can use it in cogs
	
	@commands.Cog.listener()
	async def on_ready(self):
		print("Ready")
	
	@commands.command()
	async def command(self, ctx):
		print("Ping Run.")
		await ctx.send("Pong")

def setup(client):
	client.add_cog(Ping(client))