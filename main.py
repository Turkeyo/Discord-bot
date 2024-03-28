import asyncio
from http import client
from multiprocessing.connection import Client
from xmlrpc.client import Boolean
import discord
from discord.ext import commands
import json
import os
from discord.flags import Intents

with open('config.json',mode='r',encoding='utf-8') as file:
    data = json.load(file)


#Intents = discord.Intents.default()
Intents = discord.Intents.all()

#每次輸入指令前綴字加上?
Intents.members = True
bot = commands.Bot(command_prefix='?',intents=Intents)

bot.remove_command('help')
#Bot事件
@bot.event
async def on_ready():   #開啟Bot訊息
    print('>> Bot is online!!! <<')
    
async def main():
        async with bot:
            for Filename in os.listdir('./Cmds'):
                if Filename.endswith('.py'):
                    await bot.load_extension(f'Cmds.{Filename[:-3]}')
            await bot.start(data['TOKEN'])
#開始運行
if __name__ == "__main__":
    asyncio.run(main())