from pythonping import ping
import discord
from discord.ext import commands, tasks
import datetime

bot = commands.Bot("!")

for i in range(1,10): print()

msg_id = None

def send_ping(host):
    try:
        ping_teste = ping(str(host))
        print ( ping_teste.rtt_min_ms )
        if ping_teste.rtt_min_ms >= 1900:
            return '💔'
        else:
            return '🧡'
    except:
        return '💔'


@bot.event
async def on_ready():
    print(f"Estou pronto! Estou conectado como {bot.user.name}")
    myLoop.start()

    channel = bot.get_channel(977363619241152552)
    messages = await channel.history(limit=200).flatten()
    for i in range(0,len(messages)):
        message_id = messages[i]
        await message_id.delete()
        print(messages[i].id)
    
async def send_message(node_montreal01, tcadmin, site):
    global msg_id
    embed=discord.Embed(title=f"📜  Monitoramento - CamposHost", description=f"Olá, seja bem vindo ao **central de monitoramento** da CamposHost, aqui atualizamos a vocês o status atual da nossa rede [here](www.suamae.com.br)")
    embed.set_thumbnail(url="https://img.pikbest.com/png-images/20190918/cartoon-snail-loading-loading-gif-animation_2734139.png!c1024wm0")
    embed.add_field(name=" Status:", value="🧡 Disponível.\n💔 Fora do ar.\nㅤ\nㅤ\n", inline=False)
    embed.add_field(name="🖥️  NODES: ", value="Montreal( 🇺🇸 ):  "+str(node_montreal01)+"\nBrasil ( 🇧🇷 ): Em breve", inline=False)
    embed.add_field(name="\nㅤ\n🌐  WEB: ", value="TCAdmin( 🇺🇸 ):  "+str(tcadmin)+"\nSite( 🇺🇸 ): "+str(site), inline=False)
    embed.add_field(name="ㅤ\nInformação", value="atualizando a cada 3 minutos,\npara ver em tempo real entre no nosso site.", inline=False)
    embed.set_footer(text='\u200bUltima atualização: ')
    embed.timestamp = datetime.datetime.utcnow()
    if msg_id == None:
        channel = bot.get_channel(977363619241152552)
        send_messge = await channel.send(embed=embed)
        msg_id = send_messge
    else:
        await msg_id.edit(embed=embed)

# Aqui estava o codigo do bloco de notas
@tasks.loop(seconds = 180) # repeat after every 10 seconds
async def myLoop():
    print('Esperendo para receber o Status dos sites..')
    tcadmin = send_ping('painel.camposhost.com.br')
    site = send_ping('www.camposhost.com.br')
    node_montreal = send_ping('51.161.76.130')

    await send_message(node_montreal,tcadmin, site)

bot.run("OTgzMTA5Nzk3MzkyMDUyMjg3.GgfDb_.Hp6C_GkQzqBYAVIHLZ_8vR3ixAKtgHb1I3v2eE")
