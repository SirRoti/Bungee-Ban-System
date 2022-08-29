import nextcord
from nextcord.ext import commands

from colorama import Fore
import datetime

import random
import asyncio
import json
import mysql.connector

class role_manager(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            with open("D:\Programmieren\Python\Discord Bots\Eigene Projekte\Kilux Verify\data.json", "r") as data_file:
                data = json.load(data_file)

            guild = self.client.get_guild(data["ids"]["guild_id"])

            db = mysql.connector.connect(
                host = "",
                database = "",
                user = "",
                passwd = ""
            )
            cursor = db.cursor()

            cursor.execute("CREATE TABLE IF NOT EXISTS Users(uuid varchar(36), mc_name varchar(16), dc_name varchar(100), role varchar(30), code int, status int)")
            db.commit()

            while True:
                db.reconnect()
                cursor.execute("SELECT * FROM Users")
                for user in cursor:
                    if user[5] != 4: continue
                
                    member = nextcord.utils.get(guild.members, name=user[2].split("#")[0], discriminator=user[2].split("#")[1])
                    for role_id in data["roles"]["all"]: await member.remove_roles(guild.get_role(role_id))

                    cursor.execute(f"SELECT role FROM Users WHERE dc_name='{user[2]}'")

                    for rang in cursor:
                        rang = str(rang).replace("('", "")
                        rang = str(rang).replace("',)", "")
                        role = guild.get_role(data["roles"][rang])

                    await member.add_roles(role)

                    cursor.execute(f"UPDATE Users SET status=0 WHERE dc_name='{user[2]}'")
                    db.commit()

                await asyncio.sleep(10)

        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Event {Fore.CYAN}role_manager{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")
            
def setup(client):
    client.add_cog(role_manager(client))