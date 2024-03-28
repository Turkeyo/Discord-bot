import discord
from discord.ext import commands
from discord.ext.commands.core import command
from Core.classes import Bot_Cog

class Ctxevent(Bot_Cog):

    #設定Bot發話
    @commands.command()   #ctx對句  msg訊息
    async def bottalk(self,ctx,*,msg) -> None:
        if (msg == "help"):
            await ctx.send("Testr")
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def delctx(self,ctx,num : int) -> None:
        await ctx.message.delete(limit=num+1) 
async def setup(bot) -> None:
    await bot.add_cog(Ctxevent(bot))
