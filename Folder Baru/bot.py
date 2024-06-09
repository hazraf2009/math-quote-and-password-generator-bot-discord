import discord
from main import generate, math, quotes


with open("token.txt", "r") as f:
    token = f.read()

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$halo'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$password'):
        await message.channel.send(generate(10))
    elif message.content.startswith('$matematika'):
        await message.channel.send(math())
    elif message.content.startswith('$quote'):
        await message.channel.send(quotes())
    else:
        await message.channel.send(message.content)

client.run(token)
