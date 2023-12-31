from discord.ext import commands
import requests
import os
import json

class SendData(commands.Cog):
	def __init__(self, client):
		self.client = client
    
	@commands.hybrid_command()
	async def send_data(self, ctx, data: str):
		try:
			data_dict = json.loads(data)
		except json.JSONDecodeError:
			await ctx.send("Data is not dict type.")
			return
		except Exception as e:
			# Handle other exceptions here
			await ctx.send(f"An error occurred: {str(e)}")
			return
		
		response = requests.post(os.environ['FLASK_URL'], json=data_dict)

		if response.status_code == 200:
			await ctx.send("Message sent successfully")
		else:
			await ctx.send("Failed to send message")
		await ctx.reply(f"Send {data}")

async def setup(client):
    await client.add_cog(SendData(client))