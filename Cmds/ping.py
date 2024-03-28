import discord
from discord.ext import commands
from Core.classes import Bot_Cog
#繼承core.class Bot_Cog
class Ping(Bot_Cog):

    @commands.command(name= "Ping" ,description ="Ping bot")
    async def ping(self,ctx) -> None: #ctx Bot回復
        await ctx.send(f'bot 的延遲為:{round(self.bot.latency)}')
        
    @commands.command()   #測試
    async def state(self,ctx,num) -> None:
        await ctx.send(self)

    @commands.command()   #測試
    async def cmdB(self,ctx,num:int) -> None:
        await ctx.send(num)
        
async def setup(bot) -> None: #註冊在bot
    #在bot裡註冊Ping(bot)
    await bot.add_cog(Ping(bot))