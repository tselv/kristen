import discord
import asyncio


token = ''
with open('secrets.txt') as f:
    token = f.readline().strip()


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')


@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        await client.send_message(message.channel, 'Test response')


client.run(token)
