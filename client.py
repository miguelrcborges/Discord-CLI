from discord.ext import commands
import discord
import os
import tracemalloc
import keyboard

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

tokenfile = open('token.txt')
token = tokenfile.read()
tokenfile.close()

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


@client.event
async def on_ready():
    while True:
        clearConsole()
        key = keyboard.read_event()
        string = str(key)
        if string == 'KeyboardEvent(f down)':
            for i in range(len(client.user.friends)):
                print(i,client.user.friends[i].name)
            try:
                id = int(input('.>'))
            except:
                continue
            while not keyboard.is_pressed('esc'):
                clearConsole()
                try:
                    history = await client.user.friends[id].history(limit=20).flatten()
                except:
                    continue
                history = reversed(history)
                for message in history:
                    print(message.author.name, message.content)
                text = input('Message: ')
                try:
                    await client.user.friends[id].send(text)
                except:
                    continue
        elif string == 'KeyboardEvent(s down)':
            servers = await client.fetch_guilds(limit=100).flatten()
            for i in range(len(servers)):
                print(i,servers[i].name)
            try:
                id = int(input('.>'))
            except:
                continue
            server = client.get_guild(servers[id].id)
            channels = []
            for channel in server.channels:
                if str(channel.type) == 'text':
                    channels.append(channel)
            for i in range(len(channels)):
                print(i,channels[i].name)
            try:
                id = int(input('.>'))
            except:
                continue
            channel = channels[id]
            while not keyboard.is_pressed('esc'):
                clearConsole()
                try:
                    history = await channel.history(limit=20).flatten()
                except:
                    continue
                history = reversed(history)
                for message in history:
                    print(message.author.name, message.content)
                text = input('Message: ')
                try:
                    await channel.send(text)
                except:
                    continue
        elif string == 'KeyboardEvent(esc down)':
            exit()


client.run(token, bot=False)