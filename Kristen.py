import discord
import asyncio


token = ''
with open('secrets.txt') as f:
    token = f.readline().strip()


client = discord.Client()

def has_role(roles_list, role_name):
    for role in roles_list:
        if role.name == role_name:
            return True

    return False

def make_name(message):
    return "__**" + (message.author.nick if message.author.nick else message.author.name) + " said:**__\n"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')


@client.event
async def on_message(message):
    if message.author.bot == False and has_role(message.author.roles, "Recorded"):
        if len(client.messages) > 1:
            previous_message = client.messages[len(client.messages)-2]
        if len(client.messages) > 1 and previous_message.author.id == client.user.id and previous_message.content.startswith(make_name(message)):
            update = previous_message.content[:-3] + message.content + "\n```\n"
            await client.edit_message(previous_message, update)
        else:
            recording = make_name(message)
            recording += "```\n"
            recording += message.content
            recording += "\n```\n"
            await client.send_message(message.channel, recording)
        await client.delete_message(message)



client.run(token)
