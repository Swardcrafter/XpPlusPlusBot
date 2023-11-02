from discord.ext import commands

class Purge(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.hybrid_command()
	@commands.has_permissions(administrator=True)
	async def purge(self, ctx, number: int):
		try:
			channel = ctx.channel
			
			# Check if the number of messages to purge is within a reasonable range.
			if 1 <= number <= 200:
				# Delete the specified number of messages.
				deleted_messages = await ctx.channel.purge(limit=number + 1)  # +1 to include the command message
				await channel.send(f"Successfully deleted {len(deleted_messages) - 1} message(s).")  # -1 to exclude the command message
			else:
				await channel.send("Please provide a number between 1 and 200 for the purge.")
		except Exception as e:
			await ctx.channel.send(f"Error Running Purge: {e}")

async def setup(client):
    await client.add_cog(Purge(client))