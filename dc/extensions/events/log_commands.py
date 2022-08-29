import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class log_commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, msg):
        try:
            with open("D:\Programmieren\Python\Discord Bots\Eigene Projekte\Kilux Verify\data.json", "r") as data_file:
                data = json.load(data_file)

            if msg.content.startswith(data["env"]["prefix"]) and not msg.author.bot:
                print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.YELLOW}COMMAND{Fore.RESET}] Command {Fore.CYAN}{msg.content}{Fore.RESET} von {Fore.CYAN}{msg.author}{Fore.LIGHTBLACK_EX}")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Event {Fore.CYAN}log_commands{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(log_commands(client))