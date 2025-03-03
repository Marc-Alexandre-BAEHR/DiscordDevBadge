#!/usr/bin/python3
TOKEN = ""

import discord
from discord import app_commands
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()  # Sync commands globally
    print(f"Logged in as {client.user}")

@tree.command(name="hello", description="Say hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello, {interaction.user.mention}!")

client.run(TOKEN)
