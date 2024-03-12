import discord 
import ngrok
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    #print('WE HAVE LOGGED IN as {0.user}'.format(client))
    
    channel = client.get_channel(1216618338222997527)
    await channel.send('**THE SERVER IS NOW ONLINE NOTE THE IP BELOW**')
    await channel.send(listener.url())

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$ip'):
        await message.channel.send(listener.url())

os.system('screen -dm bash -c "sleep 5;cd /home/prakhar6/mine_serv/server_1.17;./start.sh;sleep 15; exec sh"')

tok = 'MTIxNjYxOTE2NTI4NTIyNDUxOA.GG-ims.NVIn2YBmqPo6VPgFeZ32nctSqyUYvhxGL4bN8o'

ngrok.set_auth_token('2B3qSTbsHPpPeMDl4q83uAV0CML_2BYT3LkKxanKduXYNhtg7')

listener = ngrok.forward(25565, "tcp")

#print("NGROK STARTED ON CHANNEL:",listener.url())

client.run(tok)

