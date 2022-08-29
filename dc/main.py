import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

with open('data.json', 'r') as data_file:
    data = json.load(data_file)

intents = nextcord.Intents.default()
intents.members = True
intents.reactions = True

client = commands.Bot(command_prefix=data["env"]["prefix"], intents=intents)
client.remove_command('help')

if __name__ == '__main__':
    for extension in data["env"]["extensions"]:
        try:
            client.load_extension(extension)
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.GREEN}LOADED{Fore.RESET}] Cog {Fore.CYAN}{extension}{Fore.RESET} wurde geladen{Fore.LIGHTBLACK_EX}")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Cog {Fore.CYAN}{extension}{Fore.RESET} konnte nicht geladen werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

client.run(data["env"]["token"])