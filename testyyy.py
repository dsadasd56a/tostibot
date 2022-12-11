# Import the necessary modules
from discord.ui import Select, View, Button
import discord
from discord.ext import commands
# Create a new bot instance
prefix = "!"
bot = commands.Bot(command_prefix=prefix, help_comand=None, intents=discord.Intents.default())

# Define the command
@bot.tree.command( name="ticket")
@commands.has_permissions(administrator=True)
async def say(interaction: discord.Interaction):
    #select = Select(options=[
    #    discord.SelectOption(label="cloudy",description="cloud weather"),
     #   discord.SelectOption(label="cloudy2",description="cloud weather2")
    #])
    #view = View()
    #view.add_item(select)

    button = Button(label="Ticket", style=discord.ButtonStyle.green)
    async def button_callback(interaction):
        
        await interaction.response.send_message("Chose the weather")
    button.callback = button_callback
    view = View()
    view.add_item(button)
    await interaction.response.send_message("Chose the weather", view=view)

# Start the bot
bot.run('MTA0MzY1ODAwMTc2MTk1OTkzNw.GpquL0.EgxVeHHuOvkwHrPn28uRv9crnbtApMjYW3-B-c')