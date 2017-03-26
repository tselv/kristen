import discord
import asyncio
import time
import threading


token = ''
with open('secrets.txt') as f:
    token = f.readline().strip()



OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


def load_opus_lib():
    if discord.opus.is_loaded():
        return True

    for opus_lib in opus_libs:
        try:
            discord.opus.load_opus(opus_lib)
            return
        except OSError:
            pass

load_opus_lib()

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


player = None

class Foo:
  def __call__(self):
    print('called regular version')
  def __call__(self, arg):
    global player
    print('called arg version')
    print(arg)
    print(player.is_done())


class MusicQueue:
    def __init__(self, name, owner, owner_id):
        self.name = name
        self.owner = owner
        self.owner_id = owner_id
        self.queue = []
        self.position = 0
        self.repeat = True
    def get_next_song(self):
        if self.repeat:
            pass
        else:
            pass
    def add_to_queue(song_url):
        pass


class ServerData:
    def __init__(self, server):
        self.server = server
        self.queues = {}
        self.queues["default"] = MusicQueue("default", None, None)
        self.player = None
        self.active_queue = "default"
        self.lock = threading.Lock()
    def __call__(self, player):
        with self.lock:
            if self.player.is_done():
                self.player = self.queues[self.active_queue].get_next_song()


lib = None

@client.event
async def on_message(message):
    global player
    if message.content.startswith("$$"):
        voice = await client.join_voice_channel(message.author.voice.voice_channel)
        player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=sLzydHDe5N4', after=Foo())
        player.start()
    # if message.content.startswith("!test2") and message.author.voice.voice_channel != None:
    #     player.stop()
    #     player = await client.voice_client_in(message.server).create_ytdl_player('https://www.youtube.com/watch?v=sLzydHDe5N4')
    #     player.start()
    if message.author.bot == False and has_role(message.author.roles, "Recorded"):
        if len(client.messages) > 1:
            previous_message = client.messages[len(client.messages)-2]
        if len(client.messages) > 1 and previous_message.author.id == client.user.id and previous_message.content.startswith(make_name(message)):
            update = previous_message.content + "\n" + message.content + "\n"
            await client.edit_message(previous_message, update)
        else:
            recording = make_name(message) + message.content + "\n"
            await client.send_message(message.channel, recording)
        await client.delete_message(message)



def cmd_handler(message):
    global lib

    if message.content.startswith("$$m"):
        if lib == None:
            lib = ServerData(message.server)
        pass
        with lib.lock:
            pass
    youtube_url_regex = "^(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/watch\?v=)((\w|-){11})$"
    # voice = await client.join_voice_channel(message.author.voice.voice_channel)
    # player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=sLzydHDe5N4', after=Foo())
    # player.start()
    print('After the player start')
client.run(token)
