import nextcord
from nextcord.ext import commands

from colorama import Fore
import datetime

class ready(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.MAGENTA}STARTED{Fore.RESET}] Bot logged in...{Fore.LIGHTBLACK_EX}")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Event {Fore.CYAN}ready{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")
            
def setup(client):
    client.add_cog(ready(client))