import discord
from discord.ext import commands
import os

class Client(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = os.environ['COMMAND_PREFIX'],
            intents = discord.Intents.all(),
            help_command = commands.DefaultHelpCommand(dm_help=True)
        )
    
    async def setup_hook(self): #overwriting a handler
        print(f"\033[31mLogged in as {client.user}\033[39m")
        cogs_folder = f"{os.path.abspath(os.path.dirname(__file__))}/commands"
        for filename in os.listdir(cogs_folder):
            if filename.endswith(".py"):
                await client.load_extension(f"commands.{filename[:-3]}")
        await client.tree.sync()
        print("Loaded cogs")

client = Client()

@client.event
async def on_ready():
    print("Bot is ready")

client.run(os.environ['TOKEN'])