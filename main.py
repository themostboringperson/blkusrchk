import os
import discord
from discord import Message
from discord.ext import commands
from discord.ext.commands import Context
import requests
import json
from robloxapi import getinfo, getotherinfo

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot {bot.user} is online")

@bot.event
async def on_message(message: Message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command(name='user')
async def on_api(ctx: Context, username: str):
    oiser = getinfo(username)
    if 'data' in oiser:
        await ctx.send(f"The username of the requested user {oiser['data'][0]['name']}\n"
                       f"Display name of the requested user {oiser['data'][0]['displayName']}\n"
                       f"The ID of the requested user {oiser['data'][0]['id']}\n"
                       f"If the user has a badge or not: {oiser['data'][0]['hasVerifiedBadge']}")
    if 'errors' in oiser:
        await ctx.send('Sorry, an error has occurred! Most likely too many requests have been sent.')

@bot.command(name='friends')
async def on_api(ctx: Context, userid: str):
    friender = getotherinfo(userid)
    if 'data' in friender:
        with open(f'robloxfriends{userid}.json', 'w') as file:
            json.dump(friender, file, indent=4)
        await ctx.reply(file=discord.File(f'robloxfriends{userid}.json'))
    if 'errors' in friender:
        await ctx.send('Invalid user ID. If the issue persists and you are sure the ID is correct, give it a minute and then repeat.')

@bot.command(name='checkfriends')
async def check_friends(ctx: Context, userid: str):
    users_file_path = 'users.txt'

    if not os.path.exists(users_file_path):
        await ctx.send("The 'users.txt' file was not found. Please create it and add usernames (one per line).")
        return

    with open(users_file_path, 'r') as file:
        users_to_check = [line.strip() for line in file if line.strip()]

    friend_list_path = f'robloxfriends{userid}.json'
    if not os.path.exists(friend_list_path):
        await ctx.send("Friend list not found. Please run the `!friends` command first.")
        return

    with open(friend_list_path, 'r') as file:
        friend_list = json.load(file)

    usernames_in_friend_list = [friend['name'] for friend in friend_list['data']]

    results = []
    for user in users_to_check:
        if user in usernames_in_friend_list:
            results.append(f"'{user}' is in the friend list.")
        else:
            results.append(f"'{user}' is NOT in the friend list.")

    await ctx.send("\n".join(results))


bot.run("krisputyourdiscordbottokenhere")