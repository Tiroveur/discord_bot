import time 
import discord
import asyncio
import music
from discord.ext import commands
from discord.utils import get 
"""import dotenv

dotenv.load_dotenv()"""
# 1035661107093844064 id serv général serv bot 

intents = discord.Intents.all()
prefix = "?"
bot = commands.Bot(command_prefix=prefix,intents=intents, description="Tiroveur's Discord Bot")
messages_stored = []



@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}')
    start_time = int(time.time())  # Heure de début de l'activité

    # Vérifier si le bot est connecté à un salon vocal
    for guild in bot.guilds:
        voice_state = guild.voice_client
        if voice_state is not None and voice_state.is_connected():
            voice_client = discord.utils.get(bot.voice_clients, guild=guild)
            await voice_client.disconnect()
            
        bot_member = get(guild.members, id=bot.user.id)
        await bot_member.edit(nick="Tiroveur's bot")  # Remplacez "Nom du Bot" par le nom souhaité pour le bot
        if bot_member.guild_permissions.administrator:
            print("Le bot a les permissions d'administrateur sur le serveur ",guild,".")
            
        else:
            print("Le bot n'a pas les permissions d'administrateur sur le serveur ",guild,".")
    print("bot ready !")

    while not bot.is_closed():
        current_time = int(time.time())
        time_elapsed = current_time - start_time
        hours     = int(time_elapsed/3600)
        minutes   = int((time_elapsed - hours*3600)/60)
        secondes  = int(time_elapsed - hours*3600 - minutes*60)

        occupation="prefix= '"+str(prefix)+"' and developping, time elapse"+' hours '+str(hours)+ ' minutes ' +  str(minutes)+' secondes '+str(secondes)
        activity = discord.Activity( name=str(occupation), type=discord.ActivityType.playing , state=f"Temps passé : {hours} heures")
        await bot.change_presence(activity=activity)
        await asyncio.sleep(1)  # Mettre à jour toutes les heures (ici le divisé par 3600 fait que c'est toute les secondes )
        
"""@bot.event
async def on_message(message):
    # Ignorer les messages du bot
    if message.author.bot:
        return

    # Stocker le contenu du message dans la variable globale
    global messages_stored
    messages_stored.append(message.content)
    print(messages_stored)

    # Exécuter les commandes dans les salons textuels
    await bot.process_commands(message)"""


@bot.command()
async def ping(ctx):
    await ctx.channel.send('Pong!')

@bot.command()
async def hello(ctx):
    print("hello")
    contenu_du_message = ctx.message.content
    await ctx.channel.send(f'Contenu du message : {contenu_du_message}')
    await ctx.channel.send('Bonjour!')

@bot.command(hidden=True)
async def show_messages(ctx):
    global messages_stored
    await ctx.send('Messages stockés :')
    for message in messages_stored:
        await ctx.send(message)

"""        ******           """
"""        ******           """
async def load_extensions():
    await bot.load_extension("music")
    
async def main():
    async with bot:
        await load_extensions()
        await bot.start('MTAzNTYzNTQyNjA4MzQ3OTU2Mg.GMicZs.jyPYbTdWyMm9wvNN1TrXKOHBwSx3o_XkqtNL4k')

asyncio.run(main())