from discord.ext import commands
import os
import json

# Import Data
with open('secrets.json', 'r') as json_file:
    secrets = json.load(json_file)



client = commands.Bot(command_prefix = secrets["COMMAND_PREFIX"])

for f in os.listdir("./commands"):
	if f.endswith(".py"):
		client.load_extension("cogs." + f[:-3])\

client.run(secrets["TOKEN"])

print("Running")