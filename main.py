import discord, requests, server
from scraper import scraperClass
client = discord.Client()

def get_quote():
    response = requests.get("https://zenquotes.io/api/random").json()
    quote = response[0]["q"] + " -" + response[0]["a"]
    return quote


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("-ennio"):
        await message.channel.send("Morto!")

    if message.content.startswith("-inspire me"):
        await message.channel.send(get_quote())

    if message.content.startswith("-log"):
        embed = discord.Embed(title="comandi", url="", description="Ecco i comandi del bot: \n=>-ennio\n-games", color=0xFF5733)
        embed.set_author(name=message.author.display_name, url="", icon_url=message.author.avatar_url)
        await message.channel.send(embed= embed)
    
    if message.content.startswith("-games"):
        scraper = scraperClass()
        target = message.content.split(" ")
        link_list = scraper.getGames(target=target[1])

        embed = discord.Embed(title="Giochi", url="https://www.steamunlocked.com", color=0xFF5733)
        embed.set_author(name=message.author.display_name, url="", icon_url=message.author.avatar_url)
        
        if link_list == []:
            embed.description = f"Nessun gioco trovato per il nome {target[1]} "

        else:
            embed.description = f"Link trovati: "
            for  link in link_list:
                embed.add_field(name= "Link:\n", value=link, inline=True)

        await message.channel.send(embed= embed)
    
    if message.content.startswith("-browser"):
        #Scrape
        embed = discord.Embed(title="Google", url="https://www.google.com", description= f"Ecco i link:\n {scraper.getGames()}", color=0xFF5733)
        embed.set_author(name=message.author.display_name, url="", icon_url=message.author.avatar_url)
        await message.channel.send(embed= embed)
    

client.activity = discord.Game("-log")
server.keep_alive()
client.run("TOKEN")

