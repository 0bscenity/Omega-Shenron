import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"I. HATE. EVERYTHING ABOUT YOUUUU.")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Error syncing commands: {e}")


@bot.tree.command(name="tien", description="I. HATE. EVERYTHING ABOUT YOUUUU.")
async def tien(interaction: discord.Interaction):
    await interaction.response.send_message("https://files.catbox.moe/syuvhi.mp4")

@bot.tree.command(name="nappa")
async def nappa(interaction: discord.Interaction):
    await interaction.response.send_message("https://files.catbox.moe/gtkseg.mp4")

@bot.tree.command(name="yamcha")
async def yamcha(interaction: discord.Interaction):
    await interaction.response.send_message("https://files.catbox.moe/8dzifc.mp4")

@bot.tree.command(name="master_roshi")
async def MutenRoshi(interaction: discord.Interaction):
    await interaction.response.send_message("https://files.catbox.moe/kxd4kn.mp4")

@bot.tree.command(name="trunks")
async def trunks(interaction: discord.Interaction):
    await interaction.response.send_message("https://files.catbox.moe/yw0gis.mp4")

@bot.tree.command(name="vagioa")
async def vagita(interaction: discord.Interaction):
    await interaction.response.send_message("https://files.catbox.moe/h39ekv.mp4")

BOT_TOKEN = "bot token"

bot.run(BOT_TOKEN)
