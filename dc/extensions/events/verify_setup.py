import nextcord
from nextcord.ext import commands

from colorama import Fore
import datetime

import random
import asyncio
import json
import mysql.connector

class verify_setup(commands.Cog):
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
                    if user[5] == 1:
                        code = random.randint(100000, 999999)

                        try:
                            guild = self.client.get_guild(data["ids"]["guild_id"])
                            member = nextcord.utils.get(guild.members, name=user[2].split("#")[0], discriminator=user[2].split("#")[1])

                            verify_code_embed = nextcord.Embed(title="Discord Verify", description=f"Bist du **{user[1]}**?\n\nDies ist dein 6 stelliger Code:\n> **{code}**\n\nNun musst du ingame den Befehl **/verify [CODE]** ausführen, um dich zu verifizieren", color=nextcord.Color.from_rgb(32, 186, 192))
                            await member.send(embed=verify_code_embed)
                        except:
                            cursor.execute(f"UPDATE Users SET status=5 WHERE dc_name='{user[2]}'")
                            db.commit()
                            continue

                        cursor.execute(f"UPDATE Users SET status=2 WHERE dc_name='{user[2]}'")
                        db.commit()
                        cursor.execute(f"UPDATE Users SET code={code} WHERE dc_name='{user[2]}'")
                        db.commit()
                    
                    elif user[5] == 3:
                        cursor.reset()
                        cursor.execute(f"SELECT role FROM Users WHERE dc_name='{user[2]}'")
                        guild = self.client.get_guild(data["ids"]["guild_id"])
                        member = nextcord.utils.get(guild.members, name=user[2].split("#")[0], discriminator=user[2].split("#")[1])
                        for rang in cursor:
                            rang = str(rang).replace("('", "")
                            rang = str(rang).replace("',)", "")
                            role = guild.get_role(data["roles"][rang])

                        await member.add_roles(role)

                        verify_embed = nextcord.Embed(title="Discord Verify", description=f":tada:**Du hast dich nun erfolgreich mti deinem Minecraft Account verifiziert!**:tada:\n\n> [+] Rang im Discord\n> [+] Weitere Vorteile\n\n**Viel Spaß mit deinen neuen Vorteilen**:blue_heart::wave:", color=nextcord.Color.from_rgb(32, 186, 192))
                        await member.send(embed=verify_embed)

                        cursor.execute(f"UPDATE Users SET status=0 WHERE dc_name='{user[2]}'")
                        db.commit()

                await asyncio.sleep(10)

        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Event {Fore.CYAN}verify_setup{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")
            
def setup(client):
    client.add_cog(verify_setup(client))