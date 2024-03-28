import discord
from discord.ext import commands
from Core.classes import Bot_Cog
import datetime
import json

with open('config.json',mode='r',encoding='utf-8') as file:
    data = json.load(file)
class  Infornation(Bot_Cog):

    @commands.command()
    async def bot(self,ctx) -> None:
        embed=discord.Embed(title="About SaKuRa2.0 BOT", 
                            url=data['GitHub'], 
                            description="This is SaKuRa2.0 BOT", 
                            color=0x02972f, 
                            timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Author：Turkeyo", url="https://github.com/Turkeyo", icon_url=data['AutherIcon'])
        embed.set_thumbnail(url="https://assets.ppy.sh/beatmaps/534115/covers/cover.jpg?1622111523")
        embed.set_footer(text=("(燦笑"))
        await ctx.send(embed = embed)

async def setup(bot) -> None:
    await bot.add_cog(Infornation(bot))